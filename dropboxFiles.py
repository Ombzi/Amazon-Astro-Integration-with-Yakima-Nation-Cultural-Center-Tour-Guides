import dropbox
import re
def getDropboxFiles(access_token):
    # dict of audio files
    audioFiles = {}

    dbx = dropbox.Dropbox(access_token)
    for entry in dbx.files_list_folder('/Apps/MySkill').entries:
        # get a temporary link to the files in this directory
        link = dbx.files_get_temporary_link(entry.path_lower).link
        # remove the file extension from the name
        entry.name = re.sub(r'\..*$', '', entry.name)
        # add the link to the dict
        audioFiles[entry.name] = link

    # print the dict
    return audioFiles
