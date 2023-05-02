from os import environ as env
import keepachangelog
from github import Github


def getLatestChange():
    changes = keepachangelog.to_raw_dict(env['INPUT_CHANGELOG'])
    return list(changes.values())[0]


def fillTemplate(template, data):
    result = ''
    i = 0
    while i < len(template):
        if template[i] == '{':
            end = template.find('}')
            if end == -1:
                result += template[i:]
                break
            key = template[i + 1:end]
            if key in data:
                result += str(data[key]) if data[key] is not None else ''
            else:
                result += template[i:end + 1]
            i = end + 1
        else:
            result += template[i]
            i += 1
    return result


github = Github(base_url=env['GITHUB_API_URL'],
                login_or_token=env['INPUT_TOKEN'])
repo = github.get_repo(env['GITHUB_REPOSITORY'])

change = getLatestChange()
data = {
    'version': change['metadata']['version'],
    'major': change['metadata']['semantic_version']['major'],
    'minor': change['metadata']['semantic_version']['minor'],
    'patch': change['metadata']['semantic_version']['patch'],
    'prerelease': change['metadata']['semantic_version']['prerelease'],
    'build': change['metadata']['semantic_version']['buildmetadata'],
    'release-date': change['metadata']['release_date'],
}

# Create release.
release = repo.create_git_release(
    fillTemplate(env['INPUT_TAG-TEMPLATE'], data),
    fillTemplate(env['INPUT_NAME-TEMPLATE'], data),
    change['raw'],
    env['INPUT_IS-DRAFT'] == 'true',
    data['prerelease'] is not None,
    env['GITHUB_SHA'])

# Move major tag.
major_name = fillTemplate(env['INPUT_MAJOR-TAG-TEMPLATE'], data)
major = repo.get_git_ref(f'tags/{major_name}')
if major.ref is not None:
    major.edit(env['GITHUB_SHA'])
else:
    repo.create_git_ref(f'refs/tags/{major_name}', env['GITHUB_SHA'])

# Output.
data['html-url'] = release.html_url
data['upload-url'] = release.upload_url
with open(env['GITHUB_OUTPUT'], 'a') as out:
    for (key, val) in data.items():
        print(f'{key}={val if val is not None else ""}', file=out)
