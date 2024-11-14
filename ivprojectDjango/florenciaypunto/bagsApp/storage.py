from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, id, max_length=None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(id):
            os.remove(os.path.join(settings.MEDIA_ROOT, id))
        return id
