# agentic_framework_demo
A participant driven agents and skills framework building demo

## Overview

The participants codesign an agentic framework for a shared fictionalized setting.

_The example setting is a kitchen._


Participants use a mix of active learning, co design, peer review to design an
agentic workflow.  All skills point back to a simple python script to simplify
building the core workflow and this also enables some process debugging.

Other objectives:
* Participants practice forking, pull requests and upstream syncing.  
* They explore the wiki tool in GitHub.

## Process

0. Participants verify access to the primary repo. Verify they can find the Wiki and that they can create and edit pages. Each participant edit the AUTHORS page on the wiki, creating it, if it doesn't exist.
1. Participants fork the primary repo and clone the _fork_. Always want to clone the _fork_.
2. Active ideation time. For the fictionalized setting, the participants will go use whiteboards, notepads, the GitHub wiki for the primary repository to layout the agent and skill network.  Keep in mind the goal, objective, task approach and progressive disclosure.  Know that for simplicity, every skill will end up calling the python core script, if you are doing the kitchen setting, this will be `kitchen.py`

Location for the skills:
* 
* Project agent-compatible: .agents/skills/<name>/SKILL.md
