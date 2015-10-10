#!/usr/bin/env python
# coding: utf-8

#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# A chapter of the story

import os
import sys

dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if __name__ == '__main__' and __package__ is None:
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)

# from linux_story.Step import Step
from linux_story.story.terminals.terminal_cat import TerminalCat
from linux_story.story.challenges.challenge_4 import Step1 as NextChallengeStep


class StepTemplateCat(TerminalCat):
    challenge_number = 3


class Step1(StepTemplateCat):
    story = [
        "Mi piace! Mettilo di corsa. " 
        "C'è un sacco di roba interessante in camera tua.",
        "{{lb:Guarda}} nei tuoi {{lb:scaffali}} using {{lb:ls}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = ["ls scaffali", "ls scaffali/"]
    hints = "{{rb:Scrivi}} {{yb:ls scaffali/}} {{rb:per guardare i tuoi libri.}}"

    def next(self):
        Step2()


class Step2(StepTemplateCat):
    story = [
        "Lo sapevi che puoi usare il tasto TAB "
        "per scrivere i comandi più alla svelta?",
        "Prova prendendo quel fumetto. ",
        "{{lb:Guardalo}} con "
        "{{yb:cat scaffali/fumetto}}",
        "Premi il tasto TAB prima di "
        "avere finito di scrivere il comando!\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = "cat scaffali/fumetto"
    hints = "{{rb:Scrivi}} {{yb:cat scaffali/fumetto}} {{rb:per leggerlo.}}"

    def next(self):
        Step3()


class Step3(StepTemplateCat):
    story = [
        "O chi ha lasciato un'impronta sul fumetto!?",
        "Aspetta? C'è un {{lb:foglietto}} fra i tuoi libri.",
        "{{lb:Leggilo}} usando il comando {{lb:cat}}.\n"
    ]
    start_dir = "~/casa-mia/camera-mia"
    end_dir = "~/casa-mia/camera-mia"
    commands = "cat scaffali/foglietto"
    hints = "{{rb:Scrivi}} {{yb:cat scaffali/foglietto}} {{rb:per leggerlo.}}"

    last_step = True

    def next(self):
        NextChallengeStep(self.xp)
