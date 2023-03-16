# Vehicle Identification Service

## Description
Simple backend to identify a vehicle model based on an image. This service calls an external API (CarNET) to get the vehicle model.

## [How we used the AI tools to generate this project](documentation/WORKFLOW.md)



## Install
* Create virtual env
```shell
  $ python -m venv venv
  ```
* Load virtual env
```shell
  $ source venv/bin/activate
  ```
* Install dependencies
```shell
  $ pip install -r requirements.txt
  ```

* Go to CarNET site and copy your cookies (using your browser developer tool in https://carnet.ai/#free-tire) in ``local.env`` and also set the ``CARNET_URL``


* Load environment variables
```shell
  $ set -a && source local.env
  ```

* Run app
```shell
  $ python main.py
  ```
