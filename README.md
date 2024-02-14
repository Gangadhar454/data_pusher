

# Data Pusher

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installion](#installation)
- [Getting Started](#gettingstarted)

## Introduction
 Data Pusher is a web server to receive data into the app server for an account and send it across different platforms (destinations) from that particular account using webhook URLs.


The backend architecture is designed with two services and one Queue

### Services

1. **Data Handler Service:**
   - Django server responsible for handling http requests.

2. **Worker Service:**
   - Connected to the `queue`.
   - The Worker service executes a task (`send_data_to_destinations`).
   - The `/server/incoming_data` api call the `send_data_to_destinations` function by pushing a message to queue. so it reduces the load on main service(data handler service)


### Storages

1. **SQLlite**
   - Used for storing `Accounts` and `Destinations`.

### Queues

1. **queue(rabbitmq):**
   - Connects the Worker service.
   - `data handler` service pushes messages to queue and `worker` service consumes the messages .


## Requirements
1. Latest version of `docker` and `docker compose` [Link](https://docs.docker.com/engine/install/ubuntu/)
2. After installing `docker` and `docker compose` , do post installation steps [Link](https://docs.docker.com/engine/install/ubuntu/)
3. `make` (sudo apt install make) for easy use

## Getting Started
1. Go to the main directory (where the make file exists)
2. build the backend services
   ```bash
   make build
3. if step-2 fails
   ```bash
   docker compose build
4. start the services
   ```bash
   make restart
5. if step-4 fails
   ```bash
   docker compose up

 ### ACCOUNT module API Endpoints
 1. #### API to Create Account
    `POST` - http://localhost:8000/account/
    
    Payload:
    
    ```json
    {
        "account_name": "gangdhars2",
        "email": "gangs2@gamil.com",
        "website": "https://gangs.com"
    }
    ```
    ![Screenshot from 2024-02-14 10-00-38](https://github.com/Gangadhar454/data_pusher/assets/36883246/ed56a434-b517-4e97-9f6a-239f79fffc47)

  2. #### API to fetch an Account
     `GET` - http://localhost:8000/accout/?account_id=3
     ![Screenshot from 2024-02-14 10-12-25](https://github.com/Gangadhar454/data_pusher/assets/36883246/76d80f54-05ad-4c16-b532-d431b528ed97)

  3. ### API to update an Account
     `PATCH` - http://localhost:8000/account/

     Payload:
     ```json
     {
          "account_id": 3,
          "email": "gangs4@gamil.com",
          "account_name": "gangdhars4",
          "secret_token": "L6vdp2M0NO9ADiBEq77j1WtiEPcDHEw2",
          "website": "hello.com"
      }
     ```
     ![Screenshot from 2024-02-14 10-18-02](https://github.com/Gangadhar454/data_pusher/assets/36883246/89e7bfaf-bc26-4d72-b71c-7b80fb46178b)

  4. ### API to Delete an Account
     `DELETE` - http://localhost:8000/account/

      Payload:
     ```json
     {
          "account_id": 2,
          "secret_token": "5sffNPmoAfbEapEs84zbvq5YZYmSYjKn"
      }
     ```
     ![Screenshot from 2024-02-14 10-21-32](https://github.com/Gangadhar454/data_pusher/assets/36883246/d292faa4-575b-4fe9-9d26-6da357aa94c2)


 ### Destination module API Endpoints
 1. #### API to Create Destination
    `POST` - http://localhost:8000/destination/
    
    Payload:
    
    ```json
    {
        "account_id": 3,
        "url": "https://ww.google.com",
        "http_method": "GET",
        "headers": {
            "APP_ID": "1234APPID1234",
            "APP_SECTET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s",
            "ACTION": "user.update",
            "Content-Type": "application/json",
            "Accept": "*"
        }
    }
    ```
    ![Screenshot from 2024-02-14 10-54-43](https://github.com/Gangadhar454/data_pusher/assets/36883246/11c975bd-2f70-4a91-841f-243308d39878)


  2. #### API to fetch a Destination
     `GET` - http://localhost:8000/destination/?account_id=3
     ![Screenshot from 2024-02-14 11-29-29](https://github.com/Gangadhar454/data_pusher/assets/36883246/2e3325c5-b446-41b6-816a-1ec496cd89b3)

  4. ### API to update a Destination
     `PATCH` - http://localhost:8000/destination/

     Payload:
     ```json
     {
         "destination_id": 3,
         "url": "https://ww.facebook.com",
         "http_method": "GET",
         "headers": {
             "APP_ID": "1234APPID1234",
             "APP_SECTET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s",
             "ACTION": "user.update",
             "Content-Type": "application/json",
             "Accept": "*"
         }
     }
     ```
     ![Screenshot from 2024-02-14 11-24-24](https://github.com/Gangadhar454/data_pusher/assets/36883246/5be4941c-f1c9-4132-bfaa-46bdbc9e3534)

  5. ### API to Delete a Destination
     `DELETE` - http://localhost:8000/destination/

      Payload:
     ```json
     {
         "destination_id": 2
     }
     ```
     ![Screenshot from 2024-02-14 11-21-18](https://github.com/Gangadhar454/data_pusher/assets/36883246/27ed5570-8d48-4ed4-83cc-553edc9a0e61)

 ### API to recieve data and send to Destinations
 `POST` - http://localhost:8000/server/incoming_data
 
 Payload:
 ```json
 {
     "account_id": 3,
     "secret_token": "L6vdp2M0NO9ADiBEq77j1WtiEPcDHEw2",
     "data": {
         "message": "Debited 500 from credit card"
     }
 }
 ```
![Screenshot from 2024-02-14 11-47-58](https://github.com/Gangadhar454/data_pusher/assets/36883246/eb4f3980-2ffc-4a14-8866-6ec78a1847c8)

`GET` - http://localhost:8000/server/incoming_data?account_id=3&secret_token=j98457&data={encoded data}
![Screenshot from 2024-02-14 11-49-40](https://github.com/Gangadhar454/data_pusher/assets/36883246/e558c52a-a9c0-4160-86e6-fec6290a8f65)

