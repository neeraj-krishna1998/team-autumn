#!/usr/bin/env python3

import aws_cdk as cdk

from team_autumn.team_autumn_stack import TeamAutumnStack


app = cdk.App()
TeamAutumnStack(app, "team-autumn")

app.synth()
