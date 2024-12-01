{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red15\green112\blue1;\red144\green1\blue18;\red19\green118\blue70;\red107\green0\blue1;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c0\c50196\c0;\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c52549\c34510;\cssrgb\c50196\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf0 \strokec4  uagents \cf2 \strokec2 import\cf0 \strokec4  Agent, Context, Model\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  requests\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  bs4 \cf2 \strokec2 import\cf0 \strokec4  BeautifulSoup\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Define the request and response models\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 class\cf0 \strokec4  VaccineInfoRequest(Model):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     keyword: \cf2 \strokec2 str\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 class\cf0 \strokec4  VaccineInfoResponse(Model):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     results: \cf2 \strokec2 list\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Initialize the agent\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 agent = Agent(name=\cf6 \strokec6 "vaccine_agent"\cf0 \strokec4 , port=\cf7 \strokec7 8000\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Define the message handler\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 @agent\cf0 \strokec4 .on_message(model=VaccineInfoRequest, replies=\{VaccineInfoResponse\})\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 async\cf0 \strokec4  \cf2 \strokec2 def\cf0 \strokec4  fetch_vaccine_info(ctx: Context, sender: \cf2 \strokec2 str\cf0 \strokec4 , msg: VaccineInfoRequest):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     keyword = msg.keyword\cb1 \
\cb3     url = \cf6 \strokec6 'https://vaccineknowledge.ox.ac.uk/search/site/'\cf0 \strokec4 +keyword\cb1 \
\
\cb3     \cf2 \strokec2 try\cf0 \strokec4 :\cb1 \
\cb3         response = requests.get(url)\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  response.status_code != \cf7 \strokec7 200\cf0 \strokec4 :\cb1 \
\cb3             ctx.logger.error(f\cf6 \strokec6 "Failed to fetch data. Status code: \{response.status_code\}"\cf0 \strokec4 )\cb1 \
\cb3             \cf5 \strokec5 #await ctx.send(sender, VaccineInfoResponse(results=[]))\cf0 \cb1 \strokec4 \
\cb3             \cf5 \strokec5 #return\cf0 \cb1 \strokec4 \
\
\cb3         soup = BeautifulSoup(response.text, \cf6 \strokec6 'html.parser'\cf0 \strokec4 )\cb1 \
\cb3         results = []\cb1 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  link \cf2 \strokec2 in\cf0 \strokec4  soup.find_all(\cf6 \strokec6 'a'\cf0 \strokec4 , href=\cf2 \strokec2 True\cf0 \strokec4 ):\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  keyword.lower() \cf2 \strokec2 in\cf0 \strokec4  link.text.lower():\cb1 \
\cb3                 results.append(\{\cf6 \strokec6 "name"\cf0 \strokec4 : link.text, \cf6 \strokec6 "url"\cf0 \strokec4 : link[\cf6 \strokec6 'href'\cf0 \strokec4 ]\})\cb1 \
\
\cb3         \cf2 \strokec2 await\cf0 \strokec4  ctx.send(sender, VaccineInfoResponse(results=results))\cb1 \
\cb3     \cf2 \strokec2 except\cf0 \strokec4  Exception \cf2 \strokec2 as\cf0 \strokec4  e:\cb1 \
\cb3         ctx.logger.error(f\cf6 \strokec6 "Error processing request: \{e\}"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 await\cf0 \strokec4  ctx.send(sender, VaccineInfoResponse(results=[]))\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 __name__\cf0 \strokec4  == \cf6 \strokec6 "__main__"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 print\cf0 \strokec4 (f\cf6 \strokec6 "Agent Address: \{agent.address\}"\cf0 \strokec4 )\cb1 \
\cb3     agent.run()\cb1 \
\
}