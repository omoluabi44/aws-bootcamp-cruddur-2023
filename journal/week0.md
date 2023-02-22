# Week 0 — Billing and Architecture
## I installed `AWS` cli using gitpod browser environment 
i update my `.gitpod.yml` and include the follow syntax  
```
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```  
this syntax install aws cli in my env and also install automatically when i restart my env.  

![Screenshot (258)](https://user-images.githubusercontent.com/110730304/220556179-816b8dfc-5e2e-4935-aa6e-47b3e935807f.png)


## Created and IAM user named Crudder
in this session i created an `IAM` user and give the following permission  

- Administrator access
- give cli access 
- generated security access key 
- also download the csv for future referrence  
![Screenshot (257)](https://user-images.githubusercontent.com/110730304/220555708-596aa071-80a9-4be7-ade3-9e8f80a03af9.png)

## Billing alarm
created billing alarm to recieved alart   

 
![Screenshot (259)](https://user-images.githubusercontent.com/110730304/220557397-233657ec-e29f-414f-b4d7-f320da4388a6.png)

## SNS Topic 
i created sns topic to deliver the alarm 
I use the following cli command to create the sns topic

```
aws sns create-topic --name billing-alarm
```
[link for the template here](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html)  

i created the sns topic before the billing alarm 

## BUDGET
in this session i create a budget name cruddur budget and  generated my `userID` using the following syntax
```
aws sts get-caller-identity --query Account --output text
```

then i update the json files and create my budget using this syntax
```
aws budgets create-budget \
    --account-id AccountID \
    --budget file://aws/json/budget.json \
    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json
```
[find the template use under example](https://docs.aws.amazon.com/cli/latest/reference/budgets/create-budget.html) 
![Screenshot (260)](https://user-images.githubusercontent.com/110730304/220560233-f6c8c57b-4592-46ad-bd04-617791968813.png)

## ARCHITECTURE DIAGRAM
created the architecture

[view my architecture diagram here](https://lucid.app/lucidchart/7d7e3e02-49d1-4961-b507-4c7a9fef7586/edit?viewport_loc=-1331%2C-560%2C3081%2C1240%2C0_0&invitationId=inv_2be0daf7-fec4-4264-afbc-9a44f2f12f15)

![WhatsApp Image 2023-02-22 at 09 13 52](https://user-images.githubusercontent.com/110730304/220562724-c78ef740-9f4d-435d-9e07-34ecdc9cca40.jpg)

## NAPKING DIAGRAM
[View my Napkin idiagram](https://lucid.app/lucidchart/157c8691-b074-4b90-8e42-ba6721bd2a4b/edit?viewport_loc=-574%2C-81%2C2086%2C900%2C0_0&invitationId=inv_1f16cd53-2e89-493a-90d5-1bcaf33b6d44)
![WhatsApp Image 2023-02-22 at 09 19 38](https://user-images.githubusercontent.com/110730304/220562767-2ac4824a-85b2-4312-ae48-df19accd7e20.jpg)

