## Assignmentmember


## Technology
- Framework: Django Rest Framework
- Database: Postgres
- Deployment: Heroku from git connect

## API Testing Client
- Postman

### API Endpoints
1. Add user \
*url*: https://members-tracker.herokuapp.com/api/usertracker/user \
*method*: POST \
*body*: user json object

2. Add user activity_periods \
*url*: https://members-tracker.herokuapp.com/api/usertracker/user_activity/{user_email}/{user_hash} \
*method*: POST \
*body*: json object with start time and end time

3. Get all Members \
*url*: https://members-tracker.herokuapp.com/api/usertracker/get_members \
*method*: GET 

**P.S. More details about the calling of the APIs are present in Test/details.txt**

