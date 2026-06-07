 SimEd Studio Watson Orchestrate Agent

 🚀 Live Agent

The SimEd Studio conversational AI agent is deployed and running on IBM Watson Orchestrate.

 Access the Agent Now

👉 Go to: https://orchestrate.ibm.com  
🔑 Log in with your IBM Cloud account  
🔍 Find: "SimEd Studio Orchestrator"  
💬 Click: "Test agent" and start chatting



Agent Overview

Name: SimEd Studio Orchestrator  
Platform: IBM Watson Orchestrate (IBM Cloud)  
Model: GPT-OSS 120B  
Status: 🟢 LIVE - Available 24/7  


What It Does

The agent guides teachers through a 4-step process:

 Step 1: Class Twin Builder
- Asks 5-10 questions about your class
- Collects: class size, proficiency levels, engagement, constraints
- Creates anonymized classroom profile

 Step 2: Scenario Designer  
- Proposes 3 teaching strategy alternatives
- Based on your stated teaching goal
- Scenarios: Traditional Lecture, Small Groups, Project-Based

 Step 3: Simulation Runner
- Runs 100 Monte Carlo simulations
- Tests each scenario on your class twin
- Estimates: participation, workload, equity, Qiyas impact

 Step 4: Insight Narrator
- Converts results into Arabic/English narratives
- Highlights risks and benefits
- Recommends best scenario for your goal



 Languages

🇸🇦 Arabic - Primary interface language  
🇬🇧 English - Subtitles and support



 How to Replicate This Agent

If you want to create your own SimEd agent:

 Prerequisites
- IBM Cloud account (free tier available)
- Watson Orchestrate access

 Steps

1. Go to Watson Orchestrate
   - https://orchestrate.ibm.com
   - Create new agent

2. Configure Profile
   - Name: "SimEd Studio Orchestrator"
   - Description: "AI classroom simulation lab for teachers"

3. Set Behavior Instructions
   - Copy from: `agents/AGENT_INSTRUCTIONS.md`
   - Paste into Behavior section

4. Add Guidelines
   - Copy from: `agents/AGENT_GUIDELINES.md`
   - Add 2-3 guidelines for safety

5. Configure Welcome Message
   - مرحباً! Welcome to SimEd Studio - your AI classroom simulation lab. I'll help you safely test teaching strategies before trying them with real students. What class would you like to plan for today?

6. Add Quick Start Prompts
   - "I want to improve student participation without increasing my workload"
   - "Help me decide how to use AI tools in my English class safely"
   - "Compare traditional lecture vs group work for my next unit"

7. Deploy
   - Click "Deploy" button
   - Test with: "hi"



 Current Features

✅ Conversational interface (Arabic/English)  
✅ Classroom data collection  
✅ Scenario generation  
✅ Simulation workflow  
✅ Insight narratives  
✅ Risk detection  

 Planned Features

⏳ Madrasati LMS integration  
⏳ Dashboard visualization  
⏳ Student outcome tracking  
⏳ Ministry reporting features  



 Support

📧 Email: support@simed-studio.edu  
💬 Issues: GitHub Issues  
📚 Docs: /docs folder  


## License

MIT License – See root LICENSE file


Built for Saudi Vision 2030 education transformation