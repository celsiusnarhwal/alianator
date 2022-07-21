import unittest

import discord

from src import alianator


class AlianatorTests(unittest.TestCase):
    def test_true(self):
        perms = discord.Permissions.text()
        expected = ['Add Reactions', 'Send Messages', 'Send Text-to-Speech Messages', 'Manage Messages', 'Embed Links',
                    'Attach Files', 'Read Message History', 'Mention \\@everyone, \\@here, and All Roles',
                    'Use External Emoji', 'Use Application Commands']
        self.assertEqual(alianator.resolve(perms), expected)

    def test_false(self):
        perms = discord.Permissions.text()
        expected = ['Create Instant Invite', 'Kick Members', 'Ban Members', 'Administrator', 'Manage Channels',
                    'Manage Server', 'View Audit Log', 'Priority Speaker', 'Video', 'Read Messages',
                    'View Guild Insights', 'Connect', 'Speak', 'Mute Members', 'Deafen Members', 'Move Members',
                    'Use Voice Activity', 'Change Nickname', 'Manage Nicknames', 'Manage Roles', 'Manage Webhooks',
                    'Manage Emojis and Stickers', 'Request to Speak']
        self.assertEqual(alianator.resolve(perms, mode=False), expected)

    def test_none(self):
        perms = discord.Permissions.text()
        expected = ['Create Instant Invite', 'Kick Members', 'Ban Members', 'Administrator', 'Manage Channels',
                    'Manage Server', 'Add Reactions', 'View Audit Log', 'Priority Speaker', 'Video', 'Read Messages',
                    'Send Messages', 'Send Text-to-Speech Messages', 'Manage Messages', 'Embed Links', 'Attach Files',
                    'Read Message History', 'Mention \\@everyone, \\@here, and All Roles', 'Use External Emoji',
                    'View Guild Insights', 'Connect', 'Speak', 'Mute Members', 'Deafen Members', 'Move Members',
                    'Use Voice Activity', 'Change Nickname', 'Manage Nicknames', 'Manage Roles', 'Manage Webhooks',
                    'Manage Emojis and Stickers', 'Use Application Commands', 'Request to Speak']
        self.assertEqual(alianator.resolve(perms, mode=None), expected)


if __name__ == '__main__':
    unittest.main()
