import unittest
from commands import execute_command
from vfs import VFS
import configparser
class TestCommands(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        archive_path = config['vfs']['archive']
        self.vfs = VFS(archive_path)

    def test_execute_command_ls(self):
        output = execute_command(self.vfs, 'ls')
        self.assertIn('bios', output)
        self.assertIn('rec', output)
        self.assertIn('roms', output)
        self.assertIn('system', output)
        self.assertIn('passwors.docx', output)
        self.assertIn('tests.pdf', output)
        self.assertIn('ticks.txt', output)

    def test_execute_command_cd(self):
        output = execute_command(self.vfs, 'cd roms')
        self.assertEqual(output, r'Changed directory to \alndis\vfs\roms')
        output = execute_command(self.vfs, 'cd ..')
        self.assertEqual(output, r'Changed directory to \alndis\vfs')

    def test_execute_command_uname(self):
        output = execute_command(self.vfs, 'uname')
        self.assertIn('System:', output)
        self.assertIn('Release:', output)
        self.assertIn('Version:', output)
        self.assertIn('Machine:', output)
        self.assertIn('Processor:', output)

if __name__ == '__main__':
    unittest.main()