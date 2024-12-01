# I-X Team | Fetch.ai x Moderna Hackathon

## Team:
- Abdulaziz Alsaad
- Santosh Kumar Saravanan
- Asish Sayan
- Lyson Ober
- Sherwin Vadakkumcherry

This reposatiry includes the submission of Fetch.Ai hackathon in collaboration with Moderna. 

## Challenge: 
Produce a dashboard that uses Fetch.ai agents to support medical affairs with managing vaccination hesitancy.

## Flow Diagram
Flow of agents supporting the dashboard
![Copy of FetchAI-Hackathon](https://github.com/user-attachments/assets/95db1518-0e7d-433e-9442-0a07ecebaf52)

## Dashboard overiew:
https://drive.google.com/file/d/1ttwWBQwKRKPtljPQLFHVn_-ksMx9BIgB/view


## Dashboard Walkthrough:

## Fetch.ai Agents: 

- Vaccine Information Agent: This agent queries vaccine knowledge project website and retrieves vaccine specific information.
- Twitter Agent: This agent searches for tweets containing a specified keywords and returns the top 10 results which is used for dashboard sentiment analysis.
- User Agent: This agent acts as an orchestrator for the Moderna vaccination dashboard. The agent communicates with another agents at a specified address to retrieve required information.
- Vaccine hesistancy  agent: This agent queries vaccine hesitancy based on age from the office of national statistics data persisted in supabase DB.
- Vaccine hesistancy education agent: This agent queries vaccine hesitancy based on education from the office of national statistics data persisted in supabase DB.
- Vaccine hesistancy employment agent: This agent queries vaccine hesitancy based on employment from the office of national statistics data persisted in supabase DB.
- Vaccine hesistancy health statuts agent: This agent queries vaccine hesitancy based on health status from the office of national statistics data persisted in supabase DB.
- Vaccine hesistancy number of people agent: This agent queries vaccine hesitancy based on number of people in household from the office of national statistics data persisted in supabase DB.
- Vaccine hesistancy sex agent: This agent queries vaccine hesitancy based on gender from the office of national statistics data persisted in supabase DB.
- Health news report agent: This agent queries current health news report based on synthetic data generated with random news points.



