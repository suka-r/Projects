# Parcel Delivery System

**High School Computing Science (CS 30)** · Python · Sep 2022 – Jan 2023

A console simulation of a national parcel service, built with object-oriented design.

## Features
- Sign in as one of 6 preset users located across 4 Canadian cities
- View your possessions and choose an item to send to another user
- Each parcel gets a random tracking ID (`UA-####`)
- Parcel status history is recorded as it moves: *Tracking ID Created → In Transit → Awaiting Pickup → Delivered*
- View the manifest history of shipped parcels

## Class design
| Class | Responsibility |
|---|---|
| `Person` | Holds a user's name, address, and possessions; creates and receives parcels |
| `Parcel` | Stores sender, recipient, and item; assigns its tracking ID |
| `Manifest` | Records every parcel and its status history |
| `CanadaPost` | Creates a post office for each city and looks up parcel tracking |
| `PostOffice` | Ships, receives, and hands off parcels, updating the manifest |
| `Truck` | Moves a parcel to the destination city's post office |

## Run it
Requires Python 3 (standard library only).
```
python parcel_delivery.py
```
