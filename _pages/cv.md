---
title: Curriculum Vitae
layout: archive
permalink: /cv/
classes: wide
sort_by: date
sort_order: reverse
---

___


Education
======
### PhD in Computer Science, 2019 (expected)
* **Dissertation Title:** _An Algorithmic Approach to Coordinated Systems_ (working title)
* **Focus:** Computational Geometry, Algorithm Design, Computational Complexity
* **Advisor:** David M. Mount

### MS in Computer Science, University of Houston, 2011
* **Thesis Title:** _Playing Challenging Iterated Two-Person Games Well: A Case Study on the Iterated Traveler's Dilemma_
* **Focus:** Computational Intelligence and Game Theory
* **Advisor:** Predrag Tošić

### BS in Computer Science, University of Texas at Austin, 2005  
<br>

Work experience
======
### Locurio, Inc.
* 2015 to present: Co-Founder/Technology Lead

	Co-founder of consistently highest rated escape room experience in Seattle. Led technology design for one of two escape rooms and consulted on technical implementation for the second. Designed interactive puzzles from concept phase to implementation and contributed to story design. 

### University of Maryland Institute for Advanced Computer Studies (UMIACS)
* 2012 to 2013: Graduate Research Assistant

  Worked in the Computational Linguistics and Information Processing (CLIP) lab on a machine translation project that attempted to verify and refine translations through the comparison of back-translations with the original source text. This work involved the use and integration of an existing translation framework (cdec, developed by Chris Dyer) along with custom software for iterative comparison and translation refinement.
  
* 2011 to 2012: Programmer

  Supported the Foresight and Understanding from Scientific Exposition (FUSE) Program funded by the Intelligence Advanced Research Projects Activity (IARPA) by creating tools in Python for the detection of emerging technical concepts within a large corpus of published scientific, technical, and patent literature. These tools include a naive Bayes classifier, a custom UIMA-Python interface, and a series of feature extraction and metric gathering programs.

### United Space Alliance
* 2007 to 2011: Computer Science Staff II
  
  Developed, supported, and troubleshot math models within a real-time simulation architecture for the simulation of complex avionics, mechanical systems, space craft dynamics and kinematics, and natural environment effects for the NASA-JSC CEV Avionics Integration Laboratory.
  
### Multimedia Games (now Everi Holdings, Inc.)
* 2006 to 2007: Mod Programmer
  
  Modified library of existing video slot-machine games to comply with various regional laws and requirements. Includes debugging game logic, framework, and hardware, as well as modifying finite state machine based logic.
  
### Lockheed Martin Honors Graduate Internships
* 2005: Ground Systems Support Team

  Created and maintained an Access database with a Visual Basic front end for creating, editing, tracking, and closing Mission Control Center Incident Reports.
  
* 2004: Mission Support Section

  Translated and updated dynamics/kinematics modeling software for monitoring real-time Space Shuttle/International Space Station docking; includes translating from C++ and Fortran to Java and creating a Graphical User Interface for the resulting software.
  
* 2002, 2003: Dextrous Robotics Lab (DRL)

  Completed various projects in support of Robonaut, the DRL’s humanoid robot, and the Dexterous Anthropomorphic Robotic Testbed (DART); includes creating and assembling power distribution boards and force feedback hand controllers, graphical interfaces for text-to-speech and dynamical control capabilities, and conducting demonstrations and similar minor projects for visiting K-12 students, researches, and lab guests.
  
* 2001: Command System Section

  Provided software development and support for Real-Time Command Systems within the Johnson Space Center Mission Control Center.
  
* 2000: Consolidated Space Operations Contract

  Updated software package and subsequent training documentation for the Upper Atmosphere Research Satellite, including a real-time telemetry simulation program.

Publications
======
<ul>
  {% assign entries = site.publications | sort: 'date' | reverse  %}
	{% for post in entries %}
		<li>
			<p><a href="{{ post.url }}">{{ post.title }}</a>. {{ post.venue }}, {{ post.date | date: "%Y" }} [<a href="{{ post.paperurl }}">PDF</a>]</p>
		</li>
	{% endfor %}
</ul>
  
Talks
======
<ul>
  {% assign entries = site.talks | sort: 'date' | reverse  %}
  {% for post in entries %}
		<li>
			<p><a href="{{ post.url }}">{{ post.title }}</a>. {{ post.venue }}, {{ post.date | date: "%Y" }} </p>
		</li>
	{% endfor %}
</ul>
  
Teaching
======
<ul>
  {% assign entries = site.teaching | sort: 'date' | reverse  %}
  {% for post in entries %}
		<li>
			<p><a href="{{ post.url }}">{{ post.title }}</a>. {{ post.type }}. {{ post.venue }}, {{ post.date | date: "%Y" }} </p>
		</li>
	{% endfor %}
</ul>
  
Training
======
* Teaching at the Collegiate Level, provided by The Teaching and Learning Center at The University of Maryland, completed 2014
* Entrepreneurship Essentials Program, provided by the Maryland Technology Enterprise Institute at The University of Maryland, completed 2012

Service
======
* International Workshop on Combinatorial Algorithms (IWOCA) Reviewer, 2018
* Symposium on Computational Geometry (SoCG) Reviewer, 2018
* International Colloquium on Automata, Languages, and Programming (ICALP) Reviewer, 2015
* Graduate Student Representative on Computer Science Department Education Council, 2014
* Graduate Student Representative on Computer Science Department Council, 2013
* South Texas Regional FIRST Lego League Robotics Competition Judge, 2000

Awards
======
* Quest for Excellence Technical Achievement Award, United Space Alliance, 2008
* Jack Seriff Presidential Endowed Scholarship, University of Texas, anually 2001 - 2005
* Lockheed Martin Honors Graduate Internship, Lockheed Martin Space Operations, annually 2000 - 2004
* Elite Team Award, NASA-JSC Automation, Robotics, and Simulation Division, 2003
