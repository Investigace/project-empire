# Project Empire

Project Empire is a set of tools helping with keeping information about assets and companies of inluential people or groups. It was originally created for keeping information about business structures of prime minister and owner of vast business empire Andrej Babiš, but is now generalized and can be used for any person or group of interest.

Project was created by [České centrum pro investigativní žurnalistiku, o.p.s.](https://www.investigace.cz/) and between September 2021 and January 2022 was funded by [Stars4Media innovation programme](https://stars4media.eu/).

Currently running Project Empire wikis:

| Person of interest | Project Empire wiki              |
| ------------------ | -------------------------------- |
| Andrej Babiš       | https://noveimperiumab.vlki.cz/ (UPDATE WITH FINAL DOMAIN) |
| Daniel Křetínský   |  https://empirekretinsky.vlki.cz/ (UPDATE WITH FINAL DOMAIN)  |

If you have any questions related to this project, please contact (FILL EMAIL)

## Table of contents

- [How Project Empire works?](#how-project-empire-works)
  * [Database](#database)
  * [Wiki](#wiki)
  * [Scripts](#scripts)
- [How to use Project Empire?](#how-to-use-project-empire)
  * [1. Start your database](#1-start-your-database)
  * [2. Install wiki](#2-install-wiki)
  * [3. Push data from database to the wiki](#3-push-data-from-database-to-the-wiki)
  * [4. Learn to use other scripts](#4-learn-to-use-other-scripts)
- [License](#license)

---

## How Project Empire works?

There are 3 main parts to a working Project Empire. **Database**, which is a Google spreadsheet containing all the data about business structures of selected person of interest. **Wiki**, which makes it possible to publicly browse through the database. And **scripts**, which most importantly offer a way to push data from the database to wiki.

Let's show all the parts using demo data. We have put together tiny sample from our first database done for Andrej Babiš. Here are links for both the database and wiki:

* Demo database: https://docs.google.com/spreadsheets/d/1EJ-bP-qqTjZx2jcY6hfG3uAKvn6_FtCA-vqD4qVzn-k/edit
* Demo wiki: https://project-empire-wiki-demo.vlki.cz/

### Database

If you open the database, you can see that on the first sheet there is an introduction to that specific database. In our demo database we have 6 legal entities, 2 people and 2 subsidies. All the data is then organized in separate sheets.

If you are interested in the legal entities like companies, trusts, etc., you can browse them in the sheet "1. Legal entities". People are in sheet "2. People" and subsidies in "3. Subsidies". The rest of sheets are additional information for each of these base data types.

One of the important parts of databases with business structures is keeping the relationships between legal entities and people. You can find these in sheets "1.1. Legal entities owners" and "1.2. Legal entities other relationships". It is important to keep the data organized like this as the scripts rely on the structure.

Normally the database would not be publicly available, but only shared to people collaborating on the data. That's why part of Project Empire is also wiki, which allows publishing the database for anyone to browse through.

### Wiki

Project Empire wiki is a custom-configured [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) which is prepared to be run via [Docker](https://www.docker.com/) anywhere you want — in the cloud or on your server. After installing, you can customize it yourself to present your data exactly how you want.

You can see that the [demo wiki](https://project-empire-wiki-demo.vlki.cz/) right now contains the same number of legal entities, people and subsidies as the database. And if you open for example the company [AGROFERT, a.s.](https://project-empire-wiki-demo.vlki.cz/index.php/AGROFERT,_a.s.), you can see, apart from the basic information, all the owner and other relationships the company has and media mentions from the database together at that one page. Plus offers links to the related pages. There lies the value of the wiki — it displays the data clearly and in easily browsable fashion.

But how you get the data from the database to the wiki? The data don't have to be manually updated, we have a script, which is takes the database spreadsheet and pushes its data to the wiki.

### Scripts

There are few different scripts as part of Project Empire, which all help with gathering data about business structures, but the most important script is definitely the one pushing the data from the database to the wiki.

The script is a Python command line script, so you have to be at least slightly versed in running command line scripts to be able to use it, even though we tried to simplify its usage as much as possible. The process is then that you clone this GitHub repository to your machine, set up Python virtual environment and just run the script.

And that's it. That's the whole Project Empire. If you want to install it and play with it yourself, you can find the documentation for it below.

---

## How to use Project Empire?

### 1. Start your database

First step in using Project Empire is to set up the database. Since the database is a simple Google spreadsheet, you can do that by making a copy of either the demo database spreadsheet or the empty database spreadsheet. You should be able to make a copy by clicking option _File > Make a copy_ and filling information about your new spreadsheet.

* Demo database spreadsheet: https://docs.google.com/spreadsheets/d/1EJ-bP-qqTjZx2jcY6hfG3uAKvn6_FtCA-vqD4qVzn-k/edit
* Empty database spreadsheet: https://docs.google.com/spreadsheets/d/19syMW_V3G6AmG0yIHBZzys2RfBH4zsAbObO5FrhjB68/edit

When copied, you should fill your person or group of interest on sheet _0. Introduction_ and then continue with updating data on the other sheets.

We recommend sharing the spreadsheet only to the specific people who will be collaborating on the data and not publicly as it may contain sensitive information and to have a place for keeping also private information which is not available through wiki.

### 2. Install wiki

Next step is installing Project Empire wiki. As mentioned before, wiki is a custom-configured [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) which is prepared to be run via [Docker](https://www.docker.com/). We chose Docker as that way it can be safely run the same even on different systems.

### 2.1. Set up server with docker and docker-compose

Start the installation by setting up a server preferrably running latest Ubuntu (at the time of writing the Ubuntu LTS version was 20.04), with docker and docker-compose installed, SSH access, public IPv4 address and reachable HTTP (80) and HTTPS (443) ports. It can be your own physical server as well as server set up by some cloud services provider.

We expect that you are able to set up a server like that, but if not, [here is a tutorial how to set up such server on Google Cloud](/docs/set_up_wiki_server_on_google_cloud.md).
### 2.2. Update DNS records

Continue with picking the domain where you want the wiki to be run and updating the DNS records. The wiki is prepared to be run on either separate domain (e.g. project-empire-wiki.org) or subdomain (e.g. project-empire-wiki.example.org). In case of separate domain, you want to create 2 A records pointing to the public IPv4 address of server, one for the plain domain and one for www subdomain (wiki takes care of the redirecting then). In case of subdomain, you want one A record for that subdomain pointing to the public IPv4 address of the server.

Example: If the server has public IPv4 address 1.2.3.4 and you want the wiki to run at subdomain project-empire-wiki.example.org, you want to add A record for project-empire-wiki.example.org with value 1.2.3.4.

After changing the DNS records please wait for them to propagate before continuing with the installation, because obtaining HTTPS certificates from Lets Encrypt depends on server being accessible at the picked domain or subdomain.

### 2.3. (optional) Set up Amazon S3 bucket for backups

Optionally, you can create [Amazon S3](https://aws.amazon.com/s3/) bucket for backups of the wiki. Empire data in the wiki obviously does not have to be backed up, because they can always be repushed from database spreadsheet, but other wiki settings like uploaded images, custom pages, etc. would be gone if something happens to your server. Note that together with the bucket you need to create also user with the programmable access via Access key ID and Secret access key.

Even though this step is optional, wee strongly recommend creating Amazon S3 bucket for the backups.

### 2.4. Set up wiki using docker

When you have a server and, optionally, backup bucket set up, it is time for the actual installation of Project Empire wiki.

First, you will need to clone this repository to the server. For example in the home folder of the logged-in user run following:

```
$ git clone git@github.com:vlki/project-empire.git
```

That should create `project-empire` folder with `wiki` folder inside. Go to the wiki folder.

```
$ cd project-empire/wiki
```

Next is providing the configuration. Copy `.env.example` and rename the copy to `.env`. After that, edit `.env` with editor of your choice and fill in your configuration. Here we will be using `vim`.

```
$ cp .env.example .env
$ vim .env
```

Each of the configuration options in `.env` is explained, so go through each of them and set them as you need. When finished, save the changes to the `.env` file and close it.

Now we run the installation. Type in following:

```
$ docker-compose up
```

That should build images of all the wiki services, create docker containers and run them. Note that it can take few minutes to finish. If everything is fine, the output should end with similar to following:

![](/docs/screenshots/wiki-installation.png?raw=true)

At this point, the wiki is installed and running at your picked domain, but without correct certificates - if you navigate to the domain in the browser you should see warning. That is to be expected, because the certificates were just obtained from Lets Encrypt and nginx service needs to be restarted to load them. Since you cannot run the wiki in the terminal forever anyway, we will restart the wiki as daemon.

First hit Ctrl+C to stop current running services (you might have to wait a bit till they stop), And when that is done, type in following, which will start the services as daemon in background.

```
$ docker-compose up -d
```

Now if you navigate to the domain in your browser, you should see your Project Empire wiki without any warnings, ready to be used.

### 3. Push data from database to the wiki

(TODO)

### 4. Learn to use other scripts

(TODO)

## License

Everything in this repository is licensed under [GNU General Public License v3.0](https://github.com/vlki/project-empire/blob/main/LICENSE).

