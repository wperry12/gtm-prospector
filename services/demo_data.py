# /services/demo_data.py

# This file contains all the hardcoded data used for the application's demo mode.

DUMMY_CBA_NEWS = [
    {'title': 'Artificial Intelligence at CommBank', 'link': 'https://www.commbank.com.au/about-us/opportunity-initiatives/policies-and-practices/artificial-intelligence.html'},
    {'title': 'CBA backtracks on AI job cuts as chatbot lifts call volumes', 'link': 'https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492'},
    {'title': 'Reimagining banking for the future', 'link': 'https://www.commbank.com.au/articles/newsroom/2024/11/reimagining-banking-nov24.html'},
    {'title': 'CBA says customer fraud alerts speed up with AI', 'link': 'https://www.retailbankerinternational.com/news/cba-fraud-speeds-ai/'},
    {'title': 'Commonwealth Bank uses AI to enhance customer service', 'link': 'https://cfotech.com.au/story/commonwealth-bank-uses-ai-to-enhance-customer-service'}
]

DUMMY_CBA_AI_STRATEGY = """
1.  **Overall AI Adoption:** High 🔥 - Actively integrating AI in core processes
    * Commonwealth Bank (CBA) is actively integrating AI across multiple core functions, including fraud detection, customer support (messaging and call centers), and loan processing, demonstrated by multiple public announcements and initiatives. They're also sponsoring and participating in major AI research conferences like NeurIPS 2024.

2.  **Customer Support AI Status:** Actively Integrated 🔒
    * CBA has deployed AI-powered "voice-bots" and generative AI in their customer-facing messaging services, resulting in a reported 40% reduction in call center wait times. They are also one of the few banks globally to utilize generative AI for this purpose.

3.  **Build vs. Buy Approach:** Unclear 🤔
    * While CBA has a clear focus on utilizing AI and presents internal development efforts (research presented at NeurIPS), the information available doesn't clearly specify if they favor building solutions in-house or are open to external partnerships with AI platform providers.

---

### Stated Challenges & Pain Points
- CBA initially made 45 customer service roles redundant due to the introduction of an AI "voice-bot," but then reversed the decision after the Finance Sector Union raised a dispute, admitting they had not fully considered the implications and that call volumes actually increased after the bot's deployment. This incident highlights a potential pain point in accurately assessing the impact of AI implementation on staffing needs and workflows. This reversal and apology, alongside the union dispute, points towards internal struggles balancing AI adoption with workforce management, and a possible sensitivity to negative PR around AI-related job displacement.
- While CBA has made strides in AI integration, they acknowledge the challenge of understanding the long-term impact of AI on jobs, suggesting an area of uncertainty and potential concern. They also highlight the difficulty in measuring the environmental impact of their AI computing, especially with third-party providers, indicating a need for better tools and data in this area.

### Opportunities for Customer Support AI
- **Improved AI-driven call routing and agent assist:** Given the challenges CBA faced with their initial "voice-bot" rollout, our AI-powered platform could provide a more nuanced and effective solution for handling increased call volumes and complex customer inquiries, ensuring that customers are routed to the appropriate agent or provided with accurate self-service options. This would address their previous miscalculation of reduced call volumes and the subsequent overreliance on human agents and overtime.
- **Generative AI-powered knowledge management and agent training:** Our platform can leverage generative AI to create a comprehensive knowledge base and training materials for customer service agents, allowing them to quickly access relevant information and provide consistent, high-quality support across all channels. This addresses the potential for inconsistent or incomplete answers from the current generative AI messaging system and empowers agents to handle more complex issues efficiently.

### Evidence & Key Initiatives
-  Development and implementation of AI-powered "voice-bot" for customer service.
-  Integration of generative AI in customer-facing messaging services, handling over 50,000 inquiries daily.
-  Development of AI-driven fraud detection systems (NameCheck, CallerCheck, CustomerCheck) resulting in a 50% reduction in scam losses and 30% decrease in reported frauds.
-  AI-driven loan application process with automated document pre-population and expedited approvals.
-  Exploration of AI for automating annual credit reviews, potentially reducing processing time from 14 hours to 2 hours.
-  Participation and bronze sponsorship at NeurIPS 2024, showcasing research on AI investment strategies.
-  Public commitment to using AI for enhanced customer experiences and operational efficiency.
-  Focus on managing the ethical implications of AI and developing principles for responsible AI implementation.
"""

DUMMY_CBA_LUSHA_PAYLOAD = {
    "data": [
        {"name": "Simon Birch", "jobTitle": "Acting Chief Technology Officer", "companyName": "Commonwealth Bank"},
        {"name": "Rodrigo Castillo", "jobTitle": "Chief Technology Officer", "companyName": "Commonwealth Bank"},
        {"name": "Andrew Mcmullan", "jobTitle": "Chief Data and Analytics Officer", "companyName": "Commonwealth Bank"},
        {"name": "Restricted", "jobTitle": "CIO and Ciso , Commbank Health", "companyName": "Commonwealth Bank"},
        {"name": "Andrew Hinchliff", "jobTitle": "Group Chief Risk Officer", "companyName": "Commonwealth Bank"},
        {"name": "Restricted", "jobTitle": "CIO Retail and Wealth Banking", "companyName": "Commonwealth Bank"},
        {"name": "Nathan Chandler", "jobTitle": "General Manager", "companyName": "Commonwealth Bank"},
        {"name": "Restricted", "jobTitle": "Chief Information Officer", "companyName": "Commonwealth Bank"},
        {"name": "Nora Waugh", "jobTitle": "Chief Information Officer", "companyName": "Commonwealth Bank"},
        {"name": "Chris Austin", "jobTitle": "General Manager", "companyName": "Commonwealth Bank"},
        {"name": "Ishaan Sharma", "jobTitle": "General Manager", "companyName": "Commonwealth Bank"},
        {"name": "Barry Parker", "jobTitle": "General Manager", "companyName": "Commonwealth Bank"},
        {"name": "Eric Drok", "jobTitle": "Vice Chairman", "companyName": "Commonwealth Bank"},
        {"name": "Kathy Condos", "jobTitle": "Chief Operating Officer", "companyName": "Commonwealth Bank"},
        {"name": "Sam Booyachi", "jobTitle": "CIO for Commsec", "companyName": "Commonwealth Bank"},
        {"name": "Richard Nesbitt", "jobTitle": "General Manager", "companyName": "Commonwealth Bank"},
        {"name": "Jason Chan", "jobTitle": "Chief Operating Officer", "companyName": "Commonwealth Bank"},
        {"name": "Yuri Belenky", "jobTitle": "General Manager , Cloud Enablement", "companyName": "Commonwealth Bank"},
        {"name": "Simryn De Jager", "jobTitle": "General Manager", "companyName": "Commonwealth Bank"},
        {"name": "Martijn Verbree", "jobTitle": "Chief Information Risk Officer", "companyName": "Commonwealth Bank"}
    ]
}

DUMMY_CBA_GTM_STRATEGY = {
    "outreach_strategy": "Our GTM strategy for Commonwealth Bank will focus on leveraging existing connections and highlighting Lorikeet's ability to address their specific pain points around AI integration in customer support.\n\n1.  **Leverage Connections**: William Perry will introduce us to Eric Drok and Barry Parker. These warm introductions will be crucial for initial engagement.\n2.  **Targeted Outreach**: Simultaneously, we'll conduct targeted outreach to the CTO, Acting CTO, CIO, and Chief Data & Analytics Officer via email and LinkedIn, referencing their public statements on AI strategy and the challenges they've faced.\n3.  **Value Proposition**: Our messaging will emphasize how Lorikeet can improve call routing, enhance agent performance, and mitigate the risk of negative PR associated with AI-driven job displacement.\n4.  **Follow-up**: After initial emails, we will follow up within 3 business days, referencing a relevant article or CBA initiative related to AI and customer experience. For LinkedIn outreach, we'll personalize connection requests by referencing shared connections or common interests.\n5.  **Demo and Proposal**: After establishing initial contact, we'll schedule a personalized demo showcasing Lorikeet's multimodal capabilities and integrations with Salesforce and Zendesk. Following the demo, we'll submit a tailored proposal outlining the ROI and projected impact of Lorikeet on CBA's customer support operations.\n6.  **Nurture and Expand**: After initial engagement, we'll continue nurturing relationships with key stakeholders, sharing relevant content and case studies, and exploring opportunities to expand Lorikeet's implementation across other areas of CBA.",
    "message_templates": [
        {
            "target_role": "CTO",
            "channel": "Email",
            "message": "Subject: Enhancing Customer Support with AI at the Commonwealth Bank\n\nDear [CTO Name],\n\nI'm reaching out following CBA's public commitment to using AI for enhanced customer experiences. Lorikeet, an AI-native customer support platform, addresses the challenges you've highlighted regarding balancing AI adoption with workforce management. Our platform can automate up to 80% of support queries, allowing your agents to focus on complex issues and improving overall customer satisfaction. Would you be open to a brief discussion about how Lorikeet can help CBA achieve its AI goals?\n\nBest regards, [Your Name]"
        },
        {
            "target_role": "General Manager",
            "channel": "LinkedIn Connection Request",
            "message": "Hi [General Manager Name],\n\nI'm connecting with you as I was impressed by CBA's innovative use of AI in customer service and William Perry suggested I get in touch. Lorikeet's AI platform can help enhance your customer support operations by automating routine tasks and improving agent efficiency. I'd love to connect and share more.\n\nBest regards, [Your Name]"
        }
    ]
}

DUMMY_CBA_PRIORITIZED_PROSPECTS = [
    {'name': 'Eric Drok', 'role': 'Vice Chairman', 'company': 'Commonwealth Bank', 'connection_status': True, 'connected_with': 'William Perry'},
    {'name': 'Barry Parker', 'role': 'General Manager', 'company': 'Commonwealth Bank', 'connection_status': True, 'connected_with': 'William Perry'},
    {'name': 'Rodrigo Castillo', 'role': 'Chief Technology Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Simon Birch', 'role': 'Acting Chief Technology Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Nora Waugh', 'role': 'Chief Information Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Andrew Mcmullan', 'role': 'Chief Data and Analytics Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Kathy Condos', 'role': 'Chief Operating Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Jason Chan', 'role': 'Chief Operating Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Nathan Chandler', 'role': 'General Manager', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Chris Austin', 'role': 'General Manager', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Ishaan Sharma', 'role': 'General Manager', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Sam Booyachi', 'role': 'CIO for Commsec', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Richard Nesbitt', 'role': 'General Manager', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Yuri Belenky', 'role': 'General Manager , Cloud Enablement', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Simryn De Jager', 'role': 'General Manager', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Martijn Verbree', 'role': 'Chief Information Risk Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''},
    {'name': 'Andrew Hinchliff', 'role': 'Group Chief Risk Officer', 'company': 'Commonwealth Bank', 'connection_status': False, 'connected_with': ''}
]