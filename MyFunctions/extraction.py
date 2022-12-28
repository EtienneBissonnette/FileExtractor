import zipfile, os, shutil


def extraction(zip_path, filters):

    destination, _ = os.path.split(zip_path)
    destination += "/extracted"
    members_lst = []

    with zipfile.ZipFile(zip_path, "r") as zipFolder:
        for member in zipFolder.namelist():

            member_path, file = os.path.split(member)

            for filter in filters:

                f_ = filter.split("*")

                if member_path.startswith("__MACOSX"):
                    continue
                else:
                    if f_[0] == '' and file.endswith(f_[-1]):
                        members_lst.append(member)
                    elif file.startswith(f_[0]) and file.endswith(f_[-1]):
                        members_lst.append(member)
                    else:
                        continue

        if os.path.exists(destination):
            shutil.rmtree(destination)
            zipFolder.extractall(path=destination, members=members_lst)

        else:
            zipFolder.extractall(path=destination, members=members_lst)
