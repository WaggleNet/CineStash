import json
from pathlib import Path
from glob import glob
import os
import re

from .mongo import project_db
from bson import ObjectId

def split_angle_from_notes(note):
    matches = re.match('^\(([A-Z]+)\) ?(.+)', note)
    if not matches:
        return 'N/A', note
    return matches.groups()


def split_shot_number(shot):
    matches = re.match('^(\d+)[A-Z]+', shot)
    if not matches:
        return None
    return matches.group(0)


def suffixed_filename(url_name, suffix, changeext=None):
    *fname, ext = url_name.split('.')
    return '.'.join(fname) + '-' + suffix + '.' + (changeext or ext)


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', str(text)) ]


def load_scenes(project_path):
    storyboard_path = 'storyboards'
    scene_paths = [
        os.path.relpath(i, project_path) for i in (Path(project_path) / storyboard_path).glob('*')
        if os.path.isdir(i) and str(i).find('.') == -1
        and i.name.find('Scene-') > -1
    ]
    scene_paths.sort(key=natural_keys)
    scenes = [generate_scene(project_path, Path(project_path) / i) for i in scene_paths]


def get_by_id(l, _id):
    for i in l:
        if i['_id'] = l:
            return i
    return None


def sync_scenes(project_id):
    db = project_db()
    project = db.find_one({'_id': ObjectId(project_id))
    if not project:
        raise IndexError('Project not found')
    if not project.get('scenes'):
        project['scenes'] = []
    scenes = load_scenes(project['projectPath'])
    for sc in scenes:
        old_scene = get_id(project['scenes'], _id)
        if old_scene:
            # Synchronize takes to the new scene
            for shot in scene.get('shots', []):
                old_shot = get_id(old_scene.get('shots', []))
                if old_shot:
                    shot['takes'] = old_shot.get('takes', [])
    # Now that all the custom info is in, let's overwrite the scene
    db.update_one({'_id': ObjectId(project_id)}, {'$set': {'scenes': scenes}})
