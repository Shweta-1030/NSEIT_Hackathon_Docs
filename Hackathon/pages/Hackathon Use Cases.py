import streamlit as st

st.set_page_config(layout="wide")

##st.markdown("(AI)<sup>5</sup>", unsafe_allow_html=True)

st.title("List of Use Cases")
##st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

col1 = st.columns(6)
col1[0].write('Sr. No.')
col1[1].write('Use Case Name')
col1[2].write('Use Case Summary')
col1[3].write('Use Case Description')
col1[4].write('Potential Impact')
col1[5].write('Required Data/Resources')

col2 = st.columns(6)
col2[0].write('1')
col2[1].write("Text Analytics on Customer Feedback (Domain Agnostic)")
col2[2].write("Categories the customer feedback into predefined categories")
col2[3].write('''Premise: Insurance client has received data from their end customer which has feedback reagrding their services and products.
\n Goal: Feedback data is present in CSV/Excel file. Feedback
is present in 11 Indian Languages, English and Higlish.
Every feedback comment needs to be labelled into a predefined
category which has been defined by Insurance company already.
List of categories is separately provided.
\nImplementation Guidelines: Create application using Gen AI which would 
let Insurance company upload list of their categories and actual feedback data file. Application should use Gen AI to categorize the data and let the user download the labelled/categorised file for their consumption.
All regional languages, English, Hindi, Hinglish should get covered as part of this exercise.''')
col2[4].write('''This can be used for customers where end customer feedback is 
gathered via different channels and can be used to generate Net Promoter Score (NPS) which measures the loyalty of a company's customer base with a score from -100 to +100, 
which comes from customers answering the question "How likely are you to recommend this company to a friend or colleague?''')
col2[5].write('Requires access to Gen AI via APIs and Python coding language')

col3 = st.columns(6)
col3[0].write('2')
col3[1].write('Fraud Detection for Car Insurance ')
col3[2].write('Synthesize data, build, train and test fraud detection model to identify car insurance in real time')
col3[3].write('''Premise: Auto Insurance company is not able to detect the frauds in real time as lots of false claims are being inaccurately settled.
\nGoal: Auto Insurance company wants to detect frauds in car insurance
claim settlement processes in real time using Gen AI capabilities.
\nImplementation Guidelines:
Let's say an insurance company wants to detect fraudulent claims for car accidents. They could use generative AI to generate synthetic data that is similar to real car accident claims data. This data could include information such as the following:
\nType of car accident: This could include information such as the number of vehicles involved, the severity of the accident, and the location of the accident.
Severity of the accident: This could include information such as the number of injuries, the amount of property damage, and the cost of repairs.
Amount of the claim: This could include information such as the amount of medical expenses, the amount of property damage, and the amount of lost wages.
Claimant information: This could include information such as the name of the claimant, the address of the claimant, and the driver's license number of the claimant.
Insurance policy information: This could include information such as the policy number, the policy limits, and the deductible.
The generative AI could be used to generate synthetic data that is similar to this real car accident claims data. The data would be generated in a way that is statistically representative of real car accident claims data. This would allow the insurance company to train a fraud detection model that is accurate at identifying fraudulent claims.
\nHere are some examples of synthetic data that could be generated for this purpose:
\nType of car accident: The generative AI could generate a variety of different types of car accidents, including single-vehicle accidents, multi-vehicle accidents, and hit-and-run accidents.
Severity of the accident: The generative AI could generate a variety of different severities of car accidents, ranging from minor accidents to fatal accidents.
Amount of the claim: The generative AI could generate a variety of different amounts for the claim, ranging from a few hundred dollars to millions of dollars.
Claimant information: The generative AI could generate a variety of different claimant information, including names, addresses, and driver's license numbers.
Insurance policy information: The generative AI could generate a variety of different insurance policy information, including policy numbers, policy limits, and deductibles.
The synthetic data could then be used to train a fraud detection model. The fraud detection model would learn to identify patterns of fraudulent behavior in the data. For example, the model might learn to identify claims that are made for accidents that are unlikely to have happened, or claims that are made for amounts that are significantly higher than the average amount for that type of accident.
\nOnce the fraud detection model has been trained, it could be used to identify fraudulent claims in real car accident claims data. This could help the insurance company to identify fraudulent claims more quickly and efficiently.
 Customer specific PII data should be redacted and should not be sent to Gen AI Model to maintain client secrecy. ''')
col3[4].write('Auto Insurance companies can readily use this model built on synthetic data to detect frauds in real time')
col3[5].write('Requires access to Gen AI via APIs and Python coding language')

col4 = st.columns(6)
col4[0].write('3')
col4[1].write('Automation IMS Flow')
col4[2].write('Automate and expediate day-to-day jobs and develop interactive chatbot')
col4[3].write('''ICS COE
\nPremise:
The goal is to expedite day-to-day minimal jobs, reducing human dependency and error occurrence.
\nGoal:
Develop an interactive ChatBOT to handle day-to-day administration tasks on AWS.
\nImplementation Guidelines:
Utilize Gen AI to create a user-friendly ChatBOT on MS Teams, enabling users to perform routine operations using simple language.''')
col4[4].write('''Potential Impact:
The implementation is expected to accelerate task completion and decrease reliance on human intervention.''')
col4[5].write('''Required Data/Resources:
Access to GenAI API is essential for seamless integration with AWS and Terraform.''')

col5 = st.columns(6)
col5[0].write('5')
col5[1].write('Cloud Operations Managed Services issue resolution Suggestions and links for Incident and request.')
col5[2].write('Enhances IT functions through event correlation and analysis, suggesting possible solutions and providing links to correct SOP. intelligent automation  leveraging Generative AI capabilities')
col5[3].write('''In today's complex IT landscapes, businesses heavily rely on uninterrupted digital operations to maintain efficiency and competitiveness. However, managing IT incidents and maintaining system reliability can be a daunting task due to the sheer volume of events generated from various sources. To address this challenge, our solution leverages advanced event correlation and analysis powered by Generative AI capabilities, aiming to enhance IT functions by automating processes, suggesting optimal solutions, and providing immediate access to the correct Standard Operating Procedures (SOP).
\nKey Features:
1. Event Correlation and Analysis:
2. Generative AI-powered Solution Suggestion
3. Automated SOP Linking
4. Intelligent Automation
5. Continuous Learning and Improvement''')
col5[4].write('Our Intelligent IT Operations Enhancement solution empowers IT teams with advanced event correlation, Generative AI-powered solutions, automated SOP guidance, and intelligent automation. By integrating these capabilities, businesses can expect improved incident resolution times, reduced downtime, enhanced resource utilization, and a streamlined approach to managing complex IT landscapes. This solution represents a significant leap forward in IT operations efficiency and reliability.')
col5[5].write('Python, API tool, Open API, AI alogorithm ')

col6 = st.columns(6)
col6[0].write('4')
col6[1].write('Convert Cloudformation code to Terraform code')
col6[2].write('Convert AWS cloudformation code to Terraform code')
col6[3].write('''Goal: Many organizations are migrating from cloud specific IAAC tools to Terraform as it is generic IAAC. In such cases it is challenging to rewrite terraform code from scratch. The application will help to write terraform code corresponding to cloudformation template.
\nImplementation guide: Users have to upload their cloudformation template code. The application will use Generative AI to create corresponding Terraform modules/code block.''')
col6[4].write('''Potential Impact:
\nAccelerated Migration: Organizations can swiftly transition to Terraform, saving time and effort compared to manual code rewriting.
\nReduced Learning Curve: Teams experienced in CloudFormation can seamlessly adopt Terraform without extensive retraining.
\nMinimized Errors: AI-generated code lowers the risk of human errors during migration, ensuring robust infrastructure setups.
\nBroader Adoption: Easier migration encourages more organizations to adopt Terraform, leading to standardized practices.
\nResource Efficiency: Skilled personnel can focus on higher-value tasks, enhancing productivity and cost savings.
\nConsistency and Compliance: AI ensures migrated setups align with originals, simplifying compliance adherence.
\nInnovation: Streamlined migration frees resources for exploring new infrastructure possibilities and innovation.
\nBest Practice Propagation: Adoption of AI-generated code encourages use of Terraform's best practices and modular approach.''')
col6[5].write('Python, API tool, Open API, AI alogorithm ')

col7 = st.columns(6)
col7[0].write('6')
col7[1].write('analyzing call center employee conversations')
col7[2].write('Sentiment Analysis of Call center employee conversations')
col7[3].write('''Goal: Use all recorded calls from customer & representative conversation generate customer's sentiments (positive, neutral, negative) 
\nImplementation Guidelines: Use mp3/mp4 audio files and convert them into text. Use the text to drive entity recognition and generate the final sentiment output (neutral, negative or positive)''')
col7[4].write('Potential: Sentiment Analysis would be used to enhance customer experience by improving on certain aspects of product marketting, sales and services. ')
col7[5].write('Requires access to Gen AI via APIs and Python coding language')

col8 = st.columns(6)
col8[0].write('7')
col8[1].write('Generate Social media post')
col8[2].write('Generate social media post from recent Organisaztional release.')
col8[3].write('''Goal: Using the recent organisational release generate the social media post for various medias like LinkedIN, Instagram etc.
\nImplementation Guidelines : Use organisational release and transform them into useful graphics or taglines with meaningful image and catchy the social media post.''')
col8[4].write('Potential: These post can be used to engage the connections, better communication, brand promotion and audience building along with the contenet marketing.')
col8[5].write('Requires access to Gen AI via APIs and Python coding language')

col9 = st.columns(6)
col9[0].write('8')
col9[1].write('Resume Parser for TAG (HR)')
col9[2].write('Create a utility which would parse pile of resumes in bulk and generate summary to verify it against the Job Description to validate a resume for job opportunity')
col9[3].write('''Goal: Create a utility which would parse pile of resumes in bulk and generate summary to verify it against the Job Descriptionto validate a resume for job opportunity
\nImplementation Guidelines: Utility should be able to scan pile of resumes in bulk (pdf/doc format) against the job description and provide only suitable resumes back to TAG (HR).''')
col9[4].write('Potential: This can be used by TAG (Talent Aquisition People) to quickly scan hundreds of resumes without manually looking at them and provide only suitable resumes for interview process')
col9[5].write('Requires access to Gen AI via APIs and Python coding language')

col10 = st.columns(6)
col10[0].write('9')
col10[1].write('Email Automation Platform')
col10[2].write('Automate end to end email case initiation to closure including automating workflows for classification, routing, composing response, optional validation and sending response')
col10[3].write('''Goal: Build a platform that helps automate workflow of tasks performed by helpdesk for tickets raised via emails.
\nImplementation Guidelines: Ability to scan email, understand the context, sentiment, criticality and able to create ticket area, priority and sentiment, create ticket based on classification, assign and/or provide solution based on historical data and present for optional review, tone the message according to request.''')
col10[4].write('Potential: This can be used by support teams for automating any type of email based workflows')
col10[5].write('Requires access to Gen AI via APIs and Python coding language and RPA')

col11 = st.columns(6)
col11[0].write('10')
col11[1].write('Agent Assistance Platform')
col11[2].write('''Intelligent customer service agent assistance platform for aiding agents for automating manual tasks and providing information assistance
\nInformation assistance by:
\n1. Providing real time call transcript to agents
\n2. Instant access to wealth of knowledge & resources
\n3. Real-time suggestion for relevant solution
\n4. Ansering common queries
\n5. Reminder for tasks nearing SLA breach''')
col11[3].write('''Goal: Build a platform that helps agents for augmenting decisioning and improve agent experience and help to achieve gain in productivity
\nImplementation Guidelines: Ability to convert speech to text in real time for call in progress. During the call based on text generated, identify the issue or request and provide relevant solution/suggestion in real time by scanning historical data of similar requests via a chat interface with assistance Bot.''')
col11[4].write('Potential: To be used by support agents for solving issues right at first go with reduced TAT')
col11[5].write('Requires access to Gen AI via APIs, knowledge repository data set of previous support cases and relevant doucmentation and Python coding language and RPA')

col12 = st.columns(6)
col12[0].write('11')
col12[1].write('AI Powered Interaction Analytics')
col12[2].write('''Generate insights in to customer support tickets with help of below analytics:
\n1. Performance Scorecards: Analyze tickets & call data to develop diverse performance scorecards for agents, teams
\n2. Reputational Risk: Analyze call transcripts and scrape web data to detect user sentiments, grievances enabling timely identification and resolution of reputational risks
\n3. Query vs Complaint: Analyze call transcripts to classify tickets into queries and complaints for regulatory compliance. Conduct analytics to identify similar tickets and uncover root causes, aiming to reduce ticket volume in the long run''')
col12[3].write('''Goal: Build Analytics for understanding the effectiveness of helpdesk and identify potential risks
\nImplementation Guideline: Perform text analytics on call data to generate different KPIs such as sentiment score, first time right, TAT wrt area, agent, teams etc.Web scrape data from social platforms and corelate it with tickets data for understanding impact of social events, sentiments to arrive at any potential risks to organization from reputation standpoint. Group tickets with similar complaint and based on text analytics of tickets help arrive at RCA''')
col12[4].write('Potential: To be used by senior management for improving Customer experience and in turn improve NPS score')
col12[5].write('Requires access to Gen AI via APIs, knowledge repository data set of previous support cases and relevant doucmentation and Python coding language and RPA')

col13 = st.columns(6)
col13[0].write('12')
col13[1].write('Conversational BI')
col13[2].write('Generate tabular and graphical (in form of charts) results based natural language query given by user')
col13[3].write('''Goal: Build Conversational BI analytics platform that will help users to query data in natural language and ability to generate results in tabular or chart format
\nImplementation Guideline: Platform with ability to connect with standard OLTP/OLAP data base and csv, excel file
Ability to understand the natural langugage query and convert it into SQL query. Ability to understand the nature of query and choose right format of visual for displaying result for example use bar chart for comparison vs line chart for trend vs table for list vs pie chart for showing share etc.''')
col13[4].write('''Potential: To be used by executives for understanding trends in data, perform comparisons, understand performance wrt growth/rank etc.
To be used by analysts for filtering, sorting, doing conditional analysis and slicing of data for various combinations''')
col13[5].write('Requires access to Gen AI via APIs and Python coding language')

col14 = st.columns(6)
col14[0].write('13')
col14[1].write('Exec Summary from Contracts')
col14[2].write('To extract the key details from SOW/MSA contract documents')
col14[3].write('A tool that will create an exeutive summary from contracts with pertinent details like Customer details, Contract value, milestones, duration/period, Contract type like T&M/FP, SLAs, Penalities, Risks etc')
col14[4].write('Can me used as a third eye for effective governance')
col14[5].write('Gen AI, Python, sample contracts')

col15 = st.columns(6)
col15[0].write('14')
col15[1].write('Personalized Recommendation')
col15[2].write('Personalization of products, services or contents')
col15[3].write('AI based automated personalized and tailored product, services or contents recommendation. The solution may be used for various business sectors like e-commerce, financial institutions, OTTs.')
col15[4].write('None')
col15[5].write('None')

col16 = st.columns(6)
col16[0].write('15')
col16[1].write('TalentTrack Pro')
col16[2].write('Gen-AI-Powered Talent Management and Assessment Platform')
col16[3].write('''TalentTrack Pro empowers NSEIT to make data-driven decisions, enhance talent management processes, and foster skill development, resulting in improved project outcomes and a more agile and competitive workforce. This use case demonstrates the app's potential to revolutionize talent management and assessments in modern project teams.
\nNote: This is not an appraisal system, this system will only track career goals, plans, progressions, training recommendations, certifications, DU and org level metrics''')
col16[4].write('''Trend Analysis and Industry Benchmarking:TalentTrack Pro can utilize Gen AI for trend analysis and industry benchmarking. By comparing internal talent metrics with external industry data, organizations can identify areas for improvement and remain competitive.
\nEnhanced Talent Development: TalentTrack Pro will fosters skill development and career progression by offering personalized training recommendations and resources. Team members can align their development with organizational goals.
\nOptimized Team Composition: AI-driven talent matching ensures that project teams are composed of individuals with the right skills and qualifications, leading to improved project outcomes and efficiency.
\nReal-Time Feedback: Team members receive real-time feedback, enabling them to make immediate course corrections and progress in their careers more effectively.
\nCompliance and Certification Tracking: The app simplifies compliance tracking and certification management, ensuring that team members have the necessary qualifications to excel in their roles. The Gen AI powered engine also recommends certifications to be done by individuals
\nStrategic Workforce Planning: TalentTrack Pro supports NSEIT in forecasting future talent needs and skill gaps, enabling proactive workforce planning.
\nImproved Organizational Agility: By nurturing skill development and aligning talent with strategic goals, the app helps NSEIT become more agile and competitive in today's dynamic business environment.
\nAI-Powered Insights: Gen AI integration provides actionable insights and recommendations, helping NSEIT stay ahead in talent management and assessments.
\nAI-Enhanced Coaching and Mentorship:TalentTrack Pro can use Gen AI to provide personalized coaching and mentorship recommendations. It can match team members with suitable mentors based on their career goals and skill development needs.
\nCourse Recommendation: Based on the skills gap analysis, TalentTrack Pro can use Gen AI to recommend free and open online courses, tutorials, webinars, or other learning resources. These recommendations should be tailored to address the specific skill gaps identified for each team member.
\nPredictive Analytics for Talent Retention:Gen AI can help predict which team members are at risk of leaving the organization. By analyzing historical data and engagement patterns, the app can provide early warnings, allowing HR managers to implement retention strategies.
\nSentiment Analysis for Employee Engagement:Use Gen AI to perform sentiment analysis on employee engagement surveys and feedback. This helps HR managers gauge the overall satisfaction and engagement levels of team members.
''')
col16[5].write('Python, Open API, Spacy, NLTK')

col17 = st.columns(6)
col17[0].write('16')
col17[1].write('Code Buddy')
col17[2].write('Gen-AI-Powered code buddy')
col17[3].write('''Code Buddy will help in 
\nCode completion
\nCode generation
\nTest-Cases generation
\nCode documentation
\nCode debugging
\nCode migration
\nWhich means faster project execution and efficient coding and testing phase''')
col17[4].write('Impact to get the project coding and testing phased improved by around 25%. Faster and accurate issue resolutions')
col17[5].write('Python, LLAMA + Machine with GPU or Mistral 7B + machine, Open AI')

col18 = st.columns(6)
col18[0].write('17')
col18[1].write('content moderation')
col18[2].write('analyze the audio from a video clip to recognize offensive or demeaning language')
col18[3].write('''customer care agent or customer behaviour analysis.
Employee behaviour tracking''')
col18[4].write('''This helps management to track the behaviour of the employees 
whether they are engaging customers with respect''')
col18[5].write('OpenAI , Python , streamlit')

col19 = st.columns(6)
col19[0].write('18')
col19[1].write('patent documentation analysis')
col19[2].write('Analyze if a similar research paper has already been published using a similarity score ')
col19[3].write("When a new patent is submitted it is cross checked against existing patents whether it is something actually new or just a reworded document of existing patent")
col19[4].write('Helps to identify similar documents against an existing inventory')
col19[5].write('OpenAI , Python , streamlit, vector database')

col20 = st.columns(6)
col20[0].write('19')
col20[1].write('jobSearch Hotline')
col20[2].write('Gen-AI-Powered code job search, criteria management, live suitability analysis')
col20[3].write('''Creation of a new AI powered NSEIT Job Search Web Portal with following Features:
\n1. Resume Creation
A form to be filled by applying employee to create a database entry with employee details in a specific format.
\n2. Resume Analysis
Based on specfied skills, giving a generic category and job suitability percentage
\n3. Job Search
Based on assigned category, based on suitability ratio, list available jobs with Match/Suitability percentage.
\n4. Pre-Interview Prep Section
A section that will generate and make available topics and a basic description of what employee must have an idea about before applying for a role.
\n5. Post Interview Analysis
Interviewer must upload a copy of Teams Call Transcription to be analysed by AI and generate a report on how employee performed.
Points to improve etc
\n6. Interviewer's Portal
Interviewer will have a Dashboard to highlight suitable employees based on performance to choose from.
\n7. Employee Application History
Gen AI powered employee analysis to study employee application behavior to identify employee behavior. Helps to identify how serious an employee is based on whether he is sending application to all jobs or just a specific one etc''')
col20[4].write("We'll be able to discern and select Quality employees and save time for HR")
col20[5].write('OpenAI API (access to GPT3.5, GPT4), Python, Linux VM')
