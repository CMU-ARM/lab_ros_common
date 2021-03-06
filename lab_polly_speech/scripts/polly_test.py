#!/usr/bin/env python

import rospy
from lab_common.msg import(
    polly_speechGoal,
    polly_speechAction
)
import actionlib

def speak(polly_client, text, voice_id="Joanna"):
    goal = polly_speechGoal()
    goal.input.append(text)#"Hi Liz, Nice to Meet you. Do you fancy some tea?"
    goal.input.append(voice_id)
    polly_client.send_goal_and_wait(goal)

def main():
    polly_client = actionlib.SimpleActionClient("lab_polly_speech/speak", polly_speechAction)
    polly_client.wait_for_server()

    speak(polly_client, "Lalalalalalalalalalalalalalalalala.", "Matthew")
    speak(polly_client, "It's working so well!", "Emma")
#    speak(polly_client, "Ceci is Cool. ")
#    speak(polly_client, "This is working really really really really really really really well")
#    speak(polly_client,"Cats and dogs each hate the other. The pipe began to rust while new. Open the crate but don't break the glass. " + 
#    "Add the sum to the product of these three. Thieves who rob friends deserve jail. The ripe taste of cheese improves with age. "+
#    "Act on these orders with great speed. The hog crawled under the high fence. Move the vat over the hot fire.")


if __name__ == '__main__':
    rospy.init_node("polly_node_test")
    main()
