################################problem set 3#####################################

Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it?
Ans:  To schedule tasks like downloading ISINs every 24 hours, I would use Celery with a beat scheduler. It’s reliable, handles task retries if something goes wrong, and works well with message brokers like Redis. For more complex workflows, Apache Airflow is another good option.
##################################################################################

Is it reliable enough; Or will it scale?
Yes, Celery is reliable enough for scheduling tasks and can scale effectively. It can handle high volumes of tasks by distributing them across multiple workers and can retry failed tasks automatically. For large-scale systems, using a message broker like Redis or RabbitMQ helps ensure smooth operation. However, for very complex workflows, a tool like Apache Airflow might be better as it offers advanced features for orchestration and better scaling in large environments

####################################################################################
If not, what are the problems with it?
While Celery is reliable and scalable, it does have some limitations:
Complex Setup: Celery requires setting up a message broker (e.g., Redis or RabbitMQ), which adds to the complexity of the system.
Monitoring and Debugging: It can be tricky to monitor and debug tasks, especially in large-scale applications, without the right tools.
Resource Usage: As the number of tasks grows, Celery workers can consume significant memory and CPU, potentially affecting performance.
Distributed Environment: Celery doesn’t inherently handle task distribution across multiple servers without additional configurations or setup.
For these reasons, tools like Apache Airflow may be a better choice for handling more complex workflows at scale.
####################################################################################

And, what else would you recommend to fix this problem at scale in production?
To fix the scalability issue in production, I would recommend using task queues like Celery or Redis Queue (RQ). These systems handle distributed tasks across multiple servers, allow for retries, and offer better task monitoring. They scale well in high-demand environments and provide reliable task execution, even for complex workflows. These tools help ensure tasks are completed without overloading the main application.

######################################################################################
B. In what circumstances would you use Flask instead of Django and vice versa? 

When to use Flask: Flask is ideal when you're working on small, lightweight projects or microservices where you need flexibility. It doesn’t come with many built-in tools, which gives you more freedom to pick and choose the components you need. It’s also a good choice if you're building simple APIs, quick prototypes, or learning the fundamentals of web development.

When to use Django: Django is a better option for larger projects that require a lot of built-in features. If you're building a more complex application, like an e-commerce site or social network, Django provides everything you need out of the box—an ORM, user authentication, an admin panel, and security tools. It’s designed to help you scale easily, making it a strong choice for team-based projects and bigger applications.

In short, use Flask for flexibility and smaller projects, and use Django when you need a structured, feature-rich framework for larger applications.


##########problem statement 2 ##############
To run problem statement 2
run cmd
python -m venv .venv
./.venv/scripts/activate
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
#################333
apis server- http://localhost:8000/
api/register to register as admin
api/login  to login as admin
api/admin to add apps
/home to see Added apps
/task to check task name
/profile to check profiles
/points to check points achieved
/app to modify apps


##########problem statement 1################
execute the python file
python regex,py to see extracted number from ids.
