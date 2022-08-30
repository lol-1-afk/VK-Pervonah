# VK-Pervonah

## Description
It is bot to create first comment in new post in VK group

## Installation
Just download this repo

## Getting api key
go to https://vkhost.github.io , selecet "vk.com", then click on "allow" button on new window
if your browser addres you will see token ![image](https://user-images.githubusercontent.com/58441229/187542302-d5d4f522-dd02-4f8c-8e86-53889e61f61e.png)
it starts after "access_token=" and ends before "&expires_in"


## Docks
- https://dev.vk.com/method/wall.get 
- https://dev.vk.com/method/wall.createComment

## Settings.json
"token" - your vk api token
"group_id" - id if group to create first comment
"text" - text of comment
"offset" - offset by posts
"delay" - delay between checking new post
