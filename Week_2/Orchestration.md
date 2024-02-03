# Intro 
Welcome to Week 2 of the Data Engineering Zoomcamp! 🚀😤 This week, we'll be covering workflow orchestration with Mage.

## Intro to Orchestration


Used Docker which is a containerization service. Mage and a postgress database are going to run in this Docker environment. Going to do some transformations on it. Load it to postgress and going to load it to Google Cloud Storage and then going to perform some more transformation using pandas Apache Arrow and then load it to Google big query. 

A large part of data engineering is extracting transforming loading data between all these different sources and so when I say orchestration I'm defining that as a process of dependency management facilitated through Automation and automation is the key piece here. The idea is to minimize manual work. 

So the data orchestrator really manages scheduling triggering monitoring and even resource allocation for your data engineering workflows. Every workflow requires sequential steps. Steps are tasks or blocks in Mage. Workflows are a dag or a pipeline in data engineering speak.

Orchestration is one of the under currents and so when we say orchestration is an undercurrent that means it happens throughout the entire life cycle of data engineering. 

That is orchestration is kind of key to the entire process of building data engineering pipelines and so it's really important to have good orchestrator to have a good solution that fits your case.

A good orchestrator handles workflow management. They. Define schedule manage workflows efficiently. They ensure tasks are executed in the right order um and it manages dependencies as we've kind of discussed second automation. Make sure that your orchestration solution  is really good at automating things third  error handling and recovery.

Orchestrators need to come up with built-in solutions for handling errors conditional logic branching  and retrying failed tasks um recovery.  There needs to be a way to recover lost data. 
Orchestrators can handle in those situations monitoring and alerting ideally an orchestrator. If a pipeline fails or if those retries do to happen will send you some sort of notification or has the capability to do that at least um resource optimization. 
If your orchestrator is managing where jobs are executed. Ideally it would play some role in optimizing the best route for that execution. So resource optimization is another good characteristic to look forward in an orchestrator observability. A very important piece of data engineering is having visibility into every part of the data Pipeline and because orchestrators are undercurrent and they help manage the entire process from start to finish. They're going to be very important for observability and ideally would come with built-in observability functionality. Debugging is a part of observability and your orchestrator should let you debug your data pipelines very easily. Lastly because it has these observability debugging functionalities and it's a part an undercurrent of the entire process ideally your orchestrator should help you with compliance or auditing for your data. 

A lot a good orchestrator prioritizes developer experience has to have three components feedback loops, *cognitive load* and Flow State. Flow State's kind of like that feeling of flow you know almost effortless development.

*Feedback loops* the ability to iterate quickly to fail fast to build really cool stuff and get tangible feedback immediately also very important and cognitive load in the tools you're working with are you ending your day. 


What we're looking for in a good orchestrator is this thing that accomplishes all of the data engineering tasks that I mentioned earlier but also that facilitates rapid and almost seamless development of awesome data pipelines. 

Engineering Process uh processes your data engineering workflows and the orchestrator is kind of keeping everything in check. It's keeping an eye on everything it understands sort of the symphony that you got going on and it's able to properly adjust maybe the tempo maybe you know the the volume. 

All these different things to make sure that your data workflows. You know operate smoothly and and get the desired outcomes that you're looking for.0