"""This mod contains class like a Context manager"""

import os.path


class ContextManager:
    """arg[0] -> file_name: str\n
       arg[1] -> mode: str ('r' or 'w')\n
       arg[2] -> text: str"""

    def __init__(self, file_name: str, mode='r', text=''):
        self._file_name = file_name
        self._mode = mode
        self._text = text
        self.check_file = self.check_exists_file
        self.check_mode = self.check_mode

    @property
    def file_name(self):
        """Get file name"""
        return self._file_name

    @property
    def mode(self):
        """Get file mode"""
        return self._mode

    @property
    def text(self):
        """Get current name"""
        return self._text

    def check_exists_file(self):
        """Check exists by file name"""
        return os.path.exists(self.file_name)

    def check_mode(self, mode):
        """Check mode for current file"""
        if self.mode == mode:
            return True
        return False

    def read_file(self):
        """Read file and close"""
        if self.check_file() and self.check_mode('r'):
            file = open(self.file_name, self.mode, encoding='utf-8')
            try:
                return file.read()
            finally:
                file.close()
        else:
            return False

    def write_file(self):
        """Write file and close"""
        if self.check_file() and self.check_mode('w') and self.text != '':
            file = open(self.file_name, self.mode, encoding='utf-8')
            try:
                return file.write(self.text)
            finally:
                file.close()
        else:
            return False


# if __name__ == "__main__":
#     context = ContextManager(file_name='text.txt')
#     print(context.read_file())
#     text_ = 'Testing by Vlad'
#     write_to_context = ContextManager('text.txt', mode='w', text=text_)
#     write_to_context.write_file()
#     print(context.read_file())
