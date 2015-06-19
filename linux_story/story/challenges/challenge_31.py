#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story

import time
from linux_story.story.terminals.terminal_nano import TerminalNano
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateNano(TerminalNano):
    challenge_number = 31


class Step1(StepTemplateNano):
    story = [
        "Huh, you can't see Bernard anywhere.",

        "I wonder where he went.",

        "Let's {{lb:go into}} his secret room and see what "
        "he's hiding."
    ]
    start_dir = "~/town/east/shed-shop"
    end_dir = "~/town/east/shed-shop/basement"

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        Step2()


class Step2(StepTemplateNano):
    story = [
        "Look around."
    ]
    start_dir = "~/town/east/shed-shop/basement"
    end_dir = "~/town/east/shed-shop/basement"
    commands = [
        "ls",
        "ls -a"
    ]

    def next(self):
        Step3()


class Step3(StepTemplateNano):
    story = [
        "You see what looks like another tool and a diary.",
        "Examine them."
    ]
    start_dir = "~/town/east/shed-shop/basement"
    end_dir = "~/town/east/shed-shop/basement"
    commands = [
        "cat bernards-diary-1",
        "cat bernards-diary-2",
        "cat photocopier.sh"
    ]
    hints = [
        "{{rb:Use}} {{lb:cat}} {{rb:to examine the objects around you.}}"
    ]

    def check_command(self):
        if self.last_user_input in self.commands:
            self.commands.remove(self.last_user_input)

            if not self.commands:
                text = (
                    "\n{{gb:Press Enter to continue.}}"
                )
                self.send_text(text)

            else:
                text = (
                    "\n{{gb:Well done! Look at the other object.}}"
                )
                self.send_text(text)

        elif not self.last_user_input and not self.commands:
            return True

    def next(self):
        Step4()


class Step4(StepTemplateNano):
    story = [
        "Enough wandering. Let's go and try and find the "
        "{{lb:masked swordsmaster}} near the woods, and see "
        "what information he can tell us."
        "{{gb:Press Enter to continue.}}"
    ]
    start_dir = "~/town/east/shed-shop/basement"
    end_dir = "~/town/east/shed-shop/basement"
    last_step = True

    def next(self):
        self.exit()

        time.sleep(3)
