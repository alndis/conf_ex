import unittest
from vfs import VFS
import os
import configparser
class TestVFS(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        archive_path = config['vfs']['archive']
        self.vfs = VFS(archive_path)

    def test_extract_zip(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        archive_path = config['vfs']['archive']
        self.vfs.extract_zip(archive_path)
        self.assertTrue(os.path.exists(self.vfs.fs_path))

    def test_list_files(self):
        files = self.vfs.list_files()
        self.assertIn('bios', files)
        self.assertIn('rec', files)
        self.assertIn('roms', files)
        self.assertIn('system', files)
        self.assertIn('passwors.docx', files)
        self.assertIn('tests.pdf', files)
        self.assertIn('ticks.txt', files)

    def test_change_directory(self):
        self.vfs.change_directory('roms')
        self.assertEqual(self.vfs.current_path, os.path.join(self.vfs.fs_path, 'roms'))
        self.vfs.change_directory('..')
        self.assertEqual(self.vfs.current_path, self.vfs.fs_path)


    def test_read_file(self):
        content = self.vfs.read_file(os.path.join(self.vfs.fs_path, 'system', 'msql.exe'))
        self.assertIsNotNone(content)


    def test_execute_uname(self):
        output = self.vfs.execute_uname()
        self.assertIn('System:', output)
        self.assertIn('Release:', output)
        self.assertIn('Version:', output)
        self.assertIn('Machine:', output)
        self.assertIn('Processor:', output)

if __name__ == '__main__':
    unittest.main()