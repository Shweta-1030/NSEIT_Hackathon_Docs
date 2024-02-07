import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

image = Image.open('data/AI logo.jpg')
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

##st.markdown("(AI)<sup>5</sup>", unsafe_allow_html=True)

st.title("(AI)5 : Generative AI Hackathon Rules & Guidelines")
##st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

st.markdown("""
(AI)<sup>5</sup> to be read as I5: 5x Productivity with AI Solutions: Defining how AI can enhance productivity for the future. 
A hackathon to be conducted amongst NSEIT along with Cybersecurity and Cloud employees.
""", unsafe_allow_html=True)

st.markdown("""
These are the standard competition rules & guidelines used at One NSEIT’s Generative AI Hackathon\n\n
All other terms and rules listed in this document will continue to apply. Should there be a direct conflict during the Hackathon, decision of the organizing committee would be deemed as final.
""")

st.header('## The Rules of the Competition')
st.markdown("""
1. Teams may have a maximum of 3 members. Minimum 2 and Maximum 3 members per team. 
2. Teams should be made up exclusively of accepted members who are not organizers, volunteers, mentors, judges, sponsors. 
3. Teams can gain advice and support from organizers, volunteers, sponsors, and others. Point of Contact for all participants would be shared soon.
4. All work on a project must be done during the Hackathon period only. Hackathon Start & End date would be communicated soon to all participants. These  should not have any impact on your project work during this time
5. Teams can use any use case from the shortlisted use cases. Participants would need to communicate the use case they would be working upon to organizing committee upfront. Medium of communication would be shared soon. 
6. If somebody wants to work on a more than one use case, they are allowed to. 
7. Teams can work on an idea that they have worked on before (as long as they do not re-use code).
8. Teams can use libraries, frameworks, or open-source code in their projects. Working on a project before the event and open-sourcing it for the sole purpose of using the code during the event is against the spirit of the rules and is not allowed.
9. Team should not use any client’s code, environment, software and data for this Hackathon 
10. Teams must stop development once the time is up.
11. Teams that violate above rules are not allowed to participate
12. Teams can be disqualified from the competition at the organizers' discretion. Reasons might include but are not limited to breaking the Competition Rules, breaking the or other unsporting behaviour.
""")

st.header('## Submission Requirements and Demo')
st.markdown("""
After Hackathon finishes, teams must submit their projects to GitHub by the submission deadline.
A project submission must have two components to be eligible for judging:
- a link to the project's code repository; _and_
- a brief write-up on the project summary, description, use cases, video, screenshots etc
- Video call with a detailed walkthrough of the use case and implementation to judges.

After submission, teams will show their projects each other and to the judges.

Judging will take place synchronously & virtually once Hackathon finishes. Teams will be notified of their demo date and time upfront, and at least one member of the team must be present to present their project to judges for their submission to be considered for prizes. 

It's important to note that there may be multiple rounds of judges that come to judge your project, especially if you submitted your project to multiple prize categories. As such, it is important to remain available for the entire duration of the evaluation phase of Hackathon.

You are encouraged to present what you have done even if your use case is broken or you weren’t able to finish. It's okay if you didn't finish your project—that happens all the time! Completion is only one part of the judging criteria, so you might still do well. Also, demoing is not just about the competition. It's a chance to share with others what you learned and what you tried to build—that's what hackathon is all about! For being courageous enough to demo, you'll receive a special badge —it doesn't matter how good the demo is! In the case that you don't have anything to demo, you can give a presentation about what you tried and what you learned. Hearing what other people learned is interesting and inspiring for other attendees.

Each project may only be submitted to multiple domains (health, sustainability, banking, fintech, insurance), but teams cannot opt-in to multiple categories for Prizes and badges. 
""")

st.header('## Judging Criteria')
st.markdown("""
Teams will be judged on these five criteria. During judging, participants should try to describe what they did for each criterion in their project. 

- __Technology:__ How technically impressive was the project? Was the technical problem the team tackled difficult? Did it use a particularly clever technique, or did it use many different components? Did the technology involved make you go "Wow"?
- __Design:__ Did the team put thought into the user experience? How well designed is the interface? For a website, this might be about how beautiful the CSS or graphics are. For a hardware project, it might be more about how good the human-computer interaction is (e.g. is it easy to use or does it use a cool interface?). 
- __Completion:__ Does the project work? Did the team achieve everything they wanted? Does the project do what it's supposed to do?
- __Ideation:__ How creative or original is the project idea?
- __Applicability:__ How well does this project fit the prize track it's in?

These criteria will guide judges but ultimately judges are free to make decisions based on their gut feeling of which projects are the most impressive and most deserving.
""")

st.header("It's important to note that these judging criteria do not include:")
st.markdown("""
- How good your code is. It doesn't matter if your code is messy, or not well commented, or uses inefficient algorithms. Hackathon is about playing around, making mistakes, and learning new things. If your code isn't production ready, we're not going to mark you down.
- How well you pitch. Hackathon is about building and learning, not about selling.
- How well the project solves a problem. You can build something totally useless and as long as you're learning and having fun, that's a good project! Sometimes a pointless project is one of the best projects!
\nSo don't worry about coming up with the next big idea. You'll have plenty of time for that outside the hackathon. just focus on learning! At the end of the day the skills you learn and the friends you make might lead to the next big thing—but you don't have to do that to win a hackathon.
""")


image = Image.open('data/AI logo.jpg')
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")