# Oracle HCM Cloud — Implementing Recruiting
## RAG Knowledge Base
> Source: Oracle Fusion Cloud Talent Management, Implementing Recruiting (2026)

---

# Overview of Recruiting

## Overview of Implementing Recruiting
*Chunk ID: OHR-REC-0001 | Chapter: Overview of Recruiting*

Overview of
This guide describes the implementation and setup tasks of Oracle Fusion Cloud Recruiting. It's primarily for
implementors and application administrators.
Using the tasks described in the guide, you can set up and configure the complete hiring process, which includes
the configuration of career sites, job application flows, candidate selection processes, job requisitions, job offers, job
application questionnaires, interview questionnaires, recruiting campaigns, candidate pools, agency hiring, and much
more.
Oracle Recruiting is part of Oracle Cloud HCM. To start the Oracle Recruiting implementation, someone with the
Application Implementation Consultant role (ORA_ASM_APPLICATION_IMPLEMENTATION_CONSULTANT_JOB) must
opt in to the offerings applicable to your business requirements. Refer to the Oracle Fusion Cloud Applications - Using
Functional Setup Manager guide to manage the opt-in and setup of your offerings.

---

## Before You Start
*Chunk ID: OHR-REC-0002 | Chapter: Overview of Recruiting*

You need to implement either of these products:
• Oracle Fusion Global Human Resources Cloud Service
• Oracle Fusion Talent Management Cloud Service
You're also required to configure other applications and elements. The table lists sources of information and a
description of what they contain, to help you set up the configuration that fits your business needs and processes.

Source

Contents

---

## Describes the ways in which you can integrate applications with Oracle HCM Cloud. Oracle HCM Cloud
*Chunk ID: OHR-REC-0003 | Chapter: Overview of Recruiting*

is a complete solution for HR processes from hire to retire including global HR, talent management,
workforce management, and payroll.

---

## Oracle Fusion Cloud HCM - Securing HCM
*Chunk ID: OHR-REC-0004 | Chapter: Overview of Recruiting*

Describes Human Capital Management Cloud security, types of roles and how to create them,
managing user accounts, types of security profiles and managing them and Oracle Fusion
Transactional Business Intelligence and Business Intelligence Publisher security.

---

## Recruiting and Candidate Experience Offering
*Chunk ID: OHR-REC-0005 | Chapter: Overview of Recruiting*

You use the Recruiting and Candidate Experience offering in the Setup and Maintenance work area to set up the
complete hiring process, which includes the configuration of career sites, job application flows, candidate selection
processes, job requisitions, job offers, job application questionnaires, interview questionnaires, recruiting campaigns,
candidate pools, agency hiring.
The following table describes the primary functional areas of the Recruiting and Candidate Experience offering. For the
full list of functional areas and features in this offering, use the Associated Features report that you review when you
plan the implementation of your offering.

---

## Recruiting and Candidate Experience
*Chunk ID: OHR-REC-0006 | Chapter: Overview of Recruiting*

Management

Configuration of common setup applicable to job requisitions, recruiting campaigns, talent community,
intelligent matching (recommendations), candidate search archiving, recruiting content library,
geography hierarchies, and hierarchy structure.

---

## Recruiting Setup and Maintenance Tasks
*Chunk ID: OHR-REC-0007 | Chapter: Overview of Recruiting*

Complete these setup tasks to align the configuration with your Hiring business process.
You must have the Recruiting Administrator role (ORA_PER_RECRUITING_ADMINISTRATOR_JOB) to access the
Recruiting and Candidate Experience functional areas from the Navigator menu (Home page > Navigator > My
Enterprise > Set Up and Maintenance).
Note: To access the Recruiting and Candidate Experience functional areas from the Settings and
Actions menu on the top right corner, you also need the privilege Manage Recruiting Administration
(IRC_MANAGE_RECRUITING_ADMINISTRATION).

Functional areas specific to Recruiting and Candidate Experience are:
• Recruiting and Candidate Experience Management
• Job Requisitions
• Candidate Experience
• Candidate Job Applications
• Job Offers
• Source Candidates
Each functional area contains a list of tasks that you can configure to align the configuration with your Hiring business
process. To view all tasks associated to a functional area, select All Tasks in the Show menu.

---

## Enterprise Recruiting and Candidate Experience Task to enable and configure features in
*Chunk ID: OHR-REC-0008 | Chapter: Overview of Recruiting*

Information
different areas.
Recruiting Management
• Requisition Number Generation Method:
Job requisition numbers can be generated
manually or automatically. When you
select the manual method, the user can
use any format for the requisition number,
you can't enforce a given prefix, suffix, or
pattern. When you select the automatic
method, the job requisition numbers
start according to the value entered in the
Requisition Number Starting Value field.
• Requisition Number Starting Value:
A value is required only if you select
the automatic job requisition number
generation method.
• Maximum Number of Unverified Job
Applications: Number of job applications
that can be made by a candidate before
the candidate verifies its identity.
• Recruiting Organization Tree Name
and Tree Version: Select a recruiting
organization tree name from the list of
values. You can select an existing active
tree or define a new tree for Recruiting.
Organization trees are defined using the
Manage Organization Trees task.
• Allow Withdrawn Candidate to Reapply:
You can allow external and internal
candidates to reapply to job requisitions
when they've a withdrawn job application
on a requisition.
• Contingent Worker is External Candidate:
When you enable this setting, contingent
workers are processed as external
candidates.

---

## Recommended Help
*Chunk ID: OHR-REC-0009 | Chapter: Overview of Recruiting*

• Process Contingent Workers as External
Candidates
• Allow Candidates with Withdrawn Job
Applications to Reapply
• Prefill Legislative Info in Job Applications
• Prefill Responses of Prescreening
Questions in External Candidate Job
Applications
• Set Up the Recruiting Activity Center
• Archive Candidate Search
• Set Up Matching Features: Suggested
Candidates, Similar Candidates, Similar
Jobs, Suggested Jobs
• Set Up Time to Hire
• Hide Suggested Candidates in Job
Requisitions
• Purge Recruiting Campaign Data
• Turn Off Keyword Search in Career Site Job
Description Fields
• Enable Candidate Autoconfirmation
• Enable Candidate Phone Number Reuse
• Enable Email Authentication and Email
Reuse
• Enable Vanity URL
• Enable Vanity Email
• Set Up a Talent Community
• Configure the Be The First to Apply Tag
• Configure the Trending Tag
• Enable Microsoft 365 Calendar Integration
in Interviews

---

## Overview of Recruiting
*Chunk ID: OHR-REC-0010 | Chapter: Overview of Recruiting*

Description
• Prefill Legislative Information in
Candidate Applications: You can enable
a setting so that legislative information
is automatically saved while creating
applications on behalf of a candidate
and is prefilled for returning external
candidates applying for a job.
• Prefill Prescreening Questions in External
Candidate Applications: When you
enable this setting, if a returning external
candidate applies for a new job, responses
to prescreening questions are prefilled if
the candidate answered the questions in
previous job applications.
• Configure Recruiting Activity Center: This
is where you can configure the activity
items displayed in the Recruiting Activity
Center.
Search

---

## Recommended Help
*Chunk ID: OHR-REC-0011 | Chapter: Overview of Recruiting*

• Enable Microsoft Teams Integration in
Interviews
• Enable Zoom Integration in Interviews
• Methods to Adjust the Content of an Offer
Letter
• Keep Active Job Applications Upon Move
to HR
• End Dating Offer Assignments
• Configure Collaborator Types Defaulted in
Job Offers
• Configure the Candidate Duplicate Check
for Candidates Moving to the HR Phase
• Hide Candidate Data to Recruiting Agents
• Allow Internal Candidate Search by
Recruiting Agencies
• Enable Agent Actions

• Candidate Search Archiving: You can
enable candidate search archiving to track
candidate searches ran by recruiters.
Search result archiving supports
requirements from the Office of Federal
Contract Compliance Programs (OFCCP).

• Set Up an Email Marketing Campaign
• Configure the Job Application Print
Feature

---

## AI Feature Integration
*Chunk ID: OHR-REC-0012 | Chapter: Overview of Recruiting*

• You can select which AI Apps features to
enable and configure them. You can also
define which countries are excluded from
suggestions when using the Suggested
Candidates and Similar Candidates
features.
Data Purging
• You can configure data retention duration
fro recruiting campaign email metrics.
Candidate Experience
• Keep Me Signed in For External
Candidates: You can allow external
candidates to be signed in instantly
when they go to a career site to schedule
interviews, provide more information, view
offers, or apply to another job.
• Candidate Autoconfirmation: When you
enable this setting, candidates don't need
to confirm their email address when they
apply for a job. Their email address is
automatically confirmed.
• Verify last name and allow phone number
claim: You can allow external candidates to
reuse the phone number that was used by
another candidate in the past. Candidates
can claim a phone number as genuinely
being their own.

---

## Recommended Help
*Chunk ID: OHR-REC-0013 | Chapter: Overview of Recruiting*

• Verify date of birth and allow email claim:
You can allow returning candidates to
claim email addresses as being genuinely
their own by verifying either their date of
birth or last name.
• Career Site Search in Requisition
Description: You can turn off keyword
search in job description fields.
• Auto Correct in Keyword Search: If a
candidate misspells a keyword, the search
suggestions drop-down list shows items
containing corrected, or closest matched
spellings based on your organization's job
title and description data.
Corporate Branding
• Vanity URL: You use a vanity URL to
allow external candidates to access
career sites. A vanity URL is a descriptive,
pronounceable, truncated URL that
redirects users to a longer URL.
• Vanity Email: You can use a vanity email
to send email communications to external
candidates. A vanity email is used to brand
the "from email" to make it friendlier and
easy to read.
Job Tags
• Be the First to Apply - Maximum Number
of Applications
• Trending - Minimum Number of
Applications
Talent Community
• When you enable Talent Community,
external candidates can join a talent
community to show their interests in your
organization. They can create their profile,
indicate their preferred location and job
family, import their profile from a third
party such as LinkedIn and Indeed, or
upload a resume. You can also set up the
job alert frequency for both internal and
external candidates.
Microsoft Graph Integration
• You can enable the Microsoft Office 365
Calendar integration and the Teams
integration for candidate interviews.
Zoom Integration
• You can enable the Zoom integration for
candidate interviews.
Offer
• Download Offer Letter with Resolved
Tokens: If you enable this setting,

---

## Recommended Help
*Chunk ID: OHR-REC-0014 | Chapter: Overview of Recruiting*

recruiting users will only see the actual
values that belong in that offer letter and
they will see only the actual sections that
are relevant to that specific candidate.
• When candidate accepts an offer,
automatically withdraw all other active
job applications: You can keep active
job applications of a candidate after the
candidate is moved to the HR phase.
• End Dating Offer Assignments: You can
prevent old completed job offers from
being redrafted and from participating in
other processes across the suite.
• Requisition Collaborators Added to Offers:
You can configure which collaborator
types must be defaulted into the offer
team for job offers in addition to the hiring
manager and recruiter.
Move to HR
• Duplicate Check in Move to HR: You can
configure settings to perform a duplicate
check for external candidates in their
move to HR.
• Include as Potential Duplicates
Agency Hiring
• Hide Candidate Data: With this setting,
you can control how much candidate
data recruiting agents can see. When you
enable the setting, agents will only view
data in the candidate profile Attachments
tab. If you don't enable the setting, agents
will view data in the candidate profile
Details tab and Attachments tab.
• Allow Internal Candidate Search: When
you enable this setting, recruiting
agencies can search internal candidates
using their email address.
• Enable Agent Actions: You can enable a
setting to give agents the ability to take
actions on behalf of candidates to manage
the application process.
Campaigns
• You can configure email marketing
campaigns such as email batch limit, email
maximum retry count, and other emailrelated settings.
Print to PDF
• You can configure the job application print
feature to allow recruiting users to create a
PDF version of job applications.

---

## Task to review and maintain lookup values
*Chunk ID: OHR-REC-0015 | Chapter: Overview of Recruiting*

for Recruiting and Candidate Experiences,
such as data validity range, color scheme,
and meeting status. The Human Capital
Management Application Administrator role
(ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_
APPLICATION_ADMINISTRATOR_JOB) is also
required to view this task.

---

## Recruiting and Candidate Experience Value Sets Task to manage value sets to validate
*Chunk ID: OHR-REC-0016 | Chapter: Overview of Recruiting*

the content of a flexfield segment. The
Human Capital Management Application
Administrator role (ORA_HRC_HUMAN_
CAPITAL_MANAGEMENT_APPLICATION_
ADMINISTRATOR_JOB) is also required to view
this task.

---

## Task to define profile option settings and
*Chunk ID: OHR-REC-0017 | Chapter: Overview of Recruiting*

values to control behavior for Recruiting and
Candidate Experience, such as indicating
the folder in which to find review population
reports. The Human Capital Management
Application Administrator role (ORA_
HRC_HUMAN_CAPITAL_MANAGEMENT_
APPLICATION_ADMINISTRATOR_JOB) is also
required to view this task.

---

## Task to edit and create attachment entities. An
*Chunk ID: OHR-REC-0018 | Chapter: Overview of Recruiting*

attachment entity is usually a database entity,
for example a table or view, that represents
a business object with which attachments
can be associated. The Human Capital
Management Application Administrator role
(ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_
APPLICATION_ADMINISTRATOR_JOB) is also
required to view this task.

---

## Manage Attachment Categories
*Chunk ID: OHR-REC-0019 | Chapter: Overview of Recruiting*

Task to edit and create attachment categories.
An attachment category is used to classify and
secure an attachment. The Human Capital
Management Application Administrator role
(ORA_HRC_HUMAN_CAPITAL_MANAGEMENT_
APPLICATION_ADMINISTRATOR_JOB) is also
required to view this task.

---

## Configure Recruiting Interaction Categories
*Chunk ID: OHR-REC-0020 | Chapter: Overview of Recruiting*

Task to configure interaction categories.
Interactions are used by recruiters and hiring
managers when they create notes about
interactions they had with a candidate. Default
interaction types are:
• Called
• LinkedIn InMail (used with the LinkedIn
Recruiter System Connect integration)
• LinkedIn Notes (used with the LinkedIn
Recruiter System Connect integration)

---

## Recommended Help
*Chunk ID: OHR-REC-0021 | Chapter: Overview of Recruiting*

• Met in Person
• Sent Email
• Sent SMS
• Sent Text Message
Note: Don't use these lookup codes:
• ORA_LIRSC_NOTES
• ORA_LIRSC_INMAIL
• ORA_EMAIL
• ORA_SMS
• ORA_MANUAL_RMI_TRIGGER

---

## Note: Don't disable the default interaction
*Chunk ID: OHR-REC-0022 | Chapter: Overview of Recruiting*

types and change their label. This could lead
to unexpected behavior.
Also, for default values, if you remove the start
date and end date of a look up code, it will still
appear in the list of values. If your organization
doesn't want the look up codes to be visible,
follow one of these steps:
• Clear the Enabled option. Or,
• End date the row by providing an end date
to indicate the date until when the look
up code will be valid and visible in the
interface.

---

## Task to manage various text-based content
*Chunk ID: OHR-REC-0023 | Chapter: Overview of Recruiting*

used in various areas of Oracle Recruiting
such as such as notifications for candidate
job applications, candidate pool members,
candidate profiles, prospects, disclaimers, esignature statement, job offer letter template.

---

## Task to define the universe of geographies
*Chunk ID: OHR-REC-0024 | Chapter: Overview of Recruiting*

used for recruiting purposes. A geography
hierarchy is composed of a list of countries to
which geographies are added, following the
geography hierarchy structure defined for each
country.

---

## Task to define the structure of geography
*Chunk ID: OHR-REC-0025 | Chapter: Overview of Recruiting*

levels from which a geography hierarchy can
be built. A geography hierarchy structure can
have a maximum of three levels. The first level
represents the country.

---

## You can set up the Recruiting features
*Chunk ID: OHR-REC-0026 | Chapter: Overview of Recruiting*

configuration report to review the features
that are enabled, their associated settings,
the profile options to enable the features and
the value of these profile options, and metrics
on the required processes scheduled in the
customer's environment.

---

## Job Requisition Templates
*Chunk ID: OHR-REC-0027 | Chapter: Overview of Recruiting*

Task to configure job requisition templates.
Job requisition templates contain specific
requirements for a job and are used by
recruiters and hiring managers when they
create job requisitions.

---

## Task to define validation and display properties
*Chunk ID: OHR-REC-0028 | Chapter: Overview of Recruiting*

of descriptive flexfields for job requisitions.
Descriptive flexfields are used to add attributes
to entities. The Human Capital Management
Application Administrator role (ORA_
HRC_HUMAN_CAPITAL_MANAGEMENT_
APPLICATION_ADMINISTRATOR_JOB) is also
required to view this task.

---

## Note: Avoid using the apostrophe (') and
*Chunk ID: OHR-REC-0029 | Chapter: Overview of Recruiting*

period (.) characters in the segment name
and segment code of descriptive flexfields
(DFF) used in job requisitions. This will cause
issues.

---

## Task to create interview schedule templates to
*Chunk ID: OHR-REC-0030 | Chapter: Overview of Recruiting*

help recruiters and hiring managers save time
when they create interview schedules for job
requisitions.

---

## Task to configure the look and feel of external
*Chunk ID: OHR-REC-0031 | Chapter: Overview of Recruiting*

career sites such as the header, footer, logo,
background image, branding text, font, and
colors.

---

## Task to create job application flows for career
*Chunk ID: OHR-REC-0032 | Chapter: Overview of Recruiting*

sites. A job application flow is a sequence
of pages that a candidate completes when
applying for a job on a career site.

---

## Task to enable double opt in so that external
*Chunk ID: OHR-REC-0033 | Chapter: Overview of Recruiting*

candidates can opt in to receive job alerts and
recruiting marketing communications when
they apply for a job, when they sign in into a
talent community, or from their candidate self
service page. When candidates opt in, they
receive a message confirming their selection.

---

## Task to define the framework to move
*Chunk ID: OHR-REC-0034 | Chapter: Overview of Recruiting*

candidates through the hiring process to
evaluate and find the best candidates for a job.

---

## Task to manage lookups such as questionnaire
*Chunk ID: OHR-REC-0035 | Chapter: Overview of Recruiting*

status, question type, question order, section
order. The Human Capital Management
Application Administrator role (ORA_

---

## Recommended Help
*Chunk ID: OHR-REC-0036 | Chapter: Overview of Recruiting*

HRC_HUMAN_CAPITAL_MANAGEMENT_
APPLICATION_ADMINISTRATOR_JOB) is also
required to view this task.

---

## You can use fast formulas to calculate
*Chunk ID: OHR-REC-0037 | Chapter: Overview of Recruiting*

computed fields based on the data collected on
job applications. Computed fields are displayed
in job application grid views and on the Extra
Info tab within the job applications.

---

## Task to manage descriptive flexfields used in
*Chunk ID: OHR-REC-0038 | Chapter: Overview of Recruiting*

job offers. Note that offers can also include
another set of descriptive flexfields which are
managed as part of their Assignment section.
See Implementing Global Human Resources
guide on how to configure these fields.

---

## Note: Avoid using the apostrophe character
*Chunk ID: OHR-REC-0039 | Chapter: Overview of Recruiting*

in the segment name and segment code of
descriptive flexfields (DFF) used in job offers.
This will cause issues.

---

## Recommended Help
*Chunk ID: OHR-REC-0040 | Chapter: Overview of Recruiting*

agents to it so that recruiters can invite agents
to submit candidates to agency-enabled
requisitions.

---

## Referral Descriptive Flexfields
*Chunk ID: OHR-REC-0041 | Chapter: Overview of Recruiting*

You can create flexfields to allow recruiters,
agency users, and employees to enter
additional information while referring a
candidate to a job.

---

## Security Reference
*Chunk ID: OHR-REC-0042 | Chapter: Overview of Recruiting*

The tasks that people can do and the data that they can see depend on their roles, duties, and privileges. For
information about these factors, see these two guides:
• Securing HCM
• Security Reference for HCM

---

## Deep Links
*Chunk ID: OHR-REC-0043 | Chapter: Overview of Recruiting*

You can use deep links to provide easy navigation directly to a page in the HCM Cloud application.
You can also use deep links for mobile responsive pages on your intranet, custom and third-party applications, or in a
document. This helps people run transactions in the HCM cloud and provides quick access to their HR information.
To access deep links:
1. Open the main menu.
2. Go to Tools> Deep Links.
3. Copy the URL for a deep link.
4. Paste the URL in the appropriate location.
When you open Deep Links, you find a list of all available deep links.

---

## Maintaining Oracle Search for Oracle Recruiting
*Chunk ID: OHR-REC-0044 | Chapter: Overview of Recruiting*

Oracle Search is the default search engine for new and existing customers of Oracle Fusion Cloud Recruiting. Oracle
Search needs to be maintained after an upgrade or Production to Test (P2T) or Test to Test (T2T).
With Oracle Search, these features become available:
• Recruiters and hiring managers can find candidate profiles using advanced search filters and boolean
expressions.
• Recruiters and Hiring Team members can see candidates that they're responsible for when the Candidate
Security for Candidate Search is enabled.
• External candidates can see similar jobs when searching for jobs.

---

## Overview of Recruiting
*Chunk ID: OHR-REC-0045 | Chapter: Overview of Recruiting*

• External candidates can search for jobs using a postal code.
• External candidates can explore jobs using a map view.
• External candidates can see the distance between their selected location and the job location.
• External candidates can use the Work Location, Organization, and Job Requisition filters.
• External candidates can see job requisition flexfield values exposed by recruiters.
Note: If you’re not using advanced job application filters:
• You don’t need to enable the profile option ORA_IRC_JA_ORACLE_SEARCH_ENABLED.
• You don’t need to run the scheduled process called ESS job to create index definition and perform initial
ingest to OSCS, with the value fa-hcm-job application in the Index Name to Reingest field.
If you’re using advanced job application filters:
• You need to enable the profile option ORA_IRC_JA_ORACLE_SEARCH_ENABLED.
• You need to run the scheduled process called ESS job to create index definition and perform initial ingest to
OSCS after P2T or T2T. In the Index Name to Reingest field, enter the value fa-hcm-job application.

---

## New Provisioning
*Chunk ID: OHR-REC-0046 | Chapter: Overview of Recruiting*

1. Run the Load Workers into the Candidate Table scheduled process.
2. Run these scheduled processes one time sequentially:
◦ Load and Index Master Geography Hierarchy without any parameters. This scheduled process
automatically creates the Applcore index "fa-hcm-irc-geohierarchies" and ingests the data for that index.
◦ Load and Index Job Requisitions with the Drop and Recreate indexing mode. This scheduled process is
required for both Standard Search and Smart search.
◦ Load and Index Candidates with the Drop and Recreate Index indexing mode.

◦ Index Job Summary for Each Requisition with the Full mode. This scheduled process is required for the

Career Coach Search and Smart Search.
3. Schedule the following processes to run every 15 minutes:
◦ Maintain Candidates and Job Requisitions for Search

◦ Index Candidate Attachments
◦ Index Job Summary for Each Requisition with the Incremental mode. This scheduled process is
required for the Career Coach Search and Smart Search.

Upgrade
No need to run or schedule any scheduled processes.

P2T/T2T
1. Cancel these scheduled processes:
◦ Maintain Candidates and Job Requisitions for Search

◦ Index Candidate Attachments

2. Run these scheduled processes one time sequentially:

---

## Overview of Recruiting
*Chunk ID: OHR-REC-0047 | Chapter: Overview of Recruiting*

◦ Load and Index Master Geography Hierarchy without any parameters. This scheduled process

automatically creates the Applcore index "fa-hcm-irc-geohierarchies" and ingests the data for that index.

◦ Load and Index Job Requisitions with the Drop and Recreate indexing mode. This scheduled process is
required for both Standard Search and Smart search.
Load and Index Candidates with the Drop and Recreate Index indexing mode.

◦
◦ Index Job Summary for Each Requisition with the Full mode. This scheduled process is required for the

Career Coach Search and Smart Search.
3. Schedule the following processes to run every 15 minutes:
◦ Maintain Candidates and Job Requisitions for Search

◦ Index Candidate Attachments
◦ Index Job Summary for Each Requisition with the Incremental mode. This scheduled process is
required for the Career Coach Search and Smart Search.

Related Topics
• Set Up Oracle Search for HCM
• Refreshing an Environment
• Which scheduled processes are used in Recruiting?

---

## Enable Oracle Search for Recruiting List of Values
*Chunk ID: OHR-REC-0048 | Chapter: Overview of Recruiting*

You can take advantage of Oracle Search in Recruiting for the following list of values: Positions, Jobs, Locations,
Departments.
You need to review and enable these Oracle Search profile options:
• ORA_PER_ORACLE_SEARCH_POSITIONSLOV_ENABLED
• ORA_PER_ORACLE_SEARCH_DEPARTMENTSLOV_ENABLED
• ORA_PER_ORACLE_SEARCH_JOBSLOV_ENABLED
• ORA_PER_ORACLE_SEARCH_LOCATIONSLOV_ENABLED
Note: The feature ensures the use of Oracle Search to retrieve the list of values for Positions, Jobs, Locations,
Departments. There are no visible changes in the UI unless Design Studio is used to configure the changes. For
details, see the topic How You Configure List of Values (LOVs).
Before you start
Set Up Oracle Search for HCM
Here's what to do
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option codes mentioned above.
6. Set the profile value to Y at the Site level.

---

# Career Sites

## Career Sites
*Chunk ID: OHR-REC-0049 | Chapter: Career Sites*

Career Site
A career site is a website where an organization posts jobs for positions to be filled.
External candidates interact with a career site when they search for jobs, apply for jobs, create a profile, share job details,
get referred for a job, manage their job applications and talent community settings.
An organization can have several career sites and adapt branding and content of the sites to their organization business
needs. For example, the organization's different divisions, to support the organization's international presence, or
to separate external candidates from internal candidates. Career sites can also be contextualized based on location,
organization, job category, job function, recruiting type.
Note:

---

## Create a Career Site
*Chunk ID: OHR-REC-0050 | Chapter: Career Sites*

You create external career sites so that your organization can post jobs for positions to be filled by external candidates.
You can create several career sites, adapt branding and content of the sites to your organization business needs, and
contextualize career sites based on location, organization, job category, job function, recruiting type, and job requisition
flexfields.
When you start the creation of a career site, you enter basic info about the career site such as the name, code, default
language, and contextualization info.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Site Look and Feel Configuration page, click the Add Site icon.
3. Enter a name and a code for the career site. The name is the public title that appears in the browser.
4. Select a default language for the career site.
a. If you want the career site to be available in several languages, click Manage Languages and select other
languages.
5. Select a template.
6. You can contextualize the career site based on the job requisition locations, organizations, job categories, job
functions, and recruiting types, and job requisition flexfields. This is to define what job requisitions appear in the
search results.
Within each context, the "OR" operation is performed, and among all the contexts that are set the "AND" operation
is performed. Consider a career site where two contexts are set: one location and one organization. In this case, for

any requisition to get posted onto this site, both the organization as well the location of the requisition should match
with the context's location and organization.
If an organization or location (which is parent) is set as the context in a career site, then all the requisitions with this
organization (location) as well as the child organizations (locations) of this parent will get posted on this career site.
7. If you created custom content pages for other career sites, you can select the ones you want to use for this career
site. Otherwise, the template splash page is used.
8. Click Create Site.
Results:
The career site is created and its status is Inactive.
What to do next
You can configure the career site elements such as header, footer, search filters, cookie consent, and so on. You can also
configure the career site theme, define the page layout, and translate the career site.
Related Topics
• Configure a Career Site Theme
• Career Site Page Types and Layout
• Translate a Career Site
• Configure a Career Site

---

## Configure a Career Site
*Chunk ID: OHR-REC-0051 | Chapter: Career Sites*

You configure external career sites by enabling and configuring different options and features such as headers, footers,
search filters, work location display, talent community sign-up, cookie consent message.
These configuration options are available on the career site's General tab.

Option

Description

---

## You can configure up to 5 main navigation menus and 6 navigation submenus. You can reorder the
*Chunk ID: OHR-REC-0052 | Chapter: Career Sites*

display of header links using the drag and drop functionality. Click Preview to see how the links are
displayed in the header.
Make sure your header displays well in all screen resolutions. The display will depend on how many
navigation menus you add and how long the labels are. Depending on the screen resolution, a
horizontal bar might be displayed in the header area. To avoid that, you can shorten link labels or use
custom CSS for wrapping text or reducing spacing.

---

## You can configure up to 5 main navigation menus and 3 navigation submenus. You can choose 5 links
*Chunk ID: OHR-REC-0053 | Chapter: Career Sites*

for mobile and tablet. You can reorder the display of footer links using the drag and drop functionality.
Click Preview to see how the links are displayed in the footer.

---

## SEO Optimization
*Chunk ID: OHR-REC-0054 | Chapter: Career Sites*

You can increase your career site's visibility with search engines. Enter an organization name,
organization URL, and organization logo to help search engines tie the career site page to your
organization. For details, see Configure Search Engine Optimization.

---

## Search Filters
*Chunk ID: OHR-REC-0055 | Chapter: Career Sites*

You can decide which of these search filters are visible to candidates on career sites.

---

## Career Sites
*Chunk ID: OHR-REC-0056 | Chapter: Career Sites*

Description

• Locations
• Work Locations (this filter requires Oracle Search)
• Workplace
• Job Functions
• Categories
• Organizations (the Organizations filter requires Oracle Search.
• Posting Dates
You can configure career site search filters to display more than 10 values. For details, see Configure
Career Site Search Filters.
You can also add descriptive flexfields (DFFs) created with Transaction Design Studio. For details, see
Add Job Requisition Flexfields as Search Filters in Career Sites.
You can add job requisition flexfields as career site context filters. This lets you post requisitions to
career sites based on a flexfield value. First select the context in which your DFF resides, and then
select the appropriate DFF. Once selected it's added to the site context filters. Select the appropriate
values from the drop-down list.
Note: Only independent DFFs are supported. Custom filters aren't visible on the tiles for site lists.
Candidate Experience site context DFFs aren't honored in job recommendations. This means if
Similar Jobs and Recommended Jobs are enabled on the site, some jobs not matching the set DFF
site context can be recommended. For example, if the DFF value you selected as a context filter is
“Alumni”, you might see a job in the Similar Jobs section on that site that doesn't have that Alumni
DFF value.

---

## You can decide what work location details are displayed to candidates within the description of jobs on
*Chunk ID: OHR-REC-0057 | Chapter: Career Sites*

the career site.
• Full Work Location Address: The building number, street, city, state/province, postal code, and
country are displayed.
• Postal Code: Only the postal code of the work location is displayed.
• Work Location Name: Only the work location name is displayed.
• No Work Location: If work locations are added to a job requisition, no info is displayed. The
recruiting location is displayed instead.
You need to set the Work Location Display setting to Full Work Location Address if you also configured
preferred locations in the job application flow. Otherwise, when a candidate selects preferred locations
while applying for a job on an external career site, the locations that the candidate selected won't
appear.

---

## Set up a career site by selecting one or more job categories. You select the job categories, and the
*Chunk ID: OHR-REC-0058 | Chapter: Career Sites*

splash page category tiles, and the corresponding category landing pages are created for you. For
details, see Quickly Create a Career Site Using Job Categories.
If you're using the Career Site Asset Library, once generative AI creates introductory text, it uses
keywords in that text to select an asset from the asset library to populate the Hero Image URL and Tile
Image URL fields. These are just suggested image URLs. You can always add your own. For the Tile
Image URL, adding your own asset library URL displays just the URL.
Note: The Hero Image URL is only populated if there's a linked asset configured in the asset library.

---

## Career Sites
*Chunk ID: OHR-REC-0059 | Chapter: Career Sites*

Description
Note: For more details see Add Intelligent Assets to Job Details Pages

---

## This is where you set up options to display the Talent Community sign up option to candidates. When
*Chunk ID: OHR-REC-0060 | Chapter: Career Sites*

external candidates don't find jobs matching their interests, they can join a talent community to show
their interests in an organization. For details, see Set Up a Talent Community.

---

## You can track candidates who visit your external career sites so that their interactions are remembered
*Chunk ID: OHR-REC-0061 | Chapter: Career Sites*

across visits. The cookie consent is presented when a candidate visits the career site for the first time
and within consecutive visit when cookies weren't accepted before. For details, see Career Site Cookies.

---

## Recommended Jobs
*Chunk ID: OHR-REC-0062 | Chapter: Career Sites*

You can allow candidates to get a weighted list of recommended jobs based on their uploaded resume.
For details, see Configure Recommended Jobs Based on Candidate Resume.

---

## When you select the option Display distance to jobs and sort jobs by distance, candidates who search
*Chunk ID: OHR-REC-0063 | Chapter: Career Sites*

for jobs using their location or a location or postal code they typed in, will see the distance between
their selected location and the job location. The distance appears underneath the job title. The
distance is displayed in the unit selected by the candidate in the radius search. The radius unit selected
by default depends on the candidate's browser language. If the browser locale is set to a country where
imperial system is used (for example, en-US or en-GB), miles is used. For other locations or if browser
locale can't be read, the unit defaults to kilometers. Candidates can also sort jobs based on distance.
Note:
This feature requires Oracle Search.

---

## You can use pixel tracking to track your external candidates when they click the Apply button, when
*Chunk ID: OHR-REC-0064 | Chapter: Career Sites*

they start applying for a job, and when they submit their job applications. For details, see Enable
Tracking Pixel.

---

## You can allow external candidates to explore jobs using a map view. Posted jobs are pinned on the
*Chunk ID: OHR-REC-0065 | Chapter: Career Sites*

map, giving candidates a nice visual way to see job locations. Candidate can easily access job details
and calculate commute time. Search Jobs on Map is only available with the Minimal Template. For
details, see Enable Job Search on a Map.

---

## Workplace Tag Display
*Chunk ID: OHR-REC-0066 | Chapter: Career Sites*

You can configure the workplace to appear on external career sites. Workplace attributes are on-site,
remote, and hybrid. For details, see Display the Workplace on Career Sites.

---

## You can share more engaging content with social platforms when you post links to external career
*Chunk ID: OHR-REC-0067 | Chapter: Career Sites*

sites. Site-level configuration for Open Graph image is available to make content more shareable. For
details, see Enable Social Sharing.

---

## Configure a Career Site Theme
*Chunk ID: OHR-REC-0068 | Chapter: Career Sites*

You can personalize the look and feel of external career sites so it aligns with your organization's branding. The Theme
tab is where you set global elements such as the corporate logos, background image, text, fonts, colors, custom header,
footer, and CSS.
The main view on the Theme tab contains the live preview of the career site and shows the changes you make on the
configuration panel. As soon as you configure a theme element, it’s shown right away on the page preview. You can
preview the career site for desktop, tablet, and mobile devices. Changes you make to the theme will be visible on the
active career site as soon as you publish it.
Note: You need to store images on a public-facing server that doesn't require authentication. For example, this can
be the same server that you use for your corporate public websites or any publicly accessible website. Also, you can't
store images in Oracle Recruiting Cloud (ORC).The URL can't contain the customer's POD URL.

Option

Description

Logo

You can use different images as logo for mobile and desktop devices.
To use a logo on a career site, the logo must first be uploaded to any publicly accessible website. Then,
you can add the image URL in the Insert URL for desktop logo field. The logo is displayed in the left
corner of the career site. The logo allowed size is 150 x 40 pixels. If the logo is larger, it's reduced to fit
the allowed size. If the logo is smaller, it's not stretched to fit the allowed size.
If you don't add an image for Social Sharing, the desktop logo is used when jobs are shared in social
channels. For the best experience when sharing job links in social media sites, most social platforms
require aspect ratio of 1.9:1 for images. If your logo will be used for social sharing, make sure you verify
the aspect ratio recommended by the platforms you use before uploading the image. .

---

## You can upload a URL for a background image. The background image appears on the career site
*Chunk ID: OHR-REC-0069 | Chapter: Career Sites*

home page. It's applied to any screen resolution. The ideal size is 2560 x 1600 pixels. The file should
not exceed 1 MB. If the file is larger, use a tool to compress it.
In minimal template, background image applies to career site home page only. Background color of
career site search page can be defined using Theme Color 4 (for example #ffffff).

---

## Global Fonts
*Chunk ID: OHR-REC-0070 | Chapter: Career Sites*

You can select the font for all pages of the career site. A predefined list of fonts is available.
To add a new font, click Add, enter the font name, and add a woff URL or woff2 URL. For example:
• https://www.xxxxx.com.hk/fonts/noto-sans-v12-latin-regular.woff
• https://www.xxxxx.com.hk/fonts/noto-sans-v12-latin-regular.woff2
Note: For a browser to render a font correctly, the font must be installed on the operating system.

---

## You can configure colors used in the career site. Select theme colors (set of colors applying to groups
*Chunk ID: OHR-REC-0071 | Chapter: Career Sites*

of elements). The colors depend on the template that you selected. You can also define the color of

---

## Career Sites
*Chunk ID: OHR-REC-0072 | Chapter: Career Sites*

Description
several UI elements such as header, footer, buttons, text, background, panels, menus, filters, tiles. Click
Reset Colors to restore the template default colors.

---

## You can create different header design styles that can be used globally or on specific pages of the
*Chunk ID: OHR-REC-0073 | Chapter: Career Sites*

career site.
• Header Options: You can select the horizontal or hamburger navigation
• Hide Logo: When you select this option, the logo isn’t displayed.
• Hide I'm an employee button icon: When you select this option, the icon next to the text "I am an
Employee" isn’t displayed.
• I'm an Employee Text: Enter the text you want to display. Leave the field blank if you don’t want to
display any text.
• Hide profile button icon: When you select this option, the Manage Profile icon isn’t displayed.
• Profile Text: Enter the text you want to display. Leave the field blank if you don’t want to display
any text.
Note: If you enter custom text in the I'm an Employee Text and Profile Text fields, you can then
translate the text in the Translations tab.

---

## Note: If a screen width is less than 1024 px, a hamburger menu will be displayed. If a screen size is
*Chunk ID: OHR-REC-0074 | Chapter: Career Sites*

equal to or greater than 1024 px, the menu type shown is based on user configuration.

---

## You can create a custom header to match your corporate branding. The custom header is displayed on
*Chunk ID: OHR-REC-0075 | Chapter: Career Sites*

top of the template header. To create a custom header, you provide the HTML code.

---

## You can create a custom footer to match your corporate branding. To create a custom footer, you
*Chunk ID: OHR-REC-0076 | Chapter: Career Sites*

provide the HTML code. Only one footer can be active. If you use the template footer, you can't use the
custom footer.

---

## You can add Cascading Style Sheets (CSS) to apply custom styling to design elements created using
*Chunk ID: OHR-REC-0077 | Chapter: Career Sites*

the Custom HTML element within the Career Site Builder. Also, other elements—such as Paragraph
Text, Images, and Headings—can be assigned CSS class or ID names in the More Options area,
allowing them to be styled via custom CSS.
When leveraged effectively, Custom CSS can be used to create dynamic visual components, such as
image carousels and interactive content.
It can also be used adjust image view in the job details page. When an image is added to the media
section of a job requisition details page, add the following custom CSS to your career site to avoid
having grey bars at the side of the image when viewing the job on the career site.
When an image is added to the media section of a job requisition details page, add the following
custom CSS to your career site to avoid having grey bars at the side of the image when viewing the job
on the career site.
.media-slider__item-content {
background-size: cover !important;
}
It's important to adhere to best practices while applying custom CSS:
• Limit custom CSS usage to elements within the Custom HTML element and other designated
areas.

---

## Career Sites
*Chunk ID: OHR-REC-0078 | Chapter: Career Sites*

Description
• Applying custom CSS on native application elements isn't supported, as class or ID names for
those might change without a formal change management process, potentially breaking custom
styling.

---

## You can add custom JavaScript to career sites to facilitate third-party analytics tools and control
*Chunk ID: OHR-REC-0079 | Chapter: Career Sites*

custom cookies on the oracle career sites. While it allows for limited JavaScript functionality, there are
key considerations to keep in mind:
• The use of custom Java Script is supported for the following use cases:
Add third party analytics and tracking tools to Oracle career sites.

◦
◦ Control custom cookies on the career sites.

• Custom JS loads after the rest of the application, so expect a delay, and plan script execution
accordingly.
• Applying custom Java Script on native application behavior isn't supported, and the code might
not work after release update.
For third party analytics, see example codes below.

Favicon

---

## You can add a personalized favicon to your external career sites. For details, see Add a Personalized
*Chunk ID: OHR-REC-0080 | Chapter: Career Sites*

Favicon to the Career Site and Configure Career Site Location Search.

Here's an example of how an original Google Analytics tracking code would be transformed.

---

## Transformed Code to Enter in Career Site
*Chunk ID: OHR-REC-0081 | Chapter: Career Sites*

<!--Global site tag (gtag.js) Google Analytics-->

var script = document.createElement('script');
script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-12345678-9';
document.head.appendChild(script);

<script async src="https://
www.googletagmanager.com/gtag/js? window.dataLayer = window.dataLayer || [];
id=UA-12345678-9"><script>
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
<script>
gtag('config', 'UA-12345678-9');
window.dataLayer =
window.dataLayer || [];
function gtag()
{dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'UA-12345678-9');
</script>

---

## Google Tag Manager Tracking Code
*Chunk ID: OHR-REC-0082 | Chapter: Career Sites*

(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],

---

## Google Tag Manager Tracking Code
*Chunk ID: OHR-REC-0083 | Chapter: Career Sites*

j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');

---

## Career Site Page Types and Layout
*Chunk ID: OHR-REC-0084 | Chapter: Career Sites*

You can use different types of pages when you create an external career site and you can configure these pages by
defining their layout, background, and elements.
The following types of career site pages are available:
• Splash Page: This is the page that candidates first see on the career site. This is often the central panel of the
career site.
• Search Results Page: These are the pages that display when candidates perform a search or select a link that
displays a list of current jobs.
• Job Details Page: These are the pages that display when candidate select a job from the search results to view
more details. This page is the entry to the application process through the Apply Now action.
• Custom Page: These pages are primarily used to provide greater detail about the company, organization,
culture, or any other information that provides a rich candidate experience.
Pages are based on the design principle of the design grid. Pages are created using sections, rows, columns, and
elements. Pages can have several sections, sections can have several rows, and columns can have several elements.
When you add a section to a page, you can add predefined column layouts using the Actions menu located on the left
side of the section. When you're creating your column layouts, note that if you go from a 5-column layout for example,
to a 3 column layout, columns and design elements within them will get deleted. Using the Actions menu on the right
side, you can add a background color, image, or a video to a section. For videos, enter a YouTube URL or a URL to a mp4
file. Using the Elements menu, you can add and format elements such as headline, paragraph, image, and so on.
Pages can have different common elements, and these elements can be configured.

---

## Common Element
*Chunk ID: OHR-REC-0085 | Chapter: Career Sites*

Description

Heading

The heading element can be configured to insert HI, H2, H3, and other headings into the page.

Paragraph

The paragraph element can be configured to insert text into the page.

Image

The image element can be configured to insert images into the page.

Video

The video element can be configured to insert video into the page.

Button

The button element can be configured to insert a button or text link into the page.

Space

---

## The space element is a convenient method to add vertical white space to a page without using margin
*Chunk ID: OHR-REC-0086 | Chapter: Career Sites*

and padding settings. Spacers of up to 400 pixels high can be added to any row and can be stacked to
create larger areas.

Rule

The rule element can be inserted to create a break between areas of a page. Width, color, alignment,
margins can be defined.

---

## The job list element displays a list of current jobs based on keyword, location, or job family and other
*Chunk ID: OHR-REC-0087 | Chapter: Career Sites*

criteria. Jobs might be displayed with a short description, long description, or no description.

HTML

---

## The HTML element puts pure HTML on the page that can be styled via the Custom CSS area of the
*Chunk ID: OHR-REC-0088 | Chapter: Career Sites*

Theme tab. This is to account for situations where the native element doesn't meet the desired need.

---

## The Talent Community element provides the ability to place a talent community button that takes the
*Chunk ID: OHR-REC-0089 | Chapter: Career Sites*

candidate to the talent community profile creation screen. The button's style is based off of the theme
colors in the Theme tab and can't be configured.

---

## The Recommended Jobs Based on Resume allows candidates to get a weighted list of recommended
*Chunk ID: OHR-REC-0090 | Chapter: Career Sites*

jobs based on their uploaded resume. Results are weighted based on current job title, location, and
skills.

---

## The configurable cookie preferences link element provides the ability to add cookie preferences link
*Chunk ID: OHR-REC-0091 | Chapter: Career Sites*

to the page that takes candidate to either the Cookie Policy or the Cookie Preferences modal. Provides
candidates with a way to change their preferences without having to clear their cookie history.

Each page type has its own specific elements.

---

## Job Details Page
*Chunk ID: OHR-REC-0092 | Chapter: Career Sites*

• Apply Now Button
• Media
• Recommended Jobs
• Section Areas
• Job Flags
• Page Options
• Intelligent Asset

Related Topics
• Create a Career Site Splash Page
• Create a Career Site Search Results Page
• Create a Career Site Job Details Page
• Create Compelling Career Sites Using Oracle Recruiting

---

## Configure Assets in the Asset Library
*Chunk ID: OHR-REC-0093 | Chapter: Career Sites*

You can store and serve images within the career site builder using the career site asset library. This is a global library for
use with all career sites. You can upload assets from any site, and include metadata for images (such as title and
keywords), define AI specific usage types, and indicate category links to support the dynamic selection of images using
Generative AI.
These configuration options are available on the career site's Asset Library tab.

Option

Description

---

## Filter and Sort
*Chunk ID: OHR-REC-0094 | Chapter: Career Sites*

Filter assets by usage type using the Category Tiles, Career Site Assets or Requisition Asset buttons.
You can also sort them alphabetically or by date uploaded.

Slider

---

## Use the slider below each button to indicate whether assets are Active or Inactive for use with
*Chunk ID: OHR-REC-0095 | Chapter: Career Sites*

generative AI. Setting the image to active is an indication that AI can use that asset in places where AI
selects images dynamically.
Note: Assets can be uploaded to the library from any career site. They're automatically set to active
for the career sites from which they were uploaded. Changing the settings to Active or Inactive only
affects the career site where that setting is selected.

Images

Click the icon to view all image assets.

Recent

View recent assets. These are images uploaded within the last 30 days.

Copy

You can also copy image URLs to your clipboard and use it where needed.

Upload

---

## Upload new assets. When you upload a new asset you can indicate keywords, usage type, and
*Chunk ID: OHR-REC-0096 | Chapter: Career Sites*

categories.
There is a limit of 2.5 Mb for files, and they can be of the following types:
• JPG
• PNG
There's no limit to how many you can upload. You can't remove assets.

View

Click an asset image to view and edit its settings.

---

## Rename an asset
*Chunk ID: OHR-REC-0097 | Chapter: Career Sites*

While viewing an asset settings, click the icon next to the image title to give it a new one.
Note: You can only change the title of the image, not the file name.

---

## You can add and remove usage types, categories, and keywords. Selecting these items here helps
*Chunk ID: OHR-REC-0098 | Chapter: Career Sites*

Generative AI understand that you've preapproved these items for certain use cases and drives which
assets are suggested for use in the future. For usage types:
• Requisition Assets are used on job details pages.
• Career Site Assets are linked to category tiles for custom pages.
• Category Tiles are the thumbnails for the category tiles. With these you can link assets
to manually connect them with hero images.

---

## Create a Career Site Splash Page
*Chunk ID: OHR-REC-0099 | Chapter: Career Sites*

You create a splash page to define the content of the central panel of an external career site.
The splash page can contain text, images, videos, and any information that you want to display to candidates to provide
a rich candidate experience. For example, a splash page can provide information about a company's offices or benefits.
It can be linked to one of the links in the career site header.
1. Open the career site you're creating.
2. Click the Pages tab.
3. Click the Add Page icon.
4. Provide a title for the page.
5. Click Splash Page.
6. Click Create Page.
7. You can use the default splash page as a starting point and personalize it.
8. When you’re done configuring the page, click Publish in the Settings menu.
Results:
The page becomes available on the Pages tab and it's active. You can use it in your external career sites.
Related Topics
• Career Site Page Types and Layout

---

## Create a Career Site Search Results Page
*Chunk ID: OHR-REC-0100 | Chapter: Career Sites*

You create a search results page so candidates can search for jobs and see the list of current jobs.
1. Open the career site you're creating.
2. Click the Pages tab.
3. Click the Add Page icon.
4. Provide a title for the page.
5. Click Search Results Page.
6. Click Create Page.
7. You can use the default search results page as a starting point and personalize it.
8. When you’re done configuring the page, click Publish in the Settings menu.
Results:
The page becomes available on the Pages tab and it's active. You can use it in your external career sites.

---

## Create a Career Site Job Details Page
*Chunk ID: OHR-REC-0101 | Chapter: Career Sites*

You create job details pages to display information about a job. This page is the entry to the application process through
the Apply Now action.
Note: We strongly recommend that you move away from writing your own custom CSS scripts and leverage the
Career Site Customization Framework which allows for the fine grain customization of look and feel.
You can create several job details pages, but only one can be active. You can also translate the job details page.
1. Open the career site you're creating.
2. Click the Pages tab.
3. Click the Add Page icon.
4. Provide a title for the page.
5. Click Job Details Page.
6. Click Create Page.
7. You can use the default job details page as a starting point and personalize it.
8. When you’re done configuring the page, click Publish in the Settings menu.
Results:
The page becomes available on the Pages tab and it's active. You can use it in your external career sites.
Related Topics
• Career Site Page Types and Layout

---

## Add Intelligent Assets to Job Details Pages
*Chunk ID: OHR-REC-0102 | Chapter: Career Sites*

Let Generative AI select a new image daily from the career site asset library and display it on the job details page. The
image chosen is based on the job category and job description of the requisition.
Using the intelligent asset element provides you with an alternative method for dynamically adding images to the job
details display, without having to manually upload them to a requisition. It also provides image display independent
from the map feature.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Site Look and Feel Configuration page, edit a career site.

---

## Career Sites
*Chunk ID: OHR-REC-0103 | Chapter: Career Sites*

3. Click the Pages tab.
4. Add or edit a job details page.
5. Add an intelligent asset from the gear icon. The image displayed by default is selected by Generative AI for any asset
categorized as a Requisition Asset in the Career Site Library.
6. Click edit, if needed, to define your own settings. You can:

◦ Indicate your own image URL. If Generative AI doesn't define anything here and you don't add your own, no
image will display.
Indicate whether the page is for use on mobile devices.

◦
◦ Select either Landscape or Portrait if you want Generative AI to only use assets that are set for one of those
◦

layouts.
Add keywords if you want Generative AI to select images based on them, For example, perhaps you want
images using keywords such as "uplifting" or "energetic" to be selected for this page. The words you
add here will augment keywords found in the job description. Because keywords are pulled from the job
description, you may want to add keywords here that evoke a feeling. For example a technical job photo,
that is fun or exciting.

---

## Note: Using keywords in the elements will increase the chance that the same image will be displayed for
*Chunk ID: OHR-REC-0104 | Chapter: Career Sites*

multiple jobs.

◦ Configure style elements such as corner radius, border colors and width, and alignment, and other options
such as padding, margin settings, and CSS settings.

Related Topics
• Configure Assets in the Asset Library
• Quickly Create a Career Site Using Job Categories
• Configure a Career Site

---

## Translate a Career Site
*Chunk ID: OHR-REC-0105 | Chapter: Career Sites*

You can translate the text you added while creating an external career site. When a career site is available in several
languages, candidates can select a language to search for jobs, view job postings, and apply for jobs.
Before you start
You first need to select languages in the General tab, using the Manage Languages option. You can add new languages
only when the site is inactive.
Note: If you need to uninstall languages from your environment, you first need to remove those languages from all
career sites to avoid career site labels appearing as placeholders.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration

---

## Career Sites
*Chunk ID: OHR-REC-0106 | Chapter: Career Sites*

2. On the Career Site Look and Feel Configuration page, find the career site and click Edit.
3. Click the Translations tab.
4. Select the page you want to translate.
5. Select the language in which you want to translate the page.
Custom content pages can be translated only in draft mode. If you don't see custom content pages on the list of
pages to translate, make sure that the page is in draft mode. When a draft custom content page is translated, you
need to republish it.
6. To translate the career site in more languages, click Manage Languages and select the languages you want. You can
set a default language. When you add a language, you should translate the labels appearing in the career site.
Results:
On the Translations tab, you can also provide language specific content to the following URLs:
• URL for background image
• Logo URL for desktop
• Logo URL for mobile

---

## Translate Default Career Site Labels
*Chunk ID: OHR-REC-0107 | Chapter: Career Sites*

You can use the User Interface Text tool to edit and translate default labels that show up in your external career site.
Note that changing a label may have an effect not only on the career site, but also on any other area of the application,
where that label is used.
Before you start
You need to activate and enter a sandbox with the User Interface Text tool enabled. (Settings and Actions Menu > Edit
Pages > Activate a sandbox)
Here's what to do
1. From the Navigator menu, go to the Configuration menu.
2. In the Configuration section, click User Interface Text.
3. Search for the label you want to edit.
4. Edit the label.
5. Publish the sandbox.
6. Republish the career site.

---

## Translation of Career Site Labels
*Chunk ID: OHR-REC-0108 | Chapter: Career Sites*

External career sites are built using two types of text labels. Each type require different tools to translate them.
You add these labels manually when you create a career site:
• Site name
• Branding text
• View All Jobs button

---

## Career Sites
*Chunk ID: OHR-REC-0109 | Chapter: Career Sites*

• Header links
• Footer links
• Cookie consent message, policy, and buttons to accept or decline the policy
• Talent community title, description, and button to sign up to the community
• Any custom content added to the site such as custom header, custom footer, custom CSS.
There are also default labels that show up in your career sites by default. That's basically every text label that isn't added
using the career site editor. These include:
• Labels in search bar and filter panels.
• Labels in job tiles and job detail pages.
• Labels in authentication pages of job application flow, candidate self service, and talent community.
• Labels for fields in the following application flow blocks:

◦ Contact Information
◦ Education
◦ Experience
◦ Languages
◦ Licenses and Certificates
◦ Miscellaneous Documents
◦ Preferred Locations
◦ Profile Import
◦ Skills
◦ Supporting Documents
◦ Timeline
◦ Work Preferences
• Labels in navigation links and buttons
• Error, warning, and confirmation messages
Related Topics
• Translate a Career Site
• Translate Default Career Site Labels

---

## Quickly Create a Career Site Using Job Categories
*Chunk ID: OHR-REC-0110 | Chapter: Career Sites*

You can quickly set up a career site by selecting one or more job categories. You select the job categories, and the splash
page category tiles, and the corresponding category landing pages are created for you.
If Generative AI is active, you can use it to generate suggested text.
Before you start

---

## Career Sites
*Chunk ID: OHR-REC-0111 | Chapter: Career Sites*

The following profile options must be enabled to use this feature:
• ORA_IRC_CE_ADMIN_GAI_ENABLED for category tiles and pages.
• ORA_IRC_CE_JOB_FIT_GAI_ENABLED for job fit.
By default, the profile option is set to N, meaning the feature is disabled.
1.
2.
3.
4.
5.
6.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
On the Search page, search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values, search for the above profile option codes.
In the Profile Values section, set the profile value:
◦ Y: The code is enabled.

◦ N: Default value. The code isn't enabled.
7. Click Save and Close.
Here's what to do
1. On the Career Site General tab, select the job categories you want to use in the Job Categories section.
2. Scroll down and view the Category Tiles section.
3. Click in the Job Categories field to select what you want. The categories available here correspond with the job
categories you selected in the first step. If a category's fields are read-only, it means the category tile has already
been published.
Adaptive Intelligence (AI) automatically generates some introduction text for you to use on the category landing
page. You can provide custom images for the tiles and hero images (the brand images) for the category landing
page, map the category tile to an already created custom page or use the system generated category landing page,
and style the tiles displayed on the splash page.
4. Click Generate Category Pages.
5. Preview or publish the site.
On the career site configuration page, the pages for these tiles have automatically been created. They're appended
with "CL" to indicate that they're category landing pages.
What to do next
Edit the pages as you would other types of search result pages. These pages can be based on the Oracle default pages,
or you can use your own custom pages. You can also change the styling of the tiles on the splash page.
If you need to update a category page (for example, perhaps you want to use a different hero image), the best practice is
to return to the Category Tiles section of the General tab, delete the category, add it again, and make your updates.
Note: If you delete a tile based on a custom page, the custom page is still available for selection for other tiles.

---

## You can style tiles individually by selecting them from the Job Categories drop-down list in the Category to Style
*Chunk ID: OHR-REC-0112 | Chapter: Career Sites*

section. Once you've changed the style of an individual category, if you then make edits to all categories (by selecting
All from the Job Categories drop-down list) only the categories that are still using the global or default styles are
affected. Because you've formatted a category differently, it's assumed that those individual choices take precedence
over global selections. The hierarchy for style selections are:
1. Individual Style
2. Global Style

3. Default Style

---

## How Language is Determined on Career Sites
*Chunk ID: OHR-REC-0113 | Chapter: Career Sites*

If a career site is translated into more than one language, a language drop-down list displays to external candidates, and
they can use it to change the language displayed to them on the site. When they do this, a language cookie is saved to
their devices.
This cookie is used later when the candidates revisit the site. Here's how this works.
The majority of the URLs that link to career site pages contain a language parameter that determines which language
is loaded to the page when the link is used. Candidates can then change that language, but there's no additional logic
needed when the site is loaded.
However, some of the URLs may not include the language parameter. This is the case for sites that use a vanity domain
and no additional parameters (for example: HTTPS// jobs.vision.com). If a candidate uses such a link, the application has
to determine what the site display language should be.
Let's say, for example, there is a career site that has English and Italian translations, with English set as default. When a
candidate clicks the link to visit the site, the language that loads on the page is determined using the following process:
1. The application first verifies if the candidate’s device has a language preference set in a cookie (if the candidate
has visited the site before). If a cookie is there, and the language from the cookie matches one of the site
languages (English or Italian), the site is displayed in that language.
2. If there’s no cookie saved, the application checks the user’s browser language. If there’s a match between the
browser’s language and one of the site languages, then the site is loaded in that language.
3. If the user’s browser is set to a language that is not one of the site languages (for this example, let’s say French),
then the page is loaded using the site’s primary language, which in our example is English.

---

## Other Actions to Perform on a Career Site
*Chunk ID: OHR-REC-0114 | Chapter: Career Sites*

Here are more tools you can use to configure an external career site. These are available on the Career Site Look and
Feel Configuration page, in the Settings menu.

Action

Description

---

## You can edit a career site. When you edit an active career site, the application creates a copy of the
*Chunk ID: OHR-REC-0115 | Chapter: Career Sites*

page. Changes you make are visible to the candidates when you publish the career site.

Remove

You can remove a career site.

Action

Description

---

## Expose Job Requisition Fields in Job Descriptions for
*Chunk ID: OHR-REC-0116 | Chapter: Career Sites*

Career Sites
You can expose job requisition fields in job descriptions so that candidates can easily find jobs that they want to apply
to.
When a job requisition is posted on an external career site, some fields in the requisition are visible to candidates by
default.
• Requisition title
• External short description
• Primary location and number of other locations
• External description (displayed as Job Description), responsibilities, and qualifications
• Employer description (displayed as About Us)
• Recruiting organization description (displayed as About The Team)
In addition, you can expose the following:
• Other Requisition Title
• Number of openings / Unlimited Openings
• Hiring Manager Organization
• Job Function
• Worker Type
• Regular or Temporary
• Management Level
• Job Type
• Domestic Travel Required
• International Travel Required
• Work Duration Months
• Work Duration Years
• Work Hours
• Work Days
• Name of External Contact
• Email of External Contact
• Legal Employer
• Business Unit

---

## Career Sites
*Chunk ID: OHR-REC-0117 | Chapter: Career Sites*

• Department
• Grade
Note: Additionally, job requisition flexfields can also be exposed.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Site Look and Feel Configuration page, find the career site and click Edit.
3. Click the Pages tab.
4. Add a new job details page or edit an existing one.
5. Scroll down to the Job Info section and click it.
6. Scroll down to view the Additional Information Displayed section and click in the field.
7. Select the fields you want.
The sequence in which you add the fields determines the sequence in which they'll display on the job details page.
8. Click Done.
Results:
The fields you selected are displayed in the Job Info section.
What to do next
Publish the career site to see the fields on the career site.
Related Topics
• Add Job Requisition Flexfields to Job Details Pages in Career Sites and Agency Portals

---

## Expose Job Requisition Fields on Job Search Results
*Chunk ID: OHR-REC-0118 | Chapter: Career Sites*

Page for Career Sites
You can control job requisition information displayed on the search results list and manage the display style of the list so
that candidates can easily find jobs that they want to apply to.
Each job card on the list contains four sections, and the content of each section is configurable to allow controlling
information exposed to the candidates.
• Header Information Displayed
Info displayed by default:
◦ Job title

◦ Already applied tag

---

## Career Sites
*Chunk ID: OHR-REC-0119 | Chapter: Career Sites*

• Job Info Displayed
Info displayed by default:
◦ Location

◦ Posting Dates
◦ Distance
Additional fields that can be added to the section:
◦ Requisition Number

◦ Organization
◦ Job Category (career site label = Job Family)7. J
◦ Job Function
◦ Worker Type
◦ Regular or Temporary
◦ Management Level
◦ Full Time or Part Time
◦ Job Shift
◦ Job Type
◦ Education Level
◦ Domestic Travel Required
◦ International Travel Required
◦ Work Duration Months
◦ Work Duration Years
◦ Work Hours
◦ Work Days
◦ Legal Employer
◦ Business Unit
◦ Department
◦ Posting expiration date
◦ Primary Work Location and other Work Locations
◦ Responsibilities
◦ Qualifications
◦ Job Requisition Flexfields
Note: Only independent flexfields are supported.
• Job Tags Displayed
Info displayed by default:
◦ Hot Job

---

## Career Sites
*Chunk ID: OHR-REC-0120 | Chapter: Career Sites*

◦ Trending
◦ Be the First to Apply
• Main Content Information Displayed
Info displayed by default:
◦ Short Description
Or, one of the below fields can be added to the section:
◦ Responsibilities

◦ Qualifications

---

## Note: Make sure to expose enough information on job on the search results list, so the jobs can be
*Chunk ID: OHR-REC-0121 | Chapter: Career Sites*

differentiated by the UI and screen reader users. For example, if you post multiple jobs with same title and
location, on the same date, you might want to consider adding a requisition number.
The Display Style of the list can be altered: it can be displayed as list view or card view, job search results list
might also be displayed on a map. The configuration also allows to define the number of items displayed on the
list, infinite scroll or exposing Talent Community sing up button on the list. It also allows styling – using icons vs
labels for the exposed fields, and showing more features, like share and favorite icons, or apply button.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Site Look and Feel Configuration page, find the career site and click Edit.
3. Click the Pages tab.
4. Add a new job search results page or edit an existing one.
5. Scroll down to the Search Results section and click it.
6. Scroll to view the Content section to manage the content and styling. The sequence in which you add the fields
determines the sequence in which they'll display on the search results page.
7. Click Done.
Results:
The fields you selected are displayed in the Job Search Results list.
What to do next
Publish the career site to see the fields on the career site.

---

## Add Job Requisition Flexfields as Search Filters in Career
*Chunk ID: OHR-REC-0122 | Chapter: Career Sites*

Sites
You can add additional job requisition fields to the Job Information section within job descriptions on your external
career sites so that your external candidates get more information about the job.

---

## Create Job Requisition Descriptive Flexfields
*Chunk ID: OHR-REC-0123 | Chapter: Career Sites*

Make Flexfields Visible in Job Requisitions
Make Flexfields Searchable on Career Sites
This feature requires Oracle Search.
Watch video

---

## Create Job Requisition Descriptive Flexfields
*Chunk ID: OHR-REC-0124 | Chapter: Career Sites*

1.
2.
3.
4.
5.
6.

Go to the Setup and Maintenance work area and click the Tasks icon.
Click Search.
Search for the task Job Requisition Descriptive Flexfields.
Click the task name.
On the Job Requisition Descriptive Flexfields page, click the Edit icon.
In the Global Segments section, click the Create icon to create a job requisition descriptive flexfield segment.
Note: Only character data type is supported for flexfields.

7. Select a value set.
8. Click Save and Close.
9. On the Job Requisition Descriptive Flexfields page, click Deploy Flexfield.

---

## Make Flexfields Visible in Job Requisitions
*Chunk ID: OHR-REC-0125 | Chapter: Career Sites*

To make the job requisition flexfields visible, you need to edit both the Recruiting - Create Requisition and Recruiting View and Edit Requisition actions in Transaction Design Studio. The configuration is the same for both actions.
1. Access a sandbox which includes HCM Experience Design Studio.
a. Click the Navigator menu.
b. Expand the Configuration section and click Sandboxes.
c. Create a sandbox or select one which includes HCM Experience Design Studio.
2. On the Home page, go to My Client Groups.
3. In the Quick Actions menu, click HCM Experience Design Studio.
4. Click the Transaction Design Studio tab.
5. Select the action Recruiting - Create Requisition.
6. Click Add to create a new rule to display flexfields or edit an existing rule.
7. In the Page Attributes section, select the Details region.
8. Set the Job Requisition Descriptive Flexfield to Visible.
9. Click the Edit icon to edit the flexfield. Select a flexfield content code and a flexfield attribute. Set the field as
being visible. Even though all configured flexfields are shown in the menu and can be selected, only global
segments with character data type can be used as filters.
Note: The Required field isn't functional. If you change it, it won't have any effect.
10. Click Done.
11. Click Save and Close.
12. Repeat the same steps for the Recruiting - View and Edit Requisition action.

---

## Make Flexfields Searchable on Career Sites
*Chunk ID: OHR-REC-0126 | Chapter: Career Sites*

To allow candidates to filter job search results using job requisition flexfields, you need to edit the action Recruiting Define Career Site Search Filters.
1. Select the action Recruiting - Define Career Site Search Filters.
2. Click Add to create a rule or edit an existing rule.
3. In the Basic Details section, you can select a career site in the Site Name field. If no site is selected, the rule
applies to all sites.
4. In the Page Attributes section, select the Search Filters region.
5. Set the Job Requisition Descriptive Flexfield to Visible.
6. You can edit individual flexfields. Click the Edit icon. Select a flexfield content code and a flexfield attribute. Set
the field as being visible. Even though all configured flexfields are shown in the menu and can be selected, only
global segments with character data type can be used as filters.
Note: The Required field isn't functional. If you change it, it won't have any effect.
7. Click Done.
8. Click Save and Close.
What to do next
Publish the sandbox to make the changes visible.

---

## Add Job Requisition Flexfields to Job Details Pages in
*Chunk ID: OHR-REC-0127 | Chapter: Career Sites*

Career Sites and Agency Portals
You can add job requisition descriptive flexfields (DFF) to job details pages in external career sites, the internal career
site, and agency portals.
Static URL DFFs are also supported. The display type Static URL must be selected when configuring the global segment
of the DFF.
This DFF type isn't supported: View Object.
Note: This feature requires Oracle Search.
To add job requisition flexfields to job details pages in external career sites:
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Define Job Requisition Details for External Career Sites.
5. Click Add to create a rule to display flexfields.
6. In the Basic Details section, enter a name and a description for the rule. Select a career site in the Site Name
field. If no site is selected, the rule applies to all sites.
7. In the Page Attributes section, select the Job Info region.
8. Set the Job Requisition Descriptive Flexfield to Visible.

---

## Career Sites
*Chunk ID: OHR-REC-0128 | Chapter: Career Sites*

9. You can edit individual flexfields. Click the Edit icon. Select a flexfield content code and a flexfield attribute. Set
the field as being visible.
Note: The Required field isn't functional. If you change it, it won't have any effect.
10. Click Done.
11. Click Save and Close.
To add job requisition flexfields to job details pages in an internal career site:
1.
2.
3.
4.
5.
6.
7.
8.

On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
Click the Transaction Design Studio tab.
Select the action Recruiting - Define Job Requisition Details for Internal Career Site.
Click Add to create a rule to display flexfields.
In the Basic Details section, enter a name and a description for the rule.
In the Page Attributes section, select the Job Info region.
Set the Job Requisition Descriptive Flexfield to Visible.
You can edit individual flexfields. Click the Edit icon. Select a flexfield content code and a flexfield attribute. Set
the field as being visible.
Note: The Required field isn't functional. If you change it, it won't have any effect.

9. Click Done.
10. Click Save and Close.
To add job requisition flexfields to job details pages in agency portals:
1.
2.
3.
4.
5.
6.
7.
8.

On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
Click the Transaction Design Studio tab.
Select the action Recruiting - Define Job Requisition Details for Agencies.
Click Add to create a rule to display flexfields.
In the Basic Details section, enter a name and a description for the rule.
In the Page Attributes section, select the Job Info region.
Set the Job Requisition Descriptive Flexfield to Visible.
You can edit individual flexfields. Click the Edit icon. Select a flexfield content code and a flexfield attribute. Set
the field as being visible.
Note: The Required field isn't functional. If you change it, it won't have any effect.

9. Click Done.
10. Click Save and Close.

---

## Configure Career Site Tags
*Chunk ID: OHR-REC-0129 | Chapter: Career Sites*

Tags are displayed beneath jobs in career site search results, and for jobs on job details pages. They help you to promote
certain job requisitions, or to display more information about jobs to candidates. They also display for events (available
in Recruiting Booster) so candidates can quickly see which events they've already interacted with.
If you've set up custom search results pages or custom job details pages, you can also configure the style of the tags on
those pages to match your branding.
Note: Job tags are available for use with career sites using the Minimal template.

---

## Promote particular job requisitions on external career sites by displaying the Hot Job tag to indicate a
*Chunk ID: OHR-REC-0130 | Chapter: Career Sites*

job is in high recruiting demand. The tag is visible in search results and on job details pages. The tag
can also be used as a criterion in the custom job list component.
For instructions on displaying this tag, see Display the Hot Job Tag in Career Sites.

Trending

---

## Promote job requisitions based on the number of submitted job applications by displaying the
*Chunk ID: OHR-REC-0131 | Chapter: Career Sites*

Trending tag for requisitions. The tag is visible in search results and on job details pages. By default,
if there are more than 50 candidate applications for a job, this tag is shown beneath the job in search
results. For instructions on configuring this tag, see Configure the Trending Tag.

---

## Promote job requisitions based on the number of submitted job applications by displaying the Be The
*Chunk ID: OHR-REC-0132 | Chapter: Career Sites*

First to Apply tag. The tag is visible in search results and on job details pages. By default, if there are
5 or fewer candidate applications for a job, this tag is shown beneath the job in search results. For
instructions on configuring this tag, see Configure the Be The First to Apply Tag.

---

## The Already Applied tag displays to authenticated candidates for jobs they already applied to. The
*Chunk ID: OHR-REC-0133 | Chapter: Career Sites*

tag is visible in search results. If a candidate applied for a job, but didn't confirm their application, a
different label displays that says Must Confirm. Similarly, on job detail pages, if a candidate has already
applied for a job, there's a You Already Applied message that displays on an inactive button on the job
details page. If a candidate applied, but didn't confirm, an active button displays that says Confirm Your
Job Application.
You don't need to do anything to enable this tag.

---

## Display the Hot Job Tag in Career Sites
*Chunk ID: OHR-REC-0134 | Chapter: Career Sites*

Promote particular job requisitions on external career sites by displaying the Hot Job tag to indicate a job is in high
recruiting demand. The tag is visible in search results and on job details pages.
You can change the tag's visibility and styling for custom search results pages. You can also use it as a criterion in the
custom job list component. This tag is only visible on external career sites using the Minimal template.
You make the Hot Jobs field visible using Transaction Design Studio.

---

## Career Sites
*Chunk ID: OHR-REC-0135 | Chapter: Career Sites*

1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select one of these actions: Recruiting - Create Job Requisition or Recruiting - View and Edit Job Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule.
7. In the Page Attributes section, select Configuration.
8. For Hot Jobs, select Visible from the second drop-down list.
9. Click Save and Close.
What to do next
You then need to set the Hot Job option to Yes in the job requisition, in the Configuration section.
Related Topics
• How You Configure Recruiting Pages Using Transaction Design Studio

---

## Configure the Trending Tag
*Chunk ID: OHR-REC-0136 | Chapter: Career Sites*

Promote job requisitions based on the number of submitted job applications. You can configure the default number
of job applications a requisition must receive for the Trending tag to display on career sites. The tag is visible in search
results and on job details pages.
By default, if there are more than 50 candidate applications for a job, this tag is shown beneath the job in the search
results list and on job details pages.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Candidate Experience section and click Edit.
3. In the Job Tags section, enter the number of submitted job applications in the Trending field.
The default value is 50.
4. Click Save.

---

## Configure the Be The First to Apply Tag
*Chunk ID: OHR-REC-0137 | Chapter: Career Sites*

Promote job requisitions based on the number of submitted job applications by displaying the Be The First to Apply tag.
You can configure the default number of job applications a requisition must receive for the Be the First to Apply tag to
display on career sites. The tag is visible in search results and on job details pages.
This tag indicates that a job requisition has few or no candidate applications. It displays when the active candidate
applications count is less than or equal to the value configured. By default, if there are 5 or fewer candidate applications
for a job, this tag is shown beneath the job in search results.

---

## Career Sites
*Chunk ID: OHR-REC-0138 | Chapter: Career Sites*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. In the Job Tags section, enter the number of submitted job applications in the Be the First to Apply field.
The default value is 5.
4. Click Save.

---

## Hide the Be The First to Apply Tag
*Chunk ID: OHR-REC-0139 | Chapter: Career Sites*

You can hide the Be the First to Apply tag on career sites.
By default, if there are 5 or fewer candidate applications for a job, this tag is shown beneath the job on the search results
list and within the job details.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. In the Job Tags section, enter -1 in the Be the First to Apply field.
4. Click Save.

---

## Hide the Be The First to Apply Tag on a Custom Search
*Chunk ID: OHR-REC-0140 | Chapter: Career Sites*

Results Page
You can hide the Be the First to Apply tag on a custom job search results page.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. Click Edit next to a career site.
3. On the Pages tab, locate a custom search results list and deactivate it.
4. Click the Settings icon and select Edit.
5. Click the section that displays the job list.
6. Scroll to the Content section.
7. In the Additional Job Information field, remove the Be the First to Apply tag.

---

## Configure Recommended Jobs Based on Candidate
*Chunk ID: OHR-REC-0141 | Chapter: Career Sites*

Resume
You can allow candidates to upload their resumes and receive a list of recommended jobs weighted and tailored for their
current job title, location, and skills.
Candidates can either drag-and-drop their resumes or click Upload Resume. Once the resume is uploaded, a
congratulations message is displayed and candidates are shown weighted job results based on their current job title,
location, then skills. Let's say a candidate uploads a resume that states that they're a Product Manager located in New
York. The jobs that display higher in the list will be those for product managers with the job location in New York.
Note: Resume information is only stored on a per-session basis. Resumes aren't permanently stored. Once
candidates click View All Jobs to see weighted search results again, they'll need to re-upload their resumes.
You can configure the Recommended Jobs Element to match the career site look and feel. You can also configure the
call to action and other text elements.
Before you start
The career site must have the Resume Parsing functionality set to active. If Resume Parsing isn't active, the feature is
still enabled, but it won't display.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Site Look and Feel Configuration page, select Edit next to a career site.
3. On the General tab, in the Recommended Jobs section, select the option Enable recommended jobs based on
upload.
4. On the Pages tab, select the page where you want to add the Recommended Jobs element.
The element can be placed on any page except the Job Details page.
5. In the Actions menu, select Recommended Jobs.
6. In the Overall Display section, you can configure these elements:
a. In the Button Size field, select how you want to display the Upload Resume button: small, medium, or large.
b. Select the Enable Privacy Policy option if you want to display a privacy policy to candidates. When you
select that option, you can enter the privacy policy text.
c. In the Desktop Call to Action field and the Mobile Call to Action field, you can change the instructions that
appear on the career site.
d. In the Call to Action Button field, you can change the button label.
7. Click Done.

---

## Import and Export Selected Career Sites
*Chunk ID: OHR-REC-0142 | Chapter: Career Sites*

You can share your career site settings with others by exporting the career sites to zip files. You can then import the
career sites you've exported.
You can import one or more career site settings to a new site.
Note: Oracle also has template design files that you can import and use as a starting place to help you design your
company's career site. Use the link in Did you know section located at the bottom of the Career Site Look and Feel
Configuration page to view the available template design files.

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
2. In the Actions menu next to Career Sites Configuration, select Export to CSV File > Create New.
3. In the Show drop-down list, select Scope Enabled.
4. Click Save and Close.
5. Repeat the steps above until you've added all the sites you want to export.
6. Click Submit.
Results:
Depending on how many career sites you're exporting, it might take 5-10 minutes before the file is ready to download.
You can check the status of the export from the Actions menu. Once complete, you'll receive a link to download the file.
What to do next
You can also import a file of career sites to into your environment by selecting the Import from CSV File action.
(Recruiting and Candidate Experience > Candidate Experience > Actions menu for Career Site Configuration > select
Import from CSV file > click Create New > import the appropriate file.)

---

## Example of Changing the Back to Career Site Button
*Chunk ID: OHR-REC-0143 | Chapter: Career Sites*

Color on a Career Site
This example describes how you can change the color of the Back to Career Site button on an external career site.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, locate a career site and click Edit.
3. Click the Themes tab.
4. Expand the section Custom CSS.

5. Copy and paste this code in the Display Editor Window field. You can change the color to any color.
.buttons-bar__button[data-bind="click: back"]{
color: red;
}

6. Click Apply Changes.
7. Publish the career site.

---

## Career Site Cookies
*Chunk ID: OHR-REC-0144 | Chapter: Career Sites*

External career sites use essential and nonessential cookies.
Essential cookies are strictly necessary to provision the service, and are exempt from the consent requirement. These
can be installed without user permission, regardless of whether cookie consent is given by a candidate. If a candidate
blocks cookies as a browser setting, the career site won't function properly.
This table presents the list of essential cookies. These cookies are all categorized as Strictly Necessary.

Cookie

Purpose

---

## This cookie is used by Akamai to optimize site security by
*Chunk ID: OHR-REC-0145 | Chapter: Career Sites*

distinguishing between humans and bots. This cookie is set
when customer is using Akamai as their CDN.

1 hour

bm_sv

---

## This cookie is necessary for the Akamai cache function. A cache 1 hour
*Chunk ID: OHR-REC-0146 | Chapter: Career Sites*

is used by the website to optimize the response time between
the visitor and the website. The cache is usually stored on the
visitor's browser. The users bandwidth results are stored within
this cookie to help ensure the bandwidth test isn't repeated for
the same user repeatedly for the Akamai cache functionality.
This cookie is set when customer is using Akamai as their CDN.

ORA_FND_SESSION_<PODNAME>_F

---

## This is a session cookie set by Oracle Cloud or middleware for
*Chunk ID: OHR-REC-0147 | Chapter: Career Sites*

tracking web sessions and routing traffic to the correct servers.
This cookie is deleted at the end of the session.

---

## This is a session cookie set by Oracle Cloud or middleware for
*Chunk ID: OHR-REC-0148 | Chapter: Career Sites*

tracking web sessions and routing traffic to the correct servers.
This cookie is deleted at the end of the session.

---

## This is a session cookie set by Oracle Cloud or middleware for
*Chunk ID: OHR-REC-0149 | Chapter: Career Sites*

tracking web sessions and routing traffic to the correct servers.
This cookie is deleted at the end of the session.

---

## This is a session cookie set by Oracle Cloud or middleware for
*Chunk ID: OHR-REC-0150 | Chapter: Career Sites*

tracking web sessions and routing traffic to the correct servers.
This cookie is deleted at the end of the session.

---

## This is a session cookie set by Oracle Cloud or middleware for
*Chunk ID: OHR-REC-0151 | Chapter: Career Sites*

tracking web sessions and routing traffic to the correct servers.
This cookie is deleted at the end of the session.

---

## This is a domain scoped Webgate cookie that has a boolean
*Chunk ID: OHR-REC-0152 | Chapter: Career Sites*

value: either "1" or "0" set by Oracle Access Manager (OAM) for
tracking authenticated web sessions and routing traffic to the
correct servers. This cookie is deleted at the end of the session.

---

## This is an encrypted server scoped cookie that's generated by
*Chunk ID: OHR-REC-0153 | Chapter: Career Sites*

the Access Server and Webgate to store session information.
This cookie is deleted at the end of the session.

---

## This is an encrypted server scoped session cookie that's
*Chunk ID: OHR-REC-0154 | Chapter: Career Sites*

generated by the Access Server. It contains server state
that's needed to continue processing http request. It can be
broken into multiple cookies if it exceeds the size defined
in the deployment descriptor. Each cookie that's created is
represented by oam_req_0, oam_req_1, and so on. The number
of cookies created is tracked by oam_req_count. This cookie is
secure and http only.

---

## See above. The OAM_REQ_n can be broken into multiple
*Chunk ID: OHR-REC-0155 | Chapter: Career Sites*

cookies if it exceeds the size defined in the deployment
descriptor. Each cookie that's created is represented by oam_
req_0, oam_req_1, and so on. The number of cookies created is
tracked by oam_req_count.

---

## This is a transient cookie that's set or cleared by the Webgate
*Chunk ID: OHR-REC-0156 | Chapter: Career Sites*

and protected by Oracle Access Manager (OAM) server. This
cookie stores the state about user's original request to a
protected resource. This cookie is secure and http only.

---

## Nonessential cookies are used for user tracking purposes. They control add-on features available to returning
*Chunk ID: OHR-REC-0157 | Chapter: Career Sites*

candidates such as favorite jobs or language settings across session. To enable the tracking of candidate activities, you
need to configure the cookie consent feature on the career site, and candidates must accept the cookie consent. The
cookie consent is presented when candidates visit the career site for the first time and during a consecutive visit when
cookies weren't previously accepted.
Here's an example: [SITE_NUMBER] can be replaced with Site Display Name:
https://[domain]/hcmUI/CandidateExperience/en/sites/[site_number]/
This table presents the list of nonessential cookies.

Cookie

Purpose

---

## This cookie will be set when
*Chunk ID: OHR-REC-0158 | Chapter: Career Sites*

candidates either accept all cookies
(includes non essential) or accepts
Functional cookies when Cookie
Preferences is enabled.

CX_<SITE_NUMBER>_
cookieAccept_analytical

---

## This cookie is used to store the
*Chunk ID: OHR-REC-0159 | Chapter: Career Sites*

90 days
candidate's choice for Analytical
and Performance cookies.
This cookie will be set when
candidates either accept all cookies
(includes non essential) or accepts
Analytical cookies when Cookie
Preferences is enabled.

---

## This cookie is used to store the
*Chunk ID: OHR-REC-0160 | Chapter: Career Sites*

90 days
candidate's choice for custom
category cookies.
This cookie will be set when
candidates either accept all cookies
(including non essential cookies)
or accept custom cookies when
Cookie Preferences is enabled,
provided the Custom Cookie
category is configured. The
Custom Cookie category can be
configured if you’re using any
third-party tool that adds cookies
to the career site.

---

## This cookie is used to store the
*Chunk ID: OHR-REC-0161 | Chapter: Career Sites*

candidate's choice to decline all
cookie categories.
This cookie will be added when
cookie consent widget includes
a decline button, and candidate
declines to track non essential
cookies.

90 days

NA

90 days

Functional

---

## For more information see the
*Chunk ID: OHR-REC-0162 | Chapter: Career Sites*

section called "Cookie Consent
Feature Behavior with Different
Configurations" in .

ORA_CX_USERID_FUNCTIONAL

---

## This cookie is used to store a
*Chunk ID: OHR-REC-0163 | Chapter: Career Sites*

candidate’s choice of favorite jobs
and to track whether a returning
candidate has already validated
their authentication.
When this cookie is present, it
retains the candidate’s favorite
job choices and bypasses Last
Name or Date of Birth validation
during sign in if the Verify date

---

## Cookie Category
*Chunk ID: OHR-REC-0164 | Chapter: Career Sites*

of birth and allow email claim or
Verify last name and allow phone
number claim options are enabled.

ORA_CX_USERID

---

## This cookie is used to store the
*Chunk ID: OHR-REC-0165 | Chapter: Career Sites*

candidate language preference.
Next time the candidate visits the
career site that it will be loaded in
the user preferred language.

90 days

Functional

ORA_CX_DEVICEID

---

## This cookie is used for the Keep
*Chunk ID: OHR-REC-0166 | Chapter: Career Sites*

Me Signed In feature. It's used
to recognize the device used by
the candidate to allow automated
verification of candidate when
Keep Me Signed In option was
selected in the past on the same
device. This cookie isn't tied to the
cookie consent.

90 days

---

## A random number that's generated
*Chunk ID: OHR-REC-0167 | Chapter: Career Sites*

and mapped to candidate’s USERID
for unique identification will be
stored in this cookie. No other
information regarding the user’s
device will be stored.

ORA_FPC

---

## This cookie is used for user
*Chunk ID: OHR-REC-0168 | Chapter: Career Sites*

tracking purposes.

Related Topics
• Configure Third-Party or Custom Cookies
• Configure Cookie Consent on the Career Site

---

## Configure Cookie Consent on the Career Site
*Chunk ID: OHR-REC-0169 | Chapter: Career Sites*

You can configure cookie consent on external career sites to comply with the data protection regulations governing
cookies in various countries. If cookie consent isn't enabled on a site, nonessential cookies are stored by default. If
cookie consent is enabled, non essential cookies are stored only on candidate's explicit consent.

---

## Career Sites
*Chunk ID: OHR-REC-0170 | Chapter: Career Sites*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, click Edit next to a career site.
3. Click the General tab.
4. Expand the Cookie Consent Message section.
5. Configure the cookie consent content and button labels. Default descriptions and labels are provided, but you can
edit them to suit your organization's needs.
◦ Cookie Consent Message - this message is visible on the cookie consent banner to candidates who visit the
career site for the first time and to returning candidates who didn't accept non essential cookies before or
cleared cookies on the site.
◦ Link Text to Open Cookie Policy - you can edit the field to match your organization's needs.

◦ Cookie Policy - the detailed description of the policy that displays when a candidate clicks the link in the
cookie consent message. You can include a thorough explanation of the non essential cookies you'll be
storing. You can also explain which essential cookies are stored on the site that don't require candidate
consent. The cookie policy can include links to external sites.
Accept Button Label - the text that displays on the accept button.

◦
◦ Enable button to decline cookie - select the checkbox to indicate that you want to include a decline button.
◦ Decline Button Label - the text that displays on the decline button if you selected Enable button to decline
◦

cookie.
Enable cookie preferences - lets you provide users with more opportunities to accept or decline cookies
based on categories. This is disabled by default. Once enabled, the following fields are available to you, and
you can update them.
- Cookie Preferences Button Label - the text that displays on the Manage Preferences button or label.
- Cookie Preferences Save Button Label - the text that displays on the save button in the Cookie
Preferences modal.
- Cookie Policy - repeated in this section for consistency. The twin field above along with Link Text
to Open Cookie Policy will be disabled, and candidates can view the cookie policy from Cookie
Preferences modal.
- Strictly Necessary Cookies - the description that displays in this cookie category in the Cookie
Preferences modal.
- Functional Cookies – the description that displays in this cookie category in the Cookie Preferences
modal.
- Analytical and Performance Cookies – the description that displays in this cookie category in the
Cookie Preferences modal.
- Add Cookie Category to add one custom category

Note: You can update the labels for these cookie categories using the User Interface Text tool.
Note: Candidates can select the cookie categories they want to consent to. The Strictly Necessary Cookies
category is always active.
6. Click Preview to see how the cookie consent message will be displayed.
7. Click Publish site.
What to do next

---

## Career Sites
*Chunk ID: OHR-REC-0171 | Chapter: Career Sites*

Open the Widgets tab, and configure the look and feel of the modals.
Note: Once a candidate accepts or declines cookies, the cookie consent modal isn't presented to them again until
they clear their browser cookie history. However, you can add a link to cookie preferences in either the header or
footer to provide candidates with a way to change their preferences without having to clear their cookie history. Add
the cookie preferences as links within custom content pages.

---

## Configure Third-Party or Custom Cookies
*Chunk ID: OHR-REC-0172 | Chapter: Career Sites*

You can use custom JavaScript to enable third-party integrations that store cookies in any category. The executions can
be controlled based on a candidate’s preference using a variable given for each category.
Standard cookies used by Recruiting are added directly when the respective cookie category is selected by the
candidate. Use following category variables to control the cookies from third-party applications that are added by
custom JavaScript.
• Functional Cookies: vFunctionalCookies
• Analytical and Performance Cookies: vAnalyticalPerformanceCookies
• Custom cookie category: vCustomCookies

---

## Custom Cookie Category
*Chunk ID: OHR-REC-0173 | Chapter: Career Sites*

You can add one custom cookie category with the desired name and description to control the cookies that doesn’t fit in
the default categories. Add a condition in the custom JavaScript to execute the script to enable custom cookie category
functionalities only when vCustomCookies=true.

---

## Other Cookie Categories
*Chunk ID: OHR-REC-0174 | Chapter: Career Sites*

If you're adding any functionalities using custom JavaScript that store cookies of either functional analytical and
performance types, then those script executions can be controlled to run based on a candidate’s preference. Add the
condition in the scripts to execute when vFunctionalCookies=true or vAnalyticalPerformanceCookies=true respectively.

---

## Cookie Consent Feature Behavior with Different Configurations
*Chunk ID: OHR-REC-0175 | Chapter: Career Sites*

There are different ways to configure cookie consent feature with or without cookie specific categories and behavior
would be as follows:
1. Essential cookies or Strictly Necessary cookies will always be stored irrespective of whether cookie consent
feature is enabled or not.

---

## Career Sites
*Chunk ID: OHR-REC-0176 | Chapter: Career Sites*

2. Non essential cookies that include Functional, Analytical and Performance, and Custom cookies will work like
this:
a. When cookie consent feature is disabled, non essential cookies will be stored by default.
b. When cookie consent feature is enabled without cookie category preferences then candidate will not see
the cookie categories on the cookie banner and will have two choices.
- Accept all cookies: When candidate accepts cookies then all cookies essential and non essential
cookies will be stored.
- Decline all cookies: When candidate declines cookies then only essential cookies will be stored.
- Decline button not configured: If decline button isn't configured, then candidate will have no other
choice than accepting cookies.
c. When cookie consent feature is enabled with cookie category preferences then the candidate will have
following choices:
- Accept all cookies: When candidate accepts cookies then all cookies essential and non essential
cookies will be stored.
- Decline all cookies: When candidate declines cookies then only essential cookies will be stored.
- Accept specific category cookies: When candidate accepts specific category cookies for example
accepts Functional cookies and declines Analytical cookie then only essential cookies and
functional cookies will be stored.

Related Topics
• Enable Cookie Preferences Link in the Header or Footer

---

## Enable Cookie Preferences Link in the Header or Footer
*Chunk ID: OHR-REC-0177 | Chapter: Career Sites*

Once a candidate accepts or declines cookies, the cookie consent modal isn't presented to them again until they
clear their browser cookie history. You can add a link to cookie preferences in either the header or footer to provide
candidates with a way to change their preferences without having to clear their cookie history.
The cookie preferences link displays the Cookie Policy modal with Accept and Decline buttons as configured when
Enable cookie preferences is disabled. Cookie preferences link will display the Cookie Preferences modal with cookie
categories when Enable cookie preferences is enabled.
1. On the Career Sites Configuration page, click Edit next to a career site.
2. Click the General tab.
3. Expand the Header Links or Footer Links section.
4. Click Add Link or Add Sublink.
5. Enter the link text in the Navigation Link Text field.
6. Select Cookie Preferences from URL. This option is only available when you've enabled the Enable cookie consent
message checkbox.
7. Click Publish site.
You can add cookie preferences as a sublink, but you can't add any other link as sublink under the cookie preferences
link. Similarly, you can add the cookie preferences as a link within custom content pages. The cookie preferences link
is available as a common element and can be configured.

---

## Career Sites
*Chunk ID: OHR-REC-0178 | Chapter: Career Sites*

Related Topics
• Career Site Page Types and Layout
• Configure Cookie Consent on the Career Site

---

## Enable the Job Fit Metric Element
*Chunk ID: OHR-REC-0179 | Chapter: Career Sites*

You can add the Job Fit metrics bar element at the top of a page. This element uses Generative AI to compare
information from a candidate's profile or uploaded resume with the job information on the job details page. This feature
increases the quality of job postings, because candidates receive immediate information on how well they're skills,
experience, education, and domain of expertise match the job requirements.
A candidate's suitability for a job is rated using a 0-5 scale for skills, job history, education, and other data matching the
skills, requirements, and job information from the job details page. This element also provides a summary of why they
received the displayed scores.
Note: Ratings are based on provided data and are subjective. Actual hiring decisions involve a more comprehensive
assessment.

---

## Before you start
*Chunk ID: OHR-REC-0180 | Chapter: Career Sites*

Resume parsing must be active to use this feature.
Here's what to do
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. On the Search page, search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_CE_JOB_FIT_GAI_ENABLED.
6. In the Profile Values section, set the profile value:

◦ Y: Job Fit is enabled.
◦ N: Default value. Job Fit isn't enabled.
7. Click Save and Close.
This element is active for default pages, but you'll need to add it to custom pages.

---

## Enable hCaptcha
*Chunk ID: OHR-REC-0181 | Chapter: Career Sites*

Create a more secure career site experience with hCAPTCHA support. To rule out the possibility that a user entering
a career site is a bot, they're presented with a challenge that they must pass before they can join talent communities,
apply for jobs, and manage profiles.

---

## Career Sites
*Chunk ID: OHR-REC-0182 | Chapter: Career Sites*

hCAPTCHA is activated for candidate experience at the global level. You can have more than one hCAPTCHA
configuration set up, but only one can be active at a time.
Once enabled, hCAPTCHA is used on the following Oracle Recruiting verification pages when they're accessed directly
from the career site:
• Apply to Job
• Register for Event
• Join a Talent Community
• Access a Talent Profile (CSS)
• Other verification screens that open after clicking candidate experience links from email messages (RMI, offer,
interview, etc.) These are links for users who've previously passed the challenge, and proven they aren't bots.
hCAPTCHA isn't used in the following scenarios:
• Users with active Keep Me Signed In are auto-verified when returning to the career site, and therefore aren't
presented with a challenge.
• If you're using the Apply with Indeed optimized experience, it's assumed that candidates have already been
verified on the Indeed site, so no challenge is presented on the career site.
Before you start
To enable this feature you must first obtain the hCAPTCHA API keys from https://www.hcaptcha.com.
Here's what to do
1. In the Setup and Maintenance work area, go to:

◦ Setup: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Configure Candidate Experience CAPTCHA Provider
2. Click Add.
3. Enter a name, code, and description.
4. Select hCAPTCHA as the provider.
5. Complete the Provider Setting fields using the information you obtained from hCAPTCHA.
6. Click Save and Close.
Results:
Once you've created a configuration, it's added in draft status. Select Activate from the actions menu next to the
provider when you're ready to activate it.

---

## Enable a Site Display Name for a URL
*Chunk ID: OHR-REC-0183 | Chapter: Career Sites*

Enhance your corporate branding by defining a site display name for the URL. Site display names can be used in
external career site URLs instead of a site number.
You can still use the original site number to access the website. It's recommended that you don't change a site display
name once you've published the career site. This is because candidates who may have bookmarked the URL with the

---

## Career Sites
*Chunk ID: OHR-REC-0184 | Chapter: Career Sites*

original site display name will no longer be able to access the site. Candidates won't be able to access links sent to their
emails (such as referrals), and they may also have difficulties in accessing the site using search engines.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, click Edit next to a career site.
3. Type the name you want in the Site Display Name for URL field.
4. Click Publish.

---

## Enable Vanity URL
*Chunk ID: OHR-REC-0185 | Chapter: Career Sites*

You can use a corporate vanity URL to allow external candidates to access external career sites. A vanity URL is a
descriptive, pronounceable, truncated URL that also extends an organization’s brand.
When you enable the vanity URL feature, the vanity URL is used throughout the candidate journey in the career site, and
in candidate facing communication. Once a vanity URL is set, it's used across all career sites.
Note: You must use a subdomain, such as https://jobs.vision.com, to use the vanity URL feature. Relative path URLs
such as https://www.vision.com/careers aren't supported.
Here’s an example of how vanity URL works. Let’s say a company has the following web domain address: https//
jobs.vision.com.
• The company hosts a Node.js function on a serverless compute service and creates an Application Load
Balancer with the cloud provider of choice for the Vanity Career Site Application.
• Adds the newly created Application Load Balancer as the trigger for the Node.js function deployed on the
serverless compute service. The trigger for the Node.js function is an incoming request to either the Vanity
Career Site Application’s API Gateway, Application Load Balancer, or a CDN/edge compute for your Vanity
Career Site Application.
• Create a DNS record that maps the company’s vanity address to the IP or canonical name (CNAME) for the
Application Load Balancer that triggers the Node.js function. Any request to the company’s vanity career site
will then trigger the Node.js function to execute.
• Now when the candidates visit https://jobs.vision.com from their web browser, requests for https://
jobs.vision.com are routed to the Application Load Balancer which triggers Node.js function deployed on the
serverless compute service.
• The Node.js function containing the actual Fusion Application URL will forward the request to the Fusion
Application host.
• The Fusion Application server will then respond back with the career site HTML.
• The Node.js function will relay the response from Fusion Application server to the candidate’s browser.
Note: The initial request to fetch the career site will hit the Vanity URL application load balancer that triggers the
Node.js function. Other resources are directly loaded from the Fusion applications instance from the client browser
without going via the load balancer.

---

## Career Sites
*Chunk ID: OHR-REC-0186 | Chapter: Career Sites*

To enable a vanity URL, you need to:
1.
2.
3.
4.
5.
6.

Host Node.js function on a serverless compute service.
Set Up CORS.
Enable Vanity URL.
Review Third-Party Integrations Setup.
Review Features Not Supporting Vanity URL.
Test the Configuration.

---

## Host Node.js Function on a Serverless Compute Service
*Chunk ID: OHR-REC-0187 | Chapter: Career Sites*

Work with your IT department to complete this step.
• Host a Node.js function on a serverless compute service. (Examples include AWS Lambda, OCI Function, or
Azure Function). This function forwards the initial request for the career site resource to the Fusion Application
instance and responds back to the client.
• A sample Node.js function is available for you to use as a guide in the My Oracle Support document called Set
Up Search Engine Optimized Career Site Vanity URL (Doc ID 3004743.1). Update the script with your Fusion
Applications URL and Vanity URL as instructed in the sample file. After updating the function with the required
URLs, add it to run on the Node.js serverless compute instance.
• Create an Application Load Balancer with the cloud provider of choice for the Vanity Career Site Application.
(Examples include AWS Elastic Load Balancer, Azure Load Balancer, and OCI Load Balancer.)
• Add the newly created Application Load Balancer as the trigger for the Node.js function deployed on the
serverless compute service. The trigger for the Node.js function is an incoming request to either the Vanity
Career Site Application’s API Gateway, Application Load Balancer, or a CDN/edge compute for your Vanity
Career Site Application.
• Create a DNS record that maps the company’s vanity address to the IP or canonical name (CNAME) for the
Application Load Balancer that triggers the Node.js function. Any request to the company’s vanity career site
will then trigger the Node.js function to execute.
• The serverless compute service hosting the Node.js function fronts the Fusion application instance where the
career site content will be fetched from.
You must use subdomain such as https://jobs.vision.com to use the vanity URL feature. Relative path URLs
such as https://www.vision.com/careers aren't supported.

---

## Things to Consider While Switching to Search Engine Optimized Vanity
*Chunk ID: OHR-REC-0188 | Chapter: Career Sites*

URL Solution
If you used vanity URL before release 24A, you'll need to perform the following additional checks:
• If you’re currently using a relative path Vanity URL (like https://www.vision.com/careers):
◦ You need to use a new subdomain address (such as https://jobs.vision.com) as the Vanity URL while
switching to the new recommended search engine optimized solution. However, the links generated with
relative path URLs before the switch will stop functioning.
◦ To support the links generated before the switch, you'll need to continue hosting the static HTML at your
current subdomain (for example: https://www.vision.com/careers). Within the static HTML, you can
install a script to redirect the client request to the new Vanity URL address used for the search engine
optimized solution on load of the page.
◦ A sample script is available for you to use as a guide in the My Oracle Support document called Set Up
Search Engine Optimized Career Site Vanity URL (Doc ID 3004743.1).

• If you’re hosting the vanity site at your root domain or subdomain (like https://careers.vision.com) currently,
then:
◦ The same subdomain can be used while switching to the new search engine optimized solution. However,
the deep links that were generated before the switch will stop functioning as they're generated with
hashtag (#) in the URL.
◦ To support these links, you need to add a custom JavaScript in the career site configuration Theme tab
that will redirect the candidate/client request with hashtag URLs to the hashtag free Vanity URL address
on load of the page.
◦ A sample custom JavaScript is available for you to use as a guide in the My Oracle Support document
called Set Up Search Engine Optimized Career Site Vanity URL (Doc ID 3004743.1).
Note: Generally, the vanity site points to the highest order career site (the first site with Active status on the
Career Site Configuration page). If it's pointed to any other site, then the custom JavaScript should be added
to both the highest order site and the vanity site.

---

## Set Up CORS
*Chunk ID: OHR-REC-0189 | Chapter: Career Sites*

1.
2.
3.
4.
5.
6.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code ORA_CORS_ORIGINS.
Go to the Profile Values section.
◦ If the Site row already exists, make sure to retain the existing value and append the Vanity URL domain to
it.
◦ If the Site row doesn’t exist, create a Site Row and assign the Vanity URL domain.

7. Ensure the value “self” is part of the profile option value. Here’s an example.
Syntax

Example

'self' <vanityURL>

'self' https://jobs.vision.com

'self' <optional - existingURLValue>

'self' https://abc.previousvalues.com https://jobs.vision.com

<vanityURL>

8. Make sure to only enter the vanity URL domain or subdomain; don’t include any part of the relative path.
Example:
If the vanity URL is https://jobs.vision.com, add https://jobs.vision.comand and https://vision.com to the
profile option value.
9. Search for the profile option CORS_ACCESS_CONTROL_ALLOW_HEADERS.
10. Go to the Profile Values section.
11. Append these values to existing profile option value: ora-irc-language, ora-irc-access-code, ora-irc-

validation-mode, ora-irc-vanity-domain, ora-irc-cx-userid, ora-irc-oauth-token, ora-irc-cx-timestamp,
ora-irc-rest-action

12. Verify that you've entered the values exactly as specified. Make sure that there’s no extra blank space or
missing hyphens.
13. Click Save and Close.

---

## Enable Vanity URL
*Chunk ID: OHR-REC-0190 | Chapter: Career Sites*

You need to enable the Vanity URL feature in the Setup and Maintenance work area.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. Select the Vanity URL option.
4. Enter the URL. Example: https://jobs.vision.com
Select the Use search engine optimized setup option.
5. Disable the Keep Me Signed In feature. You can't use a vanity URL if this feature is enabled.
6. Click Save.

---

## Review Third Party Integrations Setup
*Chunk ID: OHR-REC-0191 | Chapter: Career Sites*

If you enabled LinkedIn Profile Import, make sure to add the vanity domain.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Category Provisioning and Configuration page, go to the Profile Import section and click Edit.
3. On the Profile Import Partners page, go to the Social Media section and review the LinkedIn details. Make
sure you entered an allowlisted URL for the vanity domain. The URLs must be in the format https://
<company_vanity_hostname> for the vanity domain.
4. Click Save.
Note: If you enabled Apply with Indeed then you need to configure the redirection URL with vanity domain
like https://<company_vanity_hostname>/profileImport/oauth . For example, https://jobs.vision.com/
profileImport/oauth.

---

## Review Features Not Supporting Vanity URL
*Chunk ID: OHR-REC-0192 | Chapter: Career Sites*

Review the list of features that don’t work with Vanity URL.
• Keep me signed in: This feature isn’t compatible with the vanity URL feature. Turn off this feature if Vanity URL
is enabled.
• Career site links in site editor: All redirections from the editor to career sites or pages (for example, “Go To Site”
link) won’t use the vanity URL; Fusion Application CE links will be used instead.
• Job details page link copied from a requisition’s preview.

---

## Test the Configuration
*Chunk ID: OHR-REC-0193 | Chapter: Career Sites*

Test your configuration on a test or staging environment. Test all candidate facing use cases before enabling Vanity URL
in production.
Related Topics
• Set Up Search Engine Optimized Career Site Vanity URL
• Configure CORS Headers

---

## Configure Search Engine Optimization
*Chunk ID: OHR-REC-0194 | Chapter: Career Sites*

You can increase your career site's visibility on the Internet by configuring search engine optimization (SEO) fields
at both the global and page-level. This helps search engines to tie your career site and specified pages to your
organization.
If you don't set anything specific at the page level, then a page uses the global level settings.

---

## Global Level SEO
*Chunk ID: OHR-REC-0195 | Chapter: Career Sites*

On the General tab for a career site, enter the appropriate information for organization name, organization URL, and
organization logo. The Organization Name, Organization URL, and Organization Logo fields are used to help search
engines tie the career site page to your organization. Web designers typically enter this information in the header tag
of a web page. Because job search and custom pages don't have headers, and they could have a different IP address
and domain than that of your parent organization you'll want to enter the Organization URL and Organization Logo in
the SEO Optimization fields. The logo is used to help search engines to identify your job search and custom pages as
belonging to your organization.
Note: You can add vanity URLs in the URL field.

---

## Page Level SEO
*Chunk ID: OHR-REC-0196 | Chapter: Career Sites*

On the Pages tab for a career site, enter an SEO description, and SEO keywords. The SEO settings you make at the
page level override the global settings. If you don't set anything specific at the page level, the page uses the global level
settings.

---

## Page Display Name for URL for Custom Pages
*Chunk ID: OHR-REC-0197 | Chapter: Career Sites*

Use page display names to make it easy for users and search engines to understand the purpose of a career site custom
page. Page display names replace the page ID numbers in the URLs. For example, you could indicate in the URL that a
page is about a company's benefits, instead of showing a random page ID number like 11605.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. Pick a career site and click the gear icon.

3.
4.
5.
6.
7.
8.
9.
10.

---

## Career Sites
*Chunk ID: OHR-REC-0198 | Chapter: Career Sites*

Click Edit In the action menu.
Navigate to Pages tab.
Click + and select Custom Page page to create a new page, or select an existing custom page and click Edit.
Click the gear icon and select Page Options.
Scroll to the SEO Optimization section.
Enter the keywords for the page in the Page Name Display for URL.
Click Save.
Publish the page and publish site.

---

## Note: If you've added or edited a page display name for URL for a custom page, make sure to update any external
*Chunk ID: OHR-REC-0199 | Chapter: Career Sites*

links that are using this page URL. Old page URLs with PageIDs will still work and redirect users to the new URL.
However, if a page name display for URL field is edited multiple times, the URLs with old keywords might stop
working.

---

## Domain Verification
*Chunk ID: OHR-REC-0200 | Chapter: Career Sites*

Use a domain verification code, which you can obtain from Google, to help the Google search engine to recognize that
your organization owns a career site.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. In the Google Domain Verification section enter the appropriate information you've obtained from Google.
In addition to these settings, you can enter domain verification to help the Google search engine to understand that
your organization owns a career site.

Related Topics
• Configure Sitemap for Search Engine Indexing

---

## Configure Sitemap for Search Engine Indexing
*Chunk ID: OHR-REC-0201 | Chapter: Career Sites*

You can proactively submit job posting URLs and career site pages to search engines for indexing using a sitemap. A
sitemap helps search engines discover your pages faster. Enabling sitemap submission through Recruiting builds and
submits the sitemap for your career site to Google. It also structures the job posting data for job search to make your job
postings eligible to appear in special user experience in Google search results.
To enable sitemap submission, you need to:
1. Create a Google search console service account.
2. Enable sitemap submission, and upload the Google service account credentials

---

## Create a Google Search Console Service Account
*Chunk ID: OHR-REC-0202 | Chapter: Career Sites*

Create a Google search console service account, and obtain the access token. Steps are available here:https://
developers.google.com/search/apis/indexing-api/v3/prereqs

---

## Enable Sitemap Submission and Upload Your Google Service Account
*Chunk ID: OHR-REC-0203 | Chapter: Career Sites*

Credentials
Once your account is set up and you've obtained the access token, you'll need to upload it to candidate experience
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. In the Search Engine Optimization section, select Enable sitemap submission and job posting markup to enable
sitemap submission through API.
The Search Configuration URL field is auto populated with the URL required for the sitemap submission API. will be
replaced with the actual URLs while pinging the search engine.
◦ Configuration URL: https://www.googleapis.com/webmasters/v3/sites/{SEARCHCONSOLE_SITEURL}/
sitemaps/{SITEMAP_URL}
◦ SEARCHCONSOLE_SITEURL will be replaced with the URL prefix property that you added in Google Search
Console while creating the service account. For example: https://<<Career_Site_Domain>>/hcmUI/
CandidateExperience or https://<<Career_Site_Vanity_Domain>>/ for vanity domain.
◦ The SITEMAP_URL will be replaced with the career site domain job postings sitemap location URL.

◦ The career site domain will contain either your domain, or your vanity domain (if vanity URL is configured).
4. Click Browse next to the Google Service Account JSON File.\
5. Upload the JSON key file generated during Google service account creation.
6. Click Save.
Your sitemap is submitted to Google search engine to enable their search bot to crawl the sitemap and index job
posting URLs. The sitemap will be refreshed and submitted to Google at least every 6 hours when the jobs are
created, updated, or expired.
All job posting pages are included in the sitemap called jobPostings. All career site pages are included in the sitemap
called careerSitePages, which allows search engines to crawl and index all event pages, custom pages, splash pages,
and search results pages.
Both the careerSitePages sitemap and jobPostings sitemap files are included in the parent file called sitemapindex,
and they'll be submitted to Google search engine for indexing.
A hidden sitemap link in the career site has been added to the header so all the career site pages can be easily
discovered and crawled by the Googlebot.

Related Topics
• Configure Search Engine Optimization

---

## Configure Career Site Search Filters
*Chunk ID: OHR-REC-0204 | Chapter: Career Sites*

You can configure career site search filters to display more than 10 values. This applies to career sites using the Minimal
template.
By default, when external candidates use any of the available filter values on a career site to narrow down the job search
results list, up to 10 values display. If more than 10 values are available for a filter, a keyword search box lets candidates
look for more values. When candidates begin typing, additional available values are suggested, and when they select
one, it displays in the list.
Note: The search box only displays for filter categories that have more than 10 filters, and is for the standard
categories, and not custom DFF filter categories.
You can set a profile option called ORA_IRC_CE_SEARCH_FILTER_VALUES_LIMIT, to show up to 100 values. This profile
option doesn't control the search box behavior. The search box for the filters will continue to show for > 10 filter values,
even if the profile option is set to show more than 10 values.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_CE_SEARCH_FILTER_VALUES_LIMIT.
6. Enter a value in the Profile Value field.
7. Click Save and Close.

---

## Searching Jobs on a Career Site
*Chunk ID: OHR-REC-0205 | Chapter: Career Sites*

Candidates visiting an external career site can search for jobs using keywords or locations.

---

## Keyword Search
*Chunk ID: OHR-REC-0206 | Chapter: Career Sites*

With the keyword search, candidates enter a term in the Find Jobs field. As they enter letters, words matching the
characters they typed are displayed. The list continues to narrow as they enter more characters. Candidates need to
enter at least one character for the autosuggest to be triggered.
Autosuggestions are derived from these job requisition's fields:
• Requisition Title
• Job Family
• Job Function
• Skill

---

## Candidates can select a term from the list, or they can provide their own keyword to start the search. Candidates can
*Chunk ID: OHR-REC-0207 | Chapter: Career Sites*

use quotation marks to search for an exact match phrase. If a phrase is entered without quotation marks, the search
engine will look for jobs matching any of the keywords, giving a higher relevancy score to the ones that match the exact
phrase.
Note: Keyword search follows the Unicode Text Segmentation algorithm. This means that some special characters
may break the provided keyword into several words. For example, if the keyword is front-end, the search engine will
convert it into two separate keywords: "front" and "end". If candidates want to search a whole phrase with special
character, they should use double quotes.
When the search results are returned, the following criteria is applied:
1. Precision Tuning - Jobs are returned only if there's a match between the provided keyword and the value in
the searched field. For keywords that are up to 2 words, all keyword terms must be found. For longer keywords,
partial matches are also returned.
2. Relevancy Calculation - The higher the relevancy score, the higher the job is on the search results page. The
following factors are considered when calculating relevancy:
◦ Field Weight - Requisition fields have different weights. Jobs that have a phrase matching fields with a
higher weight are given a higher relevancy score than those that have a phrase with a lower weight.
◦ Exact Match - If a candidate enters a phrase without quotation marks, the search engine looks for jobs
matching any of the keywords, giving a higher relevancy score to the ones that match the exact phrase.
◦ Frequency
- Term Frequency - more times a keyword appears in the requisition fields, the higher the relevancy
score.
- Inverse Document Frequency - the rarer a keyword is across all documents (requisitions), the more
it contributes to the overall relevancy score.
Posting
Date - If two jobs have a similar relevancy score based on keywords, the more recently posted job
◦
is listed higher in the search results.
◦ Hot Job - Jobs tagged with a "Hot Job" tag get a relevancy boost.
The search engine is looking for keywords in the following requisition fields:
• Requisition Title (highest weight)
• Requisition Number (medium weight)
• Job Family (medium weight)
• Job Function (medium weight)
• Skill (medium weight)
• Responsibilities (medium weight)
• Qualifications (medium weight)
• Short Description (lowest weight)
• Long Description (lowest weight)

---

## Location Search
*Chunk ID: OHR-REC-0208 | Chapter: Career Sites*

Candidates can search for jobs by location using these search modes:
• Location or Job Location
• My Location

---

## Career Sites
*Chunk ID: OHR-REC-0209 | Chapter: Career Sites*

• Postal Code
• Location or Job Location: Depending on the location search you enabled, candidates can search for jobs using
the Location search mode or the Job Location search mode. When candidates use the Location search mode,
they can search for jobs by any location. When they use the Job Location search mode, they can search for jobs
by recruiting locations. For details, see Configure Career Site Location Search.
Note: Enabling Job Location search doesn't impact My Location and Postal Code search modes. Even
though candidates can only select Job Locations from the autosuggest list, if they switch to postal code
search, they can search for any postal code.
When a career site uses the Minimal template, candidates can select the search mode from a menu in the
Location search box.
When candidates use the Location search mode, they can search for jobs in any geography. Locations are
configured in the Manage Geographies task, in the Setup and Maintenance work area. Locations are in line
with the geography hierarchy structure defined in the Geography Hierarchy Structure task. When candidates
search for a location, locations matching the characters they typed are displayed as they enter letters. The list
continues to narrow as they enter more characters. Candidates need to enter at least one character for the
autosuggest to be triggered. The United States is always boosted to the top of the respective countries list.
Locations matching the input are sorted in the autosuggest list in the following order:
◦ Country, alpha order (recruiting locations)

◦ State, alpha order (recruiting locations)
◦ City, alpha order (recruiting locations)
◦ Country, alpha order (other locations)
◦ State, alpha order (other locations)
◦ City, alpha order (other locations)
When candidates use the Job Location search mode, they can search for jobs in the locations that are defined
in the Geography Hierarchies task. This is a set of locations where jobs can potentially be posted. When
candidates move focus to the location search box, a drop-down list with all locations opens. Candidates can
either select a value from the list, or begin typing to narrow the list down to locations matching their input.
In both location search modes, candidates can select a location at any of the three geography hierarchy levels.
If the location they select is at a city level, they can add a radius to their search. The default radius value is 25
miles (or kilometers, depending on the browser locale setting). This means that search results will display jobs
posted within 25 miles from the selected location's center and those with matching posting location. If the
radius is set to 0, search results will display all jobs with a matching posting location.
When candidates perform a location search using a higher level location, jobs within the location hierarchy
are displayed. For example, when a candidate searches for jobs in Canada, results will include jobs posted in
Canada, in QC, Canada, and in Quebec, QC, Canada.
When candidates perform a location search using a lower level location, jobs within that particular location are
displayed. Search results don't include jobs posted higher in the geography hierarchy tree. For example, when a
candidate searches for jobs in Quebec, QC, Canada, results will only include jobs posted in Quebec, QC, Canada
and not in QC, Canada or Canada.

---

## Career Sites
*Chunk ID: OHR-REC-0210 | Chapter: Career Sites*

• My Location: With the My Location search mode, the location from the candidate's browser is used. Candidates
can search for jobs in their precise location, or within a selected distance from that location. The default radius
value is 25 miles (or kilometers, depending on the browser locale setting).
• Postal Code: The Postal Code search mode is available only if Oracle Search is enabled. If candidates want
to search for jobs using a postal code, they need to enter the postal code and select a country from a list.
The default radius value from the center of that postal code area is 25 miles (or kilometers, depending on the
browser locale setting). If no keyword or location is provided, a blind search can be initiated, showing all jobs in
the search results.
Note: Some non standard postal code formats, such as CEDEX or other specialized formats, might not be
supported.

---

## Job Search Results Sorting
*Chunk ID: OHR-REC-0211 | Chapter: Career Sites*

Candidates who search for jobs on external candidate experience sites using a Minimal template can sort using these
options:
• For blind searches (those in which no search criteria is provided), the job search results are sorted by posting
date by default. Candidates can then change the sorting criteria.
• For keyword searches, the job search results are sorted by relevancy by default. Candidates can then change
the sorting criteria.
• For location only searches when the distance calculation feature is disabled, results are sorted by date by
default, with the newest posting listed first. Candidates can then change the sorting criteria.
• For location only searches when the distance calculation feature is enabled, by default the results are sorted by:
◦ Distance (nearest displays first) - if a candidate searches using any type of location (location, recruiting
location, My Location or postal code), and they select a location at a level allowing distance calculation
(level 2 location [city level], or My Location, or postal code).
◦ Date (newest displays first) - if a candidate selects any type of location (location, recruiting location, My
Location, or postal code), and they select a location at a level not allowing distance calculation (level 1
location [state], or country level location).
Candidates who search for jobs on external candidate experience sites can sort by:
• Posting date (sorted by newest first) * Relevance
• Distance (nearest first, available only if distance calculation is enabled for the site)

---

## Search Result Filtering
*Chunk ID: OHR-REC-0212 | Chapter: Career Sites*

External candidates searching on sites using the Minimal template can filter search filters using the filtering panel. The
filters display sequence for default filter categories is configurable. For details, see Configure Career Site Search Filters.
When they click a filter category to open a drop-down list of filters and select them, they'll notice a count displays at
the top showing know how many selectors they're using. For example, if a user selects United States and Canada for
Locations, the count is 2.
Note: Open job counts don't match location counts, because career sites count location occurrences, not requisitions.

---

## Configure Event Location Search
*Chunk ID: OHR-REC-0213 | Chapter: Career Sites*

You can decide which location search modes are available for candidates.When you enable the ability to search for
events by location, candidates can search for events in locations where jobs may be potentially posted.
Candidates can search by:
• My Location
• Postal Code
• Distance
• Radius search (supported for all location search modes)
Note: Distance isn't calculated for virtual events because they don't have a physical location. Virtual events aren't
returned in location search.
Before you start
Ensure the following profile option is active: ORA_FND_SEARCH_EXT_ENABLED.
Here's what to do
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. On the Search page, search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values, search for the above profile option code.
6. In the Profile Values section, set the profile value:

◦ Y: The code is enabled.
◦ N: Default value. The code isn't enabled.
7. Click Save and Close.
8. Run the scheduled process called ESS Job to create index definition and perform initial ingest to OSCS. This ensures
that all hiring events that either already exist in the application or those that will be newly created are fully indexed
for search. Specify “fa-hcm-irc-hiring-events” in the Index Name to Reingest field.
1. Next, enable the search modes for events on career sites:
9. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
10. Create a career site or edit an existing one.

---

## Career Sites
*Chunk ID: OHR-REC-0214 | Chapter: Career Sites*

11. On the General tab, configure these settings:

◦ Distance Calculation – Display distance to search result location and sort search results by distance.
◦ Location Search – Enable postal code search
◦ Location Search – Enable my location search
12. Publish the site.
Related Topics
• Searching Jobs on a Career Site

---

## Configure Synonyms for Candidate Experience Keyword
*Chunk ID: OHR-REC-0215 | Chapter: Career Sites*

Search
You can enhance the keyword search experience for external career sites by allowing candidates to use common
synonyms and abbreviations.
For example, if candidates search using terms such as "Sr" results will be returned using the word "senior". Searching
for "product owner" also returns "product manager" in the results. This makes it easier for candidates to find a job they
want to apply to, because more relevant search results will be returned.
Synonyms are checked against the requisition title, job function, and job family, but not the description. This means
if a candidate searches for "Product Owner" and a job has "Product Manager" in the description (but not in the title,
function, or family), that job won't be returned in the search results.
Support for synonyms is automatically enabled, and a default list of synonyms is provided in Setup and Maintenance. To
add your own synonyms, you can download, edit, and re-upload the list.
You can add many languages to the file. The following languages are supported:
• English
• Spanish
• French
• Arabic
• German
Before you start
• Enable Oracle Search. If Oracle Search isn't enabled, or synonyms are disabled using profile option, then the
Configure Synonyms section in Setup and Maintenance is enabled, but uploading a file won't have any effect.
• Files must be zipped CSV-UTF8.

---

## Download the Synonym List
*Chunk ID: OHR-REC-0216 | Chapter: Career Sites*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

---

## Career Sites
*Chunk ID: OHR-REC-0217 | Chapter: Career Sites*

◦ Functional Area: Recruiting and Candidate Experience Maintenance
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Scroll down and expand the Configure Synonym section. Notice that you can see when the synonym file was
last updated, and a link to download a copy to work with. In the example above, the file is listed as "From Seed
Data" which means it's never been updated, and is the version that was provided by Oracle.
3. Click Download Latest Synonyms Definition File, and save the file to a location on your hard drive or network.
The downloaded file is an unzipped CSV file.
4. Open the CSV file.
Each row in the file represents one instance of synonyms. Column A lists the words and phrases that mean
the same thing; for example "recruiter, recruiting specialist, talent acquisition specialist => recruiter, recruiting
specialist, talent acquisition specialist". You'll notice the words in the synonym column appear twice, but the
instances are separated by an arrow (=>). In the seeded file, the words and phrases on both sides of an arrow
are the same. This means that when a candidate searches using one of the listed phrases, all of listed synonyms
are searched.
Similarly, when you add more words or phrases to a row in Column A, you'll need to use the same words on
either side of the arrow, and ensure that they're spelled the same way. If you don't, candidates might not see
all of the results you want them to see. For example, if you add a row containing "product manager => product
owner", candidates searching for “product manager” might end up getting only “product owner” results, even
though you might have jobs using both names. Instead you should add "product manager, product owner =>
product manager, product owner".
Column B lists the language codes. They define the language for a synonym row. The synonyms from each
row will only be used in sites that use that language. You can only add one language per row. The following
language codes must be used for the supported languages:
◦ English - en

◦ Spanish - es
◦ French - fr
◦ Arabic - ar
◦ German - de

5. Update the file as necessary and save it.
Note: Synonyms file can't contain a "?" character. You can only upload .zip files so you'll need to zip your
saved CSV file before uploading it to Recruiting. Instructions for creating CSV-UTF8 files can be found online.

---

## Upload the Synonym File
*Chunk ID: OHR-REC-0218 | Chapter: Career Sites*

1. Open and inspect your files before uploading, especially if the file contains languages other than English.
2. Check for special characters. If there are any, it means the file isn't saved correctly in a UTF-8 format.
3. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Maintenance
◦ Task: Enterprise Recruiting and Candidate Experience Information

4. Scroll down and expand the Configure Synonym section and click Edit.
5. Click Click Here to Upload, or use the drag-and-drop functionality to drag the zipped CSV file to the upload
area.

---

## Configure Alternate Location Names
*Chunk ID: OHR-REC-0219 | Chapter: Career Sites*

You can configure job location search to include commonly known alternatives for city and state level locations.
For example, a candidate can find California by typing the alternate location name of "California", instead of the usual
abbreviation of "CA".
This feature applies to the Near Location search and Job Location search.
This feature requires Oracle Search.
Here's what to do:
1. Enable the profile option to include alternative location names in search.
2. Create alternate location names.
3. Re-index the master geography hierarchy or update geography names.

---

## Enable the Profile Option
*Chunk ID: OHR-REC-0220 | Chapter: Career Sites*

To enable the use of alternate location names, you need to enable the profile option
ORA_IRC_SEARCH_LOCATION_INCLUDE_ALT_NAMES. By default, the profile option is set to N, and only primary
location names are displayed.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_SEARCH_LOCATION_INCLUDE_ALT_NAMES.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.

---

## Create Alternate Location Names
*Chunk ID: OHR-REC-0221 | Chapter: Career Sites*

To create alternate location names, you use the Manage Geographies task in the Setup and Maintenance work area.
Here’s an example of how to add alternate location names for the state of California in United States.
1. In the Setup and Maintenance work area, search for the task Manage Geographies.
2. On the Manage Geographies page, search for United States. Then go to the state of California (CA)
3. Add alternate location names. In this example, one alternate location name was added.

---

## Re-index Master Geography Hierarchy or Update Geography Names
*Chunk ID: OHR-REC-0222 | Chapter: Career Sites*

This step depends on the default location search mode configured on your career site. For details, see Configure Career
Site Location Search

---

## If your career site is using the All locations search mode, you need to run the Load and Index Master Geography
*Chunk ID: OHR-REC-0223 | Chapter: Career Sites*

Hierarchy scheduled process to recreate the location index. Don’t set any parameters upon first activation.
You need to run the Load and Index Master Geography Hierarchy scheduled process every time you make a change to
geographies on the Manage Geographies page. You can use parameters. In the above example, you could use US for
country, and CA for state.
If your career site is using the Recruiting locations search mode, you need to update the geography names on your
active recruiting geography hierarchy.
1. In the Setup and Maintenance work area, search for the task Geography Hierarchies.
2. On the Geography Hierarchies page, open active geography hierarchy.
3. In the Actions menu select Update Geography Names.

---

## Turn Off Keyword Search in Career Site Job Description
*Chunk ID: OHR-REC-0224 | Chapter: Career Sites*

Fields
You can turn off keyword search in job description fields.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Candidate Experience section and click Edit.
3. Clear the option Career Site Search in Requisition Description.
4. Click Save.

---

## Configure Career Site Location Search
*Chunk ID: OHR-REC-0225 | Chapter: Career Sites*

You can decide which location search modes are available for candidates on external career sites.
You have the option of allowing candidates to search by all locations or recruiting locations. In addition, you can disable
the My Location Search and Postal Code Search settings on particular career sites.
When you enable the ability to search for jobs by recruiting locations, candidates can search for jobs in locations where
jobs may be potentially posted. You don't have to disable the other location search modes.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration

2. Create a career site or edit an existing one.
3. On the General tab, scroll to the Location Search section.

---

## Career Sites
*Chunk ID: OHR-REC-0226 | Chapter: Career Sites*

4. Select a default location search mode. You can select either:
◦ All locations - Candidates can search jobs by any location. This is the default selection. The behavior of
search is the same as it was prior to this release. On the career site, the label is Location.
◦ Recruiting locations - Candidates can search jobs by recruiting locations. On the career site, the label is Job
Location.
5. Select the Enable postal code search check box if you want to allow candidates to search for jobs by postal code.
Note that activating this setting isn't affected by what users choose as their location search option (All Locations or
Recruiting Locations). It will always display all of the postal codes.
6. Select the Enable my location search check box if you want to allow candidates to search for jobs by candidate
browser location.

---

## Enable Autocorrect in Keyword Search
*Chunk ID: OHR-REC-0227 | Chapter: Career Sites*

You can enhance the keyword search experience in external career sites that use the Minimal template by enabling
autocorrect. Autocorrect enhances the job search flow and provides more relevant search results to candidates.
Once the feature is enabled, if a candidate misspells a keyword, the search suggestions drop-down list shows items
containing corrected, or closest matched spellings based on your organization's job title and description data. For
example, if a candidate types "jaca" instead of "java", the list displays items containing the word "java". These items
display instead because the keyword "java" is present in either the job titles or descriptions. Candidates can then select
an item from the autocorrect words list. They can also search using their spelling by clicking the Search instead for link.
The autocorrect suggestions are based on the data contained in your organization's job titles and descriptions.
Before you start
• Autocorrect can only by enabled if Oracle Search is used. Customers using SemSearch must keep the feature
disabled, otherwise it might break the job search functionality.
• This feature is only supported for use with the Minimal template. Using it with the deprecated Modern template
isn't recommended, because it might cause search to return irrelevant results.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. On the Enterprise Recruiting and Candidate Experience Information page, expand Candidate Experience and click
Edit.
3. Select the option Autocorrect in Keyword Search.
4. Click Save.

---

## Enable Job Search on a Map
*Chunk ID: OHR-REC-0228 | Chapter: Career Sites*

You can configure external career sites so that external candidates can explore jobs available using Oracle Maps. Posted
jobs are pinned on the map, giving candidates a nice visual way to see job locations.
By default, job search results appear in a list. When you enable the map view, two kinds of icons indicate the location of
jobs.
• Pin: Indicates a single location with one or more jobs. When a candidate clicks the pin, location name is listed,
followed by a list of job titles.
• Circle: Indicates a cluster of job locations in an area. When a candidate clicks the circle icon, it zooms into a map
location and displays job locations that are near each other.
Candidates can also click a job title to see the job details page. They can optionally copy the job location address to their
clipboard and paste it in a browser search bar to search for more info about the job location.
The map shows the jobs matching the search criteria (keyword and location) based on the geo-coordinates returned
for those jobs. If a job has work locations, the geo-coordinates for those work locations are considered in the map view.
If the job doesn't have a work location, the geo-coordinates of the posting locations are used instead. In this case, only
city level posting locations are considered. State level or country level locations won't be displayed on the map.
You can also configure the career site to let candidates toggle between the list view and map view.
Before you start
• This feature requires Oracle Search and the use of the Minimal template.
• This feature integrates with Oracle Maps.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, select Edit next to a career site.
3. On the General tab, expand the Search Job on Map section.
4. Select the option Enable searching jobs on map. This enables maps for the standard search results page and any
new custom search results page that you create.
5. To configure the career site to allow candidates to toggle between list view and map view, follow these steps:
a. Click the Pages tab.
b. Edit an existing Search Results page or create a new one.
c. Click the search results element to display the configuration options.
d. In the Display Style field, you can select Toggle Map and Tile, or Toggle Map and List.
e. Click Done.

---

## Display the Workplace on Career Sites
*Chunk ID: OHR-REC-0229 | Chapter: Career Sites*

You can display the workplace of a job on external career sites. Candidates can see workplace information on the job
requisition and filter jobs whether they're on-site, remote, or hybrid.
When recruiting users create job requisitions, they can define a workplace for the job. A requisition can only have one
workplace:
• On-site
• Hybrid
• Remote
Your organization may decide to display or not individual Workplace attributes on external career sites. For example, if
a vast majority of jobs require people to work on-site, you might not want to display this Workplace tag. However, if you
want to distinguish remote and hybrid jobs, you'll want to display the Hybrid and Remote workplace tags.
You can configure a setting to display the Workplace attribute. The same three workplace values are available. This
setting decides whether the Workplace attribute is displayed or not on the career site, provided that the Workplace info
was added to the job requisition. You can also add the Workplace search filter on the career site.
Before you start
The job requisition must be configured to display the workplace attribute.
Here's what to do
1. Enable the Workplace Tag Display Setting
2. Add the Workplace Search Filter
Results:
Note that the On-site filter shows jobs without any Workplace tag and those with On-site tag assigned. The Workplace
attribute is also displayed in the job details.

---

## Enable the Workplace Tag Display Setting
*Chunk ID: OHR-REC-0230 | Chapter: Career Sites*

You can configure the Workplace attribute to appear on external career sites.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, click Edit next to a career site.
3. Click the General tab.
4. In the Workplace Tag Display section, select the display you want: On-site, Remote, Hybrid.

---

## Add the Workplace Search Filter
*Chunk ID: OHR-REC-0231 | Chapter: Career Sites*

You can add the Workplace search filter to external career sites. When external candidates search for jobs on career
sites, they can see workplace information on the job and they can use the Workplace attribute to filter jobs.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, click Edit next to a career site.
3. Click the General tab.
4. In the Search Filters section, select the Workplace option.

---

## Add a Personalized Favicon to the Career Site
*Chunk ID: OHR-REC-0232 | Chapter: Career Sites*

You can add a personalized favicon to your external career sites to reflect your company branding and create consistent
brand experience for your candidates. If no favicon is added, the default Oracle favicon is displayed.
Before you start
Supported favicon file formats are: .png, .gif, .jpg, .ico.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, locate your career site and click Edit.
3. Click the Theme tab.
4. Click Favicon.
5. Click Upload Favicon.
6. Locate your favicon file and click Open.
Results:
The file is uploaded. The uploaded favicon is displayed on the browser tab and as a quick link to favorite sites.

---

## Manage Multiple Career Sites
*Chunk ID: OHR-REC-0233 | Chapter: Career Sites*

When your organization has several external career sites, there are tools you can use to manage them.

---

## Reorder Career Sites
*Chunk ID: OHR-REC-0234 | Chapter: Career Sites*

Career sites have a sequence number based on their position on the Career Sites Configuration page. First site on the
page has sequence number 1, second site has sequence number 2, and so on. If you want to change the sequence of
career sites, simply drag and drop them on the Career Sites Configuration page. Career site's sequence is important
when candidates are redirected to the site from the link.
Let's say a job is posted on multiple external career sites. When external candidates are invited to apply for a job, are
referred, or are added to a job requisition by a recruiter, they're redirected to the career site where the job is posted and
that's the top sequence (highest) on the page.
Note: The active site should be in the top position for some partner integrations, such as resume parsing, to work.

---

## Duplicate a Career Site
*Chunk ID: OHR-REC-0235 | Chapter: Career Sites*

You can use the Duplicate action on the Career Sites Configuration page to duplicate an existing career site. A new
career site is created and the configuration is the same as the original career site. The duplicated career site has the
same name and code as the original site. You can modify them by clicking the Edit option. The duplicate career site has
a unique URL.

---

## Replace a Career Site
*Chunk ID: OHR-REC-0236 | Chapter: Career Sites*

You can use the Replace action on the Career Sites Configuration page to replace an existing career site. The new career
site can be accessed with the same URL as the original site. All functional and visual setup is copied from the other site.
The duplicate and replace options are useful when you want to make more extensive changes to your career site setup.
As an example, changing the branding. You can duplicate a career site and make all the necessary changes on the
duplicate. When the carer site is ready, you can replace the original site with the duplicate one. This way all the setup
will be copied from the duplicate, while the url of the site will remain unchanged. Your candidates will reach the new
enhanced career site using the same links as before.

---

## Contextualize a Career Site
*Chunk ID: OHR-REC-0237 | Chapter: Career Sites*

If you publish multiple career sites, you may want to contextualize them. Contextualization is done in the career site
General tab.
You can contextualize a career site base on locations, organizations, job categories, job functions, and recruiting types.
When a career is contextualized, only posted job requisitions matching the same context criteria are visible on the
career site. If no context is defined, all posted job requisitions are visible on the site. Here's an example.
You create 3 career sites in the following sequence:
• Career Site 1: US jobs only
• Career Site 2: EMEA jobs only
• Career Site 3: No context
Scenario 1: Candidates receive a URL to a job requisition details page. The URL can be copied manually from a career
site. The URL includes site information pointing to Career Site 2. The job location is EMEA. Candidates are taken to a
job details page on Career Site 2. If the site is deactivated, candidates are taken to a highest sequence site where this
requisition is available, that is Career Site 3.

---

## Scenario 2: Candidates receive a URL to a job requisition details page. It could be a referral or prospect URL. The URL
*Chunk ID: OHR-REC-0238 | Chapter: Career Sites*

doesn't include site information, job location is Germany. Candidates are taken to a highest sequence site where the
requisition is available, that is Career Site 2.

---

## Import and Export Career Sites
*Chunk ID: OHR-REC-0239 | Chapter: Career Sites*

You can use the Export and Import action on the Career Sites Configuration page to export all career sites configuration
from a particular environment. All active and nonactive career sites are included in the export. The exported file
includes site settings, visual and functional configuration. The file can be imported to any environment. Imported career
sites are added on top of existing sites in the given environment and are inactive upon import. The site code must be
unique on the environment. When a career site is imported, the original site code is amended by adding (Copy_1). If
(Copy_1) already exists, the number is augmented (example: Copy_2, Copy_3).
Note: You can only export and import candidate experience sites within the same version of the application.

---

## Assign Access to Career Site Administration
*Chunk ID: OHR-REC-0240 | Chapter: Career Sites*

You can delegate career site setup to users who aren't admins without giving them full access to Setup and
Maintenance.
These users have access to a Career Sites Configuration quick action, which when clicked opens the Career Site
Configuration page. They can perform all the same functions as someone with Career Site Admin rights, but there's no
Back button to take them to other areas of the Setup and Maintenance work area.
To grant this access, users must have the following:
• The privilege called IRC_CONFIGURE_CAREER_SITE_PRIV
• Access to the My Client Groups tab
Note: Recruiting Administrators can access the Career Sites Configuration page using either Setup and Maintenance
or the quick action, because the IRC_CONFIGURE_CAREER_SITE_PRIV privilege is granted to by default to the
Recruiting Administrator role.

---

## Enable Social Sharing
*Chunk ID: OHR-REC-0241 | Chapter: Career Sites*

You can share more engaging content with social platforms when you post links to external career sites. Site-level
configuration for Open Graph image is available to make content more shareable. You can add a URL for an image you
want to use when posting jobs on social platforms.
Also, when posting jobs on Twitter, you can use a tag to decide how the image is rendered. When the image URL uses
an Open Graph image and the job is shared on Twitter, the image is rendered as a large image. The card format value is
hard-coded, you can’t configure it. The card format is: <meta name="twitter:card" value="summary_large_image">

---

## When sharing career site pages with social platforms, the following Open Graph tags were added to the splash page and
*Chunk ID: OHR-REC-0242 | Chapter: Career Sites*

search results pages.
• “<site name> Careers” is used as og:title (translated to a correct language)
• branding text is used as og:description
• image configured for a site is used as og:image (with fallback to site logo/desktop)
• "website" is used as og:type
• site name is used as og:site_name
• If the page is shared to Twitter, the twitter card is rendered in summary_large_image format
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Site Look and Feel Configuration page, select Edit next to a career site.
3. On the General tab, expand the Social Sharing section.
4. Add the URL for the image as an Open Graph image.
If no image is added, the site logo is used.
For best experience when sharing job links in social media sites, most social platforms require aspect ratio of 1.9:1 for
images. Make sure you verify the aspect ratio recommended by the platforms you use before uploading the image.

---

## Tracking Pixel Feature
*Chunk ID: OHR-REC-0243 | Chapter: Career Sites*

You can use tracking pixel on external career sites to gather information and track useful metrics about your external
candidates. A tracking pixel is a graphic with dimensions of 1x1 pixel that's loaded when a user visits a website.
Typically, candidates are driven to the career site from other sourcing channels such as Google, LinkedIn, Indeed. You
might be interested to know what happened to the candidates after they clicked on a sponsored job ad or a search
result and landed on the job description page on the career site. Here's an example. Twenty candidates saw a job ad
on Indeed and landed on your career site. Ten candidates clicked the Apply button after their identity was verified by
email or phone, 5 candidates started the job application process, and 4 candidates submitted their job application. This
information can be gathered using third-party tracking pixel URLs. Depending on the third party, these metrics can be
further broken down by requisitions and individual candidates.
You can track three different events:
• When a candidate clicks Apply to apply for a job
• When a candidate starts a job application process
• When a candidate submits their job application
You need to decide what events you can track with the third-party tracking provider. It's possible that the tracking
provider only supports the tracking of submitting job applications. In such case, you need to enter the URL for
submitting a job application. The URL for clicking the Apply button and the URL for starting the job application process
remain blank. Note that only one URL can be configured for each event.

---

## If a third-party tracking provider accepts additional parameters such as the candidate ID and requisition ID, you can
*Chunk ID: OHR-REC-0244 | Chapter: Career Sites*

configure them and define names for those parameters. It's up to the partner to interpret them appropriately.
The Tracking Pixel feature supports image pixels that are just image tags. It doesn't support third-party JavaScript code.
You need to discuss with the third-party provider whether this model is supported. If your provider asks to include a
piece of code, look for the image tag within this code. Inside the image tag there should be a URL. Use this URL while
you configure the feature.
For example, the third-party code includes the following image tag: <image height=1 width=1 border=0 src="https://
conv.indeed.com/pagead/conv/[identifier]/?script=0">

---

## Copy the URL after the src attribute: https://conv.indeed.com/pagead/conv/[identifier]/?script=0
*Chunk ID: OHR-REC-0245 | Chapter: Career Sites*

Here's another example: <img height="1" width="1" syle="display:none;" alt="" src="https://px.ads.linkedin.com/
collect/?pid=[identifier]&conversionId=[identifier]&fmt=gif" />

---

## Enable Tracking Pixel
*Chunk ID: OHR-REC-0246 | Chapter: Career Sites*

You can enable tracking pixel on external career sites to gather information and track useful metrics about your external
candidates. A tracking pixel is a graphic with dimensions of 1x1 pixel that is loaded when a user visits a website.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Configure Career Sites Configuration
2. On the Career Sites Configuration page, click Edit next to a site.
3. In the General tab, expand the section called Tracking Pixel.
4. You can configure these URLs to gather info. URLs are provided by the third party.
◦ URL when clicking the Apply button

◦ URL when starting a job application
◦ URL when submitting a job application
5. It's also possible to send the candidate ID and requisition ID as parameters if the pixel tracker accepts them. This
allows the source channel to derive conversion metrics to see how many candidates clicked apply, started applying
for a job, and eventually submitted their application.
6. You can preview the complete URL.

---

## Enable Keep Me Signed In
*Chunk ID: OHR-REC-0247 | Chapter: Career Sites*

You can allow external candidates to be signed in instantly when they go to an external career site to schedule
interviews, provide more information, view offers, or apply to another job.

---

## When you enable the feature, the option Keep me signed in is available on the verification screen of external career
*Chunk ID: OHR-REC-0248 | Chapter: Career Sites*

sites. Also, there is a visual indicator on the career site header when a user is signed in. Note that the visual indicator
appears regardless if the Keep me signed in feature is enabled or not. Candidates can easily access their profile or sign
out.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Candidate Experience section and click Edit.
3. Select the option Keep Me Signed in for External Candidates.
4. Enter the number of days to remain signed in.
5. Click Save.
Results:
The clock restarts every time the candidate visits the career site within the validity period. When signing in on the same
browser within the validity period, the candidate doesn't need to confirm their identity again.
Note that even though the candidate is signing in within the validity period, there is a required sign-in 180 days after
the initial verification. Let's say, for example, that the number of days to remain signed in is configured as 30 days.
The candidate signs in on January 1 and selects the option Keep me signed in. When the candidate comes back within
30 days, the clock will restart to add another 30 days of validity period. If the candidate visits the career site within
the validity period, the clock will restart each time. However 180 days past January 1st, the candidate will be forced to
confirm their identity again using a verification code. The candidate will be able to select the Keep me signed in option
again.

---

## Enable Apply with Indeed
*Chunk ID: OHR-REC-0249 | Chapter: Career Sites*

You can implement Indeed on your external career site to allow candidates to apply with their Indeed profiles.
To implement Indeed, you first need to get Indeed API keys. Then, you need to add the API keys in the Indeed profile
import

---

## Get Indeed API Keys
*Chunk ID: OHR-REC-0250 | Chapter: Career Sites*

You need to get Indeed API keys and configure the redirection URL.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

Go to https://secure.indeed.com/account/apikeys.
Perform the following steps if you don't have an Indeed account.
Click the Create an account free link.
Enter an email address and password. Providing a shared email address or an email address that will remain
valid in spite of personnel changes is strongly recommended.
Click Register New Application.
Enter the name of your application. For example, ABC Recruiting Application.
Add Application Website.
Select OAuth 2.0 as credential type.
Select the authorization code as OAuth 2.0 grants.
Enter the redirect URL https://<orcl_hcm_hostname>:443/hcmUI/CandidateExperience/profileImport/oauth.

---

## If you're using vanity domain then the redirect URL should be with vanity domain like https://
*Chunk ID: OHR-REC-0251 | Chapter: Career Sites*

<company_vanity_hostname>/profileImport/oauth . For example, https://jobs.vision.com/profileImport/oauth
Select Yes, review my application.
Enter the company name, company homepage, support email address, and link to public privacy policy.
Click Complete registration.
Note the application name, client ID, and client secret.

---

## Add Indeed API Keys in the Profile Import
*Chunk ID: OHR-REC-0252 | Chapter: Career Sites*

Add the Indeed authorization code URL and API keys in the Profile Import.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Enablement
2.
3.
4.
5.

On the Partner Integration Provisioning page, click Edit next to Indeed.
Change the authorization code URL to https://secure.indeed.com/oauth/v2/authorize.
Change the access token URL to https://apis.indeed.com/oauth/v2/tokens.
Click Save and Close.

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2.
3.
4.
5.
6.

On the Partner Integration Provisioning page, click Edit next to Profile Import Partners.
On the Profile Import Partners page, go to the Indeed section.
Enter the Client ID and Client Secret key for Indeed.
Click Save.
Click the Active check box to complete the activation. The Apply with Indeed option is now available to
candidates.

---

## Enable Apply with LinkedIn
*Chunk ID: OHR-REC-0253 | Chapter: Career Sites*

Apply with LinkedIn is a plugin that customers can install on their external career site to allow candidates to apply
with their LinkedIn profiles. Application data from these candidates is then available in both the customer's ATS and
Recruiter.
Here are some key benefits of the integration:
• Apply with LinkedIn drives increased conversions from the company career site and provides visibility into
Apply Starters (https://business.linkedin.com/talent-solutions/product-update/jobs/apply-starters).
• Apply with LinkedIn increases your conversion rate. Improve applicant conversion by making it possible for
candidates to automatically complete a job application using their LinkedIn profile data.

---

## Career Sites
*Chunk ID: OHR-REC-0254 | Chapter: Career Sites*

• Apply with LinkedIn improves InMail response rates by identifying warm leads. Anyone who begins the
application process using Apply with LinkedIn will be surfaced as Apply Starters in both Recruiter and a weekly
digest.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Partner Integration Provisioning page, click Edit next to Profile Import Partners.
3. On the Profile Import Partners page, in the LinkedIn section, add allowlisted URLs.
These are the URLs of career sites that will be offering the Apply with LinkedIn feature. The URLs must be in the
format https://<host>. For example: https://abc.fa.us2.oraclecloud.com. If you’re using the vanity domain, the URLs
should be in the format https://<company_vanity_hostname>.
4. Click the Start Activation Process button.
Once the activation process is started, the Client ID and Client Secret are assigned to the customer account.
5. Click the Request Integration button.
Sign in using your LinkedIn credentials. If you've already signed in LinkedIn within the browser, an active cookie will
recognize that you're signed in. You need to sign in with a LinkedIn account that's linked to your corporate LinkedIn
Recruiter contract or Paid Job Slot contract to enable the integration.
6. In the Request an Integration window, click the Request button in the Apply with LinkedIn section.
The status of the integration changes to Requested.
7. When the configuration is done and the integration status is Enabled, click the Active checkbox to complete the
activation.
Results:
The Apply with LinkedIn option is now available to candidates on all allowlisted zones.

---

## Configure the Optimized Indeed Job Application
*Chunk ID: OHR-REC-0255 | Chapter: Career Sites*

Experience
External candidates who find job opportunities on Indeed can quickly apply using their data from Indeed when Indeed is
used to set up their profiles and prefill application form fields.
When you use the optimized Indeed job application experience:
• Candidates coming from Indeed who are identified as returning candidates are automatically verified and can
proceed further without verification.
• Candidates coming from Indeed who are identified as new candidates are automatically verified and don’t need
to go through the 6-digit identity verification process.
• Candidates coming from Indeed.com or other specified Indeed domains will also benefit from the optimized
Indeed experience.
You need to enable the Apply with Indeed feature first, and then configure the optimized Indeed job application
experience.

---

## Career Sites
*Chunk ID: OHR-REC-0256 | Chapter: Career Sites*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Category Provisioning and Configuration page, go to the Profile Import section and click Edit.
3. On the Profile Import Partners page, go to the Social Media section.
4. In the Indeed section, you need to enable Apply with Indeed. Enter the Client ID and Client Secret Key and select the
Active check box.
5. Configure these two settings.

◦ Optimized Indeed Experience
◦ Trust Indeed authentication: You can enable this setting only if the Active check box of the Optimized
Indeed Experience option is selected.

---

## Note: If you enable these settings, the job application flow changes to give a better user experience to external
*Chunk ID: OHR-REC-0257 | Chapter: Career Sites*

candidates. If you don’t enable them, the job application experience is unchanged.
6. In the Indeed Domains field, enter the referrer domain “indeed.com”. This is the default value. In the event that the
domain changes, you can enter the new domain here.
7. Click Save.

---

## Enable LinkedIn Connections
*Chunk ID: OHR-REC-0258 | Chapter: Career Sites*

You can allow external candidates to view their LinkedIn connections specific to a company and to interact with their
connections by sending them messages to learn more about the company or to get recommendation and referral.
When candidates access your career site, they must first sign in to LinkedIn. They can then see their connections
who work at the company and send them messages. If the candidate doesn't have any connections, they can view
employees who work at that company.
To enable LinkedIn connections, you need to:
1. Enable the Integration with LinkedIn Connections
2. Configure LinkedIn Connections

---

## Enable the Integration with LinkedIn Connections
*Chunk ID: OHR-REC-0259 | Chapter: Career Sites*

You first need to enable the integration with LinkedIn Connections. The assumption is that you already set up and
configured the LinkedIn application.
Note: LinkedIn Connections can be enabled independent of the Recruiting System Connect.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration

2. On the Partner Integration Provisioning page, click Edit next to Profile Import Partners.

---

## Configure LinkedIn Connections
*Chunk ID: OHR-REC-0260 | Chapter: Career Sites*

You then need to configure LinkedIn Connections on your career site splash page or custom page.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. On the Career Sites Configuration page, select a career site that you want to configure with LinkedIn
Connections and click Edit.
3. Go to the Pages tab, select a splash page or custom page where you want to configure LinkedIn Connections
and click Edit.
4. Click the Show other elements menu and select LinkedIn Connections.

---

## Candidate Self Service
*Chunk ID: OHR-REC-0261 | Chapter: Career Sites*

External candidates can use self service capabilities on the career site to manage their job applications and talent
community settings.
External candidates must confirm their identity to access the candidate self service. When they're authenticated, they
can access their page and perform these actions:
• View the status of their job applications. A maximum of 5 job applications appear in each job applications
list: Active, Inactive and Draft. If there are any active applications that require the candidate's attention, these
applications are listed first and all of them are displayed. If there are more than 5 applications in any one of the
statuses, candidates can use the Show More button to see another 5 applications.
• Confirm their job applications.
• Withdraw from their job applications. Withdrawing can be done at any phase in the selection process before the
Offer phase.
• Update their talent community preferences (job locations and job category).
• Join talent communities.
• Turn on job alerts to receive updates about new job opportunities matching their preferred job category and
location.
• Edit their profile.
• Delete their profile. The deletion can be done at any phase in the selection process before the Offer phase.
• Schedule interviews if they've been sent invitations to schedule interviews. They can also view scheduled
interview details. Depending on the interview schedule configuration, they can reschedule and cancel
scheduled interviews.

---

## Display Third Party Links in Candidate Self-Service
*Chunk ID: OHR-REC-0262 | Chapter: Career Sites*

Pages
You can display links in candidate self-service pages to help external candidates complete assessments and background
checks for several partners, or complete a tax credit assessment for a single partner.
The links appear on the candidate self-service page if a candidate has pending background checks, assessments, or a
tax credit assessment after completing a job application. They also appear when a candidate selection process triggers
any of these tasks.
Before you start
For the links to appear:
• You must enable the display of links for a partner in the Setup and Maintenance work area, and add the partner
to a job requisition.
• The status of the background check for a partner and package in the job application should show as Candidate
Input Required. The status for assessment and tax credit packages should show as Requested, Initiated,
Started, or In Progress.
• Make sure the partner supports this feature before you enable it.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Enablement
2. On the Partner Enablement page, go to either the Background Check, Assessment, or Tax Credit section.
3. Click the Edit icon next to a partner.
4. Select the Display Links in Candidate Self Service for Process Triggers check box.
By default, this option is disabled.
5. Click Save and Close.

---

## Career Site Session
*Chunk ID: OHR-REC-0263 | Chapter: Career Sites*

External candidates have a secure browsing experience with an enhanced session control.
When external candidates have an active session on a career site (access code is active), there is a timeout after 27
minutes of inactivity. A message is displayed allowing candidates to extend their session and continue working, or to
sign out.
If the candidate doesn’t take any action, the session is closing after 30 minutes of inactivity. If the candidate is actively
using the career site, the session is automatically extended.

---

## The maximum duration of an access code is 4 hours. Candidates actively using a career site will have their session
*Chunk ID: OHR-REC-0264 | Chapter: Career Sites*

automatically extended every 30 minutes. However, after 4 hours of issuing the access code, the session will be ended
and the candidate will have to sign in again.
Note: When the Keep Me Signed In feature is enabled, the session timeout doesn’t apply.

---

# Job Application Flows

## Job Application Flows
*Chunk ID: OHR-REC-0265 | Chapter: Job Application Flows*

What Are Job Application Flows
A job application flow is a sequence of pages that candidates complete to provide information.
There are different types of job application flows:
• Apply: Sequence of pages that external candidates complete when they apply for a job on an external career
site.
• Request information: Sequence of pages to capture additional information from external candidates after they
applied to a job.
• Talent Community: Sequence of pages that external candidates complete to show their interests in an
organization by indicating their preferences, for example their preferred location.

---

## Application Flow
*Chunk ID: OHR-REC-0266 | Chapter: Job Application Flows*

An application flow is a sequence of pages that external candidates complete when they apply for a job on an external
career site.
When an external candidate clicks the Apply button to apply for a job, the first thing the candidate does is to enter
an email address or phone number. A verification is done in the database to check for candidate profiles or draft job
application already connected with the candidate's email address or phone number.
• If a record is found, an email or SMS with 6 digit code is sent to the candidate to validate the identity. Once the
identity is validated, the candidate is presented with the job application flow and information is prepopulated
with information from the candidate's last job application. The candidate can edit the information prior to
submitting the job application.
• If no record is found and it's a brand new candidate, the candidate is presented with the job application flow
upon entering an email address or phone number. When the candidate submits the job application, an email is
sent to the candidate to validate the identity and confirm the submitted job application.
Depending on how the application flow is configured, the candidate can import a profile from a third party such as
LinkedIn and Indeed, upload a resume, or manually fill out a job application.
External candidates can use the resume they uploaded to the recommended job widget. If they're identified as
new, their resume data automatically populates the application fields, and the resume is attached to the supporting
documents block if the block is in the flow. If a candidate has an existing profile, they're asked to authenticate their
identity, and then they're offered a choice to use the existing profile data, or import the information in the newly
uploaded resume.
Note: Parsing is only supported in job application flows, and not for talent community or events flows.

---

## Create an Application Flow
*Chunk ID: OHR-REC-0267 | Chapter: Job Application Flows*

You create an application flow to capture information from external candidates when they apply for a job on an external
career site. For details, see How do I set up a job application flow?

---

## Enable Express Apply
*Chunk ID: OHR-REC-0268 | Chapter: Job Application Flows*

Enable Express Apply so candidates can quickly import their profile information to job application form fields and
minimize the effort needed to apply for a job.
Express Apply headers are conversational and easy to read, especially on mobile devices. The flow is designed to
encourage candidates to import their profile so they can submit the application without reviewing the whole application
form.
The form contains an application form with an underlying set of blocks, and candidates will initially try to complete the
form without seeing them. If some fields are required and blank after candidates import their information, or if field
validation returns an error for some other reason, those fields are displayed in block context to candidates so they can
fix them. For example, if the Middle Name field in the Contact Info block is required and blank after import, the Contact
Info block is displayed to the candidate so they can fix it. If there are more errors in other blocks, they'll be presented to
candidates block-by-block, with each block shown on a separate page.
Note: Express Apply is only available for the Job Application Flow. It's not supported by other flow types.

---

## Note: Express Apply works best when the configured flow doesn't require many fields. If you need a longer flow with
*Chunk ID: OHR-REC-0269 | Chapter: Job Application Flows*

a lot of required information that can't be imported, it might be easier for candidates to use the standard apply flow.

In a typical flow:
• Candidates verify their profile with an email address or phone number.
• Once they've confirmed their identity, they'll see a profile import page where they can either upload a resume
(they can use the drag-and-drop functionality, or navigate to the file), or import information from Indeed or
LinkedIn (depending on what's enabled). They can also click a link to manually complete their form instead. If
they use this link, they'll be redirected to the classic application flow.
• If there's any missing information after they've uploaded or imported, candidates are notified and shown
precisely what fields need to be completed. They can use the arrows on the page to navigate forward or
backward to each issue. Candidates only see the blocks that have missing information. They don't need to
navigate to each page in the application.
Note: If a field has a default value coming from configuration that you've predefined, it will be considered a
filled value, and that block might not be shown to candidates.

---

## Job Application Flows
*Chunk ID: OHR-REC-0270 | Chapter: Job Application Flows*

• A final page displays blocks where information was imported, and lists of blocks that didn’t have any required
info. Candidates can optionally complete manually. Depending on the configuration, if there are any esignatures or marketing opt-ins needed, those fields also display.
• If a candidate wants to review all of their data, they can click the "review your data" link at the bottom of the
page. They'll be taken to the standard apply flow to review this information.
1. Create a new, or duplicate an existing application flow.
2. Add the Profile Import block to this configuration and include at least one profile import option (resume, LinkedIn, or
Indeed). This allows candidates to import their profile.
3. Enable the new Address block v2 functionality.
4. Enable the feature for the application flows.

---

## Request Information Flow
*Chunk ID: OHR-REC-0271 | Chapter: Job Application Flows*

You use a Request Information flow to capture additional information from external candidates once they have applied
to a job.
For example, a recruiter might have additional questions regarding answers provided by a candidate, or wants to ask
candidates to fill in additional questionnaires or documents requiring the consent of a candidate.
With this flow, a notification is sent to candidates. When candidates click the link in the notification, they're redirected
to the Request Information flow. At the same time that the notification is sent, the link to access the flow becomes
available in the candidate self service page where candidates can see a request to provide additional information for a
job application. Information provided by candidates is added to their candidate file.
If a block was present in previous flows, the block won't be displayed and candidates won't be able to provide
information. Exceptions are the Address, Contact Information, and Sensitive Personal Information blocks. If a block was
in a previous flow but the candidates didn't touch it, it won't be displayed in the Request Information flow. The only
exception is the contact information, address, and sensitive personal information that can be asked multiple times.
External candidates can drop off when filling out a request information flow and start over when ready without losing
data they already provided.
For details, see How do I set up a request information flow?

---

## Create a Request Information Flow
*Chunk ID: OHR-REC-0272 | Chapter: Job Application Flows*

You can configure a Request Information flow so that recruiters can capture additional information from external
candidates once they applied to a job. For details, see How do I set up a request information flow?

---

## Ask Candidates to Fill in Additional Questionnaires
*Chunk ID: OHR-REC-0273 | Chapter: Job Application Flows*

You can create a Request Information flow so that recruiters can ask external candidates to fill in additional
questionnaires once they've applied to a job. For example, a recruiter might want to ask a candidate to fill in a consent
form.
When you enable this feature, external candidates receive a notification asking them to complete a questionnaire. When
candidates click the link in the notification, they're redirected to the Request Information flow. At the same time that the
notification is sent, the link to access the flow becomes available in the candidate self service page where candidates
can see a request to complete a questionnaire for a job application. Information provided by candidates is added to their
candidate file. Recruiters can see the questionnaire in the candidate's job application, in the Questions tab.
Here's what to do
1. Create a Request Information Flow with the Questionnaire Block
2. Add the Request Information Flow to a Candidate Selection Process
3. Create a Notification to Request More Information

---

## Create a Request Information Flow with the Questionnaire Block
*Chunk ID: OHR-REC-0274 | Chapter: Job Application Flows*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.

14.

On the Job Application Flows page, click Create.
On the Application Flow Properties page, enter a name and a code.
In the Application Flow Type field, select Request Information.
Click Save and Continue.
On the creation page, go to the Versions section and click Create.
Enter the version name.
Enter the version start date. You can also select the Start on Activation option to activate the version as soon
as it's ready and activated.
Add the Questionnaire block to any section of the flow.
Click the Questionnaire link to display the Edit Block: Questionnaire window.
You can edit the headline of the block. The headline is the block name displayed to candidates.
Add instructions to provide specific information to candidates.
Select a questionnaire. The questionnaire must be created for the Recruiting subscriber, be saved in the Job
Application Flow folder, and be active. Once the questionnaire is selected, you can see the questionnaire
version number and version description.
Select Confidential if you only want users with the privilege View Confidential Questionnaire Responses
(IRC_VIEW_CONFIDENTIAL_QUESTIONNAIRE_RESPONSES) to see the responses provided by candidates in the
questionnaire.

---

## Job Application Flows
*Chunk ID: OHR-REC-0275 | Chapter: Job Application Flows*

15. Select Based on Condition to present the questionnaire to the candidate only if a specific answer was given
by the candidate in a previous Apply flow or Request Information flow. To use that option, a question must be
created in the Question Library and a questionnaire must be assigned to the answer of that question.
Note: An additional questionnaire can only be used in a Request Information flow. When a questionnaire is
marked as conditional, that questionnaire can be selected as additional questionnaire for a question which
will be asked in a prior Request Information flow or prescreening questionnaire in the same job application.
16. Click Save and Activate.

---

## Add the Request Information Flow to a Candidate Selection Process
*Chunk ID: OHR-REC-0276 | Chapter: Job Application Flows*

You need to add the Request Information flow to specific phases and states within a candidate selection process. When
a job application is moved to a specific state within a phase, a notification is automatically sent to candidates.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2.
3.
4.
5.

On the Candidate Selection Process Configuration page, create a selection process or select an existing one.
Add the Request Information action when entering a phase, leaving a phase, or for any state within a phase.
On the Action: Request Information page, select the flow to request additional information from candidates.
Select the notification for external candidates. When a job application is moved to a specific state within a
phase, a notification is automatically sent to candidates.

---

## Create a Notification to Request More Information
*Chunk ID: OHR-REC-0277 | Chapter: Job Application Flows*

You use the Automated Job Application Request Info Notification to ask external candidates to fill in additional
questionnaires. When candidates receive the notification and click the link in the notification, they're redirected to the
Request Information flow. At the same time that the notification is sent, the link to access the flow becomes available
in the candidate self service page where candidates can see a request to provide additional information for a job
application. Information provided by candidates is added to their candidate file.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library
2.
3.
4.
5.
6.

On the Recruiting Content Library page, click Create.
On the Create Content Item page, enter a name and a code.
In the Category field, select the content type Automated Job Application Request Info Notification.
Enter a subject for the message.
Enter the message text.

◦ Use rich text features to format the text.
◦ Include tokens to personalize the message so that it's specific to the candidate in the context of the job
application.
Use the token RequestInformationFlowURL to add the request information flow.

◦
◦ Insert images and logos to align with your organization's corporate branding.

---

## Job Application Flows
*Chunk ID: OHR-REC-0278 | Chapter: Job Application Flows*

7. Click the Translation Editor icon to translate the message subject and message text.

---

## Ask Candidates to Fill in Additional Questionnaires
*Chunk ID: OHR-REC-0279 | Chapter: Job Application Flows*

Based on Their Answers
When you create a job application flow of type Request Information and add the Questionnaire block, you can mark the
questionnaire as being based on a condition.
What happens is that the questionnaire is presented to the candidate only if a specific answer was given by the
candidate in a previous apply flow or request information flow.
Here's what to do
1.
2.
3.
4.

---

## Create a Question and Select a Questionnaire for an Answer
*Chunk ID: OHR-REC-0280 | Chapter: Job Application Flows*

Create a Request Information Flow with the Questionnaire Block
Add the Request Information Flow to a Candidate Selection Process
Create a Notification to Request More Information

---

## Create a Question and Select a Questionnaire for an Answer
*Chunk ID: OHR-REC-0281 | Chapter: Job Application Flows*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Question Library
2. In the Questions page, select Recruiting in the Subscriber field.
3. Click Create. The Create Question page opens.
4. Enter question properties:

◦ Folder: Select the folder where you want to save the question.
◦ Privacy: Select Private if only you can edit the question. Select Public if anyone can edit the question.
5.
6.
7.
8.

Create the question as usual.
In the Response section, click Add to add the responses to the question.
For one of the answer, select a questionnaire in the Additional Questionnaire field.
Click Save and Close.

---

## Create a Request Information Flow with the Questionnaire Block
*Chunk ID: OHR-REC-0282 | Chapter: Job Application Flows*

You need to add the Questionnaire block to the flow, select a questionnaire, and enable the Based on Condition option.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration
2. On the Job Application Flows page, click Create.
3. On the Application Flow Properties, enter a name and a code.

---

## Job Application Flows
*Chunk ID: OHR-REC-0283 | Chapter: Job Application Flows*

4.
5.
6.
7.
8.
9.
10.
11.
12.

In the Application Flow Type field, select Request Information.
Click Save and Continue.
On the creation page, click Create in the Versions section.
Enter the version name.
Add the Questionnaire bloc to any section of the flow.
Click the Questionnaire link to display the Edit Block: Questionnaire window.
Edit the headline of the block, if desired. The headline is the block name displayed to candidates.
Add instructions to provide specific information to candidates.
Select a questionnaire. The questionnaire must be created for the Recruiting subscriber, be saved in the Job
Application Flow folder, and be active. Once the questionnaire is selected, you can see the questionnaire
version number and version description.
13. Select Confidential if you only want users with the privilege View Confidential Questionnaire Responses
(IRC_VIEW_CONFIDENTIAL_QUESTIONNAIRE_RESPONSES) to see the responses provided by candidates in the
questionnaire.
14. Select Based on Condition to present the questionnaire to the candidate only if a specific answer was given
by the candidate in a previous apply flow or request information flow. To use that option, a question must be
created in the Question Library and a questionnaire must be assigned to the answer of that question.
15. Click Save.

---

## Add the Request Information Flow to a Candidate Selection Process
*Chunk ID: OHR-REC-0284 | Chapter: Job Application Flows*

You need to add the Request Information flow to specific phases and states within a candidate selection process. When
a job application is moved to a specific state within a phase, a notification is automatically sent to candidates.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2.
3.
4.
5.

On the Candidate Selection Process Configuration page, create a selection process or select an existing one.
Add the Request Information action when entering a phase, leaving a phase, or for any state within a phase.
On the Action: Request Information page, select the flow to request additional information from candidates.
Select the notification for external candidates. When a job application is moved to a specific state within a
phase, a notification is automatically sent to candidates.

---

## Create a Notification to Request More Information
*Chunk ID: OHR-REC-0285 | Chapter: Job Application Flows*

You use the Automated Job Application Request Info Notification to ask external candidates to fill in additional
questionnaires. When candidates receive the notification and click the link in the notification, they're redirected to the
Request Information flow. At the same time that the notification is sent, the link to access the flow becomes available
in the candidate self service page where candidates can see a request to provide additional information for a job
application. Information provided by candidates is added to their candidate file.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library
2. On the Recruiting Content Library page, click Create.
3. On the Create Content Item page, enter a name and a code.

---

## Job Application Flows
*Chunk ID: OHR-REC-0286 | Chapter: Job Application Flows*

4. In the Category field, select the content type Automated Job Application Request Info Notification.
5. Enter a subject for the message.
6. Enter the message text.

◦ Use rich text features to format the text.
◦ Include tokens to personalize the message so that it's specific to the candidate in the context of the job
application.
Use the token RequestInformationFlowURL to add the request information flow.

◦
◦ Insert images and logos to align with your organization's corporate branding.

Note: The maximum size of a notification is 15MB. If you exceed this limit, the notification might not be sent.
To respect this limit, you can optimize images or logos in the notification.
7. Click the Translation Editor icon to translate the message subject and message text.

---

## Ask a Question to a Candidate Based on an Answer
*Chunk ID: OHR-REC-0287 | Chapter: Job Application Flows*

You can configure questions so that they're displayed to candidates based on their answers within the current
application flow. The answer to a question might trigger another question.
This feature is supported for prescreening questions, disqualification questions, and questions within questionnaires.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Question Library

2. On the Questions page, select Recruiting in the Subscriber field.
3. You can create a new question or modify an existing one.
4. Select the option Display the question conditionally.
5. Select a controlling question.
6. Select a controlling response.
Results:
The controlled question isn't visible to candidates at first. Based on the question logic, the controlled question renders
dynamically if an appropriate controlling answer was provided.
Note: If a controlling question and its conditional question are added to a job requisition and later the controlling
question is updated but not the conditional question, this will cause the conditional question to point to an old version
of the controlling question. The conditional question will also need to be updated.

---

## When to Delete or Inactivate a Job Application Flow
*Chunk ID: OHR-REC-0288 | Chapter: Job Application Flows*

You delete a job application flow so it's no longer visible in the list of job application flows. The Delete action is only
available for draft job application flows.

---

## Job Application Flows
*Chunk ID: OHR-REC-0289 | Chapter: Job Application Flows*

You inactivate a job application flow to prevent recruiters from selecting that flow when they create a job requisition.
When you use the Inactivate action, the job application flow status changes to Inactive. The Inactivate action is only
available for active job application flows.

---

## Set Fields as Required in Job Application Flows
*Chunk ID: OHR-REC-0290 | Chapter: Job Application Flows*

You can create rules in Transaction Design Studio to set fields as required in application flows, request information
flows, and talent community flows. When fields are set as required, candidates need to complete them to submit their
job applications.
This applies to blocks which use profile content sections:
• Licenses and Certificates
• Education
• Languages
• Experience
• Skills
• Work Preferences
It also applies to the Email Address and Phone Number fields (Contact Information). By default, the Email Address field
is required.
Note: Configuring the Email Address and Phone Number as required doesn't have any effect on the candidate
identity verification method. Candidates can still decide whether they want to confirm their identity using a phone
number or email address.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Define Application Flow Required Fields.
5. Click Add to create and configure a rule.
6. In the Basic Details section, enter a name and description for the rule. Select an application flow.
7. In the Available Attributes section, select a data source. Fields available for the selected data source are displayed.
8. Decide which fields are required. If a field was set as required at the profile level, the Required setting is disabled.
Also, the Required setting is applied per profile template. This means that if a field is set as required, the required
setting applies to all content sections of that template.
Note:
The Visible field isn't functional. If you change it, it won't have any effect on the application flow.
9. Click Save and Close.

---

## Candidate Disability, Diversity, and Legislative
*Chunk ID: OHR-REC-0291 | Chapter: Job Application Flows*

Information
Your organization can collect disability, diversity, and legislative information from both external and internal candidates
when they apply for jobs.
This helps your organization to collect data as per regulatory guidelines and reporting in each country where you hire
candidates. It also helps you to monitor and improve your efforts to build a diverse workforce.
You can configure job application flows to display fields to collect disability, diversity, and legislative information.
• Standard fields for diversity and disability information

◦ Gender
◦ Marital status
◦ Date of birth
◦ Ethnicity
◦ Religion
◦ Disability information
• Oracle-delivered flexfields for each country's legislative requirements. As an example, for the United Kingdom,
NINO verified, caring responsibilities.
• Customer-defined flexfields that you need for legislative purposes. This includes only Global Data Elements.
External candidates are prompted with these standard, Oracle-delivered, and customer-defined fields when they
apply to jobs with locations in any country for which rules are configured. These private responses aren't visible to
the recruiting team during the hiring process, not even on the tab named Sensitive Info. Still, this information is made
available seamlessly as part of worker details once a candidate is hired.
If a job is posted to several countries with different setups for diversity and disability questions, those blocks are visible
to external candidates as collapsed accordion elements. Candidates click the appropriate country to expand the section,
and then provide the required information. When diversity info is prefilled for the candidate or some of the information
is required, the section is automatically expanded.
Internal mobility candidates aren't prompted with these additional sections and fields while applying to jobs, however a
snapshot of their current information in these fields is also captured in their job application to support reporting.

---

## Configure Standard Fields to Collect Diversity and
*Chunk ID: OHR-REC-0292 | Chapter: Job Application Flows*

Disability Information
You can configure job application flows to display fields to collect standard diversity and disability information.
Here's what to do
1. Configure Standard Diversity and Disability Fields

---

## Job Application Flows
*Chunk ID: OHR-REC-0293 | Chapter: Job Application Flows*

2. Review Lookup Values for Standard Diversity and Disability Fields
3. Configure the Job Application Flow

---

## Configure Standard Diversity and Disability Fields
*Chunk ID: OHR-REC-0294 | Chapter: Job Application Flows*

You need to configure which standard diversity and disability fields to display to candidates in each of the countries
where hiring is done.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Candidate Application Diversity and Disability.
5. Click Add to create and configure a rule to display certain fields for certain countries.
6. In the Basic Details section, enter the name, description, and any countries for which the rule applies.
7. In the Available Attributes section, select a data source.
8. Select which fields you want to make visible and which ones are required to be filled.

◦ Date of Birth: use the Personal Details data source
◦ Ethnicity: use the Ethnicity data source (this will display two fields for requisitions in the US)
◦ Gender: use the Demographic Info data source
◦ Marital Status: use the Demographic Info data source
◦ Religion: use the Religion data source
◦ Disability Status, Category, Reason, and Reasonable Accommodation: use the Disability Info data source.
9. Click Save and Close.
If a job requisition is posted in any United States location and if its Diversity block is configured to display the single
field Ethnicity, candidates will see two ethnicity-related questions. First a check box asks if the candidate considers
themselves to be Hispanic or Latino, and then another set of five check boxes invites them to select the race or races
that they identify with. This method of displaying the Ethnicity field is consistent with the employee self-service page
that they will see if and when they reach the end of the recruiting process successfully. After this candidate is hired, their
ethnicity responses and any other diversity values that they provided in the job application will become visible in their
personal information as a worker.
Note: In the United States, it's not correct to configure the ethnicity to be required for candidates to answer. If
a candidate doesn't fill in either of the two ethnicity questions, you should report the race and ethnicity for this
candidate as "Not Available" or "Do not want to disclose", in whichever way you're currently reporting this value for
candidates.
When collecting disability information for hiring in the United States, you should only configure a single disabilityrelated field to be visible for that country. US regulations require that federal contractors must show candidates the form
CC-305, Voluntary Self-Identification of Disability. The field Disability Status is the only field which belongs inside that
form, and it can't be displayed as a required field. Furthermore, the form's format can't be changed. If you configure
additional disability fields to appear for candidate applications within the US, they will all be displayed inside this form
when the block is displayed in the application flow. This would disturb the form's layout, making it no longer conform to
the regulations.

---

## Review Lookup Values for Standard Diversity and Disability Fields
*Chunk ID: OHR-REC-0295 | Chapter: Job Application Flows*

You can verify that the lookup values for the standard diversity and disability fields are correct for each country. This
step is optional. These lookups are configured in the Setup and Maintenance work area, using the tasks Manage
Common Lookups and Manage Person Lookups.
In Manage Common Lookups:
• DISABILITY_CATEGORY
• DISABILITY_REASON
• DISABILITY_STATUS
• ORA_PER_SELF_DISCLOSE_DISABILITY
• ORA_PER_DISABILITY_COUNTRY
In Manage Person Lookups:
• PER_ETHNICITY
• PER_RELIGION
• MAR_STATUS

---

## Configure the Job Application Flow
*Chunk ID: OHR-REC-0296 | Chapter: Job Application Flows*

You need to decide which blocks to add to the job application flow and where the blocks should be placed in the flow.
On the job application flow creation page, configure which blocks to display.
• Diversity: This block shows any of the standard diversity fields, and any of the person legislative flexfields that
are delivered by Oracle (PER_PERSON_LEGISLATIVE_DATA_LEG_DDF), and any of your customer-defined
legislative flexfields (PER_PERSON_LEGISLATIVE_DFF) for job requisitions with locations in any country.
• Disability: This block shows any disability-related fields for any country, and also shows the U.S. disability form
CC-305 for job requisitions located in the United States.
• Veteran: This block shows the US veteran status field for job requisitions located in the United States.
You can add instructions to the blocks to provide specific information to candidates. For example, you may want to
indicate that answers are optional, they're confidential, and the recruiting team won't be able to view the answers. Also
you may want to ensure that instructions for the Veteran block give the definition of all categories of protected veteran,
because candidates aren't asked to self-identify their specific category while applying for jobs. Here in the pre-offer time
frame, candidates are merely asked a single question, to disclose whether or not they fall into any category of protected
veteran.
Recruiters can now use the newly-activated application flows within requisitions to start gathering this legislative and
diversity information from external candidates. Anytime a job requisition is using a job application flow that contains
the Disability and Diversity blocks, if that requisition is hiring for a city, state, or level within the relevant country
locations, then these fields and the block instructions will appear. Anytime a job requisition is using a job application
flow that contains the Veteran block, if that requisition is hiring for a city, state, or level within the US, then this field
and its block instructions will appear. Candidate responses are always confidential, not visible to the Hiring Team who
manages the job applications, only accessible through reporting.

---

## Configure Oracle-Delivered Flexfields to Collect
*Chunk ID: OHR-REC-0297 | Chapter: Job Application Flows*

Legislative Information
You can configure job application flows to display Oracle-delivered flexfields to collect legislative information required
by a country.
Here's what to do
1. Configure Oracle-delivered Legislative Flexfields
2. Review Oracle-delivered Legislative Flexfields
3. Configure the Job Application Flow

---

## Configure Oracle-Delivered Legislative Flexfields
*Chunk ID: OHR-REC-0298 | Chapter: Job Application Flows*

You need to configure which legislative flexfields (PER_PERSON_LEGISLATIVE_DATA_LEG_DDF) to display to candidates
in each of the countries where hiring is done, chosen from the list of fields that are delivered by Oracle for each specific
country's regulations.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Candidate Application Additional Info.
5. Click Add to create and configure a rule to display certain flexfields for certain countries.
6. In the Basic Details section, enter the name and description for the rule.
7. In the Page Attributes section, the region Additional Info is selected by default. Set the Person Legislative
Information field to Visible. Click the Edit icon.

◦ Flexfield Content Code: Select the country for which the rule applies.
◦ Flexfield Attributes: Select the specific field that has been delivered in the lookups for that country.
◦ Select each field you want to make visible and which ones are required to be filled.
8. Click Done.
9. Click Save and Close.
US veteran information could be gathered from candidates in two places. However, the best practice is to configure and
display this field only once.

---

## Review Oracle-Delivered Legislative Flexfields
*Chunk ID: OHR-REC-0299 | Chapter: Job Application Flows*

You can review the legislative flexfields or attributes that are seeded per country
(PER_PERSON_LEGISLATIVE_DATA_LEG_DDF) and their associated lookups, to ensure they're desired for recruiting in
each country. This step is optional. These lookups are configured in the Setup and Maintenance work area, using the
Manage Descriptive Flexfields task.

---

## Configure the Job Application Flow
*Chunk ID: OHR-REC-0300 | Chapter: Job Application Flows*

You need to decide which blocks to add to the job application flow and where the blocks should be placed in the flow.

---

## Job Application Flows
*Chunk ID: OHR-REC-0301 | Chapter: Job Application Flows*

On the job application flow creation page, configure which blocks to display.
• Diversity: This block shows any of the standard diversity fields, and any of the person legislative flexfields that
are delivered by Oracle (PER_PERSON_LEGISLATIVE_DATA_LEG_DDF), and any of your customer-defined
legislative flexfields (PER_PERSON_LEGISLATIVE_DFF) for job requisitions with locations in any country.
• Disability: This block shows any disability-related fields for any country, and also shows the U.S. disability form
CC-305 for job requisitions located in the United States.
• Veteran: This block shows the US veteran status field for job requisitions located in the United States.
You can add instructions to the blocks to provide specific information to candidates. For example, you may want to
indicate that answers are optional, they're confidential, and the recruiting team won't be able to view the answers. Also
you may want to ensure that instructions for the Veteran block give the definition of all categories of protected veteran,
because candidates aren't asked to self-identify their specific category while applying for jobs. Here in the pre-offer time
frame, candidates are merely asked a single question, to disclose whether or not they fall into any category of protected
veteran.
Recruiters can now use the newly-activated application flows within requisitions to start gathering this legislative and
diversity information from external candidates. Anytime a job requisition is using a job application flow that contains
the Disability and Diversity blocks, if that requisition is hiring for a city, state, or level within the relevant country
locations, then these fields and the block instructions will appear. Anytime a job requisition is using a job application
flow that contains the Veteran block, if that requisition is hiring for a city, state, or level within the US, then this field
and its block instructions will appear. Candidate responses are always confidential, not visible to the Hiring Team who
manages the job applications, only accessible through reporting.

---

## Configure Customer-Defined Flexfields to Collect
*Chunk ID: OHR-REC-0302 | Chapter: Job Application Flows*

Legislative Information
You can configure job application flows to display customer-defined flexfields to collect legislative information.
Here's what to do
1. Configure Customer-defined Legislative Flexfields
2. Review Customer-defined Legislative Flexfields
3. Configure the Job Application Flow

---

## Configure Customer-Defined Legislative Flexfields
*Chunk ID: OHR-REC-0303 | Chapter: Job Application Flows*

You need to configure which customer-defined legislative flexfields (PER_PERSON_LEGISLATIVE_DFF) to display to
candidates in each of the countries where hiring is done.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Candidate Application Diversity and Disability.
5. Click Add to create and configure a rule to display certain fields for certain countries.
6. In the Basic Details section, enter the name, description, and any countries for which the rule applies.
7. In the Page Attributes sections, the setting for the region Person Legislative Attributes isn't visible by default.
Change it to Visible, and click the pencil icon to select your desired attributes.region Person Legislative Attribute
is selected by default.

---

## Job Application Flows
*Chunk ID: OHR-REC-0304 | Chapter: Job Application Flows*

8. Within each available Flexfield Context Code, you can select the desired Flexfield Attribute. Note that only
global data elements are supported here.
9. For each Flexfield Attribute, select if you want to make it visible and select if it's required to be filled by the
candidate.
10. Click Save and Close.
Only legislation-related descriptive flexfields (DFF) can be exposed to gather information from candidates, not any
other types of customer-defined descriptive flexfields. However, customer-defined extensible flexfields (EFF) can
be exposed within application flows. See Display Candidate Flexfields in Extra Info Tab and Display Job Application
Flexfields in Extra Info Tab.

---

## Review Customer-Defined Legislative Flexfields
*Chunk ID: OHR-REC-0305 | Chapter: Job Application Flows*

These customer-defined legislative flexfields (PER_PERSON_LEGISLATIVE_DFF) may already be configured by your
Global HR implementation. You can review anything that's already defined, and then add any additional fields you may
need for recruiting purposes. This step is optional. These lookups are configured in the Setup and Maintenance work
area, using the Manage Person Descriptive Flexfields task.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Workforce Information
◦ Task: Manage Person Descriptive Flexfields
2. Select and configure PER_PERSON_LEGISLATIVE_DFF.

---

## Configure the Job Application Flow
*Chunk ID: OHR-REC-0306 | Chapter: Job Application Flows*

You need to decide which blocks to add to the job application flow and where the blocks should be placed in the flow.
On the job application flow creation page, configure which blocks to display.
• Diversity: This block shows any of the standard diversity fields, and any of the person legislative flexfields that
are delivered by Oracle (PER_PERSON_LEGISLATIVE_DATA_LEG_DDF), and any of your customer-defined
legislative flexfields (PER_PERSON_LEGISLATIVE_DFF) for job requisitions with locations in any country.
• Disability: This block shows any disability-related fields for any country, and also shows the U.S. disability form
CC-305 for job requisitions located in the United States.
• Veteran: This block shows the US veteran status field for job requisitions located in the United States.
You can add instructions to the blocks to provide specific information to candidates. For example, you may want to
indicate that answers are optional, they're confidential, and the recruiting team won't be able to view the answers. Also
you may want to ensure that instructions for the Veteran block give the definition of all categories of protected veteran,
because candidates aren't asked to self-identify their specific category while applying for jobs. Here in the pre-offer time
frame, candidates are merely asked a single question, to disclose whether or not they fall into any category of protected
veteran.
Recruiters can use the newly-activated application flows within requisitions to start gathering this legislative and
diversity information from external candidates. Anytime a job requisition is using a job application flow that contains
the Disability and Diversity blocks, if that requisition is hiring for a city, state, or level within the relevant country
locations, then these fields and the block instructions will appear. Anytime a job requisition is using a job application
flow that contains the Veteran block, if that requisition is hiring for a city, state, or level within the US, then this field
and its block instructions will appear. Candidate responses are always confidential, not visible to the Hiring Team who
manages the job applications.

---

## Collect Candidate Date of Birth and National Identifier
*Chunk ID: OHR-REC-0307 | Chapter: Job Application Flows*

You can ask external candidates for their date of birth and national identifier while they apply for a job or once they've
applied to a job.
The national identifier presented to external candidates depends on the location (country) of the job requisition.
Candidates can select a type of identifier from the list of identifiers defined for a country and provide a value for
that identifier. The national identifier and date of birth provided by a candidate are reusable. Once a candidate
has provided that info, it's pre-populated in new job applications. When a candidate provides a national identifier
and date of birth, the recruiter or hiring manager with the privilege View External Candidate Sensitive Information
(IRC_VIEW_EXTERNAL_CANDIDATE_SENSITIVE_INFORMATION) can see the info in the job application's Sensitive Info
tab. As soon as the candidate becomes an employee, the info is no longer visible.
To collect the date of birth and national identifier of candidates, you need to add the Sensitive Personal Information
block in an application flow.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration
2. On the Job Application Flows page, click Create.
3. In the Application Flow Type field, select Apply or Request Information.
4. Configure the flow as any other flow.
5. Create a version of the flow and add the Sensitive Personal Information block.

---

## Collect Candidate Data Using Multiple Content Sections
*Chunk ID: OHR-REC-0308 | Chapter: Job Application Flows*

You can collect candidate data using many profile content sections for example Experience versus Military Experience,
or Education versus Special Education.
When many profile content sections are set up, candidates can enter supported profile data when applying for a job,
when updating their information in the candidate self service, or when signing up in a talent community.
Recruiters can view profile data in many sections as entered by candidates. This data is available in job applications,
candidate files, prospect records, and pool members. Sections titles and fields within each section appear as you
configured them. Recruiters can also search for candidates using data from many content sections using the keyword
search. They can also filter candidate search results using advanced search filters and basic filters.
Here's what to do
1. Create Profile Content Sections in the Profiles Work Area
2. Use Profile Content Sections in Application Flows

---

## Create Profile Content Sections in the Profiles Work Area
*Chunk ID: OHR-REC-0309 | Chapter: Job Application Flows*

You first need to create profile content sections in the Profiles work area.
1.
2.
3.
4.
5.

Go to My Client Groups and click Profiles.
On the Profiles page, click Profile Types.
On the Profile Types page, click Person.
On the Edit Profile Type: Person page, click Add Content Section.
Select a template for the content section. You can use these templates:

◦ Certification
◦ Education
◦ Language
◦ Skill
◦ Work History
◦ Work Preferences (multiple sections isn't supported)
6. On the Add Content Section page, enter a section name and a description.
7. Select the Active option.
8. In the Content Section Properties section, decide which attributes you want to display or hide as per your
business needs.
9. In the Content Section Subscribers, click Add to add Recruiting as a subscriber to this content section.
10. Click Save and Close.

---

## Use Profile Content Sections in Applications Flows
*Chunk ID: OHR-REC-0310 | Chapter: Job Application Flows*

You can then use the sections in profile content blocks when creating application flows of type Apply, Request
Information, and Talent Community.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration
2. Create a new flow or open an existing flow.
3. Create a new version of the flow.
4. Add profile content blocks to the flow. You can add the same block many times. Profile content blocks are:

◦ Education
◦ Experience
◦ Languages
◦ Licenses and Certifications
◦ Skills
◦ Work Preferences (multiple sections isn't supported)
5. Click the title of the block.

---

## Job Application Flows
*Chunk ID: OHR-REC-0311 | Chapter: Job Application Flows*

6. In the Edit Block page, define the block properties.

◦ Update the block headline to help candidates understand what info they need to provide. The headline

is the block name displayed to candidates. If you use many sections within the same block, it's even
more important to have different headlines otherwise all sections will have the same name. For example,
for an Education block with two sections, you could have Bachelor Degree and Doctoral Degree as
headlines. When you have many sections, you can click the block title to quickly see the content section
configuration.
Add instructions to provide specific information to candidates on how to fill the info.

◦
◦ Select a section for the block. The selector displays the sections created in the Profiles work area that

have Recruiting added as a subscriber. You can select only one section within the same block. Note
that the profile content section flagged as default in the Person Profile Types configuration will also be
marked as the default in the selector. For example, you can add the Languages block many times within
the same flow, but each block will have a different section. The application flow you just defined must
be used within specific job requisitions. Choose any requisition for which you want to start capturing
candidate data. In the Details tab, go to the Configuration section, and select the application flow.
7. Click Save and Close.
The application flow you just defined must be used within specific job requisitions. Recruiting users need to choose any
requisition for which they want to start capturing candidate data. In the Details tab, they need to go to the Configuration
section, and select the application flow.

Things to Consider
• If you add the Timeline block to an application flow, you can add the Education and Experience blocks but you
need to set them as having non-default sections. If you set default sections, you'll get an error message when
saving the application flow.
• When you configure an application flow, you must use a default Work Preferences block. Otherwise, candidates
won't be indexed and recruiters won't be able to search candidates based on these work preferences.
• During an application flow of type Apply, the profiles imported using LinkedIn, Indeed, and resume parsing
will be imported to default sections only (the oldest created sections). However candidates can if needed, add
additional info in default or non-default sections.
• When you merge candidate files, all additional profile section data is copied into the primary candidate file.
• When candidates move to the HR phase to become workers, profile data from many content sections is copied
to their talent profile.

---

## Collect Additional Information Using Flexfields
*Chunk ID: OHR-REC-0312 | Chapter: Job Application Flows*

You can configure an application flow to collect additional information from candidates using Person Extensible
Flexfields in PER_PERSON_EIT_EFF. The flexfields appear in the Extra Information block and candidates can provide
their responses.
This information is stored in the candidate's job application and also becomes available as part of the candidate profile.
When a candidate applies for a subsequent job, the fields in the Extra Information block are prefilled. These values
are defaulted from the candidate's profile, using the information the candidate provided when they last applied. The
candidate can edit this defaulted information before submitting the new job application. This happens when the
additional information is presented in either type of flow: a job application flow or a request information flow.

---

## When a recruiter creates a job application for a candidate, any values currently in the additional information
*Chunk ID: OHR-REC-0313 | Chapter: Job Application Flows*

section of the candidate profile become part of the new job application. Also, a recruiter or user can update or
add additional information to a job application, if they have the privilege Update Candidate Job Application
(IRC_UPDATE_CANDIDATE_JOB_APPLICATION_DATA). That updated version isn't presented to the candidate.

---

## Collect Additional Candidate Details Using Extensible
*Chunk ID: OHR-REC-0314 | Chapter: Job Application Flows*

Flexfields
You can collect data from external candidates using job application flow blocks which contain predefined content types
or data blocks.
You can configure your own set of data blocks and add them to the job application flow to collect more details from
candidates. For example, you might want to collect details about the job references of a candidate, their hobbies, their
special interests, or special needs to attend an interview. Those details are available in the candidate's job application, in
the Extra Info tab. When a candidate is hired, the info is available in the Manage Person's page, in the Extra Information
section.
Here's what to do
1.
2.
3.
4.
5.
6.

---

## Create the Context for Flexfields
*Chunk ID: OHR-REC-0315 | Chapter: Job Application Flows*

Define Display Type as List of Values
Attach the Context to the Person Extra Information Category
Add the Context to a Page
Deploy Flexfields
Add the Context to the Application Flow

---

## Create the Context for Flexfields
*Chunk ID: OHR-REC-0316 | Chapter: Job Application Flows*

You first need to create the context where extensible flexfields (EFFs) will be added. The Person EIT Information EFFs
are used for this feature. Examples of a context could be Hobby or Job References.
1.
2.
3.
4.
5.
6.

In the Setup and Maintenance work area, search for the task Manage Extensible Flexfields.
On the Manage Extensible Flexfields page, search for the Person EIT Information name.
In the Search Results section, click the Edit icon.
On the Edit Extensible Flexfield: Person EIT Information page, click the Manage Contexts button.
On the Manage Contexts page, click the Create icon in the Search Results section.
On the Create Context page, configure the context.

◦ Enter values for Display Name, Code, API Name, Behavior.
Note: Don't use special characters for the names and context code.

◦ On the Context Usages tab, click the Create icon to define the usage of the context. Select Usage Code

for Person to display the information to candidates, and Usage Code for Candidate Application to
display the information to recruiters in job applications. Usage Code for Person and Usage Code for
Candidate Application are both required for the context to appear in the Extra Information block of the
job application flow.
7. Click Save.
8. In the Context Sensitive Segments section, click the Create icon to add attributes to the context. See next
section for details on the display type.

---

## Job Application Flows
*Chunk ID: OHR-REC-0317 | Chapter: Job Application Flows*

9. Click Save and Close.
10. On the Edit Context page, click Save and Close.
11. On the Manage Context page, click Save and Close.

---

## Define Display Type as List of Values
*Chunk ID: OHR-REC-0318 | Chapter: Job Application Flows*

When you create a new context in the Context Sensitive Segments section, it's recommended to define the display type
as List of Values (LOV).
1.
2.
3.
4.

On the Create Segment page, go to the Display Properties section.
In the Display Type field, select List of Values.
Configure the remaining fields.
Click Save and Close.

---

## Note: Table-based value sets with lists of values (LOV) isn't supported for extensible flexfields (EFFs) on job
*Chunk ID: OHR-REC-0319 | Chapter: Job Application Flows*

applications. While adding attributes to the context, create a lookup in Common Lookups, build the value set based on
the lookup, and link to the context segment validation. This will allow a list of values to be displayed on the candidate
application page.
If a value set doesn't already exist for the EFFs:
1. On the Create Segment page, click the View Value Set button.
2. Configure the value set properties.
3. Click Save and Close to return to the Create Segment page.
If you need to create a lookup for the value set:
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, search for the task Manage Common Lookups.
On the Manage Common Lookups page, click the Create icon.
Configure the lookup type, meaning, and description. In the Module field, select Recruiting.
When you configure the lookup codes, use SQL to obtain the values.
Click Save and Close.

---

## Attach the Context to the Person Extra Information Category
*Chunk ID: OHR-REC-0320 | Chapter: Job Application Flows*

Once the context is created, you need to attach it to the Person Extra Information category.
1. On the Edit Extensible Flexfield: Person EIT Information page, in the Category section, select Person Extra
Information.
2. In the Person Extra Information section, click the Associated Contexts tab, then click the Select and Add icon.
3. Search for the context you created.
4. Click OK.

---

## Add the Context to a Page
*Chunk ID: OHR-REC-0321 | Chapter: Job Application Flows*

You then need to add the context to an existing page or a new page.
1. On the Edit Extensible Flexfield: Person EIT Information page, go to the Person Extra Information section and
click the Pages tab.
2. Select a page or create a new one.
3. Click Save.
4. In the Associated Context Details section, click the Select and Add icon to associate the context to the page.
5. Click OK.

---

## Deploy Flexfields
*Chunk ID: OHR-REC-0322 | Chapter: Job Application Flows*

Finally, you need to deploy the flexfields to make them available in the UI.
1. On the Manage Extensible Flexfields page, search for the Person EIT Information name.
2. Click Deploy Flexfield..

---

## Add the Context to the Application Flow
*Chunk ID: OHR-REC-0323 | Chapter: Job Application Flows*

You add the context to a job application flow, in the Extra Information block.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration

2.
3.
4.
5.
6.
7.
8.
9.
10.
11.

On the Job Application Flows page, click Create.
Enter a name and a code.
In the Application Flow Type field, select Apply.
Configure the flow as any job application flow.
When creating a version of the flow, add the Extra Information block to the desired section of the flow.
Click the Extra Information block title.
Select the context you created.
You can change the block headline and instructions.
You can add several Extra Information blocks, as needed.
Click Save.

---

## Using the Address Block in a Job Application Flow
*Chunk ID: OHR-REC-0324 | Chapter: Job Application Flows*

The Address block in the job application flow uses the address styles and address formats configured in the Setup and
Maintenance work area.
You define address styles using the Features by Country or Territory task, in the Setup and Maintenance work area.
You use this task to define whether the Postal Address or the Supplemental Taxation and Reporting Address style is
used for a given country. If the Human Resources extension is selected for a country, you can select any address style.
If you select the Payroll or Payroll Interface extension, the address style depends on the localization. For details, see the
document HCM Address Validation on My Oracle Support (ID: 2140848.1).
You define the address formats for countries using the Manage Address Formats task, in the Setup and Maintenance
work area. You use this task to define the address elements and their display sequence. If there are a few address
variations set for a country, the first variation is used.
Note: There's one exception where the display sequence isn't considered on career sites. The country field is always
at the top of the Address block.

---

## How it Works for Candidates
*Chunk ID: OHR-REC-0325 | Chapter: Job Application Flows*

The content of the Address block in a job application flow is dynamic. Address fields are rendered based on the Country
value selected in the block. Sometimes, the country is prepopulated for a candidate. If the candidate opted to use

---

## Job Application Flows
*Chunk ID: OHR-REC-0326 | Chapter: Job Application Flows*

their browser location, the country is filled based on that location. Otherwise, the country is filled based on the job
requisition's primary location.
If address elements are set as dependent LOVs, when candidates complete a form at any level, the higher levels are
automatically filled based on a candidate's selection. For example, if they select a zip code, the city and state is pre-filled
based on that zip code.
This block lets candidates select values in the location hierarchy drop-down lists in a flexible manner, and they can
navigate the hierarchy in both directions. For example, you can select a zip code, and the county and state information
is populated automatically.
For all LOVs in the address block, strings (keywords) are searched only at the beginning of a location name. For
example, if a candidate types "Gla" in the City field, the returned results include Glasgow but not Douglas. If they type
"Uni" the returned results include United States, but not Tunisia or Tanzania, United Republic of.
If the Address Line 1 field is part of an address form for a country, candidates can start typing an address in the field,
and Oracle Maps will suggest addresses to choose from. Once selected, the Address line 1 field is populated with the
street part of the selected address, and the other address fields are populated appropriately. Once selected, the other
address fields are populated.
Note: The address search feature allows users to search for address suggestions in the Address Line 1 field. To use it,
you might want to consider displaying this field at the top of the list.

---

## Note: When candidates manually type their address into Address Line 1 without selecting a suggestion from the
*Chunk ID: OHR-REC-0327 | Chapter: Job Application Flows*

list of values, it's saved exactly what they entered it. This is because Address Line 1 works as a regular text box and
accepts whatever is entered.

---

## Ensure that each geography field is correctly associated with the appropriate address element in the Manage Address
*Chunk ID: OHR-REC-0328 | Chapter: Job Application Flows*

Formats configuration task. This mapping allows to populate the correct values when address is selected.
For United Kingdom, the County geography field must be mapped to the State address element. This ensures that when
a user selects an address, the County value (such as Yorkshire or Devon) is automatically populated in the County field.
The Application Flow section displays in the site editor's General tab. It contains a checkbox that lets you control address
search. It's selected by default (the feature is enabled by default), but it can be disabled for a site.

---

## How do I configure the types of miscellaneous
*Chunk ID: OHR-REC-0329 | Chapter: Job Application Flows*

documents attached by candidates?
Use these two profile options to define the types of miscellaneous attachments candidates can upload when they apply
for a job:
• ORA_IRC_MISC_ATTACH_FILE_TYPES: Use this profile option to define the supported file types for
miscellaneous attachments. When you define the supported file types, you need to separate each value with
a comma and with a space. Candidates need to attach files of types you have defined. Otherwise, they see a
message informing them of the supported file formats.
• ORA_IRC_MISC_ATTACH_UNSUPPORTED_FILE_TYPES: Use this profile option to define unsupported file
types for the miscellaneous attachments. A list of unsupported file types is provided by default to guarantee

---

## Job Application Flows
*Chunk ID: OHR-REC-0330 | Chapter: Job Application Flows*

security. However, you can change this list. When you define the unsupported file types, you need to separate
each value with a comma, with or without a space. When candidates upload an attachment that isn't allowed,
a message is displayed indicating that the file type isn't supported. If you have configured the profile option
ORA_IRC_MISC_ATTACH_FILE_TYPES, a message indicates which types are supported.
The list of supported file types takes precedence over the list of unsupported file types. If a file type is in both lists, the
file type is supported.
Related Topics
• How do I enable a profile option?

---

## Configure Sections in Internal Job Application Flows
*Chunk ID: OHR-REC-0331 | Chapter: Job Application Flows*

You can configure which sections in internal job application flows are visible based on legal employer and recruiting
type.
You can show or hide these two sections:
• E-signature
• Supporting Documents
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Apply to Internal Jobs.
5. Click Add to create and configure a rule to display certain sections.
6. In the Basic Details section, enter a name and description. You can select a legal employer and a recruiting type to
base the visibility of the sections.
7. In the Show or Hide Regions section, indicate if the Supporting Documents and E-Signature sections are visible or
not.
8. Click Save and Close.

---

## Configure Inline Assessments in Internal Job Application
*Chunk ID: OHR-REC-0332 | Chapter: Job Application Flows*

Flows
You set up inline assessments so that internal candidates can fill assessments before they submit their job applications.
When the assessment is completed and is successful, the partner returns the status Completed by Candidate to the
Recruiting product. Assessment results are visible to recruiters once the job application is submitted.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.

---

## Job Application Flows
*Chunk ID: OHR-REC-0333 | Chapter: Job Application Flows*

3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Apply to Internal Jobs.
5. Click Add to create a rule.
6. In the Basic Details section, enter a name and description for the rule. You can select a legal employer and a
recruiting type to base the visibility of the application flow sections.
7. In the Show or Hide Regions section, set the Assessments region to Visible.
8. Click Save and Close.

---

# Candidate Selection Processes

## Candidate Selection Processes
*Chunk ID: OHR-REC-0334 | Chapter: Candidate Selection Processes*

Candidate Selection Process
A candidate selection process provides the framework to move candidates through the hiring process to evaluate and
find the best candidates for a job.
When candidates apply for a job, the candidate selection process tracks and manages candidates from the time
their job application is confirmed to the time that they're hired. An analogy can be drawn between the candidate
selection process and moving candidate resumes from one pile to another as the selection progresses and the number
of resumes retained is reduced. For example, a candidate job application is analyzed, the candidate is contacted,
interviewed, then hired.
When recruiters create or edit a job requisition, they can select a candidate selection process that matches the job
requisition context (locations, organization, job family, job function, recruiting type).

---

## Candidate Selection Process Template
*Chunk ID: OHR-REC-0335 | Chapter: Candidate Selection Processes*

Two candidate selection processes are available to get you started.
• Candidate Selection Process Template (CSP-TEMPLATE): This process can't be made active and used to hire
candidates. You can however duplicate it to create your own candidate selection process. This process contains
pre-defined phases and states.
• Default Candidate Selection Process (CSP-DEFAULT): This process is a copy of the candidate selection process
template. It contains the same pre-defined phases and states. This process is provided so that there is an active
process in new environments. You can't make many modifications to this process because it's already active.
You can use the process to hire candidates. You can also make it inactive if you want to use your own processes
instead.

---

## Candidate Selection Process Phases and States
*Chunk ID: OHR-REC-0336 | Chapter: Candidate Selection Processes*

A candidate selection process is made of multiple phases, and each phase is made of multiple states. For details, see
What are the phases and states of a candidate selection process?

---

## Modify the Name of Default Phases and States
*Chunk ID: OHR-REC-0337 | Chapter: Candidate Selection Processes*

You can change the name of the phases and states included by default in a candidate selection process.
You can change the name in all languages and regardless of the candidate selection process status (Draft, Active,
Inactive). The new name will be used immediately in all product areas showing the names. For example, when
displaying the current phase and state of a job application or when displaying the previous and upcoming phases and

states in the progress tab of a job application. Changing the name of a phase or state will also automatically update the
name in all other candidate selection processes where this phase or state is used.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, create a process or select an existing one.
3. To change the name of a default phase, select a phase then click the Translation Editor icon. Enter a name and click
Save and Close.
4. To change the name of a default state, click the Translation Editor icon next to a state. Enter a name and click Save
and Close.
Note: The translation editor isn't displayed for environments with a single language. It won't be possible to change
the names.

---

## Candidate Selection Process Actions
*Chunk ID: OHR-REC-0338 | Chapter: Candidate Selection Processes*

You can add the following actions to phases and states of a candidate selection process.

---

## Use this action to initiate a background check on candidates when the screening service is configured
*Chunk ID: OHR-REC-0339 | Chapter: Candidate Selection Processes*

on a job requisition. For details, see Use the Background Check Action for Job Applications.

Move

---

## Use this action to send a request to tax credit partners to invite candidates to complete forms to
*Chunk ID: OHR-REC-0340 | Chapter: Candidate Selection Processes*

validate their tax credit eligibility. For details, see Use the Request Tax Credit Screening Action for Job
Applications.

---

## Use this action to send an interview invitation automatically to candidates when their job applications
*Chunk ID: OHR-REC-0341 | Chapter: Candidate Selection Processes*

reach a given point in the candidate selection process. For details, see Configure the Candidate
Selection Process to Automatically Send Interview Invitations.

---

## Use this action to send different types of notifications. You can add the Send Notification action to a
*Chunk ID: OHR-REC-0342 | Chapter: Candidate Selection Processes*

state to send notifications to recruiters and hiring managers. You can also add the Send Notification
action to a phase or state to send generic notifications to other user types such as the hiring team,
candidates, agents. Candidate notifications are created in the Recruiting Content Library. Review
notifications sent to recruiters and hiring managers are created in the Alerts Composer tool. For details,
see Use the Send Notification Action for Job Applications.

---

## Send Tax Credit Hiring Confirmation
*Chunk ID: OHR-REC-0343 | Chapter: Candidate Selection Processes*

Use this action to send a notification to tax credit partners to inform them that a candidate was hired.

---

## Create a Candidate Selection Process
*Chunk ID: OHR-REC-0344 | Chapter: Candidate Selection Processes*

You create a candidate selection process to move candidates through the hiring process, evaluate candidates, and find
the best candidates for a job.
You can create multiple active candidate selection processes to adapt the selection process to your business needs.
For example, your organization might want to use a short and simple process but also use a lengthier process with
multiple phases. You can also configure candidate selection processes for different contexts (locations, organizations,
job families, job functions, recruiting types).
Note: As a best practice, complete the configuration of the candidate selection process before using it in requisitions
to avoid affecting existing job applications.

Here's what to do
1.
2.
3.
4.
5.
6.
7.

---

## Initiate the Creation Process
*Chunk ID: OHR-REC-0345 | Chapter: Candidate Selection Processes*

Create Phases and States
Configure Phases
Add Actions
Add Move Conditions
Add Reason Groups
Activate the Process

---

## Initiate the Creation Process
*Chunk ID: OHR-REC-0346 | Chapter: Candidate Selection Processes*

You start the creation process by defining properties such as the process type, name, code, and description of the
process.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, click Create.
3. On the Create Process page, select the process type:

◦ Standard: Used for standard job requisitions.
◦ Pipeline: Used for pipeline job requisitions. Contrary to the standard candidate selection process, the
Offer and HR phases aren't included in a pipeline process because no hiring occurs.

---

## Candidate Selection Processes
*Chunk ID: OHR-REC-0347 | Chapter: Candidate Selection Processes*

4. Enter a name, code, and description.
5. Click Save and Continue.
When you're done, the details page of the candidate selection process is displayed. You can click the Edit Process
Properties button to modify the information you just entered or to define the context when the process is used. If you
set a recruiting type as the default, the selection process will be automatically selected for job requisitions created for
this recruiting type.

---

## Create Phases and States
*Chunk ID: OHR-REC-0348 | Chapter: Candidate Selection Processes*

A candidate selection process is made of multiple phases, and each phase is made of multiple states.
All candidate selection processes include these two required phases. You can't remove these phases and you can't edit
the states within these two phases.
• Offer
• HR
The HR phase must be the last phase of the candidate selection process.
You can add phases between the Offer phase and the HR phase to allow users to temporarily put job applications that
have an accepted offer but that aren't yet ready to be transferred to HR because tasks, such as background checks, are
required. When you add a phase after the Offer phase, there is no longer any built-in progression for job applications
reaching the Offer - Accepted status. Users can create an automatic progression into HR, or they can manually progress
job applications into the phase.
Each phase contains these two required states. You can't remove these states and they must be the last two states of a
phase.
• Rejected by Employer
• Withdrawn by Candidate
To create a phase and add states to the phase:
1.
2.
3.
4.

Click Create to create a new phase.
Enter a name and description for the phase.
Click Create in the States section to add a state to the phase.
Enter a name for the state. When you type the name of the new state, a list of existing state names is suggested
to facilitate the reuse of existing names across processes.
5. Click Save and Close.

---

## You can change the order of phases using the Move Right and Move Left buttons in the process details page. You can
*Chunk ID: OHR-REC-0349 | Chapter: Candidate Selection Processes*

also change the order of states within a phase using the up and down arrows.
Note: If your environment only has one language activated, the translation editor isn't available.

---

## Configure Phases
*Chunk ID: OHR-REC-0350 | Chapter: Candidate Selection Processes*

You can configure a phase as being required. When a phase is required, users are required to move job applications
to mandatory phases before moving them further in the selection process. The Offer phase and HR phase
are always required. Users who have the privilege Move Candidate Job Applications Ignoring Constraints
(IRC_MOVE_CANDIDATE_JOB_APPLICATION_SKIPPING_MANDATORY_PHASES) can move job applications over
mandatory phases.

---

## You can configure a phase as being restricted. When a phase is restricted, it prevents users from viewing and managing
*Chunk ID: OHR-REC-0351 | Chapter: Candidate Selection Processes*

job applications in some phases of the candidate selection process. If you do that, unconfirmed job applications are
considered restricted. If there's no restricted phase, unconfirmed job applications are considered unrestricted. By
default, all phases are set to unrestricted. You can only set a phase as being restricted if:
• It's the first phase of the process.
• It's a phase following a restricted phase.
The Offer phase, HR phase, and any phases between the Offer and HR phases can't be set as
restricted. Users who have the aggregate privilege View Non-Restricted Candidate Job Application
(ORA_IRC_VIEW_NON_RESTRICTED_CANDIDATE_JOB_APPLICATION) can't view job applications on restricted phases.

---

## Add Actions
*Chunk ID: OHR-REC-0352 | Chapter: Candidate Selection Processes*

You can add actions to phases and states.
• For phases, you can add actions to be performed on specific events of a phase. Actions configured on phase
events are performed when the given event is triggered while job applications are within this phase (and if the
condition defined on the action is met). For details, see How to Automate the Candidate Selection Process.
• For states, the actions are automatically performed when candidate job applications are entering the state (and
if the condition defined on the action is met). If a job application is already on the state and the condition is
later met, the action won't be performed because the action is only performed when job applications enter the
state.
When you have two or more actions on an event or state, a Reorder Actions option becomes available in the Actions
menu. When you select that action, the Reorder Actions page is displayed and you can reorder the actions in a defined
order. You can reorder actions regardless of the status of the candidate selection process. Note that when the Move
or Move to HR action is performed on a state or event (and the condition is met for the move actions), the remaining
actions (placed after the move actions) won't be performed because job applications are no longer on this state or
event.
Some actions put at the very beginning of a candidate selection process used for candidates applying through an
external career site are performed after a small delay so that the creation of job applications is fully completed before
performing the actions. The actions are put in a queue. When the scheduled process Perform Recruiting Candidate
Selection Process Actions is run, the actions are performed. This delay applies to actions configured in the initial phase
and initial state of job applications of external candidates, except the Move and Move the HR actions. For details, see

---

## Add Move Conditions
*Chunk ID: OHR-REC-0353 | Chapter: Candidate Selection Processes*

You can add move conditions to specific states of a candidate selection process. Move conditions prevent job
applications from being moved out of a current state. All conditions must be met for a job application to move out of the
current state. This applies to users trying to move job applications manually and to the automated candidate selection
process actions trying to move job applications. Note that users with the privilege Move Candidate Job Applications
Ignoring Constraints (IRC_MOVE_CANDIDATE_JOB_APPLICATION_SKIPPING_MANDATORY_PHASES) can move job
applications even if the condition isn't met.
When you define move conditions, you can add predefined conditions, fast formulas used as conditions, or a
combination of both. You can define a move condition regardless of the status of the candidate selection process that is
draft, active, inactive. For details, see Define Conditions to Move Candidates.

---

## Add Reason Groups
*Chunk ID: OHR-REC-0354 | Chapter: Candidate Selection Processes*

You can add reason groups to a specific state to gather meaningful information about why a job application was
rejected or withdrawn for a job requisition. When you set a reason group on a state, users moving a job application to
this state will be able to select a reason from the reason group. For details, see Define Reasons to Reject and Withdraw
Job Applications.

---

## Activate the Process
*Chunk ID: OHR-REC-0355 | Chapter: Candidate Selection Processes*

When the candidate selection process is ready, you activate it so it can be used in job requisitions.
1. On the candidate selection process page, click the Edit Process Properties button.
2. In the Status field, select Active.
3. Click Save and Close.

---

## Define Quick Move on the Candidate Selection Process
*Chunk ID: OHR-REC-0356 | Chapter: Candidate Selection Processes*

States
You can define the expected move destination of a state in a candidate selection process.
For each candidate selection process, you can configure a quick move to be used on job applications. Note that if no
quick move destination is configured on a state, it's considered as a quick move to the next active state, without asking
for comments. The next active state is the next active state in the sequence of states configured in the phase. This
excludes the Rejected by Employer and Withdrawn by Candidates states. If the job application is already on the last
active state of a phase, the first active state of the following phase is considered the next active state.
When you're defining the destination of the quick move, only valid phases and states are available for selection. This
means:
• Any non-terminal state of the current phase.
• Any non-terminal state of an upcoming phase.
◦ You can select a state of an upcoming phase, even if it means bypassing a mandatory phase. With such
a configuration, recruiting users who can't bypass required phases won't be able to use the Quick Move
action.
• The first state of the Offer phase (Offer - To be Created)
The quick move feature isn’t available for these states:
• Terminal states of all phases:
◦ Withdrawn by Candidate

◦ Rejected by Employer

• Some states of the Offer phase:
◦ Offer - To be Created

◦ Offer - Draft
◦ Offer - Pending Approval
◦ Offer - Approval Rejected

---

## Candidate Selection Processes
*Chunk ID: OHR-REC-0357 | Chapter: Candidate Selection Processes*

◦ Offer - Approved
◦ Offer - Extended
• All states of the HR phase
You can change the quick move configuration of a candidate selection process regardless of the state of the candidate
selection process (Draft, Active, Inactive).
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, create a process or select an existing one.
3. Click a phase.
4. In the States for Phase section, click the Quick Move menu, then select Define Destination.
5. On the Quick Move page, select the phase and state where the candidate will be moved.
If you select Ask for Comments, the recruiting user performing a quick move can provide comments before moving
the job application. If you select Don't Ask for Comments, the recruiting user performing a quick move will see the
job application being moved immediately, without more information being requested.
6. You can indicate if comments must be requested.
If you select Ask for Comments, the recruiting user performing a quick move will have the opportunity to provide
comments before moving the job application. If you select Don't Ask for Comments, the recruiting user performing
a quick move will see the job application being moved immediately, without more information being requested.
7. Click Save and Close.
What to do next
You can define if the Quick Move and Quick Reject actions are used in the candidate selection process and available to
recruiting users.
1.
2.
3.
4.
5.

Open an existing candidate selection process.
Click Edit Process Properties.
On the Process Properties page, scroll to the Configuration section.
Set the Quick Move and Quick Reject actions to Show Action or Don't Show Action.
Click Save and Close.

---

## Note: When you configure an active candidate selection process, to add a quick move destination on a state where
*Chunk ID: OHR-REC-0358 | Chapter: Candidate Selection Processes*

none was previously set, the quick move destination defined for a state isn`t known by job applications that are
already in the phase where this change was made. As a result, when a recruiting user clicks the Move Forward button
on these job applications, the job applications will move to the next state in the sequence of states configured in
the phase (as if no destination was configured on the state). If a candidate selection process doesn't have a quick
move destination for a state and you add one later, existing job applications that are already in this phase won't
be impacted. The job applications will move to the next state. If a candidate selection process has a quick move
destination defined for a state and you change the destination, existing job applications will use the new destination
when the recruiting user clicks the Move Forward button. Note that this is only for existing job applications that are
already in the phase where the configuration is changed. Job applications which are created after the configuration
change and job applications which are later moved to the phase will use the new destination.

---

## How to Automate the Candidate Selection Process
*Chunk ID: OHR-REC-0359 | Chapter: Candidate Selection Processes*

You can automate the candidate selection process to facilitate the selection of candidates by recruiters and hiring
managers.
You can set up a candidate selection process to:
• Move Job Applications Automatically
• Define Conditions for Actions to be Performed Automatically
• Add Actions on Events to be Performed Automatically

---

## Move Job Applications Automatically
*Chunk ID: OHR-REC-0360 | Chapter: Candidate Selection Processes*

When you configure a candidate selection process, you can add the Move action on a phase or state so that job
applications are automatically moved to that phase or state.
Here are exceptions where you can't use the Move action:
• The Rejected by Employer state of all phases.
• The Withdrawn by Candidate state of all phases.
• All states of the Offer phase, except the Accepted state. You can add the Move action on the Offer - Accepted
status only if you have custom phases after the Offer phase (the Move action can't be used to move to the HR
phase).
If you configure multiple move actions on the same event or state, the processing of automated actions will stop once
a move action is performed (condition on the action is met and action is performed). If an action needs to be triggered
independently from the move action, you need to place it before the move in the list of actions, or place it on the
destination state of the move.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration

2. On the Candidate Selection Process Configuration page, create a selection process or select an existing one.
3. Click a phase.
4. In the States for Phase section, click the Actions menu next to a state, then select Add Action > Move.
5. On the Action: Move page, select the phase and state where job applications will be automatically moved.
6. Click Continue.
7. Click Save and Close.
Results:
When a candidate job application is automatically moved to a phase or state, the current phase and state where
the action is triggered is considered as being visited and that information is displayed in the progress history. For
example, if the Move action is configured on New - Reviewed to automatically move to Screening - Phone Screen to Be

---

## Candidate Selection Processes
*Chunk ID: OHR-REC-0361 | Chapter: Candidate Selection Processes*

Scheduled, the progress history indicates that New - Reviewed was visited and that the current status is now Screening Phone Screen to Be Scheduled.

---

## Define Conditions for Actions to be Performed
*Chunk ID: OHR-REC-0362 | Chapter: Candidate Selection Processes*

Automatically
You can configure actions to be performed automatically as candidate job applications progress in the selection process,
but only if specific conditions are met.
You can use predefined conditions, fast formulas used as conditions, or a combination of both. You can define multiple
conditions for the same action, but all conditions must be met for the action to be performed. Here are the predefined
conditions you can select:
• All requested interview feedback is received
• An initiated assessment is in error
• An initiated background check is in error
• Initiated assessments are complete
• Initiated assessments are complete, candidate failed some
• Initiated assessments are complete, candidate passed all
• Initiated background checks are complete
• The job application is external
• The job application is internal
Note: The conditions of type "is in error" are used to indicate that the partner returned an error, and not that there is
a configuration error. Only results from the partner will trigger a candidate selection process action.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration

2. On the Candidate Selection Process Configuration page, create a selection process or select an existing one.
3. Click on a phase.
4. In the States for Phase section, click the Actions menu next to a state, then select Add Action > Move.
5. On the Action: Move page, select the phase where job applications will be automatically moved.
6. Click Continue.
7. On the Action: Move page, select conditions:
◦ Click Add Predefined to select predefined conditions.

◦ Click Add Fast Formulas to select fast formulas used as conditions.

8. Enter a name for the move action.
9. Set the status to Active.
10. Click Save and Close.

---

## Add Actions on Events to be Performed Automatically
*Chunk ID: OHR-REC-0363 | Chapter: Candidate Selection Processes*

You can add actions to be performed on specific events of a phase. Actions configured on phase events are performed
when the given event is triggered while job applications are within this phase (and if the condition defined on the action
is met).
Available events are:
• Assessment Updated: This event is triggered when an assessment is updated.
• Background Check Updated: This event is triggered when a background check is updated.
• Interview Feedback Received: This event is triggered every time an interview feedback is received.
• Interview Updated: This event is triggered when a change is made to an interview while the job application
is within the phase where the event is used. This event is triggered when an interview is scheduled, updated,
canceled, completed, requested.
• Request for Information Updated: This event is triggered when a request for information is updated.
• Tax Credit Request Updated: This event is triggered when a tax credit request is updated.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, create a selection process or select an existing one.
3. Click a phase.
4. In the Phase Actions section, select an event in the Add Event field.
5. On the Action: Move page, select the phase where job applications will be automatically moved.
6. Click Continue.
7. On the Action: Move page, select conditions:
◦ Click Add Predefined to select predefined conditions.

◦ Click Add Fast Formulas to select fast formulas used as conditions.
8. Enter a name for the move action.
9. Set the status to Active.
10. Click Save and Close.

---

## Delayed Processing of Automated Actions at Beginning
*Chunk ID: OHR-REC-0364 | Chapter: Candidate Selection Processes*

of a Candidate Selection Process
Some automated actions put at the beginning of a candidate selection process used for candidates applying through
an external career site are performed after a small delay. As a result, the creation of job applications is fully completed
before performing the actions.

---

## The actions are put in a queue. When the scheduled process Perform Recruiting Candidate Selection Process Actions is
*Chunk ID: OHR-REC-0365 | Chapter: Candidate Selection Processes*

run, the actions are performed.
This delay applies to actions configured in the initial phase and initial state of job applications of external candidates,
except the Move and Move the HR actions.

---

## Define Conditions to Move Candidates
*Chunk ID: OHR-REC-0366 | Chapter: Candidate Selection Processes*

You can define conditions that must be met for job applications to be allowed to leave a state in a candidate selection
process. When you define a move condition, recruiters can't move a job application in the selection process if the
condition isn't met.
You can use predefined conditions, fast formulas used as conditions, or a combination of both. You can define a move
condition regardless of the status of the candidate selection process (draft, active, or inactive).
Note: The move conditions prevent users from manually moving job applications. When moving job applications
automatically using actions in the candidate selection process, move conditions aren't considered.

Note: The move conditions prevent a candidate from withdrawing their job application if the condition isn't met.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration

2. On the Candidate Selection Process Configuration page, create a selection process or select an existing one.
3. Click a phase.
4. In the States for Phase section, click the Move Condition menu next to a state and select Define Condition.
5. On the Move Conditions page, select conditions.
◦ Click Add Predefined to select predefined conditions.

◦ Click Add Fast Formulas to select fast formulas used as conditions.

6. Click Save and Close.
Related Topics
• Fast Formulas for Candidate Selection Processes
• How to Automate the Candidate Selection Process

---

## Trigger Automated Actions Based on Request for
*Chunk ID: OHR-REC-0367 | Chapter: Candidate Selection Processes*

Information Status
Actions can be performed automatically on job applications based on the status of a request for information.

---

## Job applications are automatically progressed forward in the candidate selection process when candidates have
*Chunk ID: OHR-REC-0368 | Chapter: Candidate Selection Processes*

provided the requested information.
Here's what to do
• Create Fast Formula Conditions
• Configure the Candidate Selection Process

---

## Create Fast Formula Conditions
*Chunk ID: OHR-REC-0369 | Chapter: Candidate Selection Processes*

Use these database items to create fast formula conditions based on the request for information status.
• IRC_CSP_REQUEST_INFO_APPFLOW_CODE: Application flow used for the request for information (Code).
• IRC_CSP_REQUEST_INFO_APPFLOW_VERSION_NAME: Application flow used for the request for information
(Version Name).
• IRC_CSP_REQUEST_INFO_STATUS_CODE: Status of the request for information (Code).
These three statuses are available for requests for information:
• ORA_TRIGGERED - Triggered: The request for information was sent and you're waiting for the candidate's
response.
• ORA_SUBMITTED - Submitted: The candidate provided the requested information.
• ORA_NOT_REQUIRED - Not Required: The request information action was triggered, but no additional
information needs to be requested to the candidate. All the information in the request information flow was
already provided by the candidate.

---

## Configure the Candidate Selection Process
*Chunk ID: OHR-REC-0370 | Chapter: Candidate Selection Processes*

You can configure the candidate selection process to trigger automated actions based on the status of a previous
Request Information action.
Let's say that you want to add the Request Information action and use a fast formula as a condition for when a
candidate provided the requested information. Once the condition is met (the candidate provided the required
information), the candidate is automatically moved to the next phase and state.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2.
3.
4.
5.
6.
7.
8.

Create a new candidate selection process or update an existing one.
Click a phase.
In the Phase: Actions section, add the event Request for Information Updated.
Click the actions menu next to the Request for Information Updated event, then select Add Action > Move.
On the Action: Move page, select the phase and state where the candidate will be moved.
Click Continue.
Click Add Fast Formula and add the fast formula condition with the submitted status which indicates that the
candidate provided the requested information.
9. Click Save and Close.

Related Topics
• Overview of Recruiting Fast Formulas

---

## Progress Job Applications Without Sending Notifications
*Chunk ID: OHR-REC-0371 | Chapter: Candidate Selection Processes*

to Candidates
You can configure candidate selection processes so that job applications are progressed through the candidate selection
process without notifications being sent to the candidates.
You can configure an option in the candidate selection process to not send candidate notifications. Notifications used in
the context of a job application (related to a specific job application) aren’t sent if all the following conditions are met:
• The job application is on a requisition for which the candidate selection process is configured to not send
notifications to candidates.
• The notification is sent using a Recruiting Content Library category which is identified to send a notification
according to the setting in the candidate selection process configuration.
Note: Notifications which aren’t in the context of a job application (not related to a specific job application but related
to the candidate) are sent as usual.
This table presents Recruiting Content Library categories related to job application notifications sent to candidates.

---

## All interview-related
*Chunk ID: OHR-REC-0372 | Chapter: Candidate Selection Processes*

notifications:

Comment

Yes

• Interview Canceled
Notification
• Interview Reminder
Notification
• Interview Reschedule
Notification
• Interview Scheduled
Notification
• Interview Updated
Notification
• Invite to Schedule
Interview Notification

---

## Category used for the Request
*Chunk ID: OHR-REC-0373 | Chapter: Candidate Selection Processes*

Information action, for the
automated and manual
actions.

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, create a selection process or select an existing one.
3. Click the Edit Process Properties button.
4. On the Process Properties page, in the Configuration section, select a value in the Notifications to Candidates field:
◦ Send Notifications (default value)

◦ Don’t Send Notifications
5. Click Save and Close.

---

## Edit Actions in an Active Candidate Selection Process
*Chunk ID: OHR-REC-0374 | Chapter: Candidate Selection Processes*

You can edit actions in active candidate selection processes. When you edit the actions of an active or inactive
candidate selection process, a warning message appears to inform you that these changes might impact existing job
requisitions and job applications.
Here's what you can do:
• Add events to a phase.
• Add actions on events and states.
• Edit actions on events and states.
• Deactivate actions on events and states. The configuration of the action is preserved, but the action is never
performed.
• Reactivate actions on events and states. The action will be performed as usual.
When you modify actions of a candidate selection process used by job applications, the changes are immediately
available on these job applications. For example, if you add an action to an event, the action is triggered the next time
the event occurs if the conditions for performing the action are met.
When you modify actions of a candidate selection process that generates additional configuration on job requisitions,
the configuration of the job requisition or requisition template using this process is updated accordingly. This applies to
these actions:
• Send Interview Invite
• Initiate Background Check
• Request Assessment
• Request Tax Credit Screening
When a job requisition uses a candidate selection process with deactivated actions, these actions are still visible on the
job requisition configuration, but there is an indication that they're deactivated.
For actions that are waiting to receive information from a partner (for example, Initiate Background Check), a user, or
candidate (for example, Request Information), the information will be accepted even if the corresponding action has
been deactivated. The fact that the action is deactivated only impacts its triggering, not the reception of information
later on.

---

## Use the Background Check Action for Job Applications
*Chunk ID: OHR-REC-0375 | Chapter: Candidate Selection Processes*

You can configure the candidate selection process so that a background check is initiated when a job application
reaches a specific state in the candidate selection process.
Background checks are run on candidates as part of their candidate selection process to ensure their background is
verified before hiring them.
Before you start
The background check partner must be enabled.
Here's what to do

---

## Candidate Selection Processes
*Chunk ID: OHR-REC-0376 | Chapter: Candidate Selection Processes*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, click a process.
3. Click a phase.
4. Add the Initiate Background Check action at the state level.
The action is triggered when job applications are moved to the specified state.
5. You can define conditions for the action to be executed. You can use predefined conditions, fast formulas used as
conditions, or a combination of both.
6. Click Save and Close.
Related Topics
• How to Automate the Candidate Selection Process

---

## Use the Request Assessment Action for Job Applications
*Chunk ID: OHR-REC-0377 | Chapter: Candidate Selection Processes*

You can configure the candidate selection process so that an assessment is initiated when a job application reaches a
specific state in the candidate selection process.
Assessments are used to assess and measure the knowledge, skills, abilities, and attributes of candidates for a job.
Before you start
The assessment partner must be enabled.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, click a process.
3. Click a phase.
4. Add the Request Assessment action at the state level. The action is triggered when job applications are moved to
the specified state.
5. You can define conditions for the action to be executed. You can use predefined conditions, fast formulas used as
conditions, or a combination of both.
6. Click Save and Close.
Related Topics
• How to Automate the Candidate Selection Process

---

## Use the Request Tax Credit Screening Action for Job
*Chunk ID: OHR-REC-0378 | Chapter: Candidate Selection Processes*

Applications
You can configure a candidate selection process so that a tax credit screening action is initiated when a job application
enters or exits a phase of the candidate selection process, or is moved to a specific state within a phase.
You use tax credit screenings to validate tax credit eligibility of candidates. Candidates can be eligible to various federal,
state, and other tax credits.
Before you start
The tax credit partner must be enabled.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, click a process.
3. Click a phase.
4. Add the Request Tax Credit Screening action at the phase or state level.
◦ At the phase level, you can trigger the action when job applications enter or exit a phase.

◦ At the state level, you can trigger the action when job applications are moved to the specified state.
5. You can define conditions for the action to be performed. You can use predefined conditions, fast formulas used as
conditions, or a combination of both.
6. Click Save and Close.
Related Topics
• How to Automate the Candidate Selection Process

---

## Use the Send Notification Action for Job Applications
*Chunk ID: OHR-REC-0379 | Chapter: Candidate Selection Processes*

You can configure the candidate selection process so that notifications are sent automatically when candidate job
applications are moved through the candidate selection process.
Notifications can be sent automatically to candidates, recruiters, hiring managers, hiring team members, and recruiting
agents. Candidates receive emails and are kept informed of their progress. Recruiting users can view notifications that
were sent and the content of those notifications in the Interactions tab of job applications.
Automated notifications are available in the Recruiting Content Library. You can personalize them as needed.

---

## Candidate Selection Processes
*Chunk ID: OHR-REC-0380 | Chapter: Candidate Selection Processes*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, click a process.
3. Click a phase.
4. In the States for Phase section, click the Actions menu next to a state, select Add Action, then Send Notification.
Note: The Send Notification action isn't working when the Move action is defined for the same state.
5. On the Action: Send Notification page, you can configure the following notifications:
a. Recruiter and Hiring Manager Notifications: Select the members of the job requisition's hiring team who
will be sent job application review notifications when job applications reach this state in the candidate
selection process. The notification contains a link to the list of job applications in the phase or state where
the action is configured.
b. Automated Notifications - Hiring Team Notifications: Select the notification that's sent to the recruiter,
hiring manager, and collaborators as job applications are moved through the candidate selection process.
c. Automated Notifications - Agent Notifications: Select the notification that's sent to the recruiting agent
as job applications are moved through the candidate selection process. You can set a delay so that the
notification is sent at a specified time after the job application has been moved.
d. Automated Notifications - Candidate Notifications: Select the notification that's sent to internal candidates
and external candidates. You can set a delay delivery so that the notification is sent at a specified time after
the job application has been moved.
6. Click Save and Close.
Related Topics
• Recruiting Content Library
• Configure Automated Job Application Notifications

---

## Automatically Initiate a Candidate Duplicate Check
*Chunk ID: OHR-REC-0381 | Chapter: Candidate Selection Processes*

You can configure the candidate selection process to automatically initiate a candidate duplicate check.
You can configure the duplicate check at multiple points in the candidate selection process. When a job application
reaches a specific state in a phase, the candidate duplicate check is automatically triggered. The recruiter or designated
members of the Hiring Team are informed of duplicate check results. They receive a notification about the candidate
and the number of duplicates found. They can click a link to see the duplicates. Candidates can be automatically
progressed in the selection process based on duplicate check results.
Before you start
Users need these privileges to click the link in the Automated Duplicate Check Notification to see the duplicates:
• Access to Hiring as Manager (IRC_ACCESS_TO_HIRING_AS_MANAGER) or Access to Hiring as Recruiter
(IRC_ACCESS_TO_HIRING_AS_RECRUITER)
• Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE)

---

## Candidate Selection Processes
*Chunk ID: OHR-REC-0382 | Chapter: Candidate Selection Processes*

Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration

2. On the Candidate Selection Process Configuration page, click a process.
3. On the process page, click a phase.
4. In the States for Phase section, select a state, then select the Initiate Candidate Duplicate Check action in the
Actions menu. The action is triggered when job applications are moved to the specified state.
5. You can select members of the hiring team who will receive candidate duplicate check results such as the recruiter,
hiring manager, or other designated members.
6. You can select an email notification template. A notification template is available in the Recruiting Content Library:
Automated Duplicate Check Notification. The notification contains info about the candidate and the number of
duplicates found. The recipient can click a link to see the duplicates.
7. You can set the threshold "Minimum Match Score to Send Notification" for receiving a notification. The notification
will be sent to the recipients only when the duplicate check match score is equal to or greater then the set threshold.
8. Click Save and Close.

---

## Add or Remove Candidate Labels While Configuring the
*Chunk ID: OHR-REC-0383 | Chapter: Candidate Selection Processes*

Candidate Selection Process
You can automatically assign labels to candidates or remove them by using the Add or Remove Candidate Labels action
while configuring the candidate selection process. When job applications navigate through different states and phases,
labels are automatically added or removed.
You can add the Add or Remove Candidate Labels action:
• To a phase, when entering a phase.
• To a phase, when leaving a phase.
• To a specific state.
When the candidate reaches the selected phase or state, the selected label is automatically assigned to the candidate if
it doesn’t already exist, or it’s removed.
Let’s say you want to add the Premium Candidate label when top candidates leave the Interview and Selection phase.
Before you start
You first need to create labels to tag candidates. For details, see Create Labels to Tag Candidates. If a label is removed
from the Manage Recruiting Labels configuration page, the label is also removed from the Add or Remove Candidate
Labels selector.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications

---

## Candidate Selection Processes
*Chunk ID: OHR-REC-0384 | Chapter: Candidate Selection Processes*

◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, create a candidate selection process or edit an existing one.
3. Click the Interview and Selection phase.
4. In the Phase Actions section, click When Leaving Phase > Add Action > Add or Remove Candidate Labels.
5. On the Action: Add or Remove Candidate Labels page, in the Labels to Add section, add the label Premium
Candidate.
6. Click Continue.

---

## Reasons to Reject and Withdraw Job Applications
*Chunk ID: OHR-REC-0385 | Chapter: Candidate Selection Processes*

Reasons are used to gather meaningful information about why a job application was rejected or withdrawn for a job
requisition.
Your organization may want to know, for example, why candidates are declining job offers, why candidates are
withdrawing their job application, or why candidates are being rejected from the hiring process. That information helps
organizations improve their sourcing and hiring processes and also respond to audits about why a candidate was
rejected. Those reasons are displayed to recruiters in the progress panel of job applications.
Default reasons are available within the product. When job applications are automatically moved to the Rejected by
Employer or Withdrawn by Candidate state of any phase of a candidate selection process, a reason is automatically
selected. Here is the list of default reasons. You can change the name of these default reasons.
• The job requisition was filled.
• The job requisition was canceled.
• The candidate was hired on another job requisition.
• Candidate declined job offer.
• Work relationship was canceled.
• Candidate withdrew job application.
• The job application was disqualified.
You can also create your own reasons to identify why a job application was rejected or withdrawn.

---

## Define Reasons to Reject and Withdraw Job Applications
*Chunk ID: OHR-REC-0386 | Chapter: Candidate Selection Processes*

Reasons are used to gather meaningful information about why a recruiter rejected or withdrawn a job application for a
job requisition. Reasons can also be used for when candidates withdraw themselves by declining a job offer.
Default reasons are available within the product. But you can define your own reasons to identify why a job application
was rejected or withdrawn, or why a candidate declined a job offer. You can also define reason groups that are assigned
to various states of the selection process. For example, when a recruiter moves a job application to a state for which a
reason group was selected, the recruiter can select a reason for which the move is taking place.

---

## Note: If you want candidates to be able to choose reasons to decline job offers, you also need to enable a setting in
*Chunk ID: OHR-REC-0387 | Chapter: Candidate Selection Processes*

the candidate selection process and configure a notification in the Alerts Composer.

---

## Define a Reason
*Chunk ID: OHR-REC-0388 | Chapter: Candidate Selection Processes*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Reasons
2.
3.
4.
5.
6.

Click the Reasons tab.
Click Create.
Enter a name and a code.
Select the Active status. A reason must be active to be added to a group.
Click Save and Close.

---

## Define a Group of Reasons
*Chunk ID: OHR-REC-0389 | Chapter: Candidate Selection Processes*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Reasons
2.
3.
4.
5.
6.
7.
8.

Click the Groups tab.
Click Create.
Enter a name and a code.
Click Add to add an existing reason.
Click Create to create a new reason.
Set the status to Active
Click Save and Close.

Related Topics
• Define Reasons to Decline Job Offers

---

## Define the Scope of Candidate Selection Processes Being
*Chunk ID: OHR-REC-0390 | Chapter: Candidate Selection Processes*

Exported
When you want to export setup data for candidate selections processes, you can define the scope of which candidate
selection processes you want to export. You can select all candidate selection processes but you can also select specific
ones.
Exporting only specific candidate selection processes makes it easier to export only the processes you need to import in
another environment.

---

# Recruiting Content Library

## Candidate Selection Processes
*Chunk ID: OHR-REC-0391 | Chapter: Recruiting Content Library*

1. In the Setup and Maintenance work area, go to:
a. Offering: Recruiting and Candidate Experience
b. Functional Area: Candidate Job Applications
2. Click the Actions menu next to Candidate Job Applications and select Export or Export to CSV File > Create New.
3. On the Export Setup Data to CSV File page, go to the Business Objects section.
4. In Search field, enter Candidate Selection Process and click the Search icon.
5. In the Candidate Selection Process: Scope section, click Add to select the candidate selection processes you want to
export. You can select one or multiple processes. You can use search parameters to filter the list.
6. Click Save and Close.
What to do next
While it's possible to export all processes regardless of their status, the import of setup data for candidate selection
processes only imports candidate selection processes in the draft status.

Recruiting Content Library
The Recruiting Content Library contains various text-based content and notifications used in job requisitions, job
requisition templates, candidate job applications, job offers. The text-based content and notifications are organized into
several categories.
Notifications are also available in Alerts Composer. This tool contains notification templates sent to recruiters, hiring
managers, collaborators, interviewers, job offer team members for different events in the job application process, the
hiring process, and when a job offer moves through its life cycle. Note that interview notifications sent to the recruiters,
hiring managers, and interviewers are available in Alerts Composer, whereas interview notifications sent to candidates
are available in the Recruiting Content Library.
The maximum size of a notification is 15MB. If you exceed this limit, the notification might not be sent. To respect this
limit, you can optimize images or logos in the notification.
Note: Don't disable predefined notifications because they support the intended functionality. However, you can
change their content.
The following table presents the notification categories, their description, and where the notifications appear. Note that
the notification appears in the Interactions tab only if the Capture Interactions checkbox is enabled for the content item.
Similarly, the outgoing email or SMS message appears in the Messages tab only if the Capture Message checkbox is
enabled.

Category

Description

---

## Message automatically sent to the recruiter
*Chunk ID: OHR-REC-0392 | Chapter: Recruiting Content Library*

or designated members of the Hiring Team
to inform them of duplicate check results.
These notifications are sent when the selection
process is configured to automatically initiate a
candidate duplicate check before the candidate
is moved to the HR phase.

---

## Message automatically sent to members of the
*Chunk ID: OHR-REC-0393 | Chapter: Recruiting Content Library*

job requisition and job offer hiring teams as job
applications are moved through the candidate
selection process. The sent notifications appear
in the Interactions tab of job applications.

---

## Message automatically sent to candidates
*Chunk ID: OHR-REC-0394 | Chapter: Recruiting Content Library*

throughout the candidate selection process
so they're kept informed of their progress.
Recruiters and hiring managers can view the
notifications that were sent and the content of

---

## Where the Notification Appears
*Chunk ID: OHR-REC-0395 | Chapter: Recruiting Content Library*

those notifications in the Interactions tab of the
candidate's job application.
For details, see Configure Automated Job
Application Notifications.

---

## Message automatically sent to external
*Chunk ID: OHR-REC-0396 | Chapter: Recruiting Content Library*

candidates to ask them to provide more
information once they've applied to a job.

---

## Text describing the candidate's agreement to
*Chunk ID: OHR-REC-0397 | Chapter: Recruiting Content Library*

The opt in statement is displayed to candidates
receive recruitment marketing communications. as part of the candidate's job application
process. By default, only candidates that have
opted in are included in campaign audiences.

---

## You can include tokens in the notification so
*Chunk ID: OHR-REC-0398 | Chapter: Recruiting Content Library*

that the message is specific to the candidate in
the context of the job application.
You can add logos and images to support your
branding.
You can contextualize the message with job
requisition attributes including recruiting type,
organization, location, job family, and job
function.
You can translate notifications so they're sent
in the candidate's job application language.
Recruiters can select these notifications when
using the Send Email action.
You can have multiple active content items for
this category.

---

## Message that can be sent in bulk in any
*Chunk ID: OHR-REC-0399 | Chapter: Recruiting Content Library*

candidate pool context. You can include tokens
in the notification. You can add logos and
images to support your branding. You can
translate notifications so they're sent in the
candidate's preferred language. Recruiters can
select these notifications when using the Send
Email action.

---

## Message that can be sent in bulk in any
*Chunk ID: OHR-REC-0400 | Chapter: Recruiting Content Library*

candidate profile context. You can include
tokens in the notification. You can add logos
and images to support your branding. You can
translate notifications so they're sent in the
candidate's preferred language. Recruiters can
select these notifications when using the Send
Email action.

---

## Message sent to candidates to confirm their
*Chunk ID: OHR-REC-0401 | Chapter: Recruiting Content Library*

options to receive recruiting marketing
communications and job alerts when they
apply for a job, when they sign in into a talent
community, of from their candidate self service
page.

---

## Employer Description
*Chunk ID: OHR-REC-0402 | Chapter: Recruiting Content Library*

Text describing the company hiring candidates.
Recruiters and hiring managers select the
employer description in the Job Formatting
tab of job requisitions. The Recruiting
Administrator also selects the employer
description in the Job Formatting tab of job
requisition templates.

Displayed to candidates in job postings.

---

## Message sent to the Hiring Team members to
*Chunk ID: OHR-REC-0403 | Chapter: Recruiting Content Library*

Interactions tab
notify them of actions they need to take on job
requisitions, job applications, or job offers and
keep them informed through the hiring process.
You can configure hiring team notification
templates to be sent to specific Hiring Team
members. You need to define all Hiring Team
collaborator types before creating notification
templates.
It's recommended to include the lookup code
in the collaborator type tokens so that users
can easily select the correct token when
managing notification templates and sending
messages to the Hiring Team. For example, the
lookup code defined was INTERVIEW_TEAM
then the tokens available in the notification
would be Requisition_INTERVIEW_TEAM_
DisplayNameList and Offer_INTERVIEW_TEAM_
DisplayNameList.

Category

Description

---

## Instructions displayed to candidates when
*Chunk ID: OHR-REC-0404 | Chapter: Recruiting Content Library*

they provide their electronic signature as
part of the candidate's application process.
The E-Signature option is turned on or off by
the Recruiting Administrator using the Job
Application Flow Configuration task, in the Set
Up and Maintenance work area.

---

## For this content category, you can have one
*Chunk ID: OHR-REC-0405 | Chapter: Recruiting Content Library*

active content item for internal postings, one
active content item for external postings, or
one content item covering both internal and
external postings.

---

## Text intended to specify or delimit the scope of
*Chunk ID: OHR-REC-0406 | Chapter: Recruiting Content Library*

rights and obligations that might be exercised
between the hiring company and candidates.
The Legal Disclaimer option is turned on or off
by the Recruiting Administrator using the Job
Application Flow Configuration task, in the Set
Up and Maintenance work area.

---

## Text displayed to candidates as they're about to
*Chunk ID: OHR-REC-0407 | Chapter: Recruiting Content Library*

accept job offers. The Recruiting Administrator
can configure the content of the statement
to target external candidates, current internal
workers, or both. When a candidate accepts
a job offer, the current job offer e-signature
statement is shown to the candidate according
to the candidate type (internal, external) and
the candidate must provide their name as a
light e-signature. The Job Offer Team can't edit
the text for each specific job offer.

---

## For this content category, you can have one
*Chunk ID: OHR-REC-0408 | Chapter: Recruiting Content Library*

active content item for internal postings, one
active content item for external postings, or
one content item covering both internal and
external postings.

---

## Message sent to candidates to inform them
*Chunk ID: OHR-REC-0409 | Chapter: Recruiting Content Library*

that they're no longer considered for a job.
This notification can only be sent to candidates
who were already aware of their job offer, and
who are rejected directly from the state Offer Extended.

---

## Template to create a job offer letter. To create
*Chunk ID: OHR-REC-0410 | Chapter: Recruiting Content Library*

offer letters for candidates, there must be at
least one job offer letter template upon which
to base the offer letters. This template provides
the formatting, branding, and most of the
text that each candidate will see when they
receive their offer letter. It also contains tokens
that are replaced by specific values for each
person's offer letter. When each individual
offer letter gets created, using either of the
available methods for resolving tokens, this
template becomes personalized by merging the
template's text with that candidate's specific
offer values, such as the requisition title, offer
start date, and work location as replacements
for all of its tokens.

---

## For each offer letter template, only the current
*Chunk ID: OHR-REC-0411 | Chapter: Recruiting Content Library*

version will be used. When a candidate's offer
is associated with a given offer letter template,
it will be generated based on the currentlyactive version of that template. If you need to
make a change to the content or formatting
to be reflected in the offer letters of future
candidates whose offers use a given template,
you should inactivate the template in the
Content Library and upload a new template
to a new item in the Content Library to avoid
impacting active offers. For details, see Job
Offer Letter Template.
To provide each job offer letter template
translated into various languages, it's
recommended to create one job offer letter
template that contains every desired language
translation on subsequent pages. That template
should be configured to display only the pages
in the appropriate language conditionally,
depending on the language in which the
candidate applied to the job.

---

## Candidates can be shown any short text
*Chunk ID: OHR-REC-0412 | Chapter: Recruiting Content Library*

immediately after they accept the job offer.
You can configure this text to acknowledge
the candidate's acceptance, or to suggest next
steps for external and internal candidates after
they agree to take a new job.

---

## Subsequent times when the candidate
*Chunk ID: OHR-REC-0413 | Chapter: Recruiting Content Library*

returns to view their accepted offer letter or
download the PDF file of their offer letter, this
acknowledgment text is no longer shown.

---

## Message sent to candidates to inform them that Messages tab
*Chunk ID: OHR-REC-0414 | Chapter: Recruiting Content Library*

the start date on their job offer was changed.
For the changes to the start date to appear in
the candidate application Messages tab, you
need to select the Capture Message option.

---

## Message that can be sent in bulk in any
*Chunk ID: OHR-REC-0415 | Chapter: Recruiting Content Library*

candidate prospect context. You can include
tokens in the notification. You can add logos
and images to support your branding. You
can contextualize the message with job
requisition attributes including recruiting type,
organization, location, job family, and job
function. You can translate notifications so they
are sent in the candidate's preferred language.
Recruiters can select these notifications when
using the Send Email action.

---

## Text describing the organization for which the
*Chunk ID: OHR-REC-0416 | Chapter: Recruiting Content Library*

candidate will be working. Recruiters and hiring
managers select the recruiting organization
description in the Job Formatting tab of job
requisitions. The Recruiting Administrator also
selects the recruiting organization description
in the Job Formatting tab of job requisition
templates. The recruiting organization
description is displayed to candidates in job
postings.

---

## Message sent to external candidates to inform
*Chunk ID: OHR-REC-0417 | Chapter: Recruiting Content Library*

them that their draft job application was saved
and that they can complete and submit it.

---

## Message sent to external candidates to remind
*Chunk ID: OHR-REC-0418 | Chapter: Recruiting Content Library*

them that their draft job application was saved
and that they can complete and submit it.

---

## Where the Notification Appears
*Chunk ID: OHR-REC-0419 | Chapter: Recruiting Content Library*

landing page is tied to a career site that doesn't
have Talent Community enabled.

---

## Create a Content Item
*Chunk ID: OHR-REC-0420 | Chapter: Recruiting Content Library*

You can create various text-based content in the Recruiting Content Library that can be used in job requisitions, job
requisition templates, candidate job applications, job offers.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library

2. On the Recruiting Content Library page, click Create.
3. In the Content Item Details section, enter the following information:
◦ Name

◦ Code
◦ Category
◦ Visibility: A content item can be used for internal postings, external postings, or both. For automated job

application notifications, the visibility determines for which types of candidates the template is available for
selection when using the Send Notification action in the candidate selection process.

4. Complete the Interactions or Messaging section.
◦ Capture Interaction: If you select this option, the notification appears in the Interactions tab.

◦ Capture Message: If you select this option, the sent email or SMS message appears in the Messages tab,
according to the context of the notification.

5. In the Version Details section, enter the date and time when the item will be available for use.
If you want the content item to be available as soon as it's activated, select the Start on Activation option.
6. Add the content to the content item. Depending on the category you selected, you might need to enter text-based
content in the Content field or the Message Text field.
◦ For content text, enter text specific to the content item you're creating. For example, if you're creating
a campaign opt in statement, enter the text for the statement. You can enter a maximum of 50 000
characters. Rich text features are available to format the text.
◦ For a message text, enter the subject and text for the message. You can enter a maximum of 50 000
characters. Rich text features are available to format the text. You can also enter SMS text.
◦ When you copy content from another source and paste it in a content item, only formatting options offered
by the text editor are supported (bold, italics, underline, bulleted list, numbered list, indentation, links). If

◦
◦

---

## Recruiting Content Library
*Chunk ID: OHR-REC-0421 | Chapter: Recruiting Content Library*

the pasted content contains unsupported formatting, the text editor will try to remove it. You should review
the output as there might be formatting issues.
The font and font color used in the content items aren't set by default. The values from the browser (when
previewing the content) and email (when viewing the email normally) are used. To ensure consistency, you
can select a specific font and font color when designing the content. Note that the font used for HTML
templates is Arial by default.
For content items of type notification, you can:
- Include tokens so that the message is specific to the candidate. Only use job offer and assignment
tokens in automated notifications that are sent during the offer phase or later phases in the selection
process. These tokens won't resolve if the job offer wasn't created.
- Add logos and images to ensure the candidate experience aligns with your organization's corporate
branding.
Note: The maximum size of a notification is 15MB. If you exceed this limit, the notification might
not be sent. To respect this limit, you can optimize images or logos in the notification.
- Click the Translation Editor icon to translate notifications so they're sent in the candidate's job
application language or preferred language (depending on the context the notification is sent). When
not translated, notifications are sent in the source language of the notification.
- Contextualize the message with job requisition attributes including recruiting type, organization,
location, job family, and job function.

7. You can translate some parts of the content item using the Translation Editor tool, represented by the earth logo.
8. When you're done entering the information, click Save and Activate to make the item available for use or Save as
Draft to edit and activate the item at a later time.
What to do next
Create a Version of a Content Item

---

## Content Item Versions
*Chunk ID: OHR-REC-0422 | Chapter: Recruiting Content Library*

A content item in the Recruiting Content Library can have several versions to respond to different needs.
There are different ways to create versions of a content item:
• While creating a content item version.
• Using the Create Content Item From Version action: Use this action to create a new content item using a version
of another content item.
• Using the Copy to Create New Version action: Use this action to create a new version of a content item by
copying the content of an existing version of this item.
• Using the Create New Version action: Use this action to create a new version of a content item. When you create
a new version, the new version is prepopulated with the content of the latest version of this item (the version
with the higher start date, which can be a future date). You can also create a new version using the Create
button in the version details page.
A content item version can have one of the following statuses:
• Active: The content item is available to be used in job requisitions, job requisition templates, candidate job
applications, or job offers.
• Draft: The content item version can be edited and activated when ready.

---

## Recruiting Content Library
*Chunk ID: OHR-REC-0423 | Chapter: Recruiting Content Library*

• Current: The content item version is being used. You can't modify its content.
• Future: The content item version is scheduled to be used at a later time. You can modify its content.
• Ended: The content item version was used in the past and has been replaced by another one. You can't modify
its content.

---

## Create a Version of a Content Item
*Chunk ID: OHR-REC-0424 | Chapter: Recruiting Content Library*

When you create a content item in the Recruiting Content Library, you create the first version of the item. A content item
can have several versions. For example, you can create two versions of an employer description.
1. Open a content item.
2. In the Additional Versions section, click Create.
3. On the Create Version page, select a start date when the version will be available for use.
If you want the version to be available as soon as it's activated, select the Start on Activation option.
4. Enter the text for the new version.
5. Click Save and Activate to make the version available for use. Or Save as Draft to edit and activate the version at a
later time.

---

# Notifications

## When to Delete or Deactivate a Content Item Version
*Chunk ID: OHR-REC-0425 | Chapter: Notifications*

Here's the difference between deleting and deactivating a content item version.
You delete a content item version to remove a version from the list of versions of a content item. The Delete action is
only available for versions with the Draft or Future status to prevent deleting versions being used. If the version you
delete is the only version on the content item, deleting the version also deletes the content item.
You deactivate a content item to prevent the content item from being used. When you deactivate a content item,
its status changes to Inactive. The Deactivate Content Item action is only available for active items. When an item is
deactivated, it remains in use where it was previously selected but it can no longer be selected. For example, when you
deactivate an employer description it's no longer available for selection in job requisitions.

Notifications

Types of Notifications
You use notifications to keep stakeholders informed of key events and actions. You can send notifications to candidates,
recruiters, hiring managers, hiring team collaborators, and recruiting agents at specific points in the candidate selection
process.
There are different types of notifications:
• Automated job application notifications: These notifications are automatically sent to candidates as their job
applications move through the candidate selection process. For example, a candidate receives a notification
after being selected for an interview. You configure these notifications in the Recruiting Content Library.
• Automated agent notifications: These notifications are automatically sent to recruiting agents when they create
a job application on behalf of a candidate, then move the candidate through the candidate selection process.
(Note: Agents don't receive a notification when a referred candidate applies to a job). You configure these
notifications in the Recruiting Content Library.
• Automated hiring team notifications: These notifications are automatically sent to members of the Hiring Team
and Offer Team as job applications move through the candidate selection process. Notifications that are sent
appear in the Interactions tab of job applications. You configure these notifications in the Recruiting Content
Library.
• Candidate notifications: These notifications are used by recruiters to send messages to candidates. For
example, a recruiter sends a message to 5 candidates asking for details on their certifications. You configure
these notifications in the Recruiting Content Library.
• Hiring team notifications: These notifications are sent to the Hiring Team members (hiring manager, recruiter,
collaborators) to inform them of actions they need to perform on job requisitions, job applications, or job
offers. These notifications keep the hiring team informed throughout the hiring process. You configure these
notifications in the Recruiting Content Library.
• Review notifications: These notifications are used to inform recruiters and hiring managers that they need to
review job applications. For example, a hiring manager receives a notification indicating that 3 new candidates
have passed the screening process and they're ready to be reviewed. You configure these notifications in Alerts
Composer.
• Notifications in Alerts Composer: These notifications are used to inform recruiters, hiring managers,
collaborators, job offer team members that events occur within the hiring process. For example, an alert is sent
to a hiring manager to confirm that a job was posted.
Note: Don't disable default notifications because the intended functionality won't work.

---

## Note: When you use a token with an email attribute, for example {RequisitionRecruiterEmail}, the primary email
*Chunk ID: OHR-REC-0426 | Chapter: Notifications*

is used to resolve the token. Make sure that the primary email is set to use the person work email (W1), and not the
home email (H1).

Notifications

Related Topics
• Configure Automated Job Application Notifications
• Configure Hiring Team Notifications
• Notifications in Alerts Composer
• Configure Candidate Notifications
• Configure Review Notifications

---

## Configure Automated Job Application Notifications
*Chunk ID: OHR-REC-0427 | Chapter: Notifications*

Candidates can automatically receive notifications throughout the candidate selection process to be kept informed
of their progress. Recruiters and hiring managers can view the notifications that were sent and the content of those
notifications in the Interactions tab of the candidate's job application.
As an example, you could create an automated notification that would be sent to candidates when they're rejected in
the candidate selection process.
Here's what to do
1. Create Automated Job Application Notifications
2. Configure the Candidate Selection Process With the Send Notification Action

---

## Create Automated Job Application Notifications
*Chunk ID: OHR-REC-0428 | Chapter: Notifications*

You create notifications in the Recruiting Content library using the Automated Job Application Notification category.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library
2. On the Recruiting Content Library page, click Create.
3. In the Content Item Details section, enter the following information:

◦ Name
◦ Code
◦ Category: Select Automated Job Application Notification.
◦ Visibility: A content item can be used for internal postings, external postings, or both. For automated job

application notifications, the visibility determines for which types of candidates the template is available
for selection when using the Send Notification action in the candidate selection process.
4. Complete the other fields. For details, see Create a Content Item.

---

## Configure the Candidate Selection Process with the Send Notification
*Chunk ID: OHR-REC-0429 | Chapter: Notifications*

Action
When notifications are created, you configure the candidate selection process by adding the Send Notification action
to specific phases and states of the selection process. When a job application enters or exits a phase or is moved to

Notifications

a specific state within a phase, a notification is automatically sent to the candidate. You can set a delay so that the
notification is sent at a specified time after the job application has been moved.
Related Topics
• Use the Send Notification Action for Job Applications

---

## Configure Candidate Notifications
*Chunk ID: OHR-REC-0430 | Chapter: Notifications*

You can create and manage a library of notifications that can be sent in bulk in any candidate context.
Available candidate notifications are:
• Candidate Job Application Notification
• Candidate Pool Member Notification
• Candidate Profile Notification
• Prospect Candidate Notification
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library
2. On the Recruiting Content Library page, click Create.
3. In the Content Item Details section, enter the following information:
◦ Name

◦ Code
◦ Category: Select one of these categories: Candidate Job Application Notification, Candidate Pool Member
◦

Notification, Candidate Profile Notification, Prospect Candidate Notification.
Visibility: A content item can be used for internal postings, external postings, or both.

4. In the Context Information section, if you selected the Candidate Job Application Notification or Prospect
Candidate Notification, you can contextualize the message with job requisition attributes including recruiting
type, organization, location, job family, and job function. This ensures users are using the correct templates for the
requisition.
5. Complete the other fields. For details, see Create a Content Item.
Results:
When these notifications are created, recruiters and hiring managers use the Send Email action to send these
notifications. They can create an email from scratch or select a notification template. The list of notification
templates available for selection depends on the context the Send Email action is initiated from. For example,
if they use the Send Email action from the job application list, only candidate job application notifications are
available. In the requisition context, the list of templates available for selection might be further refined depending
on the contextualization defined on the template. If users have the privilege Update Email Created from Template
(IRC_UPDATE_EMAIL_CREATED_FROM_TEMPLATE), they can edit the template. Once the email is sent, an interaction
note of type email is automatically added in the Interactions tab where the action was launched (candidate profile,
candidate job application, prospect, candidate pool).

Notifications

---

## Configure Hiring Team Notifications
*Chunk ID: OHR-REC-0431 | Chapter: Notifications*

You can create hiring team notification templates to be sent to specific Hiring Team members to inform them of actions
they need to take on job requisitions, job applications, or job offers.
To send these notifications, recruiting users use the Send Message to Team action.
Before you enable this feature, consider whether you need more granular collaborator types on your job requisition and
job offer hiring teams. You can configure Hiring team notification templates to be sent to specific Hiring Team members.
So, you should define all hiring team collaborator types before creating notification templates.
You also need to consider whether your organization will use hiring team notification templates. The Send Message to
Team action doesn't require the use of templates but templates do save time and are especially convenient when the
same messages are sent frequently across job requisitions, job applications, and job offers.
Here's what to do
1. Create Collaborator Types
2. Create Hiring Team Notification Templates

---

## Create Collaborator Types
*Chunk ID: OHR-REC-0432 | Chapter: Notifications*

If you want to use hiring team collaborator types, you need to define them prior to creating notification templates. By
default, this collaborator type is available: Collaborator To define new collaborator types:
By default, this collaborator type is available: Collaborator
To define new collaborator types:
1.
2.
3.
4.

In the Setup and Maintenance work area, search for the task Manage Common Lookups.
Click the task name.
Search for the lookup type ORA_IRC_COLLABORATOR_RESP_TYPE.
Create lookups as required. Lookup codes should not begin with the prefix "ORA".

---

## It's not recommended to disable the seeded Collaborator look up because this lookup is used by any existing requisition
*Chunk ID: OHR-REC-0433 | Chapter: Notifications*

and job offer hiring teams where collaborators have been defined.
It's recommended to include the lookup code in the collaborator type tokens so that users can easily select
the correct token when managing notification templates and sending messages to the hiring team. For
example, the lookup code defined was INTERVIEW_TEAM then the tokens available in the notification would be
Requisition_INTERVIEW_TEAM_DisplayNameList and Offer_INTERVIEW_TEAM_DisplayNameList.

---

## Create Hiring Team Notification Templates
*Chunk ID: OHR-REC-0434 | Chapter: Notifications*

You can create and manage a library of hiring team notification templates, which can be sent in the context of job
requisitions or job applications.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library

Notifications

2. On the Recruiting Content Library page, click Create.
3. In the Content Item Details section, enter the following information:

◦ Name
◦ Code
◦ Category: Select Hiring Team Notification.
◦ Visibility: A content item can be used for internal postings, external postings, or both.
4. In the Context Information section, you can contextualize the message with job requisition attributes including
recruiting type, organization, location, job family, and job function. This ensures users are using the right
templates for the requisition. You can also select default recipients such as Collaborator, Hiring Manager, and
Recruiter.
5. In the Version Details section, enter the date and time when the notification is available for use. If you want the
content item to be available as soon as it's activated, select the Start on Activation option.
6. Enter the subject and text for the message. Rich text features are available to format the text.
7. Click Save and Activate.

---

## Configure Review Notifications
*Chunk ID: OHR-REC-0435 | Chapter: Notifications*

You can configure a candidate selection process to automatically send review notifications to recruiters and hiring
managers to notify them that there are job applications to be reviewed.
The review notification message is available in Alerts Composer (Tools > Alerts Composer). Two versions are available,
one for the hiring manager and one for the recruiter.
• IRC_JobApp_Review_HM
• IRC_JobApp_Review_Recruiter
1. In Setup and Maintenance, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, create a new process or update an existing one.
3. Click a phase.
4. Add the Send Notification action at the phase level, when job applications enter or exit a phase, or at the state level,
when job applications are moved to a specific state within a phase.
Note: The Send Notification action isn't working when the Move action is defined for the same state.
5. On the Action: Send Notification page, select to whom you want the review notification to be sent: recruiter, hiring
manager,or both.
6. Add conditions if needed.
7. Click Save and Close.
Results:
Review notifications that are sent appear in the Interactions tab of the candidate job application.

Notifications

---

## How to Display Site Logo in Candidate Notifications
*Chunk ID: OHR-REC-0436 | Chapter: Notifications*

Some predefined external candidate notifications contain a logo (pulled from the career site) and when HTML templates
are used this could cause two logos to appear in the notification.
To display the site logo in candidate notifications, you need to remove this HTML from the predefined notification
template in the Recruiting Content Library.
Note: The maximum size of a notification is 15MB. If you exceed this limit, the notification might not be sent. To
respect this limit, you can optimize images or logos in the notification.

---

## Note: You need to store images on a public-facing server that doesn't require authentication. For example, this can
*Chunk ID: OHR-REC-0437 | Chapter: Notifications*

be the same server that you use for your corporate public websites or any publicly accessible website. Also, you can't
store images in Oracle Recruiting Cloud (ORC).The URL can't contain the customer's POD URL.

---

## Requirements for Images in Notifications
*Chunk ID: OHR-REC-0438 | Chapter: Notifications*

It's recommended to embed images in notifications using a URL. If you decide to insert an image in a notification,
consider the following:
• The image must not exceed 64 KB.
• The image must be in RGB format.
• The image must be one of these file formats: .png, .jpeg, .bmp, .gif.
Note: The maximum size of a notification is 15MB. If you exceed this limit, the notification might not be sent. To
respect this limit, you can optimize images or logos in the notification.

---

## Note: You need to store images on a public-facing server that doesn't require authentication. For example, this can
*Chunk ID: OHR-REC-0439 | Chapter: Notifications*

be the same server that you use for your corporate public websites or any publicly accessible website. Also, you can't
store images in Oracle Recruiting Cloud (ORC).The URL can't contain the customer's POD URL.

Notifications

---

## Notifications in Alerts Composer
*Chunk ID: OHR-REC-0440 | Chapter: Notifications*

You use notifications in the Alerts Composer tool to set up notifications to be sent to recruiters, hiring managers,
collaborators, and job offer team members for different events in the job application process, the hiring process, and
when a job offer moves through its life cycle. Notifications sent to candidates are managed in the Recruiting Content
Library.
Alerts Composer is available in the Tools work area. To use Alerts Composer, you need specific functional privileges.
All recruiting notifications start with the word IRC. For example, IRC_JobOffer_Accepted_External.
Note: Don't change or disable the IRC_Candidate_Notifications_Gateway alert. This is a gateway alert for all internal
candidate email notifications. Disabling this will stop all internal candidate email notifications.
With the Alerts Composer tool, you can:
• Set notifications to be delivered to recipients by email or worklist (bell icon). By email, the notification is
delivered by email. By worklist, the notification is delivered by both email and worklist (a separate email
method isn't required). For internal recipients, both email and worklist notifications are supported. For external
recipients (candidates), only email is supported.
• Add or remove recipients.
• Change the content and formatting of messages.
Note: The maximum size of a notification is 15MB. If you exceed this limit, the notification might not be sent.
To respect this limit, you can optimize images or logos in the notification.
• Turn notifications on or off.
• Add and change tokens in notifications. You can only use tokens available for the context. For example, if you
change a notification sent to candidates, you can only use tokens for the candidate context. For a list of tokens
available for recruiting notifications, see the document Tokens for Alert Notifications on My Oracle Support (ID
2513219.1).
Notifications are sent in the language understood by the recipients. The language varies whether the notification is sent
to external candidates, internal candidates, or users interacting with job applications.
• When notifications are sent to external candidates in the context of a job application, the candidate's job
application language is used.
• When notifications are sent to internal candidates in the context of a job application, the language of the
candidate job application is used. When notifications are sent to internal candidates for a context outside of
a job application, for example an invitation to apply for a job, the default language of the user is used (default
language set in the user's preferences).
• Notifications and job requisition content included in notifications are displayed in the preferred language of the
user receiving the notification.
• If a notification is sent to many users, each user receives the notification in their preferred language (could be
different languages). If the user's preferred language isn't an active language on the job requisition, the job
requisition's default language is used when including job requisition content in the notification.
Note: Notifications are sent for events done in the UI. For events done using REST API, no notification is sent.

Notifications

---

## Alerts and Translation
*Chunk ID: OHR-REC-0441 | Chapter: Notifications*

The content of some alerts include groovy expressions and translation isn't available for these alerts. Here's a list of
these alerts.
• IRC_Agent_Invite_Alert
• IRC_Agent_Invite_Expiry
• IRC_Agent_Invite_Update
• IRC_BatchAction_Done
• IRC_Candidate_Assessment_Completed
• IRC_Candidate_Assessment_Error
• IRC_Candidate_Merge_Status
• IRC_Candidate_Tax_Credit_Screening_Completed
• IRC_Candidate_Tax_Credit_Screening_Issue
• IRC_Intrv_Canceled_Interviewer
• IRC_Intrv_Canceled_ReqOwners
• IRC_Intrv_Reminder_Interviewer
• IRC_Intrv_Scheduled_Interviewer
• IRC_Intrv_Schedule_Low_Openings
• IRC_Intrv_Schedule_No_Openings
• IRC_Intrv_Scheduled_ReqOwners
• IRC_Intrv_Updated_Interviewer
• IRC_Intrv_Updated_ReqOwners
• IRC_JobOffer_Accepted_External
• IRC_JobOffer_Accepted_Internal
• IRC_JobOffer_Declined_External
• IRC_JobOffer_Declined_Internal
• IRC_JobOffer_Extended_External
• IRC_JobOffer_Extended_Internal
• IRC_JobOffer_Extnd_Rejctd_Extrnl
• IRC_JobOffer_Extnd_Rejctd_Intrnl
• IRC_JobOffer_MergeDraftInitiated
• IRC_JobOffer_Not_Extended_Rejctd
• IRC_JobOffer_Withdrawn
• IRC_JobApp_Review_HM
• IRC_JobApp_Review_Recruiter
• IRC_PRINT_ACTION_DOWNLOAD
• IRC_PRINT_ACTION_HYPERLINK
• IRC_PRINT_POOL_MEMBER_ACTION_DOWNLOAD

Notifications

• IRC_PRINT_POOL_MEMBER_ACTION_HYPERLINK
• IRC_Req_Exp_JobDist_Ext
• IRC_Req_Exp_JobDist_Int_Ext
• IRC_Req_Openings_Hired
• IRC_Req_Posted_Int_Ext
• IRC_Req_Unposted_Expired_Ext
• IRC_Req_Unposted_Expired_Int
• IRC_Req_Unposted_Expired_Int_Ext
• IRC_Requisition_Canceled
• IRC_Requisition_Initiation
• IRC_Requisition_Open_Not_Posted
• IRC_Requisition_Posted_Ext
• IRC_Requisition_Posted_Int
• IRC_Requisition_Posting
• IRC_Requisition_Redrafted
• IRC_Requisition_Suspended
• IRC_SAVE_AS_PDF_ACTION_CANDIDATE_ATTACHED
• IRC_SAVE_AS_PDF_ACTION_CANDIDATE_HYPERLINK
• IRC_SAVE_AS_PDF_ACTION_EVENT_ATTACHED
• IRC_SAVE_AS_PDF_ACTION_EVENT_HYPERLINK
• IRC_SAVE_AS_PDF_ACTION_PROSPECT_ATTACHED
• IRC_SAVE_AS_PDF_ACTION_PROSPECT_HYPERLINK
Alerts come into two formats: plain text format and rich text format. Plain text alerts are automatically translated,
whereas rich text alerts aren't translated even when other languages are enabled in the environment. To translate rich
text alerts, here's how to proceed:
1.
2.
3.
4.
5.
6.

In Alerts Composer, select an alert.
In the Templates tab, click the Translation Editor icon.
In the language field, select a language.
Add the translated message text to the Body text box.
Click Apply.
Click Save and Close.

Related Topics
• Functional Privileges and Access Levels
• Functions and Groovy Expressions

---

## Notifications for Unposted Job Requisitions
*Chunk ID: OHR-REC-0442 | Chapter: Notifications*

Notifications are sent when job requisitions are unposted from a career site.

The notification being sent is determined based on whether the job requisition is still posted internally, externally, or if
it's no longer posted.
Here are the rules which govern which notification is sent. The notifications are available in Alerts Composer.

Scenario

---

## The job requisition is posted externally and
*Chunk ID: OHR-REC-0443 | Chapter: Notifications*

internally. It's later unposted only externally.

IRC_Requisition_Unposted_Expired_External

---

## The job requisition is posted externally and
*Chunk ID: OHR-REC-0444 | Chapter: Notifications*

internally. It's later unposted only internally.

IRC_Requisition_Unposted_Expired_Internal

---

## Notification when all job requisition postings
*Chunk ID: OHR-REC-0445 | Chapter: Notifications*

on career sites have been unposted or have
expired.

Here are examples:
A job requisition is posted internally and externally, and the internal posting expires. The
IRC_Requisition_Unposted_Expired_Internal notification is sent because the internal posting expired, but the requisition
is still posted externally.
A job requisition is posted internally only, and the internal posting expires. The
IRC_Requisition_Unposted_Expired_Internal notification is sent because the requisition is no longer posted.
Related Topics
• Notifications in Alerts Composer

---

## HTML Email Templates
*Chunk ID: OHR-REC-0446 | Chapter: Notifications*

You use HTML email templates to create branded notification templates that are used for specific career site
notifications, for communications with candidates using the Send Message feature, and for recruiting campaigns.
You can create a brand new HTML email template or duplicate an existing one. When you create an HTML email
template, an editor opens where you can personalize the template. You can personalize elements such as background
color, background image, alt text for images, branding text, fonts, font colors, rows, columns. You can also lock the
template so that recruiters can't modify it.
Note: The font used for HTML templates is Arial by default.

Note: The Alt text field is visible when you insert an image using the Select Element Type window. Alt text is available
for campaign user email templates only.

Notifications

Two types of template are available:
• Campaign user email template: This template is available when recruiters create campaign emails.
• Candidate notification email template: This template is available when recruiters send messages using the Send
Message action. It's also available at the career site level to send notifications to candidates.
A recruiter creating a campaign email can select one of the three default templates (Blank, Basic, Multi-Column) or any
HTML email template you created and made available for campaigns. The recruiter can modify the unlocked sections
within the HTML template to personalize its content for a specific use.
When creating a message using the Send Message action from the Candidate Search page, from a list of job
applications and prospects, and from within a candidate pool, the recruiter selects a template made available for
messages. The recruiter can't personalize the template but can insert their own content or content from the Recruiting
Content library.
When creating a career site, the administrator selects a template from a list of templates made available for career site
notifications. If no template is selected, the global template is used.

---

## Create an HTML Email Template
*Chunk ID: OHR-REC-0447 | Chapter: Notifications*

You can create and manage HTML email templates that are used for specific career site notifications, for
communications with candidates using the Send Message feature, and for recruiting campaigns.
Before you start
You need these privileges:
• Manage Recruitment Campaign (IRC_MANAGE_RECRUITMENT_CAMPAIGN)
• View Recruitment Campaign (IRC_VIEW_RECRUITMENT_CAMPAIGN)
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: HTML Email Templates
2. On the Manage HTML Email Templates page, click Add.
3. Enter a name for the template.
4. Select a template type:
◦ Campaign user email template

◦ Candidate notification email template
5. If you selected Campaign user email template, you need to select a campaign purpose:
◦ Respond to Request

◦ Refer Job
◦ Apply to Job

Notifications

6. If you selected Candidate notification email template, you need to select an email type:
◦ Internal Template

◦ CE Notification Template
◦ AdHoc Template
◦ Global Template
7. Select a template.
8. Click Save.
Results:
An editor opens in a new browser tab where you can personalize the template. You can personalize elements such as
background color, background image, alt text for images, branding text, fonts, font colors, rows, columns. You can also
lock the template so that users won't modify it.
Note: Alt text field is visible when you insert an image using the Select Element Type window. Alt text is available for
campaign user email templates only.

---

# Candidate Messaging

## Candidate Messaging
*Chunk ID: OHR-REC-0448 | Chapter: Candidate Messaging*

Set Up Candidate Messaging
To send SMS and email messages to candidates, you need to set up one-way SMS and email communications. For
details, see these topics:
• Workflow to Set Up One-Way SMS Communications
• Workflow to Set Up One-Way Email Communications
If you've enabled Recruiting Booster, you can send and receive SMS, emails, and WhatsApp messages from candidates.
To set up these communication channels, see:
• Workflow to Set Up Two-Way SMS Communications
• Workflow to Set Up Two-Way Email Communications
• Workflow to Set Up Two-Way WhatsApp Communications

---

# Job Requisition Templates

## Job Requisition Templates
*Chunk ID: OHR-REC-0449 | Chapter: Job Requisition Templates*

Job Requisition Template
A job requisition template provides a way to facilitate the creation of job requisitions by defaulting values in several
fields. You can create three types of job requisition template. For details, see What are the types of job requisition
templates?

---

## Create a Job Requisition Template of Type Standalone
*Chunk ID: OHR-REC-0450 | Chapter: Job Requisition Templates*

You create a job requisition template of type standalone if you want a template to be used by recruiters when they
create a requisition based directly on a template.
Here's what to do
1.
2.
3.
4.
5.
6.

---

## Create Job Requisition Template
*Chunk ID: OHR-REC-0451 | Chapter: Job Requisition Templates*

Add Questionnaires
Add Screening Services
Enter Job Formatting Information
Preview Job Requisition Template
Activate Job Requisition Template

---

## Create Job Requisition Template
*Chunk ID: OHR-REC-0452 | Chapter: Job Requisition Templates*

When you create a job requisition template, you need to select a template type and enter detailed information.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Job Requisitions
◦ Task: Job Requisition Templates

2. On the Job Requisition Templates page, click Create and select Standalone.
3. On the Details tab, enter details about the job requisition template by navigating to each section and
completing fields such as the recruiting type, business unit, code, requisition title, requisition name, hiring
team, posting structure, posting description, candidate selection process.
4. Click Save.
The job requisition template status is set to Draft and you can still edit the content as required.

---

## Add Questionnaires
*Chunk ID: OHR-REC-0453 | Chapter: Job Requisition Templates*

When you save details about the job requisition template, the details page displays the Prescreening Questionnaires
section and the Interview Questionnaires section.
• The Prescreening Questionnaires section contains two empty questionnaires: one for internal candidates,
one for external candidates. You can open the questionnaires and add questions from the questions library

---

## Job Requisition Templates
*Chunk ID: OHR-REC-0454 | Chapter: Job Requisition Templates*

or create questions. When you create a question, the question becomes available in the questions library and
available for use in other templates.
• In the Interview Questionnaires section, you can add interview feedback questionnaires that contain questions
used by recruiters and hiring managers to collect feedback on candidates during candidate interviews.
When you manually add a question, only questions matching the following criteria are available for selection:
• Active questions.
• Questions with the "Prescreening Question Added by User" classification.
• Questions matching the context of the requisition template.

---

## Add Screening Services
*Chunk ID: OHR-REC-0455 | Chapter: Job Requisition Templates*

When you save the details of the job requisition template, the Screening Services tab becomes available and you can
add screening services such as background checks, assessments, tax credits.
You can add one or more background check screening packages, usually it's a single package with several screenings.
Once you've selected the desired background check partner and user account, go to the partner's site to add the
background check screening packages to the job requisition. You can also specify the order in which the partner will run
the screening packages.
You can add one or more assessments to a job requisition template. Select an assessment partner and user account.
Specify if the assessment for the internal job application flow, the external flow, or both.
You can add one or more tax credit screening packages, usually it's a single package with several screenings. You then
select the desired partner and user account, and also a location package, if needed. Indicate if the tax credit screening is
triggered during the candidate application flow or the candidate selection process.

---

## Enter Job Formatting Information
*Chunk ID: OHR-REC-0456 | Chapter: Job Requisition Templates*

On the Job Formatting tab, you can select predefined descriptions of the employer, organization, department, or team
for which the candidate is hired. The descriptions are created in the Recruiting Content Library.
You can also select images and videos you want to show candidates. For example, images of the facilities, video of the
corporate history of the organization, video of testimonials from current employees. When you add a URL for a video,
by default the Thumbnail URL automatically points to a high-quality version of the video. It's recommended that you
add URLs of the type HTTPS to avoid displaying insecure items in a secure career site page. You can select specific
images and videos to be shown to the candidates who will receive job offers.
Any image or video can be shown on the requisition and on job offers for that requisition as well, making them more
interesting and more informative.
You can also select for which languages each item is available, and translate the media title in the appropriate
languages.

---

## Preview Job Requisition Template
*Chunk ID: OHR-REC-0457 | Chapter: Job Requisition Templates*

When you're done, you can use the Preview action to see how the info in the job requisition template will be displayed.
You can preview the info on a desktop computer or a mobile device. You can also select a career site and preview how
the requisition will be displayed.

---

## Activate Job Requisition Template
*Chunk ID: OHR-REC-0458 | Chapter: Job Requisition Templates*

When you're done filling out all the details about the job requisition template, select Activate Template in the Actions
menu. The job requisition template status is set to Active and the template can be used by recruiters and hiring
managers when they create job requisitions.

---

## Info About Job Requisition Template Fields
*Chunk ID: OHR-REC-0459 | Chapter: Job Requisition Templates*

While you create a job requisition template, consider the following info regarding specific fields.

Field

Description

---

## When you select this option, it indicates if the requisition is visible in the My Team work area and the
*Chunk ID: OHR-REC-0460 | Chapter: Job Requisition Templates*

organization chart available in the Directory work area. Note that the responsive UI version of the
Directory work area doesn't display requisitions in the organization chart; only older versions of the
Directory are impacted by the value of this field.

Organization, Legal Employer,
Department, Business Unit selectors

---

## When you select the Hiring Manager, you're asked if you want to use the business unit and department
*Chunk ID: OHR-REC-0461 | Chapter: Job Requisition Templates*

associated with the selected Hiring Manager. If you say yes, these fields are automatically filled.

---

## What is the purpose of the Organization field compared to the Department field? The Organization
*Chunk ID: OHR-REC-0462 | Chapter: Job Requisition Templates*

field has important functional implications which the Department field doesn't provide.
The value selected in the Organization field can be used to drive the possible values to be selected for
other requisition fields (candidate selection process and prescreening questions for example). This
Organization value can also be used to drive data security, meaning it can be used to define which
requisitions a user is allowed to see. The hierarchical nature of the Organization field (which is a value
within the Organization tree) allows taking into account where the selected Organization is placed
within the tree.
However, the Department field in the Offer section is a simple selection which will be defaulted in an
offer created for this requisition. It doesn't impact anything else.

---

## This is where you define the posting description, short description, qualifications, and responsibilities
*Chunk ID: OHR-REC-0463 | Chapter: Job Requisition Templates*

of the job posted on the internal carer site, external career sites, or both.
The short description appears on the career site job search results page. That page displays the name,
location, and brief description of the job. The Short Description field can contain a maximum of 1000
characters.
The description appears when a candidate clicks on a job to view the complete description of the
job requisition. You can specify a different description for the internal career site and the external
career site. Note that the internal short description is currently not used on the internal career site. The
description is only displayed within the requisition.

Configuration

This is where you can select configuration options for the job requisition template:
• Candidate selection process: You select the candidate selection process used for the requisition.
• External application flow: You select the application flow used for the requisition.

---

## Job Requisition Templates
*Chunk ID: OHR-REC-0464 | Chapter: Job Requisition Templates*

Description
• Allow candidates to apply when not posted: When you enable this option, recruiting users can
invite candidates to apply on a job requisition that's currently not visible to other candidates. This
could be the case if your organization wants to fill a high-level job or even a replacement and they
want to keep it confidential.
• Automatically open requisition for sourcing: You can specify if the requisition is automatically
open for sourcing once it's approved, and post it on career sites.
• Automatically unpost requisition: You can specify if the requisition will be automatically unposted
from the internal career site, the external career sites, or both.
• Automatically fill requisition: When you enable this option, the status of the job requisition is
automatically changed to Filled once the number of hired candidates matches the number of
openings on the job requisition.

---

## Preview a Job Requisition Template
*Chunk ID: OHR-REC-0465 | Chapter: Job Requisition Templates*

You can use the Preview Template action to see how the info in the job requisition template will be displayed. You
can preview the info on a desktop computer or a mobile device. You can also select a career site and preview how the
requisition will be displayed.
1. In the Setup and Maintenance work area, go to.
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Job Requisitions
◦ Task: Manage Job Requisition Templates

2. Click on a job requisition template.
3. In the Actions menu, select Preview Template.
4. In the Preview field, indicate if you want to preview the template as an external candidate on a desktop computer or
on a mobile device.
5. Select the career site.
Only active external career sites for which the requisition template context matches the filters of the site are available
for selection.
6. In the Language field, select the language to preview the template.
You can preview the information in the different languages that are active for the template.

---

## Apply the Values of a Job to a Job Requisition Template
*Chunk ID: OHR-REC-0466 | Chapter: Job Requisition Templates*

You use the Apply Job action when you want to use the values of a job and add them to a job requisition template. The
content of the job overwrites the content of the job requisition template.
Note: If you apply a job to a job requisition template, users creating a requisition from the template won't be able to
select a different template after the template is selected on the requisition.
1. In the Setup and Maintenance work area, go to.

---

## Job Requisition Templates
*Chunk ID: OHR-REC-0467 | Chapter: Job Requisition Templates*

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Job Requisitions
◦ Task: Manage Job Requisition Templates
2. Click on a job requisition template.
3. In the Actions menu, select Apply Job.
4. Select a job.
5. Click Save.

---

## When to Delete or Inactivate a Job Requisition Template
*Chunk ID: OHR-REC-0468 | Chapter: Job Requisition Templates*

You delete a job requisition template to remove it from the Job Requisition Templates page so that it can't become an
active template. The Delete Template action is only available for draft job requisition templates.
You inactivate a job requisition template to prevent recruiters from selecting that template when creating a job
requisition.

---

## Job Requisition Template Multilingual Content
*Chunk ID: OHR-REC-0469 | Chapter: Job Requisition Templates*

Oracle Fusion Cloud Recruiting is available in multiple optional languages to deliver a multilingual recruiting experience.
When you sign in Oracle applications, you can select your session language in your user preferences. American English
is the default session language for the first visit (the application remembers the last session language). The session
language you select defines the language of every label in a product. The session language is used as the creation
language. For example, Spanish is installed in the environment. If you sign in Spanish, you create job requisition
templates in Spanish.
When you create a job requisition template, the current user's session language is automatically set as the default
language. You can then translate the job requisition content in the selected languages. The default language cannot be
deselected on a job requisition template.
You can provide translation whether the job requisition template is Draft, Active, Inactive. You can provide translation
for job requisition template multilingual content without having to sign out and sign in a different language. Use the
Translation Editor tool, represented by the earth logo, to translate these multilingual values:
• Name
• Requisition Title
• Other Requisition Title
• Short Description for Internal Candidates
• Description for Internal Candidates
• Responsibilities for Internal Candidates
• Qualifications for Internal Candidates
• Short Description for External Candidates

---

# Job Requisitions

## Job Requisition Templates
*Chunk ID: OHR-REC-0470 | Chapter: Job Requisitions*

• Description for External Candidates
• Responsibilities for External Candidates
• Qualifications for External Candidates

Configure Job Requisition Creation Options
You can configure which creation options are available to users who create job requisitions. When a user creates a job
requisition, the Use selector only displays the creation options to which the user has access.
These privileges control the creation of job requisitions:

---

## Initiate Job Requisition Using Template
*Chunk ID: OHR-REC-0471 | Chapter: Job Requisitions*

(IRC_INITIATE_JOB_REQUISITION_USING_
TEMPLATE)

Allows users to create job requisitions based on a requisition template.

---

## Initiate Job Requisition Using Blank
*Chunk ID: OHR-REC-0472 | Chapter: Job Requisitions*

Requisition (IRC_INITIATE_JOB_
REQUISITION_USING_BLANK_
REQUISITION)

Allows users to create job requisitions using a blank form (a requisition with no values).

---

## Initiate Job Requisition Using Existing
*Chunk ID: OHR-REC-0473 | Chapter: Job Requisitions*

Requisition (IRC_INITIATE_JOB_
REQUISITION_USING_EXISTING_
REQUISITION)

Allows users to create job requisitions based on an existing job requisition.

---

## Initiate Job Requisition Using Job (IRC_
*Chunk ID: OHR-REC-0474 | Chapter: Job Requisitions*

INITIATE_JOB_REQUISITION_FROM_JOB)

Allows users to create job requisitions based on a job.

---

## Initiate Job Requisition Using Position
*Chunk ID: OHR-REC-0475 | Chapter: Job Requisitions*

(IRC_INITIATE_POSITION_BASED_JOB_
REQUISITION)

Allows users to create job requisitions based on a position.

---

## Profile Options Controlling Requisition Behavior
*Chunk ID: OHR-REC-0476 | Chapter: Job Requisitions*

When users create a job requisition based on a job or position, these profile options control a few behaviors.

• PER_DEFAULT_GRADE_FROM_JOB_POSITION: The grade value is defaulted if requested with this profile
option.
• PER_ENFORCE_VALID_GRADES: If the profile option is set accordingly, you can only select grades which are
valid for this job or position.
• ORA_IRC_REQ_DEFAULT_SHORT_POSTING_DESC_FROM_PROFILE_DESC_ENABLED: The short description is
defaulted from the Profile Description of the profile only if the profile option is set.

---

## Job Requisitions
*Chunk ID: OHR-REC-0477 | Chapter: Job Requisitions*

• ORA_IRC_REQ_DEFAULT_RESP_QUAL_FROM_PROFILE_ENABLED: You can define if responsibilities and
qualifications must be defaulted from the profile when creating a requisition using a job or position. This profile
option is off by default.
• ORA_POS_HIRING_STATUS_FILTER: If the profile option is set accordingly, the Show Only Approved Positions
check box is displayed next to the selector. This option allows users to select a position to create a requisition.
When this option is selected (it's selected by default), only positions with the Approved hiring status are
available for selection. When the option isn't selected, all positions can be selected, regardless of their hiring
status. If the user selects a position whose hiring status isn't Approved, a warning message is displayed to
ensure this was done on purpose.
If you don't want to give recruiters the ability to select positions whose hiring status isn't approved, this check
box can be hidden using the Create Requisition action in HCM Experience Design Studio. Hiding this option is
useful for companies with a policy of not creating a job requisition until a position is approved. On the other
hand, showing this option is useful for companies who allow creating a job requisition in advance of when
the position is approved, because the recruiting interview and selection process may take a little while as the
position becomes approved. Remember that offers are stricter than requisitions: an offer's proposed start date
must be on or after the time when its associated position's hiring status reaches the Approved state.

---

## Enable Full Job Requisition Creation by Hiring Managers
*Chunk ID: OHR-REC-0478 | Chapter: Job Requisitions*

You can allow users without the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION), usually hiring
managers, to enter all the details of a requisition when they create a job requisition, instead of only a small subset of the
information.
When initiating a job requisition, hiring managers go through the same guided process as the recruiters, where all
sections and fields are available.
To enable this feature, you need to enable the profile option
IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED at the Site level. Then, hiring managers can create
standard job requisition, pipeline job requisitions, and position-based job requisitions.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.
Related Topics
• Create and Edit Profile Options

---

## Enable Job Requisition Creation When Requesting a New
*Chunk ID: OHR-REC-0479 | Chapter: Job Requisitions*

Position
You can allow users to create a job requisition while requesting a new position or duplicating an existing one.
A section called Requisition Details is available. Not all requisition fields are visible in the Requisition Details section,
only a small subset of the standard
Here's what to do
1. Add Requisition Details Section in Position Creation Flow
2. Select Requisitions Fields to Make Visible in Requisition Details Section
3. Configure Job Requisitions to be Automatically Approved

---

## Add Requisition Details Section in Position Creation Flow
*Chunk ID: OHR-REC-0480 | Chapter: Job Requisitions*

You can create rules in Transaction Design Studio to add the Requisition Details section in the request a position
creation flow.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Request a New Position.
5. Click Add to create and configure a rule.
6. In the Basic Details section, enter a name and description for the rule. You can select a business unit and roles.
7. In the Show or Hide Regions section, set the Requisition Details region to Visible.
8. Click Save and Close.

---

## Select Fields in Requisition Details Section
*Chunk ID: OHR-REC-0481 | Chapter: Job Requisitions*

You can also create rules in Transaction Design Studio to decide which requisition fields are visible in the Requisition
Details section. You can create rules with these two actions:
• Request a New Position
• Position Details
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Position Details.
5. Click Add to create and configure a rule.
6. In the Basic Details section, enter a name and description for the rule. You can select a business unit and roles.
7. In the Page Attributes section, select the Requisition Details region.

---

## Job Requisitions
*Chunk ID: OHR-REC-0482 | Chapter: Job Requisitions*

8. Decide which fields you want to make visible and required.
Note: Some fields are always required, but can still be configured as Not Visible. You should use such a
configuration only in situations where you know the user won't have to provide a value because a value
will always be defaulted for the field. Otherwise an error could occur on requisition creation since these are
required values.
9. Click Save and Close.

---

## Configure Job Requisitions to be Automatically Approved
*Chunk ID: OHR-REC-0483 | Chapter: Job Requisitions*

You can configure job requisitions to be automatically approved if they have been created from a position.
Use the Requisition Creation Source attribute in requisition approval rules. This attribute contains the ORA_POSITION
value which indicates if the requisition was created using the Request a New Position or Duplicate Position action. If the
requisition wasn't created while creating a position, the value is null.

---

## Example of Controlling Job Requisitions Visibility for a
*Chunk ID: OHR-REC-0484 | Chapter: Job Requisitions*

User
Job requisition visibility can range from viewing few requisitions to viewing all requisitions. By default, users can view
job requisitions for their own team and those of their subordinates. This can be an issue when a user, such as a recruiter,
needs access to more job requisitions, or when a user has access to too many requisitions but only needs access to
some requisitions within their job responsibility.
Let’s walk through an example of a recruiter user who currently has default access but needs to view more requisitions
within a certain recruiting location. Here are the steps to configure this scenario:
1.
2.
3.
4.

Create a job requisition security profile.
Identify the user's role that contains job requisition privileges.
Verify the job requisition security profiles.
Verify the area of responsibility aligns to the security profile.
Watch video

---

## Create a Job Requisition Security Profile
*Chunk ID: OHR-REC-0485 | Chapter: Job Requisitions*

For this example, we’ll create a security profile for job requisitions secured by recruiting location.
1. In My Client Groups, click Workforce Structures.
2. On the Workforce Structures page, in the Security Profiles section, click Job Requisition Security Profiles.
3. On the Job Requisition Security Profiles page, click Search to see the list of available security profiles. By
default, the View My Team’s Requisitions and View All Job Requisitions are displayed.
4. Click Create to add a new security profile for job requisitions secured by recruiting location.
5. On the Create Job Requisition Security Profile page, enter a name. For example, Job Requisition Secured by
Recruiting Location.
6. In the Area of Responsibility section, select the options Secure by Area of Responsibility and Secure by
Location. Take note of the responsibility type on the new job requisition security profile.

---

## Job Requisitions
*Chunk ID: OHR-REC-0486 | Chapter: Job Requisitions*

7. You can secure the security profile by hiring team types. In the Hiring Team Member Type section, select the
option Secure by Hiring Team Member Type and select hiring team member types such as Recruiter, Hiring
Manager, and All collaborators.
8. Click Save and Close.
Note: You can create several job requisition security profiles for different hiring team members. For example, if you
want collaborators to view, but not update job requisitions. In that case, the list of hiring team members would be
more targeted on each job requisition security profile.

---

## Identify the User's Role that Contains Job Requisition Privileges
*Chunk ID: OHR-REC-0487 | Chapter: Job Requisitions*

Now that you've created the job requisition security profile, go to the Security Console and find the user with the issue.
1.
2.
3.
4.

In the Navigator menu, go to Tools and click Security Console.
Click the Users tab.
Search for the user having the issue and click the user's name.
In the Roles section, identify the role containing the view job requisition privilege and take note of the role
name or code.
Note: If you don’t know where the job requisition privilege is located, you'll need go back to the role details to
view which privileges sit in which role assigned to the user.

5.
6.
7.
8.
9.
10.

In My Client Groups, click Workforce Structures.
On the Workforce Structures page, in the Data Role section, click Data Roles and Security Profiles.
Search for the role by name or code.
Click Edit.
Click Next to view the security criteria.
In the Job Requisition Security Profile field, select the security profile you created which is Job Requisitions
Secured by Location.
11. Click Next.
12. Click Submit.

---

## Verify the Job Requisition Security Profiles
*Chunk ID: OHR-REC-0488 | Chapter: Job Requisitions*

You now need to verify that the role has the proper job requisition security profile in the Security Console.
1.
2.
3.
4.
5.
6.

In the Navigator menu, go to Tools and click Security Console.
Click the Roles tab.
Search for the role you used earlier.
In the Actions menu, click Edit Role to view the privileges.
In the navigation bar, click Data Security Policies.
Filter the list by requisition using the Privilege column. You can view the conditions of the security profile for
viewing job requisitions. The user can now view job requisitions by recruiting location.

---

## Verify the Area of Responsibility Aligns to the Security Profile
*Chunk ID: OHR-REC-0489 | Chapter: Job Requisitions*

Lastly, verify that the area of responsibility and recruiting location hierarchy of the user.
1. In My Client Groups, click Show More then click Areas of Responsibility.
2. On the Areas of Responsibility page, search for the user and click the user's name.
3. If the user has been assigned an area of responsibility, you can edit it. Or, you can create a new one using
the Add button. Note: When creating an area of responsibility, it's recommended to create one using the
Responsibility from Template option.

---

## Job Requisitions
*Chunk ID: OHR-REC-0490 | Chapter: Job Requisitions*

4. On the Create Responsibility page, verify the existing area of responsibility or select the responsibility type you
noted earlier.
5. You can set the recruiting location hierarchy for this user to define the requisition locations that the user can
access. For example, you could select United States. If you define a specific location, the user will be able to
access requisitions that correspond to the recruiting location selected in their area of responsibility. Note: If the
user needs access to multiple job requisition locations, you need to create another responsibility with the same
responsibility type and recruiting location hierarchy node.
6. Click Submit.

---

## Posting Descriptions for Job Requisitions
*Chunk ID: OHR-REC-0491 | Chapter: Job Requisitions*

You can create posting descriptions in the Recruiting Content Library that recruiters can use when they create job
requisitions. For details, see How do I create posting descriptions to be used in job requisitions?

---

## Configure Job Requisitions to Display a Work
*Chunk ID: OHR-REC-0492 | Chapter: Job Requisitions*

Requirements Section
You can create rules in Transaction Design Studio to display a Work Requirements section in job requisitions so that
recruiters can define specific requirements required for a job.
Like all sections displayed on job requisitions, you can indicate if the Work Requirements section is visible or
not using the Transaction Design Studio. However, you can't configure the fields displayed in that section using
Transaction Design Studio. Since the Work Requirements section is coming from a job profile, you need to edit the
Work Requirements section available on the job profile type to configure which fields are displayed. Not all Work
Requirements fields available on job profiles can be displayed in requisitions. Only the following fields will be visible on
requisitions if they're configured to be shown within the job profile configuration (other fields will not be visible even if
configured to be shown):
• Travel Required
• International Travel Required
• Willing to Relocate
• Work Duration Months
• Work Duration Years
• Work Days
• Work Hours
• Full Time Equivalent
Note: Work Requirements section needs to be subscribed to Recruiting under Person Profile Type configuration.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.

---

## Job Requisitions
*Chunk ID: OHR-REC-0493 | Chapter: Job Requisitions*

4. Select one of these actions: Recruiting - Create Job Requisition or Recruiting - View and Edit Job Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule.
7. You can select a role, one or more recruiting types, and one or more countries for which the rule applies.
◦ If you don't select a role, the rule applies to all roles.

◦ When you select a recruiting type, the rule applies only to job requisitions with the same recruiting type.
◦ When you select a country, the rule applies only to job requisitions for which one of the location is part of

this country. The Primary Location or one of the Other Locations must be part of the selected country. For
example, you select the country "United States". A requisition's location is Pleasanton, California, US. The
rule applies to this requisition.

8. In the Show or Hide Regions section, set the Work Requirements section to Visible.
9. Click Save and Close.

---

## Configure Job Requisitions to Display a Responsibilities
*Chunk ID: OHR-REC-0494 | Chapter: Job Requisitions*

and Qualifications Section
You can create rules in Transaction Design Studio to display fields in job requisitions so that recruiters can define the
responsibilities and qualifications required for job for both internal and external candidates.
Recruiters can provide a different value for internal and external candidates, just like the Description field.
Note: This feature applies to standalone job requisition templates as well. In these templates, the Responsibilities
and Qualifications fields are always visible; it's not possible to configure their visibility. Also, the Responsibilities and
Qualifications fields aren't available when creating a job requisition template for jobs or for positions. The content
provided in the Responsibilities and Qualifications fields of a job requisition can be displayed on career sites and is
available to be used by job distribution partner services. However, this content isn't included in LinkedIn job postings
created with the LinkedIn Recruiter System Connect functionality.

---

## Display the Responsibilities and Qualifications Fields
*Chunk ID: OHR-REC-0495 | Chapter: Job Requisitions*

In job requisitions, the Responsibilities and Qualifications fields are hidden by default and aren't required. To display
them, follow these steps.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select one of these actions: Recruiting - Create Job Requisition or Recruiting - View and Edit Job
Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule. You can select a role name, recruiting
type, and country.
7. In the Page Attributes section, select the Posting Description region.
8. Configure the following fields as being visible. You can also make them required.
◦ Qualifications for External Candidates

---

## Job Requisitions
*Chunk ID: OHR-REC-0496 | Chapter: Job Requisitions*

◦ Qualifications for Internal Candidates
◦ Responsibilities for External Candidates
◦ Responsibilities for Internal Candidates
9. Click Save and Close.

---

## Define Responsibilities and Qualifications
*Chunk ID: OHR-REC-0497 | Chapter: Job Requisitions*

You can use the Posting Description category in the Recruiting Content Library to define responsibilities and
qualifications. Note that the Posting Description category is also used to define the posting description of a job
requisition. When the Description, Responsibilities, and Qualifications fields are defined and the recruiter selects them
when creating a job requisition, the three values are defaulted to the requisition. Recruiters can override the content and
personalize it, as needed.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library

2. On the Recruiting Content Library page, click Create.
3. On the Create Content Item page, select the Posting Description category.
4. Enter content in the Responsibilities and Qualifications fields. You can use the rich text editor features to
format the text.
5. Complete the other fields like any other content item.

---

## Enable the Profile Option for the Default Responsibilities and Qualifications
*Chunk ID: OHR-REC-0498 | Chapter: Job Requisitions*

You can define if responsibilities and qualifications must be defaulted from the profile when creating a requisition using
a job or position.
You need to enable the profile option ORA_IRC_REQ_DEFAULT_RESP_QUAL_FROM_PROFILE_ENABLED at the Site
level. This profile option is off by default.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_REQ_DEFAULT_RESP_QUAL_FROM_PROFILE_ENABLED.
6. Set the profile value at the Site level to Yes.
7. Click Save and Close.

Related Topics
• Create and Edit Profile Options

---

## Configure Job Requisitions to Display a Skills Section
*Chunk ID: OHR-REC-0499 | Chapter: Job Requisitions*

You can create rules in Transaction Design Studio to display a Skills section in job requisitions so that recruiters can
define skills required for a job.

---

## Job Requisitions
*Chunk ID: OHR-REC-0500 | Chapter: Job Requisitions*

Note: Skills section needs to be subscribed to Recruiting under Person Profile Type configuration.

---

## Display the Skills Section
*Chunk ID: OHR-REC-0501 | Chapter: Job Requisitions*

The Skills section in job requisitions is hidden by default and isn't required. To display the Skills section, you need to
create a rule in Transaction Design Studio using these actions:
• Recruiting - Create Job Requisition
• Recruiting - View and Edit Job Requisition
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select one of these actions: Recruiting - Create Job Requisition or Recruiting - View and Edit Job
Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule.
7. You can select a role, one or more recruiting types, and one or more countries for which the rule applies.
◦ If you don't select a role, the rule applies to all roles.

◦ When you select a recruiting type, the rule applies only to job requisitions with the same recruiting type.
◦ When you select a country, the rule applies only to job requisitions for which one of the location is part

of this country. The Primary Location or one of the Other Locations must be part of the selected country.
For example, you select the country "United States". A requisition's location is Pleasanton, California, US.
The rule applies to this requisition.
8. In the Show or Hide Regions section, set the Skills to Visible.
9. Click Save and Close.
When the Skills section is displayed, the Edit button is available when all the following conditions are met:
• The job requisition is in one of these phases: Approval, Job Formatting, Posting, Open.
• The job requisition state isn't Deleted.
• The user has these privileges: Update Job Requisition (IRC_UPDATE_JOB_REQUISITION_PRIV) and Update Job
Requisition After Draft Phase (IRC_UPDATE_JOB_REQUISITION_AFTER_DRAFT_PHASE_PRIV).

---

## Enable the Profile Option
*Chunk ID: OHR-REC-0502 | Chapter: Job Requisitions*

You can define the defaulting behavior for skills on job requisitions created using a job or position by enabling the
profile option ORA_IRC_REQ_DEFAULT_SKILLS_FROM_PROFILE_ENABLED. This profile option is disabled by default.
When you enable it, skills are defaulted from the profile when recruiters create a job requisition based on a job or
position.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_REQ_DEFAULT_SKILLS_FROM_PROFILE_ENABLED.
6. Set the profile value at the Site level to Yes.

---

## Job Requisitions
*Chunk ID: OHR-REC-0503 | Chapter: Job Requisitions*

7. Click Save and Close.
For details, see Create and Edit Profile Options.
All skill content sections configured to be displayed as part of the Job profile type configuration will be displayed in
requisitions. The requisitions will also display the fields configured to be displayed in these content sections in the Job
profile type configuration. (My Client Groups > Profiles > Profile Types > Job).
If many skill content sections are configured to be displayed in the Job profile type configuration, they will all be
grouped into a single Skills section in requisitions. While job requisitions can show many skill content sections defined
in the Job profile type configuration, it's strongly recommended to use a single skill content section in that Job profile
type configuration so that a single skill content section is displayed in requisitions. Furthermore, if you have subscribed
to the Skills Center product, the single skill content section used in the Job profile type configuration should be the one
to which Skills Center is a subscriber. This will help simplify the uptake of future improvements to skill support related to
requisitions.
Consider this information related to skills in job requisitions:
Skills aren't multilingual, it's not possible to translate the name of a skill in many languages. For this reason, it's
recommended to not use skills in multilingual job requisitions because the skill name will always be displayed to
candidates exactly as entered, regardless of the language in which candidates are viewing the requisition.
Skills added to a job requisition are visible to external candidates and internal candidates when they view the details of
the requisition on a career site. They're currently not displayed to agents viewing the requisition details.
When additional skill attribute values are captured on requisitions, only the skill name is displayed to candidates viewing
the requisition details. Other attributes aren't displayed to candidates.

---

## Configure Job Requisitions to Display a Metrics Section
*Chunk ID: OHR-REC-0504 | Chapter: Job Requisitions*

You can create rules in Transaction Design Studio to display a Metrics section in job requisitions so that recruiters can
view various metrics regarding the job applications for a requisition.
The Metrics section displays an OTBI report containing various info about the requisition. The report displayed in the
Metrics section contains these 3 tabs:
• Job Applications
• Source Tracking
• Candidate Type
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - View and Edit Job Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule.
7. In the Page Attributes section, select the Sections in Overview region.
8. Set the Metrics section to Visible.
9. Click Save and Close.

---

## Job Requisitions
*Chunk ID: OHR-REC-0505 | Chapter: Job Requisitions*

What to do next
You can replace the report displayed in the Metrics section by a different report using Page Composer. You can edit the
Overview page and find the region containing the report. This region has a BI Catalog Path property. Replace the current
path with the path of the report you want to use. The custom report must accept the requisition ID as a prompt as this is
the identifier which can be used in the report to display only information relevant to the current requisition.
You can also add a contextualized OTBI report in other requisition pages using Page Composer. The Requisition ID of
the current requisition can be passed as a parameter in various requisition pages to show an OTBI report related to the
current requisition. The Requisition ID can be passed as a parameter in reports added to the following requisition tabs:
• Overview
• Details
• Job Formatting
• Progress
• Interviews
• Feedback
For the requisition ID to be passed to the report, the following token must be used:
#{backingBeanScope.DetailsBean.promptFilterValue}

---

## How to Configure Job Requisition DFFs as Visible in
*Chunk ID: OHR-REC-0506 | Chapter: Job Requisitions*

Some Places and Not Visible in Others
When a descriptive flexfield (DFF) is configured as Required, it’s visibility can’t be changed. If you want a DFF to be
required and visible in some places, and hidden in other places, you need to create rules in Transaction Design Studio.
Here’s an example to set a DFF as required and visible while creating a job requisition, but hidden in a career site filter
panel. This allows the hiring team to capture important information in the DFF when creating requisitions, without
exposing information that's not relevant to candidates.
Before you start
This feature requires Oracle Search.
Here's what to do
1. Configure DFFs as Not Required
2. Create Rule to Configure DFFs as Required
3. Add Job Requisition Flexfields as Search Filters in Career Sites

---

## Configure DFFs as Not Required
*Chunk ID: OHR-REC-0507 | Chapter: Job Requisitions*

You configure descriptive flexfields (DFFs) as not required so you can change their visibility.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Job Requisition Descriptive Flexfields.
4. Click the task name.

---

## Job Requisitions
*Chunk ID: OHR-REC-0508 | Chapter: Job Requisitions*

5. On the Job Requisition Descriptive Flexfields page, select the task and click the Edit icon.
6. Select each flexfield and under the Context Segments section, clear the Required check box.
7. Click Save and Close.
8. On the Job Requisition Descriptive Flexfields page, click Deploy Flexfield.

---

## Create Rule to Configure DFFs as Required
*Chunk ID: OHR-REC-0509 | Chapter: Job Requisitions*

You create a rule in Transaction Design Studio to configure description flexfields (DFFs) as Required.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Create Job Requisition.
5. Click Add to create a rule.
6. In the Basic Details section, enter a name and a description for the rule.
7. In the Page Attributes section, select the Details region.
8. Set the Job Requisition Descriptive Flexfield to Visible.
9. Click the Edit icon next to the Job Requisition Descriptive Flexfield.
10. Select the Required option for each flexfield that needs to be required.
11. Click Done.
12. Click Save and Close.
Related Topics
• Add Job Requisition Flexfields as Search Filters in Career Sites

---

## Add Job Requisition Flexfields as Search Filters in Career Sites
*Chunk ID: OHR-REC-0510 | Chapter: Job Requisitions*

You can add additional job requisition fields to the Job Information section within job descriptions on your external
career sites so that your external candidates get more information about the job.
Here's what to do
1.
2.
3.
•

---

## Create Job Requisition Descriptive Flexfields
*Chunk ID: OHR-REC-0511 | Chapter: Job Requisitions*

Make Flexfields Visible in Job Requisitions
Make Flexfields Searchable on Career Sites
This feature requires Oracle Search.
Watch video

---

## Create Job Requisition Descriptive Flexfields
*Chunk ID: OHR-REC-0512 | Chapter: Job Requisitions*

1. Go to the Setup and Maintenance work area and click the Tasks icon.
2. Click Search.

3.
4.
5.
6.

---

## Job Requisitions
*Chunk ID: OHR-REC-0513 | Chapter: Job Requisitions*

Search for the task Job Requisition Descriptive Flexfields.
Click the task name.
On the Job Requisition Descriptive Flexfields page, click the Edit icon.
In the Global Segments section, click the Create icon to create a job requisition descriptive flexfield segment.
Note: Only character data type is supported for flexfields.

7. Select a value set.
8. Click Save and Close.
9. On the Job Requisition Descriptive Flexfields page, click Deploy Flexfield.

---

## Make Flexfields Visible in Job Requisitions
*Chunk ID: OHR-REC-0514 | Chapter: Job Requisitions*

To make the job requisition flexfields visible, you need to edit both the Recruiting - Create Requisition and Recruiting View and Edit Requisition actions in Transaction Design Studio. The configuration is the same for both actions.
1. Access a sandbox which includes HCM Experience Design Studio.
a. Click the Navigator menu.
b. Expand the Configuration section and click Sandboxes.
c. Create a sandbox or select one which includes HCM Experience Design Studio.
2. On the Home page, go to My Client Groups.
3. In the Quick Actions menu, click HCM Experience Design Studio.
4. Click the Transaction Design Studio tab.
5. Select the action Recruiting - Create Requisition.
6. Click Add to create a new rule to display flexfields or edit an existing rule.
7. In the Page Attributes section, select the Details region.
8. Set the Job Requisition Descriptive Flexfield to Visible.
9. Click the Edit icon to edit the flexfield. Select a flexfield content code and a flexfield attribute. Set the field as
being visible. Even though all configured flexfields are shown in the menu and can be selected, only global
segments with character data type can be used as filters.
Note: The Required field isn't functional. If you change it, it won't have any effect.
10. Click Done.
11. Click Save and Close.
12. Repeat the same steps for the Recruiting - View and Edit Requisition action.

---

## Make Flexfields Searchable on Career Sites
*Chunk ID: OHR-REC-0515 | Chapter: Job Requisitions*

To allow candidates to filter job search results using job requisition flexfields, you need to edit the action Recruiting Define Career Site Search Filters.
1. Select the action Recruiting - Define Career Site Search Filters.
2. Click Add to create a rule or edit an existing rule.
3. In the Basic Details section, you can select a career site in the Site Name field. If no site is selected, the rule
applies to all sites.
4. In the Page Attributes section, select the Search Filters region.
5. Set the Job Requisition Descriptive Flexfield to Visible.
6. You can edit individual flexfields. Click the Edit icon. Select a flexfield content code and a flexfield attribute. Set
the field as being visible. Even though all configured flexfields are shown in the menu and can be selected, only
global segments with character data type can be used as filters.
Note: The Required field isn't functional. If you change it, it won't have any effect.
7. Click Done.

---

## Job Requisitions
*Chunk ID: OHR-REC-0516 | Chapter: Job Requisitions*

8. Click Save and Close.
What to do next
Publish the sandbox to make the changes visible.

---

## Add Job Requisition Flexfields as Search Filters in Career Sites
*Chunk ID: OHR-REC-0517 | Chapter: Job Requisitions*

You can add additional job requisition fields to the Job Information section within job descriptions on your external
career sites so that your external candidates get more information about the job.
Here's what to do
1.
2.
3.
•

---

## Create Job Requisition Descriptive Flexfields
*Chunk ID: OHR-REC-0518 | Chapter: Job Requisitions*

Make Flexfields Visible in Job Requisitions
Make Flexfields Searchable on Career Sites
This feature requires Oracle Search.
Watch video

---

## Create Job Requisition Descriptive Flexfields
*Chunk ID: OHR-REC-0519 | Chapter: Job Requisitions*

1.
2.
3.
4.
5.
6.

Go to the Setup and Maintenance work area and click the Tasks icon.
Click Search.
Search for the task Job Requisition Descriptive Flexfields.
Click the task name.
On the Job Requisition Descriptive Flexfields page, click the Edit icon.
In the Global Segments section, click the Create icon to create a job requisition descriptive flexfield segment.
Note: Only character data type is supported for flexfields.

7. Select a value set.
8. Click Save and Close.
9. On the Job Requisition Descriptive Flexfields page, click Deploy Flexfield.

---

## Make Flexfields Visible in Job Requisitions
*Chunk ID: OHR-REC-0520 | Chapter: Job Requisitions*

To make the job requisition flexfields visible, you need to edit both the Recruiting - Create Requisition and Recruiting View and Edit Requisition actions in Transaction Design Studio. The configuration is the same for both actions.
1. Access a sandbox which includes HCM Experience Design Studio.
a. Click the Navigator menu.
b. Expand the Configuration section and click Sandboxes.
c. Create a sandbox or select one which includes HCM Experience Design Studio.
2. On the Home page, go to My Client Groups.
3. In the Quick Actions menu, click HCM Experience Design Studio.
4. Click the Transaction Design Studio tab.
5. Select the action Recruiting - Create Requisition.
6. Click Add to create a new rule to display flexfields or edit an existing rule.
7. In the Page Attributes section, select the Details region.
8. Set the Job Requisition Descriptive Flexfield to Visible.

---

## Job Requisitions
*Chunk ID: OHR-REC-0521 | Chapter: Job Requisitions*

9. Click the Edit icon to edit the flexfield. Select a flexfield content code and a flexfield attribute. Set the field as
being visible. Even though all configured flexfields are shown in the menu and can be selected, only global
segments with character data type can be used as filters.
Note: The Required field isn't functional. If you change it, it won't have any effect.
10. Click Done.
11. Click Save and Close.
12. Repeat the same steps for the Recruiting - View and Edit Requisition action.

---

## Make Flexfields Searchable on Career Sites
*Chunk ID: OHR-REC-0522 | Chapter: Job Requisitions*

To allow candidates to filter job search results using job requisition flexfields, you need to edit the action Recruiting Define Career Site Search Filters.
1. Select the action Recruiting - Define Career Site Search Filters.
2. Click Add to create a rule or edit an existing rule.
3. In the Basic Details section, you can select a career site in the Site Name field. If no site is selected, the rule
applies to all sites.
4. In the Page Attributes section, select the Search Filters region.
5. Set the Job Requisition Descriptive Flexfield to Visible.
6. You can edit individual flexfields. Click the Edit icon. Select a flexfield content code and a flexfield attribute. Set
the field as being visible. Even though all configured flexfields are shown in the menu and can be selected, only
global segments with character data type can be used as filters.
Note: The Required field isn't functional. If you change it, it won't have any effect.
7. Click Done.
8. Click Save and Close.
What to do next
Publish the sandbox to make the changes visible.

---

## Configure a Contextual Journey for Create Job
*Chunk ID: OHR-REC-0523 | Chapter: Job Requisitions*

Requisition
You can configure contextual journeys for the Create Job Requisition action. A journey comprises a checklist or a set of
tasks that help automate routine or special processes effectively in your organization.
Based on the contextual journey setup, when users click the Create Job Requisition quick action from either My Team or
My Client Groups, a single contextual journey or a list of eligible contextual journeys are displayed and users can launch
the contextual journey to accomplish the action.
You configure contextual journeys from the Checklist Templates setup page.
Before you start
• You need the function privilege Manage Journey (PER_MANAGE_CHECKLIST_TEMPLATE_PRIV) to work on
checklist templates.
• You first need to enable the profile option ORA_PER_CONTEXTUAL_JOURNEYS_ENABLED at the site level.

---

## Job Requisitions
*Chunk ID: OHR-REC-0524 | Chapter: Job Requisitions*

Here's what to do
1. In the Setup and Maintenance work area, search for the task Checklist Templates.
2. On the Checklist Templates page, click Create.
3. In the Create Checklist window, complete the fields.
◦ Name: Enter a name for the checklist.

◦ Category: Select Contextual Journey.
◦ Archive After Months: Enter the number of months after which the checklist can be archived.
◦ Purge After Months: Enter the number of months after which the checklist can be purged.

4. Click OK.
5. Complete the fields in the General tab.
◦ Context: Select the context where the quick action will appear: My Team or My Client Groups.

◦ Contextual Action: Select Create Job Requisition.
◦ Status: Select Active.

6. Click Save.
7. On the Tasks tab, click the Create icon and select Create Task to create a task so that the users can perform the
quick action as part of the contextual journey. Complete the fields in the Tasks tab.
◦ Name: Enter a name for the task.

◦ Sequence: 1 is selected by default.
◦ Required: Select this option.
◦ Performer: The person who will perform the task. If you select Line Manager, the task will be displayed

under My Team. If you select Areas of Responsibility, the task will be displayed under My Clients Group.
Task Type: Select Application Task.

◦
◦ Application Task: Select Create Job Requisition.
◦ Status: Select Active.
8. Click Save and Close.
Related Topics
• Create and Edit Profile Options
• Overview of Contextual Journeys

---

## Force Users to Access Sections While Creating Job
*Chunk ID: OHR-REC-0525 | Chapter: Job Requisitions*

Requisitions
You can define if sections within a job requisition need to accessed or not by users. When sections are configured as
required, users who create job requisitions or modify draft job requisitions need to access and open these sections in
the requisition to be able to save the requisition or submit it for approval.
If fields within a required section are configured as Required, users won’t be able to leave the section until those
required fields are filled. Also, if users don’t access required sections, an error message is displayed indicating which
ones need to be accessed to proceed with the selected action.

---

## For users who can only initiate job requisitions (users without the privilege Update Job Requisition
*Chunk ID: OHR-REC-0526 | Chapter: Job Requisitions*

(IRC_UPDATE_JOB_REQUISITION), the error message is displayed when saving the requisition. For users with the
privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION), the error message is displayed when submitting the
requisition. This allows users to save changes in the requisition even if not all required sections have been visited, while
making sure required sections are visited before submitting.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the actions Recruiting - Create Job Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule. You can select a role name, recruiting
type, and country.
7. In the Show or Hide Regions section, set the Show questionnaire page to Yes to display the Required/Not
Required configuration option for all sections of the requisition.
8. You can change the value of the Required/Not Required configuration option for all sections, except the
How section. This section must be visible every time a new requisition is created. When you set a section as
Required, it's automatically set as Visible.
9. Click Save and Close.

---

## Tips and Considerations
*Chunk ID: OHR-REC-0527 | Chapter: Job Requisitions*

We recommend that you set the Show questionnaire page setting to No when you create a rule. Currently, the
questionnaire page isn't available when users create requisitions, regardless of the value of this setting. If eventually
such questionnaire page support is added for requisitions (in a future release), the setting value will be taken into
consideration. If the setting was set to Yes, users would start seeing the questionnaire page without having asked for
it. For this reason, we recommend that you set the setting value to Yes only to change the value of the Required/Not
Required configuration for a section and change the value back to No when you're done. The values selected for the
Required/Not Required configuration option are kept even if the Show questionnaire page is set to No.
The How section is set as Required by default. Also, the following sections which were previously Required by default
are now Not Required by default:
• Provide Details
• Basic Info
• Hiring Team
• Requisition Structure
Setting a section as Required has the side effect of disabling built-in business rules defined for this section. For
example, the Screening Services section in a job requisition is displayed when screening services such as background
check, assessment, tax credit screening are enabled. If you set the Screening Services section to Required, the section
will always be displayed in job requisitions, regardless if screening services are enabled. Here's another example. The
Provide Details section is available to users who can only initiate the creation of a job requisition by entering a subset
of information. These users don't have the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION) and the
profile option IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED is set to No. If you set the Provide Details
section as Required, the section will always be displayed, regardless of the user's privileges and the profile option value.
For this reason, it's recommended that if you set some sections as being Required, you explicitly define in your rules
which sections must be visible or not and define different rules for each user role requiring different sections to be
visible.
The table presents the built-in business rules for each section, which rules will be disabled if the section is set as
Required.

Section

Rule

How

Not configurable. Only shown in creation.

---

## Provide Details
*Chunk ID: OHR-REC-0528 | Chapter: Job Requisitions*

Can be displayed if:
• User doesn't have the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
• AND Profile option IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED is set to No.

---

## Basic Info
*Chunk ID: OHR-REC-0529 | Chapter: Job Requisitions*

Hiring Team
Requisition Structure
Details
Work Requirements

Can be displayed if:
• User has the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
OR
• User doesn't have the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
• AND Profile option IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED is set to Yes.

---

## Estimated Time to Hire
*Chunk ID: OHR-REC-0530 | Chapter: Job Requisitions*

Can be displayed if:
• Time to Hire is enabled
• AND User has the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
OR
• Time to Hire is enabled
• AND User doesn't have the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
• AND Profile option IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED is set to Yes.

---

## Screening Services
*Chunk ID: OHR-REC-0531 | Chapter: Job Requisitions*

Can be displayed if:
• Background check, assessment, or tax credit is enabled.
• AND User has the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
OR
• Background check, assessment, or tax credit is enabled.
• AND User doesn't have the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
• AND Profile option IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED is set to Yes.

---

## Configure the Automatic Unpost of Job Requisitions
*Chunk ID: OHR-REC-0532 | Chapter: Job Requisitions*

You can configure a job requisition to be automatically unposted from the internal career site, the external career sites,
or both.
Recruiters need to configure the option Automatically Unpost Requisition and select the condition when the unpost will
happen using the option Automatically Unpost Condition.
Here's what to do
1. Add Specific Fields Using Transaction Design Studio
2. Create Fast Formula Used as Condition for Job Requisitions
Watch video

---

## Add Specific Fields Using Transaction Design Studio
*Chunk ID: OHR-REC-0533 | Chapter: Job Requisitions*

The fields Automatically Unpost Requisition and Automatically Unpost Condition aren't displayed by default in job
requisitions. You need to make them visible using Transaction Design Studio.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select one of these actions: Recruiting - Create Job Requisition or Recruiting - View and Edit Job
Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule.
7. You can select a role, one or more recruiting types, and one or more countries for which the rule applies.

◦ If you don't select a role, the rule applies to all roles.
◦ When you select a recruiting type, the rule applies only to job requisitions with the same recruiting type.
◦ When you select a country, the rule applies only to job requisitions for which one of the location is part

of this country. The Primary Location or one of the Other Locations must be part of the selected country.
For example, you select the country "United States". A requisition's location is Pleasanton, California, US.
The rule applies to this requisition.
8. In the Show or Hide Regions section, make sure the Configuration section is visible.
9. In the Page Attributes section, select the Configuration region. Then set the field Automatically Unpost
Requisition to visible. You can also set it as required.
10. Click Save and Close.

---

## Create Fast Formula Used as Condition for Job Requisitions
*Chunk ID: OHR-REC-0534 | Chapter: Job Requisitions*

You can create fast formulas and use them as conditions for job requisitions using the fast formula type Recruiting Job
Requisition.
1. In the Setup and Maintenance work area, use the Fast Formulas task.
2. On the Fast Formulas page, select Create in the Actions menu.

---

## Job Requisitions
*Chunk ID: OHR-REC-0535 | Chapter: Job Requisitions*

3. On the Create Fast Formula page, enter a name for the formula. For the Type field, select Recruiting Job
Requisition. Complete the other fields as needed.
4. Click Continue.
5. Enter formula details in the Formula Text section.
6. Click Compile.
7. Click Save.
When you run the scheduled process Publish Job Requisitions, the application verifies if requisitions must be
automatically unposted according to the automatic unpost configuration.

---

## Enable Managers to Initiate a Job Requisition to Direct
*Chunk ID: OHR-REC-0536 | Chapter: Job Requisitions*

Reports
To allow managers to initiate a job requisition to direct reports, you need to set up the responsive layout for My Team
page.
This is done by enabling these profile options at the Site level:
• HCM_RESPONSIVE_PAGES_ENABLED
• PER_MY_TEAM_RESPONSIVE_ENABLED
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
HCM_RESPONSIVE_PAGES_ENABLED.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.
8. Perform the same steps for the profile option PER_MY_TEAM_RESPONSIVE_ENABLED.
Related Topics
• Create and Edit Profile Options

---

## How Locations and Work Locations Work Together
*Chunk ID: OHR-REC-0537 | Chapter: Job Requisitions*

When you create a job requisition, you can use the work location of a job requisition as the location of a job posted on
career sites. This is done by selecting both the location and work location of the requisition.
To facilitate the process and to help properly align the location and work location, here's what happens:
• When a job requisition is created, the primary location of the requisition is defaulted to the geography (if there
is one) associated to the work location, if the work location is defaulted from the current user's assignment or
from a position.

• If this geography isn't part of the geography hierarchy used by Oracle Fusion Cloud Recruiting, the application
will look at the parent geographies until a geography that's part of the geography hierarchy is found.
• The primary location is defaulted only if there's not already a primary location selected on the requisition
(selected by the user or defaulted from another source).
• The Primary Location drop-down shows the first 25 configured locations in alphabetical order, from the
geography hierarchy. If a location isn't available in the drop-down, you can do a search using keyword in the
Primary Location field.
• For a geography to be successfully associated to a work location, the tax validation configuration for the No
Styles Format address style of the work location's address country (which is configured using the Manage
Geographies task under Setup and Maintenance) must:

◦ Include only contiguous geography types (there can't be unselected geography types between selected
◦

geography types).
Include only geography types which can be provided as part of the address when managing locations
(which is configured using the Manage Locations task under Setup and Maintenance).

The table presents different scenarios of when the locations and work locations are used.

Scenario
You create a job requisition from a blank
requisition.

Result
• The hiring manager is defaulted as the current user.
• The primary work location is defaulted to the current user's assignment.
• The primary location is defaulted to the geography associated to the primary work location only if
it hasn't already been provided by the user or defaulted from another source.

---

## You create a job requisition from a
*Chunk ID: OHR-REC-0538 | Chapter: Job Requisitions*

requisition template.

• The primary location is selected in the How section.
• If there's no hiring manager on the template, the hiring manager is defaulted from the current
user.
no work location is defaulted from the template, the primary work location is defaulted to the
◦ Ifcurrent
user's assignment. The work location is defaulted only if it's geographically aligned with
the primary location.
• If there's a hiring manager on the template, the hiring manager is defaulted from the template.

You create a job requisition from a job.

• If no template is associated to the job or if there's no hiring manager on the template, the hiring
manager is defaulted from the current user.
no work location is defaulted from the template, the primary work location is defaulted to the
◦ Ifcurrent
user's assignment.
a primary location is defaulted from the template, the work location is defaulted only if it's
◦ Ifgeographically
aligned with the primary location or one of the other locations. If no primary
location is defaulted from the template, the primary location is defaulted to the geography
associated to the work location.
• If there is a hiring manager on the template, the hiring manager is defaulted from the template.

---

## You create a job requisition from a
*Chunk ID: OHR-REC-0539 | Chapter: Job Requisitions*

position.

• If a work location is defaulted from the position and no primary location is defaulted from the
template associated to the position, the primary location is defaulted to the geography associated
to the work location.

---

## Job Requisitions
*Chunk ID: OHR-REC-0540 | Chapter: Job Requisitions*

Result
• If no template is associated to the position and its job or if there is no hiring manager on the
template, the hiring manager is defaulted from the current user.
no work location is defaulted from the position, the primary work location is defaulted to the
◦ Ifcurrent
user's assignment.
a primary location is defaulted from the template, the work location is defaulted only if it's
◦ Ifgeographically
aligned with the primary location or one of the other locations.
no primary location is defaulted from the template, the primary location is defaulted to the
◦ Ifgeography
associated to the work location.

---

## Configure the Organization Tree List of Values
*Chunk ID: OHR-REC-0541 | Chapter: Job Requisitions*

The Organization field available to recruiting users when they create job requisitions requires specific configuration to
display a list of valid values.
Here are the steps to configure the Organization field so that recruiting users see the organization that they need when
they create a job requisition.
1.
2.
3.
4.

---

## Verify the Organization Tree Code
*Chunk ID: OHR-REC-0542 | Chapter: Job Requisitions*

Flatten the Organization Tree
Confirm Data Role Assigned to User
Verify the Organization Tree Being Used
Watch video

---

## Verify the Organization Tree Code
*Chunk ID: OHR-REC-0543 | Chapter: Job Requisitions*

You need to verify the organization tree code to make sure it doesn't contain any spaces. Here's an example of a code
without any spaces: ORC_ORC_TREE.
If the tree code contains spaces, you'll need to duplicate the tree. Here's how to proceed.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, search for the task Manage Organization Trees.
Click the task name.
On the Manage Organization Trees page, locate the active recruiting organization tree, and select it.
In the Actions menu, select Duplicate.
In the Create Tree window, enter a new name and new code. Make sure that the code doesn't contain any
spaces. Select the tree version, if applicable.
6. Click Save and Close.
7. You need to set the tree status to Active.
a. On the Manage Organization Trees page, select the tree you just created.
b. Click the Actions menu, and set the tree status to Active.
8. You need to run an audit to make sure the tree can be active.
a. On the Manage Organization Trees page, select the tree you just created.
b. Click the Actions menu, select Audit then click Online Audit. When the verification is completed, click
Done.

Make sure to go back to the original active recruiting tree and set its status to Inactive.

---

## Flatten the Organization Tree
*Chunk ID: OHR-REC-0544 | Chapter: Job Requisitions*

You need to flatten the organization tree to display the organization tree values.
1.
2.
3.
4.
5.
6.
7.
8.

In the Setup and Maintenance work area, search for the task Manage Organization Trees.
Click the task name.
On the Manage Organization Trees page, locate the active recruiting organization tree and select it.
In the Actions menu, select Flatten, then Row Flattening.
On the next page, select Online Flattening.
A confirmation window will display once completed. Click OK.
Click Done.
Click Save and Close.

---

## Confirm Data Role Assigned to User
*Chunk ID: OHR-REC-0545 | Chapter: Job Requisitions*

You need to confirm that the correct data role was assigned to the user and that the data role includes the appropriate
organization security profile.
1.
2.
3.
4.

In My Client Groups, click Workforce Structures.
On the Workforce Structures page, click the task Preview HCM Data Security.
On the Preview HCM Data Security page, enter the name of the user you need to verify.
When the currently assigned roles appear, view the organization security profile column. If the organization
needed isn't listed, a new data role will need to be assigned to the user.

---

## Verify the Organization Tree Being Used
*Chunk ID: OHR-REC-0546 | Chapter: Job Requisitions*

You need to verify that Oracle Fusion Cloud Recruiting is using the correct organization tree.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Recruiting Management section and click Edit.
3. Verify that the organization tree selected is the correct tree.

---

## Define Collaborator Types
*Chunk ID: OHR-REC-0547 | Chapter: Job Requisitions*

You can define collaborator types that recruiters can select while creating job requisitions and job offers. Collaborator
types help recruiters define the Hiring Team roles more precisely and to better manage communications with members
of the job requisition and offer Hiring Teams.
When a user is added as a collaborator on a job requisition or job offer (regardless of the collaborator type), the user has
the required data security to view this requisition or offer.
Before you start
By default, the Collaborator collaborator type is always visible. You can't disabled it.
Here's what to do

---

## Job Requisitions
*Chunk ID: OHR-REC-0548 | Chapter: Job Requisitions*

1. In the Setup and Maintenance work area, search for the task Manage Common Lookups.
2. Click the task name.
3. Search for the lookup type ORA_IRC_COLLABORATOR_RESP_TYPE.
4. Create new lookups as required. Lookup codes should not begin with the prefix "ORA".

---

## Set Up Pipeline Job Requisitions
*Chunk ID: OHR-REC-0549 | Chapter: Job Requisitions*

Recruiters and hiring managers use pipeline job requisitions to gather candidates who have the skills, background, and
experience your organization is looking for. These candidates can later be added to a standard job requisition for which
they can eventually get hired.
To set up pipeline job requisitions, you need to create a candidate selection process of type Pipeline.
Note: A standard requisition can be created from a template for which a candidate selection process of type pipeline
is selected. In that situation, the candidate selection process selected on the template is ignored by the requisition
(because it is an invalid value for a standard requisition).
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, click Create.
3. On the Create Process page, select the Pipeline process type.
4. Complete the fields as for any other process.
5. Click Save and Continue.
Optionally, you can select the pipeline candidate selection process in a job requisition template.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Job Requisitions
◦ Task: Manage Job Requisition Template
2. On the Job Requisition Templates page, click Create.
3. In the Candidate Selection Process field, select a pipeline process.
4. Complete the fields as for any other process.
5. Click Save.
Users need the privilege Initiate Pipeline Job Requisition (IRC_INITIATE_PIPELINE_JOB_REQUISITION) to create pipeline
requisitions.
Only users with the privilege Add Candidate to Job Requisition (IRC_ADD_CANDIDATE_TO_JOB_REQUISITION) can add
a job application from a pipeline requisition to a linked hiring requisition.

---

## Create an Approval Rule Using Job Requisition Flexfields
*Chunk ID: OHR-REC-0550 | Chapter: Job Requisitions*

You can create job requisition approval rules using job requisition flexfields.
To enable this feature, you first need to create descriptive flexfields and then use these flexfields to create job
requisition approval rules.

---

## Create Descriptive Flexfields
*Chunk ID: OHR-REC-0551 | Chapter: Job Requisitions*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Job Requisitions
◦ Task: Job Requisition Descriptive Flexfields

2.
3.
4.
5.

On the Job Requisition Descriptive Flexfields page, click the Edit icon.
In the Global Segments section, click Create to create segments.
Click Save and Close.
On the Job Requisition Descriptive Flexfields page, click Deploy Flexfield to deploy the flexfield in the
environment.

---

## Create Job Requisition Approval Rule
*Chunk ID: OHR-REC-0552 | Chapter: Job Requisitions*

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.

On your Home page, click the Notifications icon.
On the Notifications page, click Show All.
Click Worklist.
In the menu next to your name, select Administration.
Click the Task Configuration tab.
Search for the task RequisitionApprovalHumanTask.
When the task is displayed, click on the task name.
Click the Edit icon. A message indicates that a flexfield was added.
Click Start Synchronization.
When the synchronization is complete, search for the RequisitionApprovalHumanTask task again.
Click the Assignees tab.
Click on the task to configure it. The flexfield you created is available to create a rule.

---

## Configure the Management Hierarchy for Job
*Chunk ID: OHR-REC-0553 | Chapter: Job Requisitions*

Requisition Approvals
In HCM, each employee can have multiple assignments, and each assignment has its own management chain. All the
assignments for the employee appear in the Directory work area (Me > Directory).

---

## Every assignment can have its own management hierarchy used for approval instead of always relying on primary
*Chunk ID: OHR-REC-0554 | Chapter: Job Requisitions*

assignment as before. As an administrator, you can decide to use the primary assignment or other assignments for the
requisition approval process. Also, you can select the recruiter in the approval chain for requisition approvals.
1. Go to the Tools work area.
2. Click Transaction Console.
3. Click the Approval Rules tab.
4. Select the Approve Job Requisition process and click the Edit icon.
5. Click the Management Hierarchy box.
6. Go to the Management Hierarchy section at the bottom of the page.
7. In the Approval Chain Of field, select one of these options:
◦ Hiring Manager

◦ Requester
◦ Recruiter
◦ User
8. If you select Hiring Manager or Recruiter, you can select an assignment type:
◦ Use primary assignment hierarchy (default value)

◦ Use current assignment hierarchy

---

## Where Can Users See Recruiting Representatives
*Chunk ID: OHR-REC-0555 | Chapter: Job Requisitions*

The Recruiter selector displays recruiters that were recently selected as well as the recruiting representatives.

---

## Prescreening Questionnaires and Questions
*Chunk ID: OHR-REC-0556 | Chapter: Job Requisitions*

10 Prescreening Questionnaires and
Questions
Prescreening Questionnaire
Prescreening questionnaires contain questions specific to a job that candidates answer when they apply for a job.
Prescreening questionnaires appear automatically in job requisitions. For each job requisition, there's an internal
questionnaire for internal candidates and an external questionnaire for external candidates. Prescreening
questionnaires contain two types of questions:
• Disqualification question
• Prescreening question
You can edit prescreening questionnaires in a job requisition as long as there are no candidate job applications for that
job requisition. Here are some things you can do when you edit a prescreening questionnaire in a job requisition.
• You can view the automatically populated disqualification questions, but you can't remove them.
• You can view the prescreening questions added automatically, but you can't edit, add nor remove them.
• You can add and remove prescreening questions added by the user.

---

## Disqualification Question
*Chunk ID: OHR-REC-0557 | Chapter: Job Requisitions*

A disqualification question is a single or multiple answer question that contains the minimum requirements for a
candidate to be eligible for a job.
When candidates apply for a job, it's mandatory to respond to the disqualification questions. Answers to the
disqualification questions decide if candidates move forward in the selection process or are automatically disqualified.
An example of a disqualification question could be "Are you entitled to work in the United States?".
It's the Recruiting Administrator who creates and manages the disqualification questions in the Question Library.
When creating a disqualification question, the administrator can contextualize the question based on the recruiting
organization, location, job family, job function. When a recruiter creates a job requisition, disqualification questions
matching the context of the job requisition are automatically added to the prescreening questionnaires of the job
requisition. The recruiter can't add, edit, or remove disqualification questions.
Note: Disqualification questions aren't added to prescreening questionnaires of job requisition templates.

---

## Create a Disqualification Question
*Chunk ID: OHR-REC-0558 | Chapter: Job Requisitions*

A disqualification question is a single or multiple answer question that contains the minimum requirements
for a candidate to be eligible for a job. When you create disqualification questions, they appear in prescreening
questionnaires.
It's recommended to create folders to organize questions; one folder for disqualification questions, and one folder for
prescreening questions.
Note: The following features aren't supported when you create questions: You can't add images to a question and its
answers. You can't add HTML, attachments, and additional comments.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Question Library
2. On the Questions page, select Recruiting in the Subscriber field.
3. Click Create.
4. On the Create Question page, enter question properties:
◦ Folder: Select the folder where you want to save the question.

◦ Privacy: Select Private if only you can edit the question. If you select Public, anyone who can access the
Question Library can edit the question.

5. Enter the question in the Question Text field.
6. Select the question type. For a disqualification question, you need to select Single Choice or Multiple Choice.
7. Select Score Question to set a score for each answer of the question.
8. Define the context of the question:
a. In the Question Classification field, select Disqualification.
b. In the Candidate Types, select the type of candidates who answer the question: internal candidates,
external candidates, or both.
c. Specify the context when the question is used: Recruiting Organizations, Recruiting Locations, Job
Families, Job Functions.
9. Enter answer properties:
a. Response Type: Select the display of the response in the Response Type field.
10. Click Add to add the responses of the question.
11. Enter a score for each response. Use a negative score for answers that disqualify candidates.
12. If you want to tell the hiring manager and recruiter which question disqualified a job application, click Response
Feedback next to the responses and enter a message. Since the response is negative, you don't need the response
feedback to know which response disqualifies a candidate. It's used to know why such response disqualifies a
candidate. The feedback is not visible to candidates.
13. Set the question status to Active if you want to make the question available for selection when users create job
application questionnaires.
14.Click Save and Close. The question is available in the selected folder.
What to do next

---

## You can translate questions and the short description of the answers (text of the answers when the question offers
*Chunk ID: OHR-REC-0559 | Chapter: Job Requisitions*

predefined answers) without having to sign out and sign in a different language. Use the Translation Editor tool,
represented by the earth logo. Translate the questions before they're being used when candidates apply. Otherwise,
you'll have to create a new version of the questions and provide a new translation.
When you change the context of a disqualification question, job requisitions without candidate applications using these
questions are updated accordingly.
When you create a disqualification question, job requisitions using these questions are updated accordingly once the
Update Job Application Questionnaire scheduled process has run.
Related Topics
• Guidelines for Scoring Questions

---

## Prescreening Question
*Chunk ID: OHR-REC-0560 | Chapter: Job Requisitions*

Prescreening questions are used to ask candidates about their career goal, job preferences, knowledge, and more. If a
prescreening question is configured as required, the candidate can't skip it while applying for the job.
Here's an example of a prescreening question: "How good are your Java skills?"
Prescreening questions are created and managed by the Recruiting Administrator in the Question Library. When
creating a prescreening question, the administrator can specify the classification of the question and can also
contextualize the question based on the recruiting organization, location, job family, job function. When a recruiting
user creates a job requisition, questions available for selection depend on the classification of the question and the
context of the job requisition (recruiting organization, location, job family, job function).
The following question classifications are available:
• Prescreening Question Added Automatically: These questions are automatically added to a job requisition
based on the context of the job requisition. The recruiting user can't edit, add nor remove these questions in a
job requisition. If the recruiting user changes the context of the job requisition, these prescreening questions
might be adjusted. Also, if the context of a question is changed, job requisitions without candidate applications
will be adjusted to align with the automatically added questions (this happens when running a scheduled
process).
• Prescreening Question Added by User: The recruiting user can manually add these questions to a job
requisition, but the questions must match the context of the job requisition. Once there are job applications on
the job requisition, the recruiting user can no longer add or remove these questions. Also, the recruiting user
won't be able to submit a job requisition if manually added questions are invalid.
Prescreening questions can be manually added to job requisition templates by the Recruiting Administrator. When a
recruiting user creates a job requisition based on a template, prescreening questions of the job requisition template are
added to the requisition. The recruiting user can add and remove questions. If the recruiting user changes the context
of a job requisition where there is no candidate application yet, disqualification questions and prescreening questions
added automatically can be added to the requisition or removed if they don't apply to the context of the of requisition.
This ensures that only questions matching the context of the requisition are included. In the case of questions added
manually, the recruiting user won't be able to use them if they no longer match the context of the requisition.
The recruiting user can't edit prescreening responses provided by a candidate. This ensures that the information
provided by the candidate is retained. Only when a recruiting user answered prescreening questions on behalf of the
candidate can those responses be edited by the recruiting user.

---

## Create a Prescreening Question
*Chunk ID: OHR-REC-0561 | Chapter: Job Requisitions*

You create prescreening questions to ask candidates about their career goal, job preferences, knowledge, and more.
It's recommended to create folders to organize questions; one folder for disqualification questions, and one folder for
prescreening questions.
Note: The following features aren't supported when you create questions: You can't add images to a question and its
answers. You can't add HTML, attachments, and additional comments.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Question Library
2. On the Questions page, select Recruiting in the Subscriber field.
3. Click Create.
4. On the Create Question page, enter question properties:
◦ Folder: Select the folder where you want to save the question.

◦ Privacy: Select Private if only you can edit the question. Select Public if anyone can edit the question.
5. Enter the question in the Question Text field.
6. You can enter instructions in the Instructions field. You can use rich text features to format the text. You can also use
URL links
7. Select the question type:
◦ Text

◦ Single Choice
◦ Multiple Choice
◦ No Response
8. If you selected Single Choice or Multiple Choice, you can select the Score Question option to set a score for each
answer of the question.
9. In the Question Classification field, select the type of prescreening question you want. Two options are available:
◦ Prescreening Question Added Automatically: These questions are automatically added to a job requisition
based on the context of the job requisition. You can't add nor remove these questions in a job requisition.
◦ Prescreening Question Added by User: You can manually add these questions to a job requisition. The
questions must match the context of the job requisition. You can remove these questions from the job
requisition. Once there are job applications on the requisition, you can no longer add or remove questions.
10. Select the type of candidates who answer the question.
11. Select the context when the question is used: Recruiting Organizations, Recruiting Locations, Job Families, Job
Functions.
12. In the Response section, select the presentation of the response. Available choices depend on the question type you
selected.
13. Click Add to add the question responses.
14.Enter a score for each answer if you selected the Score Question option.

---

## Prescreening Questionnaires and Questions
*Chunk ID: OHR-REC-0562 | Chapter: Job Requisitions*

15. Set the question status to Active if you want to make the question available for selection when users create job
application questionnaires.
16. Click Save and Close. The question is available in the selected folder.
What to do next
You can translate questions and the short description of the answers (text of the answers when the question offers
predefined answers) without having to sign out and sign in a different language. Use the Translation Editor tool,
represented by the earth logo.
When you create a prescreening question added automatically or when you change the context of a prescreening
question added automatically, job requisitions using these questions are updated accordingly once the Update Job
Application Questionnaire scheduled process has run.

---

## Guidelines for Scoring Questions
*Chunk ID: OHR-REC-0563 | Chapter: Job Requisitions*

Consider the following guidelines when using the Score Question option for questions used in questionnaires.

---

## Prescreening Questions
*Chunk ID: OHR-REC-0564 | Chapter: Job Requisitions*

You can score questions in external and internal prescreening questionnaires filled by candidates when they apply for a
job. This helps rank job applications based on prescreening score.
When you create a prescreening question with a single choice or multiple choice answer, you can select the Score
Question option and set a score to each answer of the question. The application automatically calculates the
questionnaire overall score where such question is used.
When you change the score of a question, you can see the maximum possible score of all impacted questionnaires
adjusted right away. Here's how it works. You can change questions added to questionnaires not being used. Changes
are reflected right away in questionnaires, with the exception of any overwritten score at the questionnaire level. If you
want to change questions in questionnaires being used, consider the following:
• You will need to create a new version of the question if you want to change:

◦ Answer labels, including translation
◦ Context
◦ Question type
◦ Question score
• The new version of the question will be propagated in questionnaires not being used, unless they have
overwritten question's score.

---

## Disqualification Questions
*Chunk ID: OHR-REC-0565 | Chapter: Job Requisitions*

Disqualification questions require a score so that candidates submitting a job application are entered in the selection
process or are automatically disqualified.
When you create a disqualification question, you need to select the Score Question option then define a negative score
for the response that disqualifies candidates. Let's say this disqualification question is added to a questionnaire and it's
the only question in the questionnaire. If the candidate answers Yes, the candidate is automatically disqualified.

Question

Answer

Score

---

## Are you entitled to work in the United States?
*Chunk ID: OHR-REC-0566 | Chapter: Job Requisitions*

Yes

-1

No

A single answer to a negative score of a disqualification question will disqualify a candidate. You no longer need to enter
a big negative score number to cover for all cases of usage with various positive numbers.

---

## Prefill Responses of Prescreening Questions in External
*Chunk ID: OHR-REC-0567 | Chapter: Job Requisitions*

Candidate Job Applications
You can activate a setting so that when a returning external candidate applies for a new job, responses to prescreening
questions are prefilled if the candidate answered the questions in previous job applications.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Recruiting Management section and click Edit.
3. Select the option Prefill Prescreening Questions in External Candidate Applications.
4. Click Save.

---

# Candidate Interviews

## Candidate Interviews
*Chunk ID: OHR-REC-0568 | Chapter: Candidate Interviews*

Create a Candidate Interview Schedule Template
You can create interview schedule templates to help recruiters and hiring managers save time when they create
interview schedules for job requisitions. For example, you can specify a commonly-used conference room or location or
the URL and dial-in information.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Job Requisitions
◦ Task: Interview Schedule Templates
2. On the Interview Schedule Templates page, click Add.
3. Complete the Basic Information section:
a. Enter a title and a code for the interview schedule template.
a. Select the schedule type, either managed by the candidate or the hiring team.
a. Select the Default Template option if you want the interview schedule template to be the default template.
If Recruiting Booster is enabled, the option is displayed for both hiring team managed and candidate
managed schedule templates. If Recruiting Booster isn't enabled, the option is displayed for hiring team
managed schedule templates only.
a. You can define an interview title to indicate the purpose of the interview such as if this is a first interview,
second interview, or a technical interview.
a. You can select a schedule owner who's different from the schedule creator. When users create an interview
schedule using a schedule template, the schedule owner is defaulted from the schedule template. If the
template doesn’t have a named user, the schedule creator is the schedule owner.
4. Complete the Location Details section:
Select the format for the interview: in person, by phone, by web conference. The web conference format generates a
link for the interview. The Use Teams integration option or the Use Zoom integration option is available depending
on the integration enabled within your organization.
a. If you select the Use Teams integration option, define the meeting host. This is the person which Microsoft
Office 365 account is used to generate the Teams link. You can select a specific person or a member of the
hiring team. If you select a collaborator type as the meeting host, but no such collaborator type is defined
on the requisition, the schedule owner will be defaulted as the meeting host on interviews and interview
slots. If you select a collaborator type as the meeting host and the requisition has many users assigned to
this collaborator type, the first user of this collaborator type (the first one displayed in the requisition) will
be the meeting host.
b. If you select the Use Zoom integration option, define the meeting host. This is the person whose Zoom
account is used to generate the Zoom link. You can select a specific person or a member of the hiring team
(recruiter, hiring manager, collaborator). Selecting a hiring team member type is only available on interview
schedule templates and interview schedules. When you select a person, you'll get an error message if the
person you selected didn't authorize the Zoom integration. If you select yourself as the meeting host, you'll
be offered to authorize the Zoom integration if it's not already authorized. If that's the case, you'll can do it
on the page without needing to access the Zoom authorization quick action. When you save an interview
schedule for the first time, the schedule owner (the current user creating the schedule) is asked to authorize

the Zoom integration if not already done. That's because in some situations it's possible to have a meeting
host who hasn't provided the Zoom authorization. When that happens, the schedule owner is used as the
meeting host instead.
Note: The other fields related to web conference are disabled: Phone, Web Conference Link, Access Code.
5. Complete the Settings section:
a. Select which actions candidates can perform on their interviews. See Interview Schedule Settings.
6. Complete the Candidate Info section:
a. Enter more information for the candidate.
- Preschedule details are instructions for candidates before scheduling their interview.
- Postschedule details are instructions for the interview such as directions to the interview location,
instructions on how to join a web conference.
7. Complete the Interviewer Documents section:
a. Include documents attached to the notification sent to interviewers.
- You can include a link to the job posting so that the interviewers can refer to the job description,
qualifications, or other details.
- You can include a link to the resume.
- You can include a .ics attachment so that candidates and interviewers can add the interview to their
calendar. The .ics setting is used for both the interviewer and the candidate, and contains complete
interview location information. The subject text includes the candidate's name.
8. Complete the Candidate Notifications section:
a. Select notification templates to send candidates. Templates provided with the application are selected by
default. You can select notification templates for interview scheduled, canceled, updated, rescheduled and
interview reminder.
b. Complete the Reminders section for candidate managed interview schedules.
9. Complete the Reminders section for candidate managed interview schedules.
a. You can indicate if you want to send a reminder notification to the interview schedule creator when the
schedule has a low number of available interview openings. You can also send a reminder notification
when the schedule is full. The number of available interview openings can decrease when candidates are
scheduling interviews, but also due to time passing (interview openings now being in the past).
10. Click Save and Close.
The template appears on the Interview Schedule Templates page.
11. While the template is still in Draft status, you can translate the template using the Translate Template action available
in the Interview Schedule Templates page.
12. Select the Activate Template action to make the template available for selection on job requisitions.

---

## Candidate Interviews
*Chunk ID: OHR-REC-0569 | Chapter: Candidate Interviews*

Settings for Candidate Managed Interview Schedule

• Candidates can cancel their
interviews on external and internal
career sites. When candidates view a
scheduled interview, they can use the
Cancel Interview action.
Candidates can't make last-minute
changes - Hours Before Interview

• Candidates can reschedule their interviews on external and internal career sites when the
schedule permits it. When candidates view a scheduled interview, they can use the Reschedule
Interview action.

---

## Candidates can cancel
*Chunk ID: OHR-REC-0570 | Chapter: Candidate Interviews*

• Candidates can cancel their interviews on external and internal career sites. When candidates
view a scheduled interview, they can use the Cancel Interview action.

• Select the number of hours before
an interview when candidates can no
longer make changes.

---

## Candidates can schedule on same day
*Chunk ID: OHR-REC-0571 | Chapter: Candidate Interviews*

• Same day scheduling means candidates can schedule an interview on the same day they are
viewing the interviews on the interview scheduling page. For example, if a candidate gets an
interview invitation today, the candidate can see interviews available today.
Candidates can see future interviews - Interview Visibility
• Select the number of weeks or months of the interview schedule to which candidates have access
to when scheduling an interview.
Candidate limit on rescheduling - Reschedule Limit
• Indicate the number of time the candidate can reschedule an interview.
Candidates can't make last-minute changes - Hours Before Interview
• Select the number of hours before an interview when candidates can no longer make changes.

---

## Candidate Interview Notifications
*Chunk ID: OHR-REC-0572 | Chapter: Candidate Interviews*

Notifications are sent to different stakeholders during the candidate interview process.
The following notifications are sent to candidates. They're available in the Recruiting Content Library. You can use them
as is, configure them, or create new ones.
• Interview Canceled Notification
• Interview Reminder Notification
• Interview Reschedule Notification
• Interview Scheduled Notification
• Interview Updated Notification
• Invite to Schedule Interview Notification

---

## Candidate Interviews
*Chunk ID: OHR-REC-0573 | Chapter: Candidate Interviews*

The following notifications are sent to recruiters and hiring managers. They're available in Alerts Composer. You can use
them as is or configure them.
• Interview Canceled Notification to Interviewer (IRC_Intrv_Canceled_Interviewer): Notification sent to the
interviewer when an interview has been canceled.
• Interview Canceled Notification to Requisition Owners (IRC_Intrv_Canceled_ReqOwners): Notification sent to
the recruiter and hiring manager when an interview has been canceled.
• Interview Reminder Notification to Interviewer (IRC_Intrv_Reminder_Interviewer): Notification sent to the
interviewer when a scheduled interview is occurring soon.
• Interview Scheduled Notification to Interviewer (IRC_Intrv_Scheduled_Interviewer): Notification sent to the
interviewer when an interview has been scheduled.
• Interview Scheduled Notification to Requisition Owners (IRC_Intrv_Scheduled_ReqOwners): Notification sent to
the recruiter and hiring manager when an interview has been scheduled.
• Interview Updated Notification to Interviewer (IRC_Intrv_Updated_Interviewer): Notification sent to the
interviewer when an interview has been rescheduled or updated.
• Interview Updated Notification to Requisition Owners (IRC_Intrv_Updated_ReqOwners): Notification sent to the
recruiter and hiring manager when an interview has been rescheduled or updated.
• Interview Schedule With Low Number of Available Openings (IRC_Intrv_Schedule_Low_Openings): Notification
for when there's a low number of available interview openings for a candidate-managed interview schedule
used on a job requisition.
• Interview Schedule With No Available Openings (IRC_Intrv_Schedule_No_Openings): Notification for when there
are no available interview openings for a candidate-managed interview schedule used on a job requisition.
• Interviewer Removed Notification to Interviewer (IRC_Intrv_Removed_Interviewer): Notification sent to the
interviewer when the interviewer is removed from a scheduled interview and when a candidate is invited to
reschedule an interview (candidate managed schedule) and the candidate selects a new interview slot which
has different interviewers than the initial slot.
Note: It’s recommended to not change the recipient token ${InterviewerUserName} in notifications sent to requisition
owners (recruiters and hiring managers). Despite the token referring to the interviewer, the notification does go to
different recipients as explained in each notification description. Changing the recipient could result in unintended
outcomes, like recipients getting duplicated notifications.
The scheduled process that needs to run for the reminder notifications to be sent is Send Interview Reminder
Notification.

---

## Create an Interview Scheduled Notification and Correctly
*Chunk ID: OHR-REC-0574 | Chapter: Candidate Interviews*

Display Interview Location
If you decide to create an interview scheduled notification by copying the content of the notification template, the
groovy expression used in the template will be lost.
To correctly display the interview location details, you need to add the groovy expression in the message text showing
the location information and the InterviewSchedulingLocationSingleLineAddress token. Here's an example.

---

## Candidate Interviews
*Chunk ID: OHR-REC-0575 | Chapter: Candidate Interviews*

Note: The example is using English labels (“Location: ”, “Phone Number: ” and “Access Code: ”). For other languages,
you’ll need to translate these labels in the appropriate language.
<% if (InterviewSchedulingLocationTypeCode == "ORA_IS_LOCATION_PHONE") print("Location:" +
InterviewSchedulingLocationPhoneNumber); %> <% if (InterviewSchedulingLocationTypeCode ==

"ORA_IS_LOCATION_WEBCONFERENCE" && InterviewSchedulingOnlineMeetingProvider != "ORA_IS_TEAMS"
&& InterviewSchedulingOnlineMeetingProvider != "ORA_IS_ZOOM") print("Location:" +

---

## Access Code: " + InterviewSchedulingLocationPhoneNumberPasscode); %> <% if (InterviewSchedulingLocationTypeCode
*Chunk ID: OHR-REC-0576 | Chapter: Candidate Interviews*

== "ORA_IS_LOCATION_WEBCONFERENCE" && (InterviewSchedulingOnlineMeetingProvider == "ORA_IS_TEAMS"
|| InterviewSchedulingOnlineMeetingProvider == "ORA_IS_ZOOM")) { print("Location: " +

---

## InterviewSchedulingLocationWebConferenceLink); if (InterviewSchedulingLocationPhoneNumberPasscode !
*Chunk ID: OHR-REC-0577 | Chapter: Candidate Interviews*

= null && InterviewSchedulingLocationPhoneNumberPasscode != "") print(" Access Code: " +

---

## InterviewSchedulingLocationPhoneNumberPasscode);}%> <% if (InterviewSchedulingLocationTypeCode ==
*Chunk ID: OHR-REC-0578 | Chapter: Candidate Interviews*

"ORA_IS_LOCATION_IN_PERSON") print("Location: " + InterviewSchedulingLocationSingleLineAddress);%>

---

## Candidate Interview Time Zones
*Chunk ID: OHR-REC-0579 | Chapter: Candidate Interviews*

Candidate notifications and interview scheduling areas reflect the candidate's time zone. This ensures that the
candidate and interview coordinators are scheduling interviews at the appropriate times.
When possible, the candidate's time zone is captured and displayed on the scheduling pages. Users creating and
managing interviews can define which time zone to be used. When viewing interview details in read-only areas, the time
is converted to the viewing user's time zone.
• The candidate's time zone is displayed in the Preferences section on the candidate details tab.
Note: The Preferences section isn't displayed on the job application details tab.
• When a Recruiting user schedules an interview on behalf of a candidate, the time zone is displayed next to the
start and end date fields. The time picker defaults to the candidate's time zone.
• When a Recruiting user scheduled an interview, or view a schedule time slot, the user sees the time and time
zone based on their regional preference setting in HCM.
Note: If a candidate doesn't have a preferred time zone defined, notifications will use the interview
organizer's time zone preference.
• For internal candidates, the time zone defined in their regional preference in HCM is used.
• If external candidates have no value set for their preferred time zone, it will be automatically captured based on
the candidate's browser time zone.

---

## Configure the Candidate Selection Process to
*Chunk ID: OHR-REC-0580 | Chapter: Candidate Interviews*

Automatically Send Interview Invitations
You can configure a candidate selection process so that an interview invitation is sent automatically to candidates when
their job applications reach a given point in the candidate selection process. This is done using the Send Interview Invite
action.
You can add the Send Interview Invite action to all phases except the HR phase. You can't add it to terminal states of all
phases (Rejected by Employer, Withdrawn by Candidate). You can add the action to phase-level events, including when
entering or leaving a phase.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, click a process.
3. Click a phase.
4. Add the Send Interview Invite action at the phase or state level.
5. You can define conditions for the action to be executed. You can use predefined conditions, fast formulas used as
conditions, or a combination of both.
6. You can define an interview title to indicate the purpose of the interview such as if this is a first interview, second
interview, or a technical interview. When you schedule an interview for a candidate, the interview title is defaulted
from the interview schedule but you can change it.
7. Click Save and Close.
Results:
When the action Send Interview Invite is configured, a section called Automated Interview Invitation is available in the
Interviews tab of a requisition.

---

## Configure Candidate Interview Durations
*Chunk ID: OHR-REC-0581 | Chapter: Candidate Interviews*

You can configure interview meeting durations and make them available to users when they schedule interviews with
candidates.
The values you enable for the Meeting Duration field are available everywhere the field is displayed. For example:
• When users define slots in candidate-managed interview schedules.
• When users request interviews to be scheduled for candidates (available in Recruiting Booster).
• When interview coordinators change the meeting duration of an interview using the Send Interview Invite
action (available in Recruiting Booster).
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

---

## Candidate Interviews
*Chunk ID: OHR-REC-0582 | Chapter: Candidate Interviews*

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting and Candidate Experience Lookups
2. On the Recruiting and Candidate Experience Lookups page, search for the lookup type
ORA_IRC_IS_MEETING_DURATION.
3. In the Lookup Codes section, select the duration values you want to enable. You can also change the meaning of a
value. For example, you might want to change 1 hour to display as 60 minutes.
It's not recommended to create custom values as the product won't know how to interpret the values.
4. Click Save and Close.

---

## Configure Double Booking of Interviewers
*Chunk ID: OHR-REC-0583 | Chapter: Candidate Interviews*

You can configure the application to allow multiple interviews to be scheduled for the same interviewer at the same date
and time.
Here are scenarios of double booking:
Scenario 1 - Double booking is prevented: John and Mary are booked for an interview on April 14, from 9 am to 10
am. The user tries to schedule Mary for another interview scheduled on April 14, from 9:30 am to 10:30 am. An error
message is displayed indicating that the user can’t schedule the interview at that time because one of the interviewer
has an interview already scheduled.
Scenario 2 - Double booking is allowed: John and Mary are booked for an interview on April 14, from 9 am to 10 am. The
user tries to schedule Mary for another interview scheduled on April 14, from 9:30 am to 10:30 am. No error message is
displayed, double booking isn't prevented.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. On the Search page, search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values, search for the profile option code
ORA_IRC_IS_INTERVIEWER_DOUBLE_BOOKING_CHECK_ENABLED.
6. In the Profile Values section, set the profile value:
◦ Y: Default value. Double booking is prevented. recruiter can’t book an interview or create an interview slot
that overlaps a scheduled interview with one of the interviewers. Any overlapping unscheduled slot is
removed when an interview is booked for any given interviewer.
◦ N: There's no validation, double booking is allowed. When an interviewer is scheduled for an interview,
unscheduled time slots during that period for that interviewer continue to be available for candidates to
select, and additional interviews can be scheduled during the same period
7. Click Save and Close.

---

## Microsoft 365 Calendar Integration in Interviews
*Chunk ID: OHR-REC-0584 | Chapter: Candidate Interviews*

The Microsoft 365 Calendar integration enables interview coordinators to view free / busy calendar information of
interviewers and to create, reschedule, and delete interviewers to sync with the interviewer's calendar.
When the integration is enabled, here's how users can use interview scheduling:
• They can view the interviewer availability when scheduling interviews on behalf of candidates and when
creating interview slots for candidates to self-schedule.
• When editing scheduled interviews or interview slots, they can also view interviewer availability to ensure
they're rescheduling when the interviewer is free.
• Interviewers and interview coordinators will receive interview events in Microsoft 365 that they can easily add
to their calendar. As those events are changed in Oracle Fusion Cloud Recruiting, the event in Microsoft 365 is
updated automatically.
• When Microsoft 365 events are sent to interviewers, and the interviewers respond to the invite, meeting
organizers can view the interviewer response (Accept, Tentative, Decline, Propose New Time) in the interview
details.
Note: On-premise mailboxes aren't supported by this integration.
To use the interviewer availability viewer, you need to grant users the privilege Manage Job Requisition Interview
Schedule (IRC_MANAGE_JOB_REQUISITION_INTERVIEW_SCHEDULE).

---

## Access Type Configuration
*Chunk ID: OHR-REC-0585 | Chapter: Candidate Interviews*

When you enable and configure the Microsoft Graph Integration in Recruiting, you can configure the access type to all
users or a single user.
When you select All Users:
• The option provides the same behavior as in previous releases.
When you select Single User:
• Users can’t select a meeting host when using the Teams integration. The Meeting Host field isn’t available. The
default user configured in the integration is used as the meeting host.
• Users can’t respond to interviews. When an interviewer views the Interview Details page for an interview, they
can’t accept, decline, or propose a new time for the interview. Note that responses provided in Microsoft 365
will continue to be displayed in Recruiting.
• Users can create interviews without receiving a Microsoft 365 calendar event for this interview. The interview
creator receives a Microsoft 365 calendar event for an interview only if the interview creator is also an
interviewer.
For both access types, in all internal notifications related to specific interviews, you can include the name of the
interview creator using the token ${InterviewCreatorDisplayName}. The display name of the interview creator is
displayed.

---

## Enable Microsoft 365 Calendar Integration in Interviews
*Chunk ID: OHR-REC-0586 | Chapter: Candidate Interviews*

When you enable the integration with Microsoft 365 Calendar, interview coordinators can view free / busy calendar
information of interviewers. They can also create, reschedule, and delete interviewers to sync with the interviewer's
calendar.
The integration with Microsoft 365 Calendar is delivered disabled.
Here are some details to be aware of when you integrate the Microsoft 365 Calendar for interviews:
• Interviewers will continue to receive the Oracle Fusion Cloud Recruiting interview notifications, in addition to
the Microsoft 365 interview event invitation.
• While internal candidates are likely Microsoft 365 users, their availability isn't displayed in the availability
viewer in Oracle Recruiting. They're also not sent interview events in Microsoft 365. They'll receive the existing
Recruiting interview notifications.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Microsoft Graph Integration section and click Edit.
3. Select the Enable Calendar Integration option.
4. Complete these fields:
Access Type

Two options are available:
Users: This is the default value. When you select the All Users
◦ All
access type configuration, the integration uses the O365 account of

◦

the current user to retrieve the interviewers’ availability. If no O365
account can be found for the current user, the account of the user
configured as the default user in the Microsoft Graph Integration
configuration is used instead. If no default user is configured, then
it won't be possible for the integration to retrieve the interviewers’
availability.
Single User: With the Single User option, a restricted mode is used.
This means that all operations are performed using this user, and
that all Microsoft 365 interview meetings will be created by this
user (this user will be visible as being the meeting organizer in the
Microsoft 365 meetings) since the integration can't access other
accounts. When you select Single User, the Default User Identifier
field is required and you need to provide a value.

---

## Application ID
*Chunk ID: OHR-REC-0587 | Chapter: Candidate Interviews*

Tenant ID
Application Authentication Type

Two options are available:
Secret: Use this option to authenticate using a password. You
◦ Client
need to enter the password in the Application Password field.

---

## Use this option to authenticate using a certificate. Click
*Chunk ID: OHR-REC-0588 | Chapter: Candidate Interviews*

◦ Certificate:
Browse to select and upload the certificate created on Microsoft
Azure portal, then enter the certificate password.

---

## For detailed steps on setting up the authentication
*Chunk ID: OHR-REC-0589 | Chapter: Candidate Interviews*

process, see the document Email and Calendar
Integration: Setting up Microsoft 365 integration for
interview scheduling and emails on My Oracle Support
(ID 2664168.1).
Default User Identifier

---

## This is the fallback user ID that can be used to write
*Chunk ID: OHR-REC-0590 | Chapter: Candidate Interviews*

and delete the interview events or view interviewers
availability. This user is used when the original user can't
write the event and when trying to viewing interviewers
availability.

---

## In most Microsoft 365 instances the default calendar
*Chunk ID: OHR-REC-0591 | Chapter: Candidate Interviews*

name is Calendar.

5. Click Validate Integration to ensure the connection is successful.
What to do next
Run the scheduled process Synchronize Interview Details with External Calendars. It's recommended that you set this
process to run every 10 minutes.
Related Topics
• Microsoft 365 Calendar Integration in Interviews
• Email and Calendar Integration: Setting up Microsoft 365 integration for interview scheduling and emails

---

## Set Up National Clouds
*Chunk ID: OHR-REC-0592 | Chapter: Candidate Interviews*

You can configure the Microsoft Graph integration by defining different endpoints to integrate with different Microsoft
Graph national cloud deployments.
National clouds are environments (different than the Microsoft global environment) which are made available by
Microsoft for country-specific needs. If you're using such national clouds, you now have the possibility to configure the
endpoints used by the Microsoft Graph integration, allowing to connect to the desired national cloud. If you keep the
default endpoints, the integration will connect to the Microsoft global environment as it did before.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Microsoft Graph Integration section and click Edit.
3. Clear the Use Default Endpoints check box.
4. Enter values in the Microsoft Entra ID Endpoint and Microsoft Graph Endpoint fields.
5. Click Save.

---

## Configure the Content of Calendar Events for Candidate
*Chunk ID: OHR-REC-0593 | Chapter: Candidate Interviews*

Interviews
You can configure and personalize the content of the .ics attachments and Office 365 calendar events used when
scheduling candidate interviews.
Three content item categories are available in the Recruiting Content Library:
• Interview Calendar File For Candidates: This is for the .ics attachment provided to candidates.
• Interview Calendar File For Interviewers: This is for the .ics attachment provided to interviewers.
• Interview Office 365 Event For Interviewers: This is for the Office 365 calendar events provided to interviewers.
Default content items are available for each category. The content of these items is the same as the one available in
previous releases. Default content items are active by default and only one content item can be active for each category.
Since a default content item can’t be deactivated, you’ll need to create versions of the item to change its content.
When you personalize the content of Office 365 calendar events used when scheduling candidate interviews, that
personalized content is used when the Teams or the Zoom integration is used for an interview. The content of the Office
365 calendar event varies whether you're using the Teams or Zoom integration.
• When the Teams or Zoom integration isn't used, the content of the calendar event consists of the content
defined in the Recruiting Content Library.
• When the Zoom integration is used, the content of the calendar event consists of the content defined in the
Recruiting Content Library (in previous releases, the subject from the content library was used, but the body of
the event was empty).
• When the Teams integration is used, the content of the calendar event consists of the content defined in the
Recruiting Content Library, to which the meeting info provided by Teams is appended at the end (in previous
releases, the subject from the content library was used, but only the Teams content was included in the body of
the event).
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library
2. On the Recruiting Content Library page, select a content item category and open it:
◦ Interview Calendar File For Candidates

◦ Interview Calendar File For Interviewers
◦ Interview Office 365 Event For Interviewers
3. Open a content item.
4. In the Additional Versions section, click Create.
5. On the Create Version page, select a start date when the version will be available for use.
If you want the version to be available as soon as it's activated, select the Start on Activation option.

---

## Candidate Interviews
*Chunk ID: OHR-REC-0594 | Chapter: Candidate Interviews*

6. Define the content of the subject and of the message.
Tokens are available for both the subject and message. The tokens will vary depending on the category selected. For
the Office 365 calendar event message, rich text features are available to format the text.
Note: In the case of multi-seat interviews where several candidates are scheduled for the same time slot,
candidate and job application tokens can't be resolved in the interviewer .ics and Office 365 events. Tokens will
return an empty value. This is because for interviewers, only 1 notification is sent for multi-seat interviews even
if there are 10 candidates. If you want, you can use groovy expressions in the content for these items to avoid
including the tokens and their associated text when tokens are empty.
Note: If you include the InterviewSchedulingLocationWebConferenceLink token in the content of an item of the
"Interview Office 365 Event For Interviewers" content library category, this token will return an empty value when
Teams is used for the interviews. However, the actual link for the Teams web conference will be part of the content
appended to the calendar event (appended after the personalized library content) and interviewers will still have
access to this link. This is due to a technical limitation which only occurs when initially scheduling the interview.
When the interview is updated (rescheduled, for example), the token will return a value. The same behavior is
present for all interview notifications and calendar files, this token will return a value.
7. Click Save and Activate to make the version available for use. Or Save as Draft to edit and activate the version at a
later time.

---

## Enable Microsoft Teams Integration in Interviews
*Chunk ID: OHR-REC-0595 | Chapter: Candidate Interviews*

When you enable the Microsoft Teams Integration feature, you allow recruiting users to generate web conference links
for interviews.
This feature is available for both the candidate managed and hiring team managed interview schedules.
1. In the Setup and Maintenance work area, go to
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Microsoft Graph Integration section and click Edit.
3. Select Active and complete the fields.
4. Select the Enable Teams option.
5. Click Save.

---

## Enable Zoom Integration in Interviews
*Chunk ID: OHR-REC-0596 | Chapter: Candidate Interviews*

When you enable the Zoom integration, you allow recruiting users to select Zoom to generate web conference links for
interviews.
1. Create the Zoom Application on the Zoom App Marketplace Site
2. Configure the Zoom Application
3. Configure Oracle Recruiting to Use Zoom

---

## Create the Zoom Application on the Zoom App Marketplace Site
*Chunk ID: OHR-REC-0597 | Chapter: Candidate Interviews*

You first need to create the Zoom application on the Zoom App Marketplace site.
1. Go to Zoom App Marketplace (https://marketplace.zoom.us/) and sign in using your zoom account.
2. On the Discover apps page, click the Develop menu, then click Build App.
3. On the Choose your app type page, click Create in the OAuth section.
4. On the Create an OAuth app window, complete these fields:
◦ App Name: Enter an app name. For example, ORC Zoom Integration.

◦ User-managed app: Select this option.
5. Click Create.

---

## Configure the Zoom Application
*Chunk ID: OHR-REC-0598 | Chapter: Candidate Interviews*

When the Zoom app is created, you need to configure it.
1. On the App Credentials tab, complete these fields:
◦ Client ID: The Client ID is automatically generated and it’ll be used when you configure the Zoom
integration in Recruiting.
◦ Client Secret: The Client Secret is automatically generated and it’ll be used when you configure the Zoom
integration in Recruiting.
◦ Redirect URL for OAuth: Enter a URL. The format of this URL is: https://<Host>/hcmUI/
CandidateExperience/zoomIntegration/oauth. You need to replace the <Host> by the appropriate host
name of your Fusion instance.
◦ Add Allow List: Enter the same URL as the one you entered in the Redirect URL for OAuth field.
2. On the Information tab, complete these fields:
◦ App name: For example, Oracle Recruiting Zoom Integration.

◦ Short description: For example, Zoom app for Oracle Recruiting.
◦ Long description
◦ Developer contact name and email.
3. On the Scopes tab, click Add Scopes and select these privileges:
◦ Meeting: View your meetings, View and manage your meetings.
4. On the Activation tab, ensure that all the required info is there.

---

## Configure Oracle Recruiting to Use Zoom
*Chunk ID: OHR-REC-0599 | Chapter: Candidate Interviews*

You configure Oracle Recruiting to use Zoom for interviews.
Before you start
If the Teams integration is enabled, you need to disable it. You can only enable one web conference at a time.

---

## Candidate Interviews
*Chunk ID: OHR-REC-0600 | Chapter: Candidate Interviews*

Here's what to do
1. In the Setup and Maintenance work area, go to
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Zoom Integration section and click Edit.
3. Select Active and enter the Client ID and Client Secret.
4. Click Save.
5. Click Edit then click Validate Integration. Click OK when the confirmation message is displayed.
6. Click Save.

---

## Assign the Authorize Zoom Integration Privilege
*Chunk ID: OHR-REC-0601 | Chapter: Candidate Interviews*

You need to grant a privilege for users to see and access the quick action Authorize Zoom Integration for Interviews.
Name: Access Zoom Authorization Page for Interviews
(IRC_ACCESS_ZOOM_AUTHORIZATION_PAGE_FOR_INTERVIEWS_PRIV)

---

## Interview Feedback Questionnaires and Questions
*Chunk ID: OHR-REC-0602 | Chapter: Candidate Interviews*

12 Interview Feedback Questionnaires and
Questions
Create Interview Feedback Questionnaires
Interview feedback questionnaires contain questions used by recruiters and hiring managers to collect feedback on
candidates during candidate interviews.
Interview feedback questionnaires are attached to job requisitions and job requisition templates. They can be used at
any time during the candidate selection process. They're not limited to the interview phase.
Unlike prescreening questionnaires which are answered by candidates, interview feedback questionnaires are intended
for the recruiter, hiring manager, or other people in the interview panel.
Here are the main steps to create an interview feedback questionnaire:
1. Create an Interview Feedback Question
2. Create an Interview Feedback Questionnaire Template
3. Create an Interview Feedback Questionnaire
4. Add Interview Feedback Questionnaires to Job Requisitions and Job Requisition Templates

---

## Create an Interview Feedback Question
*Chunk ID: OHR-REC-0603 | Chapter: Candidate Interviews*

Interview feedback questions appear in interview feedback questionnaires.
Before you start
It's recommended to create a folder to organize interview feedback questions. You could for example name the folder
Interview Feedback Questions.
Before you start
You need the privilege Manage Questions (HRT_MANAGE_QUESTIONS_PRIV).
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Question Library
2. In the Manage Questions page, select Recruiting in the Subscriber field.
3. Click Create.
4. On the Create Question page, enter the question.

---

## Interview Feedback Questionnaires and Questions
*Chunk ID: OHR-REC-0604 | Chapter: Candidate Interviews*

5. Select the question type.
Possible choices are Text, Single Choice, Multiple Choice, No Response.
6. In the Question Classification field, select Interview Feedback.
7. In the Response section, specify the response type and presentation method.
Values differ depending on the question type selected. For example, for single-choice questions, you can specify that
the possible responses appear either in a list or as radio buttons.
8. Specify if attachments can be provided as part of the response.
9. For single-choice and multiple-choice questions, click Add to add the question responses.
The Additional Questionnaire option isn't functional.
10. Click Preview to see how the question appears in interview questionnaires.
11. Click Save and Close.
The question appears in the selected subscriber and folder.
12. Set the question to Active so it's available for selection when creating interview questionnaires.
What to do next
You can translate questions without having to sign out and sign in a different language. Use the Translation Editor tool,
represented by the earth logo, to translate the question text.

---

## Create an Interview Feedback Questionnaire Template
*Chunk ID: OHR-REC-0605 | Chapter: Candidate Interviews*

Interview feedback questionnaire templates are required to create interview feedback questionnaires. All questionnaires
are based on templates, which promotes consistency.
Depending on the desired level of control over interview feedback questionnaires, you can create a generic, mostly
blank template to give users the ability to fully control the questionnaire properties and contents when creating the
questionnaire. If more control is required, you can create templates with limited configuration options available at the
questionnaire level.
Before you start
It's recommended to create a template for the different types of feedback your organization collects: phone screens,
recruiter interviews, hiring manager interviews, panel or hiring team interviews.
You need these privileges to create questions and questionnaires:
• Manage Questionnaire Templates (HRT_MANAGE_QUESTIONNAIRE_TEMPLATES_PRIV)
• Manage Questionnaires (HRT_MANAGE_QUESTIONNAIRES_PRIV)
• Manage Questions (HRT_MANAGE_QUESTIONS_PRIV)
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Questionnaire Templates

2. On the Questionnaire Templates page, search for any existing templates for Recruiting by selecting Recruiting in the
Subscriber field and clicking Search.

---

## Interview Feedback Questionnaires and Questions
*Chunk ID: OHR-REC-0606 | Chapter: Candidate Interviews*

3. If you find a template that you want to use, copy the template and modify its content.
4. If you want to create a new template, click Create.
5. On the Create Questionnaire Template: Basic Information page, enter a name and description for the template.
6. Add instructions for the questionnaire's users.
These instructions appear at the top of page one of the questionnaire. You can also attach help material if desired.
Instructions are not required to display the attachments.
7. Select the option Allow changes to instructions if you want to allow the person who requested the feedback to
provide additional instructions or notes to respondents.
These will appear on the questionnaire. When creating a request for feedback the user also has the chance to add
notes to respondents, which appear in the header area of the questionnaire along with the candidate and requisition
details.
8. Click Next.
9. On the Create Questionnaire Template: Contents page, configure the following options:
◦ Section Order: Select Sequential to display the sections in the order you specified. Select Random to
change the section order whenever the questionnaire is accessed.
◦ Allowed Response Types: This option identifies the response types that can appear in questionnaires
created from the template. Only questions with the selected response types can appear in the
questionnaire.
10. Add and configure sections using the following options:
◦ Allow Additional Questions: This option controls whether authorized users can add questions when
creating a questionnaire from the template.
◦ Question Order: This option controls the default order of questions in a section. Select Vertical for
questions to appear in the specified order. Select Random for question order to change randomly when a
user accesses the questionnaire.
◦ Response Order: This option controls the default order of responses in a section. Select Vertical for
responses to appear in the specified order. Select Random for response order to change randomly when a
user accesses the questionnaire.
◦ Required: Select this option if you want respondents to answer all questions in the section.
11. Add questions from the Question Library or create new questions.
Question properties can be modified from the template creation page. Changing the response type or making a
question required or not required only applies to the template being created. If you want to modify other question
properties such as the question text or responses, you can create a new version of the question or edit the existing
version.
12. Click Next to review the template properties and contents.
13. Click Save and Close.
The questionnaire template appears in the Questionnaire Templates page, in the selected subscriber.
14.Set the questionnaire template to Active so it's available for selection when creating interview questionnaires.

---

## Create an Interview Feedback Questionnaire
*Chunk ID: OHR-REC-0607 | Chapter: Candidate Interviews*

Interview feedback questionnaires contain questions used by recruiters and hiring managers to collect feedback on
candidates during candidate interviews.
Before you start

---

## Interview Feedback Questionnaires and Questions
*Chunk ID: OHR-REC-0608 | Chapter: Candidate Interviews*

You need these privileges to create questions and questionnaires:
• Manage Questionnaire Templates (HRT_MANAGE_QUESTIONNAIRE_TEMPLATES_PRIV)
• Manage Questionnaires (HRT_MANAGE_QUESTIONNAIRES_PRIV)
• Manage Questions (HRT_MANAGE_QUESTIONS_PRIV)
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Questionnaires
2. On the Questionnaires page, select Recruiting in the Subscriber field.
3. Select the Interview Feedback folder to see interview feedback questionnaires that are available.
4. If you find a questionnaire that you want to use, copy the questionnaire and modify its content.
5. If you want to create a new questionnaire, click Create.
a. Questionnaires are based on templates to promote consistency. Enter a questionnaire template ID or name
then click Search.
b. Select the questionnaire template from the search results list.
6. Several fields are already filled from the template, but you can modify them for the questionnaire.
7. Enter the questionnaire name.
8. Click Next. The page Create Questionnaire: Contents is displayed.
9. You can configure the sections and also add new ones:
◦ Question Order: This option controls the default order of questions in a section. Select Vertical for
questions to appear in the specified order. Select Random for question order to change randomly when a
user accesses the questionnaire.
◦ Response Order: This option controls the default order of responses in a section. Select Vertical for
responses to appear in the specified order. Select Random for response order to change randomly when a
user accesses the questionnaire.
◦ Required: Select this option if you want respondents to answer all questions in the section.
10. You can add questions from the Question Library or create questions.
11. Click Next to review the questionnaire properties and contents.
12. Click Preview to see how the questionnaire is presented to respondents.
13. Click Save and Close. The questionnaire appears on the Questionnaires page, in the selected subscriber.
14.Set the questionnaire to Active so it's available for selection when creating interview questionnaires.

---

## Add Interview Feedback Questionnaires to Job
*Chunk ID: OHR-REC-0609 | Chapter: Candidate Interviews*

Requisitions and Job Requisition Templates
Interview feedback questionnaires are added to job requisitions and job requisition templates so that the recruiters and
hiring managers can collect feedback during candidate interviews.

---

## Job requisitions that are created from job requisition templates will automatically include any interview feedback
*Chunk ID: OHR-REC-0610 | Chapter: Candidate Interviews*

questionnaires attached to the template. Additional interview questionnaires can be added to the job requisition, and
the questionnaires inherited from a template can be removed from the job requisition.
When adding questionnaires to job requisitions or job requisition templates, only active questionnaires created in the
Questionnaire library are available for selection.

---

## Add Feedback Respondents to the Hiring Team
*Chunk ID: OHR-REC-0611 | Chapter: Candidate Interviews*

You can decide if interview feedback respondents are added to the job requisition's Hiring Team as collaborators.
By default, interview feedback respondents are added to the job requisition's Hiring Team as collaborators so that
they're suggested automatically for future feedback requests. However, some organizations don't want interview
feedback respondents to be added to the requisition's Hiring Team, either because they don't want these users to have
access to the requisition or because they don't want them to be inherited on the job offer's Hiring Team.
To enable this feature, you need to enable the profile option
ORA_IRC_ADD_FEEDBACK_RESPONDENTS_AS_COLLABORATORS at the Site level. By default, the profile value is set to
Y, which means respondents are added as collaborators. When set to N, respondents aren't added as collaborators.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_ADD_FEEDBACK_RESPONDENTS_AS_COLLABORATORS.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.
What to do next
You also need to provide collaborators access to the feedback form by granting one of these privileges:
Access to Hiring as Manager (IRC_ACCESS_TO_HIRING_AS_MANAGER_PRIV), Access to Hiring as Recruiter
(IRC_ACCESS_TO_HIRING_AS_RECRUITER_PRIV).
Related Topics
• Create and Edit Profile Options

---

# Candidates and Candidate Job Applications

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0612 | Chapter: Candidates and Candidate Job Applications*

Supported Candidate Types
These candidate types are supported in Oracle Recruiting.
• Employees
• Contingent workers
• Ex-employees
• Ex-contingent workers
• Candidates (External)

---

## Enable Candidate Autoconfirmation
*Chunk ID: OHR-REC-0613 | Chapter: Candidates and Candidate Job Applications*

When you enable the Candidate Autoconfirmation feature, external candidates don't need to confirm their email
address when they apply for a job. Their email address is automatically confirmed.
Here's what happens when you don't enable the Candidate Autoconfirmation feature:
• If there is no candidate profile:

◦ And there is no draft associated with the email or phone: the verification code is sent at the end of the
◦

apply flow or talent community flow.
And there is a draft associated with the email or phone: the verification code is sent before entering the
apply flow or talent community flow.

• If there is a candidate profile:

◦ When the candidate enters the apply flow, the verification code is sent as soon as the candidate provides
◦
◦

the email or phone. After a successful verification, the candidate can enter the flow and see profile data
associated with the email or phone that was used.
When the candidate enters the talent community flow, the verification code is sent as soon as the
candidate provides the email (there is no phone verification when entering the talent community flow).
After successful verification, the candidate can access the self-service dashboard on the career site to
manage their profile (there is no entry to the talent community flow because the candidate already has a
profile).

Here's what happens when you enable the Candidate Autoconfirmation feature:
• If there is no candidate profile, or draft associated with the email or phone, the verification code isn't sent after
completing the apply flow or the talent community flow, and the email or phone is auto confirmed.
• If there is a candidate profile, the behavior is the same as when the Candidate Autoconfirmation setting is
disabled.
1. In the Setup and Maintenance work area, go to:

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0614 | Chapter: Candidates and Candidate Job Applications*

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Manage Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. Select the option Candidate Autoconfirmation.
4. Click Save.

---

## Enable Email Authentication and Email Reuse
*Chunk ID: OHR-REC-0615 | Chapter: Candidates and Candidate Job Applications*

You can allow returning candidates to claim email addresses as being genuinely their own by verifying either their date
of birth or last name (depending on what information has been entered for that candidate in the past). When candidates
enter the correct information, a verification code is sent to their email address to further verify ownership.
This feature adds another layer of security to email verification and the associated candidate profile. It also allows
candidates to create profiles even though the email address they used belonged to another candidate in the past. Once
their identity is confirmed, candidates can move forward with the job application process.
If a candidate can't authenticate their ownership of an email address using last name or date of birth, it could mean the
email address they're trying to use is currently assigned to another user in the Recruiting. This might have happened
for several reasons, including scenarios where candidates made typo in Last Name and Date of Birth details, previous
candidates made spelling mistakes when entering their email address, or perhaps a previous candidate lost the email
address due to inactivity when their email provider recycled it.
When this happens, they're given the option of creating a new profile using that email address. A verification code is
sent to their email address to further verify ownership, and they can then create the new profile. Once a new profile is
associated with the email address, the previous candidate using that email address is marked as unverified.
Returning candidates are allowed 4 attempts to authenticate date of birth or last name during sign-in using their email.
If they fail to provide the correct details after 4 attempts, all buttons and fields are disabled on the Confirm Your Identity
window, except for the create a new profile link. Candidates can use that link to create a new profile and claim their
email. Or, candidates can wait 30 minutes to try the sign-in process again.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. Select the option Verify date of birth and allow email claims.
4. Apply the validation to:

◦ Ex Workers - includes ex-employees and ex-contingent workers
◦ All Candidates - includes ex-workers, contingent workers as external candidates, external candidates

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0616 | Chapter: Candidates and Candidate Job Applications*

5. Click Save.
This setting applies to all the flows where candidates verify their identity:
◦ Application flows

◦ Talent community sign ups
◦ Event Registration flows
◦ Profile logins from Manage Profile (Candidates aren't given an opportunity to create profiles from this flow)

---

## Enable Candidate Phone Number Reuse
*Chunk ID: OHR-REC-0617 | Chapter: Candidates and Candidate Job Applications*

You can allow external candidates to reuse the phone number that was used by another candidate in the past.
Candidates can claim a phone number as genuinely being their own.
In some areas, when a person stops using a phone number, providers are re-allocating the phone number to a new
person. If these two people are applying for a job, additional verification is required to ensure that the person is who
they claim to be and the new candidate who genuinely owns the phone must be able to assert this fact, while at the
same time not exposing info from the general profile or job applications of the previous owner.
Here's how the feature works.
Use case 1 - A returning candidate applies for a job, candidate has used the same device before. Let's say candidate Jane
B has a candidate file in Oracle Recruiting. Jane applies for a job and enters the phone number 510.123.1234. This phone
number is recognized and a previous cookie is found. A 6-digit verification code is sent to Jane's phone and Jane enters
the verification code. Jane continues to apply for the job. Jane's profile is updated and a new application is created.
Use case 2 - A new candidate applies with phone number used by another candidate before. Let's say John A has a
candidate file in Oracle Recruiting with a phone number 510.123.1234 assigned to his profile as verified. Now another
candidate Jane B doesn't have a candidate file in Oracle Recruiting. Jane applies for a job and enters the phone number
510.123.1234. This phone number is recognized, but no previous cookie is found. Jane is asked to enter her last name.
The last name and phone number don't match and Jane is offered to claim the phone number. A 6-digit verification
code is sent to Jane's phone and Jane enters the verification code. Jane continues to apply for the job. Jane's profile
is created and her phone number is now verified (John A phone number gets unverified). If Jane decides to no longer
apply for the job, a draft profile is saved. If Jane applies to another job using the phone number, the draft profile will be
connected to Jane.
Returning candidates are allowed 4 attempts to authenticate their last name during sign-in using their phone number.
If they fail to provide the correct details after 4 attempts, all buttons and fields are disabled on the Confirm Your Identity
window, except for the create a new profile link. Candidates can use that link to create a new profile and claim their
phone number. Or, candidates can wait 30 minutes to try the sign-in process again.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Experience section and click Edit.
3. Select the option Verify last name and allow phone number claim.
4. Click Save.

---

## Set Candidate Phone Legislation Code as Required
*Chunk ID: OHR-REC-0618 | Chapter: Candidates and Candidate Job Applications*

Phone legislation code is required when users create or update a phone for a candidate.
The phone legislation code is a field in the back-end table that's automatically populated if the country code is selected
in the UI, provided the profile option ORA_IRC_PHONE_LEGISLATION_CODE_ENABLED is enabled.
The profile option ORA_IRC_PHONE_LEGISLATION_CODE_ENABLED is set to Y by default.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_PHONE_LEGISLATION_CODE_ENABLED.
6. Set the profile value to Y.
7. Click Save and Close.

---

## Create a Candidate Without Email, Phone, or Both
*Chunk ID: OHR-REC-0619 | Chapter: Candidates and Candidate Job Applications*

You can allow recruiters and hiring managers to create candidates even though they don't have an email, phone, or
both. This can be the case with seasonal, temporary, or construction workers.
Recruiters and hiring managers can take the candidates though the application, interview, and offer process without any
communication. At a later time, they can add a phone or email, if needed and available.
By default, the Email field is a required field. Based on your business needs, you can configure your career sites so that
email is required when candidates apply for a job or that phone is required. All candidates will have at least email or
phone (or both, if the candidate enters the info).
You can create rules in Transaction Design Studio to set the email and phone fields as required.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Define Application Flow Required Fields.
5. Click Add to create and configure a rule.
6. In the Basic Details section, enter a name and description for the rule. Select an application flow.
7. In the Available Attributes section, select the Contact Information data source.
8. Decide if you want the Email Address and Phone Number fields to be required.
9. Click Save and Close.

---

## Process Contingent Workers as External Candidates
*Chunk ID: OHR-REC-0620 | Chapter: Candidates and Candidate Job Applications*

You can decide to process contingent workers as internal or external candidates to align with the business practices and
processes of your organization. By default, contingent workers are processed as internal candidates.
Before you decide to process contingent workers are external candidates, make sure that:
• All job applications of contingent workers are in terminal status.
• Users (including employees) aren't active on Oracle Fusion Cloud Recruiting. This is to avoid the creation of any
new candidate job applications.
Here's what to do
1. Activate the Contingent Worker Setting
2. Submit the Contingent Worker Scheduled Process
3. Modify the Contingent Worker Role Privilege

---

## Activate the Contingent Worker Setting
*Chunk ID: OHR-REC-0621 | Chapter: Candidates and Candidate Job Applications*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Recruiting Management section and click Edit.
3. Select the option Contingent Worker is External Candidate.
4. Click Save.

---

## Submit the Contingent Worker Scheduled Process
*Chunk ID: OHR-REC-0622 | Chapter: Candidates and Candidate Job Applications*

You need to submit the scheduled process Classify Contingent Workers in Recruiting in the Scheduled Processes
work area to classify contingent workers as external candidates in the recruiting process.

---

## Modify the Contingent Worker Role Privilege
*Chunk ID: OHR-REC-0623 | Chapter: Candidates and Candidate Job Applications*

By default, the privilege Access Internal Candidate Experience (IRC_ACCESS_INTERNAL_CANDIDATE_EXPERIENCE)
is granted to the Contingent Worker role. You need to revoke this privilege to the Contingent Worker role so that they
can apply to external career sites as external candidates. By revoking the privilege, contingent workers won't be able to
access internal jobs and to answer interview questionnaires as this is required to access internal career sites.

---

## Update the Address of External Contingent Workers
*Chunk ID: OHR-REC-0624 | Chapter: Candidates and Candidate Job Applications*

You can allow recruiting users to update the address of contingent workers.
To allow any recruiting user to update a contingent worker address when the contingent worker is treated as external
candidate, you need to set the profile option ORA_IRC_ALLOW_CWK_EXT_RECRUITER_ADDRESS_UPDATE to Y.

---

## Note: When set to Y, contingent workers treated as external candidate might not be able to apply through Direct
*Chunk ID: OHR-REC-0625 | Chapter: Candidates and Candidate Job Applications*

Apply partners, as they usually include the candidate address. The REST service will prevent updating the candidate
file.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_ALLOW_CWK_EXT_RECRUITER_ADDRESS_UPDATE.
6. Set the profile value to Y.
7. Click Save and Close.

---

## Enable Job Type Lookup Values for Contingent Hiring
*Chunk ID: OHR-REC-0626 | Chapter: Candidates and Candidate Job Applications*

You can enable job type lookup values for the Job Type field for contingent hiring. These values are useful for customers
who hire contractors for filling their temporary and short term positions.
The lookup codes are disabled by default. To enable them for contingent hiring, use the common lookup type called
ORA_IRC_JOB_TYPE in the Manage Common Lookups task, in the Setup and Maintenance work area.
1. In the Setup and Maintenance work area, search for the task Manage Common Lookups.
2. On the Manage Common Lookups page, search for the lookup type ORA_IRC_JOB_TYPE.
3. Select the lookup codes you want to enable.
4. Click Save and Close.

---

## Allow Candidates to Apply to Multiple Jobs Before
*Chunk ID: OHR-REC-0627 | Chapter: Candidates and Candidate Job Applications*

Verifying Their Identity
You can set a limit for the number of jobs to which external candidates can apply before their identity is verified.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Recruiting Management section and click Edit.
3. In the Maximum number of unverified job applications field, enter the limit. The default value is 1.
4. Click Save.

---

## Allow Candidates with Withdrawn Job Applications to
*Chunk ID: OHR-REC-0628 | Chapter: Candidates and Candidate Job Applications*

Reapply
You can allow external and internal candidates to reapply to job requisitions when they've a withdrawn job application
on a requisition.
When candidates have a withdrawn job application that's in any phase before the Offer phase, they can submit a new
job application. Information from their candidate profile, like personal and contact info and content sections, will be
prefilled in the application flow. However the candidate will need to answer prescreening questions again. The new job
application will start at the beginning of the candidate selection process and the candidate will have to go back through
any configured request information flows. The new job application and all withdrawn job applications will display a
message on the Details tab informing the user that this candidate has previously applied to the requisition. Recruiting
users can access the candidate's withdrawn job application from the job application's Activity tab and by filtering the list
of job applications to see withdrawn job applications.
Tips:
• Candidates can reapply to a job requisition when they use the Withdraw action in candidate self-service and
when the job application was withdrawn on their behalf by a recruiting user.
• Withdrawn job applications appear in the candidate's list of inactive job applications in candidate self-service.
• Candidates can no longer reapply once they've a job application that has reached the Offer phase.
• Once a candidate has reapplied to a requisition, their withdrawn job application can no longer return to its prior
state. The Return to Prior State action becomes disabled.
• Recruiting users can access the candidate's withdrawn job application from the new job application's Activity
tab and by filtering the list of job applications to see withdrawn job applications.
• Content like interview feedback, scheduled interviews, prescreening and disqualification questions, conditional
questionnaires included in request info flows, is retained on the withdrawn job application but not copied over
to the new job application.
• Referral information, including referred icon, referrer and endorsement info, is copied over to the new job
application.
◦ The referred icon and referral details are no longer displayed on the withdrawn job applications.

◦ The referral source information should still be available on the withdrawn job applications.

• The following actions are disabled on the withdrawn job application when a new job application is submitted for
a requisition:
◦ Move

◦ Return to Prior Phase
◦ Return to Prior State
◦ Send Interview Invite

• The following actions are still available on a withdrawn job application when a new job application is submitted:
◦ Add to Requisition

◦ Add to Candidate Pool
◦ Add Interaction

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0629 | Chapter: Candidates and Candidate Job Applications*

◦ Send Message
◦ Send Message to Team
◦ Collect Feedback
◦ Check Duplicates
◦ Delete Job Application
• When you create OTBI reports, you can include the Application Discarded Indicator available in the Job
Application - Basic Information folder. For details, see the feature Discarded Flag in Job Application Reports,
which is available under Transactional Business Intelligence for Recruiting.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Recruiting Management section and click Edit.
3. Select the option Allow Withdrawn Candidate to Reapply.
4. Click Save
Results:

---

## Save Draft Job Applications
*Chunk ID: OHR-REC-0630 | Chapter: Candidates and Candidate Job Applications*

When external candidates create draft job applications, they receive a notification and they can access the saved draft
application using a direct link.
Here's how it works:
• The candidate job application is automatically saved when the candidate identifier (email address or phone
number) and legal disclaimer consent are provided. The data is saved every 10 seconds. A candidate can drop
off from the application process and start over when ready, without losing any data.
• The candidate receives an email or SMS notification as soon as a draft job application is saved. A first
notification is sent after 60 minutes of candidate inactivity. A second notification is sent 3 days after the last
save of the draft application. Both notifications are only sent once for a draft to avoid spamming the candidate.
• The candidate can access the draft job application using the URL provided in the notification, by accessing their
candidate self service, or by starting to apply for the job again.
• If the candidate doesn't interact with the draft job application for 30 days, the application is automatically
removed.
• If a candidate profile is updated after a draft job application was saved, the draft job application will be updated
with the candidate profile data. Note that changing the date of birth doesn't update the draft job application.
• Recruiters and hiring managers can't view draft job applications.
To notify candidates about their saved draft job applications, you need to run the Send Draft Application Reminder
Notifications and Automatically Confirm Applications scheduled process. When the process is run, the following
notifications are sent to candidates so they're aware that drafts job applications were saved. These notifications are
available in the Recruiting Content Library:
• Saved Draft Application Notification

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0631 | Chapter: Candidates and Candidate Job Applications*

• Saved Draft Application Reminder
Note: Any changes affecting an active apply flow might impact data saved in a job application. Draft data might have
been saved for a candidate and the candidate won't be able to edit it when coming back to the flow.

---

## Configure the Job Application Print Feature
*Chunk ID: OHR-REC-0632 | Chapter: Candidates and Candidate Job Applications*

You can configure the job application print feature to allow recruiting users to create a PDF version of job applications.
1. In the Setup and Maintenance work area, go to
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Print to PDF section and click Edit.
3. Select the method to deliver the PDFs:
◦ File Attachment: Users will receive a notification with a zipped file containing a separate PDF for each job
application. This is the default.
◦ Hyperlink: Users will receive a notification with a link to download the PDFs.
4. Indicate the maximum number of job applications that the user can select for a single Print action. Default is 30,
maximum is 100.
5. Indicate the maximum size of the PDF file. Default is 10 MB, maximum is 10 MB.
6. Click Save.
What to do next
These two notifications are available in Alerts Composer. You can use them as is or personalize them:
• Print Action Download Notification (IRC_PRINT_ACTION_DOWNLOAD): This notification is used when the PDFs
are attached to the notification.
• Print Action Hyperlink Notification (IRC_PRINT_ACTION_HYPERLINK): This notification is used when the PDFs
can be downloaded using a link.
Note: If you want to add fields in the PDF output other than the fields defined by default, you need to create a
custom BI Publisher (BIP) report. The report provided by default is located under Shared Folders > Human Capital
Management > Recruiting > Job Application. If you create a custom report, it will be located under Shared Folders
> Custom > Human Capital Management > Recruiting > Job Application. Once a custom report is created, it will be
picked up and used by the Print action.

---

## Enable Advanced Job Application Filters
*Chunk ID: OHR-REC-0633 | Chapter: Candidates and Candidate Job Applications*

You can enable advanced job applications filters so that recruiting users can perform more complex, targeted searches
on the job applications list with advanced filtering capabilities.

---

## Before you start
*Chunk ID: OHR-REC-0634 | Chapter: Candidates and Candidate Job Applications*

This feature requires Oracle Search. For details, see Maintaining Oracle Search for Oracle Recruiting.
Here's what to do
1. Set the ORA_IRC_JA_ORACLE_SEARCH_ENABLED profile option at the Site level to Y.
By default, job application filters on Oracle Search feature aren't available.
a.
b.
c.
d.
e.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_JA_ORACLE_SEARCH_ENABLED.
f. Set the profile value at the Site level to Y.
g. Click Save and Close.
2. Enable job application attachment indexing, prior to running the initial ingestion of the search index.
a. In the Setup and Maintenance work area, click the Tasks icon.
b. Click Search.
c. Search for the task Manage Administrator Profile Values.
d. On the Manage Administrator Profile Values page, search for the profile option code
ORA_FND_SEARCH_ATTACH_ENABLED. This profile option isn't unique to Recruiting and may already be
enabled.
e. Set the profile value at the Site level to Yes.
f. Click Save and Close.
g. In the Setup and Maintenance work area, search for the task Manage Global Search Configurations.
h. On the Manage Global Search Configurations page, click the Configure Attachment Search button.
i. Click the Create button to add a new row and select the index name fa-hcm-jobapplication.
j. In the Content Type field, you can use the Create From Sample button to see content types or enter */* for
all content types.
3. Make sure the Enable File Search and Enable Content Search are set to Yes. Also set the Maximum File Size and
Maximum Content Size to maximum. For details, see Configure Attachment Search.
4. Run the scheduled process ESS job to create index definition and perform initial ingest to OSCS.
The index name to reingest is fa-hcm-jobapplication.

---

## Display Candidate Flexfields in Extra Info Tab
*Chunk ID: OHR-REC-0635 | Chapter: Candidates and Candidate Job Applications*

You can configure flexfields to allow recruiting users to view, edit, and add info provided by candidates in those
flexfields, and to add candidate flexfields for internal usage.
The Extra Info tab in candidate profiles is divided into two sections to display those flexfields:
• Candidate Extra Info: Recruiting users can view, edit, and add info provided by the candidate in those flexfields.
• Extra Internal Info: Recruiting users can add flexfields or edit data in those flexfields for internal use. Internal
Info flexfields aren't visible to the candidate.

---

## You first need to define flexfields to allow recruiting users to view and edit extra information about candidates. When
*Chunk ID: OHR-REC-0636 | Chapter: Candidates and Candidate Job Applications*

defining flexfields, you need to consider the following:
• Add or adjust contexts and context sensitive segments.
• For each job application context, add Usage Code for Candidate Application and Usage Code for Person in the
Context Usages tab.
• Associate contexts to the Person Extra Information category.
• Add or adjust pages to the Person Extra Information category.
• Add or adjust Associated Context Details for a page.
As an example, here's how to define flexfields for a context called Hobbies, add context usages, and create value sets.
1. In the Setup and Maintenance work area, go to

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Workforce Information
◦ Task: Manage Person Extensible Flexfield
2.
3.
4.
5.
6.
7.

Select the extensible flexfield called Person EIT Information.
Click the Edit icon.
On the Manage Person Extensible Flexfield page, click Manage Contexts.
In the Search Results section, click the Create icon.
On the Create Context page, let's say you create a context called Hobbies.
On the Context Usages tab, click the Create icon and add these two usages. For a context to be used in a job
application, you must include these context usages:

◦ Usage code for candidate application
◦ Usage code for person
8. In the Context Sensitive Segments section, click the Create icon.
9. On the Create Segment page, click Create Value Set. Let's say you create a value set named Hobby Category.
10. When you're done creating the value set, click Manage Values.
11. On the Manage Values page, create values such as Arts, Sports.
12. When you're done, associate contexts to pages.
You then need to configure the candidate file Extra Info tab in the Transaction Design Studio.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Candidate Extra Info.
5. Click Add to create a rule to display flexfields.
6. In the Basic Details section, enter a name and description for the rule. Select a role, or one or more countries,
or both if you want to render flexfield contexts and pages in the candidate file Extra Info tab based on a role,
countries, or both.
7. In the Page Attributes section, select a region: Candidate Extra Info or Extra Internal Info.
8. Click the Edit icon.
9. Select the pages and regions you want to make visible.
10. Click Done.
11. Click Save and Close.

---

## Display Job Application Flexfields in Extra Info Tab
*Chunk ID: OHR-REC-0637 | Chapter: Candidates and Candidate Job Applications*

You can define flexfields to allow candidates and recruiting users to enter extra information about job applications. Any
information provided by the candidate through an apply flow or request information flow can't be edited nor added.
This ensures that candidate provided information is retained.
Note: The configuration described below isn't supported when internal candidates apply for a job using Opportunity
Marketplace.
The Extra Info tab in job applications is divided into two sections to display those flexfields:
• Application Extra Info: Recruiting users can view info provided by the candidate in those flexfields. They can
then decide to initiate next steps as per their business practices. For example, a recruiter views the special
interest or hobbies of a candidate and engages appropriate interviewer with relevant knowledge to interact with
the candidate.
• Extra Internal Info: Recruiting users can add flexfields or edit data in those flexfields for internal use. For
example, union review notes, additional assessment requirements. This internal information is specific to that
job application. It's not visible on the candidate's profile or any subsequent job application.
Note: Users with the privilege Update Candidate Job Application (IRC_UPDATE_CANDIDATE_JOB_APPLICATION) can
add or edit flexfields in the Application Extra Info section.
You first need to define flexfields for job applications. When defining flexfields, you need to consider the following:
• Add or adjust contexts and context sensitive segments.
• For each job application context, add Usage Code for Candidate Application and Usage Code for Person in the
Context Usages tab.
• Associate contexts to the Person Extra Information category.
• Add or adjust pages to the Person Extra Information category.
• Add or adjust Associated Context Details for a page.
As an example, here's how to define flexfields for a context called Hobbies, add context usages, and create value sets.
1. In the Setup and Maintenance work area, go to

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Workforce Information
◦ Task: Manage Person Extensible Flexfield
2.
3.
4.
5.
6.
7.
8.

Select the extensible flexfield called Person EIT Information.
Click the Edit icon.
On the Manage Person Extensible Flexfield page, click Manage Contexts.
Enter a display name, code, and API name.
In the Search Results section, click the Create icon.
On the Create Context page, let's say you create a context called Hobbies.
On the Context Usages tab, click the Create icon and add these two usages. For a context to be used in a job
application, you must include these context usages:

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0638 | Chapter: Candidates and Candidate Job Applications*

◦ Usage code for candidate application
◦ Usage code for person
9. In the Context Sensitive Segments section, click the Create icon.
10. On the Create Segment page, click Create Value Set. Let's say you create a value set named Hobby Category.
11. When you're done creating the value set, click Manage Values.
12. On the Manage Values page, create values such as Arts, Sports.
13. When you're done, associate contexts to pages.
You then need to configure the job application Extra Info tab in the Transaction Design Studio.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Application Extra Info.
5. Click Add to create a rule to display flexfields.
6. In the Basic Details section, enter a name and description for the rule. You can also select a role.
Note: The Country field isn't functional. If you select one or more countries, it won't have any effect.
7.
8.
9.
10.
11.

In the Page Attributes section, select a region: Application Extra Info or Extra Internal Info.
Click the Edit icon.
Select the pages and regions you want to make visible.
Click Done.
Click Save and Close.

Note: The Start Date field is automatically added to the Extra Info tab. You can hide the field using Page Composer.

---

## Prefill Legislative Info in Job Applications
*Chunk ID: OHR-REC-0639 | Chapter: Candidates and Candidate Job Applications*

You can enable a setting so that legislative information is automatically saved while creating applications on behalf of a
candidate and is prefilled for returning external candidates applying for a job.
This feature is always enabled for creating applications on behalf of a candidate. Here's how to enable it for external job
applications.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Recruiting Management section and click Edit.
3. In the Prefill Legislative Information in Candidate Applications field, select Yes.
4. Click Save.

---

## View National Identifier Data of Contingent Workers
*Chunk ID: OHR-REC-0640 | Chapter: Candidates and Candidate Job Applications*

You can allow recruiters to view National Identifier Data (NID) of contingent workers on the candidate's job application,
in the Sensitive Info tab.
To view NID data for contingent workers, you need to configure contingent workers as external candidates by enabling
the profile option IRC_TREAT_CWK_AS_EXTERNAL at the Site level.
Note: Candidate experience doesn't support warning type validations. The Kuwait NID isn't supported.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
IRC_TREAT_CWK_AS_EXTERNAL.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.
Related Topics
• Create and Edit Profile Options

---

## Job Alert for New Job Opportunities
*Chunk ID: OHR-REC-0641 | Chapter: Candidates and Candidate Job Applications*

Candidates can receive job alerts about new job opportunities matching their job preferences.
When you enable job alerts, here's what happens for external and internal candidates.

---

## Job Alerts for External Candidates
*Chunk ID: OHR-REC-0642 | Chapter: Candidates and Candidate Job Applications*

External candidates can decide to receive alerts about new job opportunities matching their preferred job category and
location. Here's how it's done:
• In their candidate self service page, candidates select the option "I agree to receive updates about new job
opportunities" and they specify the job category they're interested in and their preferred location.
• When applying for a job, candidates select the option "I agree to receive updates about new job opportunities".
The job category and job location are selected for the candidates based on the job category and job location of
the job.
• When signing in into a talent community, candidates select the option "I agree to receive updates about new
job opportunities". The job category and job location are selected for the candidates based on the talent
community setup.

---

## When newly posted jobs match one or more of their job preferences, candidates receive an email listing the new jobs
*Chunk ID: OHR-REC-0643 | Chapter: Candidates and Candidate Job Applications*

with links to view details of each job on the career site. The email also contains a link to view all the jobs available on the
company's career site.

---

## Job Alerts for Internal Candidates
*Chunk ID: OHR-REC-0644 | Chapter: Candidates and Candidate Job Applications*

Internal candidates can decide to receive alerts about new job opportunities matching their preferred organizations,
locations, jobs, and job families. This encourages internal mobility by keeping candidates informed as jobs are posted
that align with their job interests.
In Opportunity Marketplace, in the Interests tab, the candidate indicate their preferred jobs, job families, workplace
types, and they can select the option "I want to receive news about new opportunities". When requisitions are posted
and they match the candidate's job preferences, the candidate receives an email listing the new jobs with links to view
details of each job on the career site. The email also contains a link to view all the jobs available on the company's career
site. The candidate is also automatically added to the Talent Community pools that match the job preferences.
Internal candidates can also subscribe to receive alerts for careers appearing in the Career Development's Careers
of Interest (Me > Career and Performance > Career Development > Careers of Interest). When job requisitions are
posted, internal candidates will receive a notification which contains links to job postings and to the job search list in
Opportunity Marketplace.

---

## Job Alerts Aren't Sent
*Chunk ID: OHR-REC-0645 | Chapter: Candidates and Candidate Job Applications*

Job alerts aren't sent when a job matches:
• Location only
• Organization only
• Location and organization only

Related Topics
• Which scheduled processes are used in Recruiting?

---

## Enable Job Alert for External Candidates
*Chunk ID: OHR-REC-0646 | Chapter: Candidates and Candidate Job Applications*

You can enable job alerts for external candidates so they receive notifications about new jobs.
Here's what to do
1.
2.
3.
4.

---

## Enable Job Alert in Job Application Flow
*Chunk ID: OHR-REC-0647 | Chapter: Candidates and Candidate Job Applications*

Activate Job Alert Notification
Run Scheduled Processes
Set Frequency of Job Alerts

---

## Enable Job Alert in Job Application Flow
*Chunk ID: OHR-REC-0648 | Chapter: Candidates and Candidate Job Applications*

You need to configure the job application flow so that candidates are presented with the option to receive job alerts
when applying for a job.
1. In the Setup and Maintenance work area, go to:

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0649 | Chapter: Candidates and Candidate Job Applications*

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration
2.
3.
4.
5.

Click a flow.
Click on a version of the flow.
Select the option Job Alert Opt In.
Click Save.

---

## Activate Job Alert Notification
*Chunk ID: OHR-REC-0650 | Chapter: Candidates and Candidate Job Applications*

You need to enable the job alert notification in the Recruiting Content Library.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library
2. On the Recruiting Content Library page, click Show Filters and select the Job Alert Notification filter.
3. Activate the Job Alert External Notification and Job Alert Internal Notification

---

## Run Scheduled Processes
*Chunk ID: OHR-REC-0651 | Chapter: Candidates and Candidate Job Applications*

Make sure the following processes are scheduled according to the recommended frequency. For details, see .
• Process Recruiting Job Alerts
Once the above jobs are scheduled, candidates will only receive job alerts from that point forward; it won't apply to old
or existing requisitions.

---

## Set Frequency of Job Alerts
*Chunk ID: OHR-REC-0652 | Chapter: Candidates and Candidate Job Applications*

Job alerts aren't triggered or sent as soon as a matching requisition is posted. They're sent once per week (every 7 days)
when there are newly-posted jobs matching the candidate's preferences or the Talent Community they subscribed to.
You can set job alerts to a desired frequency. For example, if you set the frequency to 2 days, this will trigger the job
alerts to be sent every 2 days.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2.
3.
4.
5.

Expand the Candidate Pools section and click Edit.
Select Active.
Use the option Send Job Alert Every n Days to set the frequency to send the job alert.
Click Save.

---

## How Candidates Receive Job Alerts
*Chunk ID: OHR-REC-0653 | Chapter: Candidates and Candidate Job Applications*

Candidates can set up job alerts to receive updates about new job opportunities matching their preferred job category
and location. There are two ways that candidates can set up job alerts:
• In their candidate self-service page.
◦ Candidates select the option "I agree to receive updates about new job opportunities".

◦ Candidates indicate the category of jobs they're interested in and their preferred location.
• When applying for a job.
◦ Candidates select the option "I agree to receive updates about new job opportunities".

◦ The job category and job location are selected for the candidate based on the category and location of
the job they applied for.

Related Topics
• Which scheduled processes are used in Recruiting?

---

## Enable Job Alert for Internal Candidates
*Chunk ID: OHR-REC-0654 | Chapter: Candidates and Candidate Job Applications*

The Job Alerts tile in the Current Jobs page appears by default. This is where internal candidates can subscribe to
receive job alerts for newly posted jobs that match their job preferences. You can set the frequency of these job alerts.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Talent Community section and click Edit.
3. Select Active.
4. Use the option Send Job Alert Every n Days to set the frequency to send the job alert.
5. Click Save.
The notification sent to candidates is available in the Recruiting Content Library: Job Alert Internal Notification
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

Login to the environment and activate a sandbox.
Click the Navigator icon.
Go to Configuration and select Structure.
Click the Me link.
Click the Quick Actions tab.
Expand the Current Jobs link.
Click Job Alerts.
Set the Visible option to No.
Click Save and Close.
Publish the sandbox.

---

## Double Opt In for Job Alerts and Marketing
*Chunk ID: OHR-REC-0655 | Chapter: Candidates and Candidate Job Applications*

Communications
External candidates can opt in to receive job alerts and recruiting marketing communications.
Candidates can opt in when they apply for a job, or sign in into a talent community, or from their candidate self-service
page. When candidates opt in, they receive a message confirming their selection.
Double opt in is an email marketing term where a person informs a company that they want to subscribe to some form
of communication. They typically fill a form on the company's website. (this is the first opt in). Then, the company sends
an email to that person to confirm that the address that was provided is valid. The person then clicks a confirmation link
in the message (this is the second opt in). After the second opt in, the email address provided is added to the company's
communication distribution list.

---

## Enable Double Opt In
*Chunk ID: OHR-REC-0656 | Chapter: Candidates and Candidate Job Applications*

You enable double opt in so that external candidates can opt in to receive job alerts and recruiting marketing
communications when they apply for a job, when they sign in into a talent community, or from their candidate selfservice page.
You can configure the double opt to be global or specific to countries where your organization exists. When you
configure it for specific countries, it covers the following use cases:
• European Union resident applies to a job at European Union.
• Non-European Union resident applies to a job in European Union.
• European Union resident applies to a job in non-European Union countries.
You can use these notifications to ask candidates to confirm that they want to receive recruiting marketing or job alerts.
These notifications are available as email message and SMS text. You can use these notifications as is, configure them,
or create new ones:
• Double Opt In Email Confirmation (for external candidates)
• Double Opt In Email Confirmation (for internal candidates)
The following data is captured for auditing purposes:
• Name of the person who accepted the double opt-in
• Date and time when the double opt in was given
• Location of the person (IP address)
• Specific purpose for which the double opt in was given
• Text of the double opt in message
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0657 | Chapter: Candidates and Candidate Job Applications*

◦ Functional Area: Candidate Experience
◦ Task: Double Opt In Management
2. Select the double opt in configuration:
◦ No Double Opt in

◦ Enable Globally
◦ Set Specific Regions
3. If you selected Set Specific Regions, select the locations. Indicate if you want to enable double opt in if the
candidate's location can't be determined.
4. Click Save and Close.

---

## Configure Candidate Security for Candidate Search
*Chunk ID: OHR-REC-0658 | Chapter: Candidates and Candidate Job Applications*

Your organization can define role-based data security for candidate search. When you configure candidate security for
candidate search, recruiters and Hiring Team members can see candidates that they're responsible for according to
different dimensions such as Country, Person Type, Recruiting Type, Business Unit, and Grade Level.
Note: This feature requires Oracle Search. By default, recruiters and Hiring Team members can see all candidates
when searching for candidates because of the View All role.
Here's what to do
1.
2.
3.
4.

---

## Create a Candidate Security Profile
*Chunk ID: OHR-REC-0659 | Chapter: Candidates and Candidate Job Applications*

Enable the Profile Option for Candidate Security
Create a Data Role and Assign the Security Profile
Assign the Data Role to Users

---

## Create a Candidate Security Profile
*Chunk ID: OHR-REC-0660 | Chapter: Candidates and Candidate Job Applications*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Candidate Security Profiles (Use Show All Tasks to see this task)
2. On the Candidate Security Profiles page, click Create.
3. Enter a name and a description.

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0661 | Chapter: Candidates and Candidate Job Applications*

4. Secure the security profile by selecting dimensions.
◦ Country: Location of the internal or external candidate, based on the address. You can select Not Defined
for candidates without an address.
◦ Recruiting Type: Possible values are Agency Hiring, Campus, Contingent, Executive, Hourly, Professional.
You can select Not Defined to include candidates who didn’t apply.
◦ Person Type: Possible values are Contingent, Employee, Ex-Contingent, Ex-Employee, External.

◦ Grade Level: Based on primary assignment and only applies to internal candidates.
◦ Business Unit: Based on primary assignment and only applies to internal candidates.

---

## Enable the Profile Option for Candidate Security
*Chunk ID: OHR-REC-0662 | Chapter: Candidates and Candidate Job Applications*

You need to enable the profile option ORA_IRC_CANDIDATE_SECURITY_ENABLED at the Site level. When enabled,
candidate security is based on the assigned roles and security profile.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_CANDIDATE_SECURITY_ENABLED.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.

---

## Create a Data Role and Assign the Security Profile
*Chunk ID: OHR-REC-0663 | Chapter: Candidates and Candidate Job Applications*

1. In the Setup and Maintenance work area, search for the task Manage Data Role and Security Profiles and
click the task name.
2. On the Data Roles and Security Profiles page, click Create.
3. On the Create Data Role page, enter a data role, select a job role, and enter role description.
4. On the Security Criteria page, select security criteria to see the appropriate visibility.
5. On the Candidate Security Profile page, select the security profile you just created in the Candidate Security
Profile field.

---

## Assign the Data Role to Users
*Chunk ID: OHR-REC-0664 | Chapter: Candidates and Candidate Job Applications*

1.
2.
3.
4.
5.
6.

From the navigation menu, go to Tools and click Security Console.
Click the Users tab.
On the User Accounts page, find the user to whom you want to assign the data role with the candidate security.
Click Edit.
Assign the role.
Click Save and Close.

Related Topics
• Create and Edit Profile Options

---

## Create Labels to Tag Candidates
*Chunk ID: OHR-REC-0665 | Chapter: Candidates and Candidate Job Applications*

You can create labels that recruiters and hiring managers can use to tag candidates. For example, a recruiter may want
to tag a candidate as being a finance expert.
1. In the Setup and Maintenance work area, go to:
a. Offering: Recruiting and Candidate Experience
b. Functional Area: Recruiting and Candidate Experience Management
c. Task: Manage Recruiting Labels
2. On the Candidate Labels page, click the Create icon.
3. Enter a label name.
4. You can translate the label in multiple supported languages using the Translation Editor tool.
5. Click Save and Close.

---

## Use Fast Formulas to Calculate Job Application
*Chunk ID: OHR-REC-0666 | Chapter: Candidates and Candidate Job Applications*

Computed Fields
You can use fast formulas to calculate computed fields based on the data collected on job applications. Computed fields
are displayed in job application grid views and on the Extra Info tab within the job applications.
1. Create Fast Formulas of Type Recruiting Job Application Computed Field
2. Create Extensible Flexfields to Store Values
3. Configure Job Application Computed Fields
4. Add the Calculate Computed Fields Action to a Candidate Selection Process

---

## Create Fast Formulas of Type Recruiting Job Application
*Chunk ID: OHR-REC-0667 | Chapter: Candidates and Candidate Job Applications*

Computed Field
You create fast formulas using the fast formula type Recruiting Job Application Computed Field.
Before you start
• You can use all the database items supported for fast formulas of type Recruiting Candidate Selection Process.
For a complete list of database items, refer to the spreadsheet Database Items for Oracle Recruiting Cloud Fast
Formulas on My Oracle Support (ID 2723251.1).
• You need to store the returned values of the fast formula in CONDITION_MESSAGE.
Here's what to do
1. In the Setup and Maintenance work area, use the Fast Formulas task.
2. On the Fast Formulas page, select Create in the Actions menu.
3. On the Create Fast Formula page:

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0668 | Chapter: Candidates and Candidate Job Applications*

a. Enter a name for the formula.
b. For the Type field, select Recruiting Job Application Computed Field.
c. Complete the other fields as needed.
4. Click Continue.
5. Enter formula details in the Formula Text section.
6. Click Compile.
7. Click Save.
Related Topics
• Database Items for Oracle Recruiting Cloud Fast Formulas

---

## Create Extensible Flexfields to Store Values
*Chunk ID: OHR-REC-0669 | Chapter: Candidates and Candidate Job Applications*

You use extensible flexfields (EFFs) to store computed field values.
When you create a context for the EFF:
• Set the Behavior field to Single Row.
• It’s recommended to set the context usage to Usage code for candidate application.
When you create a context sensitive segment for the EFF:
• Set the Data Type field to Character (VARCHAR2).
• Set the Value Set field to a minimum of 5 characters and a maximum of 150 characters. This is the maximum
number of characters that can be displayed in an EFF column in the job application grid view.
• In the Display Properties section, select Read-only so that recruiting users can’t edit computed fields in the job
application’s Extra Info tab.
• It's not recommended to have any validation on flexfield segments.
1. In the Setup and Maintenance work area, search for the task Manage Extensible Flexfields.
2. On the Manage Extensible Flexfields page, search for the name Person EIT Information.
3. In the Search Results section, click the Edit icon.
4. On the Edit Extensible Flexfield: Person EIT Information page, click the Manage Contexts button.
5. On the Manage Contexts page, click the Create icon in the Search Results section.
6. On the Create Context page, configure the context.
a. Enter values for Display Name, Code, API Name, Behavior. You need to set the behavior to Single Row.
b. On the Context Usages tab, click the Create icon to define the usage of the context. It’s recommended to
select Usage Code for Candidate Application to display the information to recruiters in job applications.
7. Click Save.
8. In the Context Sensitive Segments section, click the Create icon to add attributes to the context.
a. For the Data Type field, select Character.
b. For the Value Set field, the maximum is 150 characters.
c. In the Display Properties section, select Read-only.
9. Click Save and Close.

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0670 | Chapter: Candidates and Candidate Job Applications*

10. On the Edit Context page, click Save and Close.
11. On the Manage Context page, click Save and Close.
12. When the context is created, you need to attach it to the Person Extra Information category.
a. On the Edit Extensible Flexfield: Person EIT Information page, select the Person Extra Information
category.
b. On the Associated Contexts tab, click the Select and Add icon.
c. Search for the context you created.
d. Click OK.
13. You then need to add the context to an existing page or a new page.
a. On the Edit Extensible Flexfield: Person EIT Information page, click the Pages tab.
b. Select a page or create a new one.
c. Click Save.
d. In the Associated Context Details section, click the Select and Add icon to associate the context to the
page.
e. Click OK.
14.You need to deploy the flexfields to make them available.
a. On the Manage Extensible Flexfields page, search for the Person EIT Information name.
b. Click Deploy Flexfields.

---

## Configure Job Application Computed Fields
*Chunk ID: OHR-REC-0671 | Chapter: Candidates and Candidate Job Applications*

You need to configure computed fields by mapping the Recruiting Job Application Computed Field fast formula to the
EFFs you created. Only the mapped fields are calculated.
Only the mapped fields are calculated.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Job Application Computed Fields Configuration
2. On the Job Application Computed Fields Configuration page, select the flexfield context you created.
Only single-row contexts for job applications are displayed in the Flexfield Context field.
3. Map the fast formula to the flexfield segment.
4. Click Save and Close.

---

## Add the Calculate Computed Fields Action to a Candidate
*Chunk ID: OHR-REC-0672 | Chapter: Candidates and Candidate Job Applications*

Selection Process
You can add the Calculate Computed Fields action to a candidate selection process. This will automatically calculate
computed fields in job application grid views when candidates reach the phase and state of the selection process where
you added the action.
The Calculate Computed Fields action is available when entering a phase, leaving a phase, and for specific states within
a phase.

---

## The Calculate Computed Fields action is asynchronous and the scheduled process Perform Recruiting Candidate
*Chunk ID: OHR-REC-0673 | Chapter: Candidates and Candidate Job Applications*

Selection Process Actions must be run for the calculation to be done. When the process is completed, the calculated
values appear on the job applications list.
Recruiting users with the privilege Manage Candidates Lists (IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS)
can manually calculate computed fields by using the Calculate Computed Fields action available on the job applications
list and within job applications. When recruiting users add the Calculate Computed Fields action from the job
application list, they can select up to 10 job applications for the action to be performed in real time. If they select more
than 10 job applications, the action will be processed in the background and they'll be notified when the action is
completed.

---

## Email Validation
*Chunk ID: OHR-REC-0674 | Chapter: Candidates and Candidate Job Applications*

Email address validation follows RFC standards and is consistent across the entire application. Email address validation
checks for characters that are RFC compliant.
Email address validation is enforced in:
• Career site
• Referrals
• Agency
• Recruiter user interface
RFC-compliant characters include:
• Numbers 0-9
• Uppercase letters A-Z
• Lowercase letters a-z
• Plus sign +
• Minus sign –
• Hyphen • Underscore _
• Tilde ~
• Dot .
• Percent sign %
• Dollar $
• Exclamation mark !
• Question mark ?
• Number sign #
• Ampersand &
• Single quote ‘
• Asterisk *

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0675 | Chapter: Candidates and Candidate Job Applications*

• Slash /
• Equals =
• Circumflex ^
• Grave accent `
• Opening brace {
• Closing brace }
• Vertical bar |

---

## What Candidate Email and Phone Types Are Necessary?
*Chunk ID: OHR-REC-0676 | Chapter: Candidates and Candidate Job Applications*

In Recruiting, you need to define these email and phone types:
• HM - Home Mobile Phone: External candidate home phone number which is added from the career site or by
the recruiter.
• W1 - Work Phone: Internal employee or contingent worker work phone number which comes from Global HR.
• H1 - Home Email: External candidate email address which is added from the career site or by the recruiter.
• W1 - Work Email: Internal employee work email address which comes from Global HR.

---

## What Happens if I Don't Define the Candidate Phone
*Chunk ID: OHR-REC-0677 | Chapter: Candidates and Candidate Job Applications*

Type?
You need to define the candidate phone type to enable several candidate actions such as creating candidate files,
adding candidates to job requisitions, using resume parsing.
You need to enable the Home Mobile Phone (HM) for external candidates, and the Work Phone (W1) for internal
employees.
1.
2.
3.
4.

In the Setup and Maintenance work area, search for the task Manage Common Lookups.
On the Manage Common Lookups page, search for the lookup type PHONE_TYPE.
Enable the Home Mobile Phone (HM) and Work Phone (W1).
Click Save and Close.

---

## What Happens if I Don't Define the Candidate Home
*Chunk ID: OHR-REC-0678 | Chapter: Candidates and Candidate Job Applications*

Email?
You need to define the Home Email (H1) for external candidates and the Work Email (W1) for internal employees to send
email invitations and notifications to candidates.

---

## Candidates and Candidate Job Applications
*Chunk ID: OHR-REC-0679 | Chapter: Candidates and Candidate Job Applications*

1. In the My Client Groups work area, click Person Management.
2. On the Person Management: Search page, search for the person.
3. Select the person in the search results.
4. In the Actions menu, select Personal and Employment, then Person.
5. Click Edit next to Communication Methods and select Email Details.
6. Select Home Email or Work Email.
7. Click OK.
You now need to run the scheduled process Complete the Recruiting Process.

---

## How is The Candidate Name Format Defined?
*Chunk ID: OHR-REC-0680 | Chapter: Candidates and Candidate Job Applications*

A person name format type defines how a person's name appears across applications. In Oracle Recruiting, the
universal name type is used for candidates, for fields that appear in the career site, the create candidate flow, and the
candidate profile.
The person name style is configured using the Manage Person Name Styles task in the Setup and Maintenance work
area.
Here's an example to change the formal of the Suffix field from text to a list of values:
1. You first need to create a lookup for the Suffix field using the Manage Common Lookups task in the Setup and
Maintenance work area.
2. After that, you need to configure the person name style.
3. In the Setup and Maintenance work area, click the Tasks icon.
4. Click Search.
5. Search for the task Manage Person Name Styles.
6. On the Person Name Styles page, select a country.
7. On the Name Styles page, add the Suffix name component if it's not already selected, then add the lookup you
created in Step 1.
Related Topics
• Person Name Styles
• Overview of Lookups

---

# Candidate Pools

## What Happens if I Need to Remove Any Content Items
*Chunk ID: OHR-REC-0681 | Chapter: Candidate Pools*

From the Overall Talent Profile?
To stop gathering any of these items from your candidates, it's not recommended to delete the item in the profile
configuration. Instead, change that item's effective date to end as of today or any date you want.

Set Up a Candidate Pool
You set up candidate pools so that recruiters and hiring managers can group candidates and manage sourcing activities
for a current or future job position that they will potentially fill.
For details, see How do I set up a candidate pool?

---

## Candidate Pool Process Phases and States
*Chunk ID: OHR-REC-0682 | Chapter: Candidate Pools*

The candidate pool management process provides the framework to progress pool members through the sourcing
lifecycle to ensure they're engaged with the organization even if they aren't actively involved in a hiring effort.
The candidate pool process consists of a series of phases and states. Recruiters move pool members from one phase to
another. The process isn't sequential, pool members can go back and forth between phases and states.
The table lists the phases and states provided as part of the default candidate pool process.

Phase

State

---

## Needs Attention
*Chunk ID: OHR-REC-0683 | Chapter: Candidate Pools*

Contacted
Interested
Not Interested
Rejected by Employer
Withdrawn by Candidate

Phase

State

Nurture

---

## Needs Attention
*Chunk ID: OHR-REC-0684 | Chapter: Candidate Pools*

Ready to Be Placed Now
Ready in 6 Months
Ready in 12 Months
Rejected by Employer
Withdrawn by Candidate

---

## Provide Access to All Pools
*Chunk ID: OHR-REC-0685 | Chapter: Candidate Pools*

You organization might need to give some specific people a super-user access to candidate pools so that they can
perform any action related to any candidate pools, though the person isn’t an owner of the candidate pool. With super
user access, users will be able to access all pools at all times, perform global reporting, and efficiently manage talent
community pools by a super user.
As an IT Security Manager, you can grant access to all pools through data security using the Security Console for
managing, selecting, or reporting candidate pools.
• Security business object: Candidate Pool
• Manage Candidate Pool Data (IRC_MANAGE_CANDIDATE_POOL_DATA)
• REST Service privilege: Choose Candidate Pool Data (IRC_CHOOSE_CANDIDATE_POOL_DATA)
• OTBI privilege: Report Candidate Pool Data (IRC_REPORT_CANDIDATE_POOL_DATA)
Using the Security Console, edit the data role to which you want to grant full access to candidate pools and create a new
data security policy. In the Create Data Security Policy, configure the fields as follows:
• Data Resource: Select Candidate Pool as the business object
• Data Set: Select All Values for the data set.
• Actions: Select the actions you want: Choose Candidate Pool, Manage Candidate Pool, Report Candidate Pool.
Reporting users can only report on their own pools and global pools by default. When you add the All Values option
to the data role, it can be applied to both product access and reporting access. To get specific access to a global pool
without having to grant the All Values access, users can mark the global pool as a preferred pool. This adds the user to
the list of owners indirectly, and will grant reporting access without requiring a view all and report all access.

---

## Configure the Candidate Pool Print Feature
*Chunk ID: OHR-REC-0686 | Chapter: Candidate Pools*

You can configure the print feature to allow recruiting users to create a PDF version of pool member information.
1. In the Setup and Maintenance work area, go to

---

## Candidate Pools
*Chunk ID: OHR-REC-0687 | Chapter: Candidate Pools*

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Print to PDF section and click Edit.
3. Select the method to deliver the PDFs:
◦ File Attachment: Users will receive a notification with a zipped file containing a separate PDF for each pool
member. This is the default.
◦ Hyperlink: Users will receive a notification with a link to download the PDFs.
4. Indicate the maximum number of pool members that the user can select for a single Print action. Default is 30,
maximum is 100.
5. Indicate the maximum size of the PDF file. Default is 10 MB, maximum is 10 MB.
6. Click Save.
What to do next
These two notifications are available in Alerts Composer. You can use them as is or personalize them:
• Print Action Download Notification (IRC_PRINT_ACTION_DOWNLOAD): This notification is used when the PDFs
are attached to the notification.
• Print Action Hyperlink Notification (IRC_PRINT_ACTION_HYPERLINK): This notification is used when the PDFs
can be downloaded using a link.

---

## Remove Candidates from Candidate Pools When They
*Chunk ID: OHR-REC-0688 | Chapter: Candidate Pools*

Move to the HR Phase
You can enable a setting that lets you automatically remove candidates from all candidate pools when they move to the
HR phase on a job requisition.
1. In the Setup and Maintenance work area, go to
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Offer section and click Edit.
3. Select the option Remove candidates from candidate pools when they move to the HR phase.
4. Click Save.

---

## Assign Follow-Up Task Privileges
*Chunk ID: OHR-REC-0689 | Chapter: Candidate Pools*

You can assign aggregate privileges to secure the visibility of follow-up tasks.
The following are granted by default to the Recruiter role.
• View Candidate Follow-Up Task (ORC_IRC_VIEW_CANDIDATE_FOLLOW_UP_TASK)

---

## Candidate Pools
*Chunk ID: OHR-REC-0690 | Chapter: Candidate Pools*

• Manage Pending Candidate Follow-Up Task (ORC_IRC_MANAGE_PENDING_CANDIDATE_FOLLOW_UP_TASK)
The following is granted by default to the Recruiting Manager role. This role includes the ability for a recruiting
administrator to delete already completed follow-up tasks for the purposes of cleanup or other reasons.
• Manage Completed Candidate Follow-Up Task
(ORC_IRC_MANAGE_COMPLETED_CANDIDATE_FOLLOW_UP_TASK)
These aggregate privileges handle candidate follow-up tasks for which the user is the owner. Additionally, your
organization might need to give some specific people a super-user access to follow-up tasks so that they can view and
manage tasks for which they aren’t the owner.
As an IT Security Manager, you can grant access to all follow-up tasks through data security using the Security Console
for manage or view Candidate Follow-up Task.
Using the Security Console, edit the data role to which you want to grant full access to candidate follow-up tasks, and
create a new data security policy. In the Create Data
Security Policy, configure the fields as follows:
• Data Resource: Candidate Follow Up Task
• Data Set: Select All values for the data set
• Actions: Select the actions you want: Manage Candidate Follow-Up Task, View Candidate Follow-Up Task

---

# Talent Community

## Talent Community
*Chunk ID: OHR-REC-0691 | Chapter: Talent Community*

Talent Community
When external candidates don't find jobs matching their interests, they can join a talent community to show their
interests in an organization.
Internal candidates can be automatically added to talent community pools based on their job preferences matching
one or more pool attributes. External candidates can create their profile, indicate their preferred location and job family,
import their profile from a third party such as LinkedIn and Indeed, or upload a resume. Candidates also have the option
to receive news about new job opportunities and marketing communications.
Note: Recruiting users can't manually add candidates to a Talent Community. Candidates can only be manually
added to candidate pools that aren't defined as a Talent Community.

---

## Set Up a Talent Community
*Chunk ID: OHR-REC-0692 | Chapter: Talent Community*

You set up a talent community so that external candidates can join it to show their interests in your organization.
Here's what to do
1. Enable Talent Community
2. Configure the Career Site with Talent Community Sign Up
3. Create a Talent Community Application Flow

---

## Enable Talent Community
*Chunk ID: OHR-REC-0693 | Chapter: Talent Community*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Candidate Pools section and click Edit.
3. Select Active.
4. Select the fields to display to external candidates so they can set their preferences when they join a talent
community. Possible options are Category, Job function, and Category and job function. Note that Location is
always displayed.
5. Use the option Send Job Alert Every n Days to set the frequency to send the job alert.
6. Click Save.

---

## Talent Community
*Chunk ID: OHR-REC-0694 | Chapter: Talent Community*

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Career Sites Configuration
2. Select a career site and click Edit.
3. Click the General tab.
4. Expand the Talent Community Sign Up section and specify the following:

◦ Display of a sign up button in the job list
◦ Display of a sign up button when no jobs are found.
◦ Title and description for the talent community.
◦ Label on the button allowing candidates to sign up.
5. Publish the career site.

---

## Create a Talent Community Application Flow
*Chunk ID: OHR-REC-0695 | Chapter: Talent Community*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration
2. Click Create.
3. In the Basic Information section, enter a name and a code for the flow and select Talent Community for the
application flow type.
4. Click Save and Continue.
5. Click Create to create a version of the flow.
6. Enter the version name.
7. Enter the version start date. You can also select the Start on Activation option to activate the version as soon
as it's ready and activated.
8. Select options for the flow.

◦ Legal Disclaimer: You can ask candidates to accept a legal disclaimer. The legal disclaimer appears at the

beginning of the job application flow. Candidates must click Agree to proceed. The Job Application Legal
Disclaimer is configured in the Recruiting Content Library.
◦ Campaign Opt In: You can ask external candidates if they agree to receive recruitment marketing
communications. Candidates don't have to agree to proceed with their job application. The optin check box appears with this short sentence "I agree to receiving future recruitment marketing
communications." If an active version of the campaign opt-in statement is available in the content library,
the sentence is displayed as a link that the candidate can click to read the full statement. The campaign
opt-in statement is configured in the Recruiting Content Library.
◦ Job Alert Opt In: You can ask candidates to set up job alerts to receive updates about new job
opportunities matching their preferred job category and location.
9. Add blocks to the Personal Info section by dragging and dropping them to the desired location. By default, the
Profile Import and Contact Information blocks are added.
10. Click Save and Activate.
The active Talent Community Flow will determine what data can be edited by external candidates in the Edit Personal
Information section of the Profile Management page.

---

## Candidates will see Preferred Location and Preferred Category, or Preferred Job Function on the Talent Community
*Chunk ID: OHR-REC-0696 | Chapter: Talent Community*

sign-up page. They will need to provide a value in at least one of these fields for the sign-up to be successful. If you
added the Profile Import and Contact Information blocks to the flow, they're displayed below these selectors. If any
other blocks are in the flow, they'll be visible after the candidate uses the Show More Fields button.
Note: The Show More Fields button isn't displayed if there's a required field after the Profile Import and Contact
Information blocks.

---

# Candidate Sources

## Talent Community
*Chunk ID: OHR-REC-0697 | Chapter: Candidate Sources*

Candidate Source Tracking
Source tracking helps identify from what source candidates originated. Source information is available for candidates
created as part of initial data load, incremental data imports, and candidates that were added by recruiters or who
created profiles themselves.
Source tracking information is displayed in the Source Info section in the candidate profiles, candidate job applications,
prospect records, and candidate pool members.
When source information is captured, the domain name of the source is captured along with the long URL. The domain
name appears as the display name, whereas the long URL is available in the database for reporting purposes. Source
information (source medium and source name) can be changed by recruiting users to make sure the right source is
captured. Note that the source information of type referral can't be changed.
Note: It's not possible to change the source info when the medium is Candidate created manually, and the source is
Agency.
When recruiting users create candidate profiles, these sources are available.
• LinkedIn
• Facebook
• Email
• Phone
• Resume Handed in Person
The source mediums and sources listed in the following table are provided with the product. For some source mediums
using UTM codes, the list of source names is extensible. You can decide on the actual source name that will be captured.
Here are the source mediums having extensible list of source names:
• Shared for posting
• Job board
• Job aggregator
• Third party

---

## The candidate applied from a
*Chunk ID: OHR-REC-0698 | Chapter: Candidate Sources*

campaign email or from social
media channels.

utm_source=email&utm_
medium=campaign

LinkedIn
Facebook
Twitter

utm_source=linkedin&utm_
medium=campaign
utm_source=facebook&utm_
medium=campaign
utm_source=twitter&utm_
medium=campaign

---

## The recruiter uses the Add to
*Chunk ID: OHR-REC-0699 | Chapter: Candidate Sources*

Job Requisition action to add
a candidate to a job requisition
from another requisition, from
a candidate profile, or after
performing a candidate search.

utm_source=job+requisition&utm_
medium=manual+add

Example:

utm_source=candidate
+search&utm_medium=manual
+add

---

## Candidate Pool
*Chunk ID: OHR-REC-0700 | Chapter: Candidate Sources*

• Source Medium: Candidate
added to job requisition
• Source: Job Requisition

utm_source=candidate+pool&utm_
medium=manual+add

• Job Requisition: Java
Developer
• Added By: John Smith
Candidate added to pool

---

## The recruiter adds a candidate to a
*Chunk ID: OHR-REC-0701 | Chapter: Candidate Sources*

job requisition from another pool,
from a candidate profile, from a
requisition, or after performing a
candidate search.

none

---

## The application automatically adds
*Chunk ID: OHR-REC-0702 | Chapter: Candidate Sources*

a candidate to a talent community
pool by matching candidate
preferences to the pool context.
Example:
• Source Medium: Candidate
added to pool
• Source: Candidate Profile
• Added By: John Smith

---

## The recruiter creates a candidate
*Chunk ID: OHR-REC-0703 | Chapter: Candidate Sources*

manually using the Create
Candidate action. For example, a
recruiter was actively searching for
new candidates on LinkedIn, or a
candidate handed a resume in a
restaurant.

none

---

## The candidate applied from an
*Chunk ID: OHR-REC-0704 | Chapter: Candidate Sources*

external career site or an internal
career site, or a candidate received
a job alert and applied using an
external career site. It doesn't
include referred candidates who
applied using an external or
internal career sites.

utm_source=job+alert&utm_
medium=career+site

---

## UTM Code
*Chunk ID: OHR-REC-0705 | Chapter: Candidate Sources*

Example:
• Source Medium: Career site
• Source: External Career Site
• Career Site: ABC Career Site 001
Intelligent matching

---

## The candidate is selected by the
*Chunk ID: OHR-REC-0706 | Chapter: Candidate Sources*

intelligent matching feature.

none

Example:
• Source Medium: Intelligent
Matching
• Source: Job Requisition
• Job Requisition: Java
Developer
• Added By: John Smith
Job aggregator

---

## The candidate found a link to a job
*Chunk ID: OHR-REC-0707 | Chapter: Candidate Sources*

requisition on a job aggregator.

utm_source=indeed&utm_
medium=job+aggregator

Example:

or imported using Direct Apply

• Source Medium: Job
Aggregator
• Source: Indeed Direct Apply
Job board

---

## The user or agent is referring a
*Chunk ID: OHR-REC-0708 | Chapter: Candidate Sources*

person outside of the company
(external candidate) or an
employee (internal candidate).

utm_source=external
+referral&utm_medium=referral

---

## Internal Referral
*Chunk ID: OHR-REC-0709 | Chapter: Candidate Sources*

Agency Referral

utm_source=agency
+referral&utm_medium=referral

Example:
• Source Medium: Referral
• Source: External Referral
• Referred by: John Smith
• Career Site: ABC Career Site 001
Referral website

---

## The candidate originated from any
*Chunk ID: OHR-REC-0710 | Chapter: Candidate Sources*

other referral website.
Example:
• Source Medium: Referral
Website
• Source: Referral website
domain

none
If you have an external career
site that has a link to the Oracle
Recruiting career site, by default
the Oracle Recruiting career
site is considered as an external
referral and it's logged as such
in the source tracking. To track
candidates as direct visitors, you

---

## UTM Code
*Chunk ID: OHR-REC-0711 | Chapter: Candidate Sources*

need to add the rel="noreferrer"
attribute to the link. For example:
<a href="www.mycareersite.com"
rel="noreferrer"> Find Jobs
Today</a>

---

## The candidate searched for
*Chunk ID: OHR-REC-0712 | Chapter: Candidate Sources*

a company career site or job
requisition using a search engine
such as Google, Yahoo, Bing.

none

Bing
Example:
• Source Medium: Search
Engine
• Source: Google
• Career Site: ABC Career Site 001
Shared job posting

none

---

## The job shared using the copy link
*Chunk ID: OHR-REC-0713 | Chapter: Candidate Sources*

on a career site.

utm_source=external+job
+share&utm_medium=jobshare

Example:
• Source Medium: Share Job
Posting
• Source: Social Media ABC
• Career Site: ABC Career Site 001
Social media

Facebook
Twitter

---

## The candidate found a link to a
*Chunk ID: OHR-REC-0714 | Chapter: Candidate Sources*

career site or job requisition on
Facebook or Twitter.

LinkedIn

Example:

none

• Source Medium: Social
• Source: Twitter
• Career Site: ABC Career Site 001
Third Party

---

## The recruiter manually adds codes
*Chunk ID: OHR-REC-0715 | Chapter: Candidate Sources*

to the job url link.

utm_source=ITJobs&utm_
medium=third+party

Example:
• Source Medium: Third Party
• Source: IT Jobs
• Career Site: ABC Career Site 001
HR

Initial

---

## Note: When the application tries to find the source of a candidate from a URL (using utm_source/utm_medium
*Chunk ID: OHR-REC-0716 | Chapter: Candidate Sources*

attributes), a referrer website, or a source the candidate used to apply, if a match can't be found, the source will appear
as Unknown in the candidate profile and candidate application.

---

## URL Code to Capture a Source
*Chunk ID: OHR-REC-0717 | Chapter: Candidate Sources*

For source mediums that use UTM parameters in the URL, the utm_medium and utm_source parameters must be
added to the URL to capture the source. In some cases, the UTM code is added automatically. In other cases, you must
add it.
Use the following schema:
<client domain>/hcmUI/CandidateExperience/<LanguageCode>/sites/<SiteCode>/job/<jobid>/?
utm_medium=<medium_code>&utm_source=<source_code>
Example:
https://clientpod.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/75/?
utm_medium=jobboard&utm_source=indeed
Only source mediums that use URL parameters can be hand coded.
These source mediums have nonextensible list of source names. You must use the URM code in the above table.
• Candidate added to job requisition
• Career site, job alert
• Referral
• Campaign
These source mediums have extensible list of source names. You can decide on the actual source name that will be
captured.
• Shared for posting
• Job board
• Job aggregator
• Third party

---

## Candidate Sources
*Chunk ID: OHR-REC-0718 | Chapter: Candidate Sources*

You can:
• Modify the name and description of default sources.
• Order the display sequence of default sources.
• Remove default sources but at least one default source must remain on the list.
• Remove manually added sources if they're being used in candidate profiles and candidate job application.
• Translate the name of the sources so that recruiters can see the name of sources in the language they used to
sign in the application.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Candidate Dimension Source Names
2. Modify the sources.
3. Click Save and Close.

---

## Add a Candidate Source
*Chunk ID: OHR-REC-0719 | Chapter: Candidate Sources*

You can add new candidate sources. This way, when candidates are created manually by recruiters the proper source
can be assigned.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Candidate Dimension Source Names
2. Click the Add Row icon.
3. Enter a name for the new source.
4. Click Save and Close.

---

## Source Tracking Information for Candidate Selection
*Chunk ID: OHR-REC-0720 | Chapter: Candidate Sources*

Process Fast Formulas
You can create candidate selection process fast formulas to be used as conditions on automated actions, taking into
account the source tracking information of the job application.
Source tracking database items (DBI) are available to expose source tracking information for job applications and
candidates. Source tracking information is stored at the job application and candidate levels. Information for both levels
is exposed through the DBIs. You can use these DBIs in fast formulas of type Recruiting Candidate Selection Process.
For a complete list of database items, refer to the spreadsheet Database Items for Oracle Recruiting Cloud Fast Formulas
(ID 2723251.1) on My Oracle Support.

---

# Candidate Referrals

## Candidate Referrals
*Chunk ID: OHR-REC-0721 | Chapter: Candidate Referrals*

Collect Candidate Referral Information Using Flexfields
You can create flexfields to allow recruiters, agency users, and employees to enter additional information while referring
a candidate to a job.
When flexfields are configured:
• Recruiting users can view the flexfields in prospect records and job applications in a section
called Referral Additional Info. Recruiting users can update referral additional information of
a prospect or job application if they have the privilege Update Referral Additional Information
(IRC_UPDATE_REFERRAL_ADDITIONAL_INFORMATION). The Edit icon is available next to the Referral
Additional Info section.
• In the agency portal, when agents select the action Submit with Additional Info, they can see the flexfields in
the Referral Info section and provide info in these fields.
• Employees who refer employees or candidates for a job can view the flexfields in the Referral Info section (Me >
Current Jobs > Referrals).
To enable this feature, you need to create referral flexfields, then use these flexfields to create rules.

---

## Create Referral Flexfields
*Chunk ID: OHR-REC-0722 | Chapter: Candidate Referrals*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Source Candidates
◦ Task: Referral Descriptive Flexfields
2. In the Referral Descriptive Flexfields page, click the Edit icon.
Note: When you're in the Referral Descriptive Flexfields page, the display type is set to Hidden. It's
recommended not to change it.
3.
4.
5.
6.
7.
8.

Click Manage Contexts.
In the Manage Contexts page, enter %REFERRAL in the Context Code field and click Search.
In the Search Results section, you will see the two seeded contexts: Agency Referral and Employee Referral.
Select a seeded context and click the Edit icon.
In the Edit Context page, create context sensitive segments.
Click Save and Close.

---

## Create Rules
*Chunk ID: OHR-REC-0723 | Chapter: Candidate Referrals*

By default, flexfields are hidden. To display them, you need to go in Transaction Design Studio and create a rule for
these actions:
• Recruiting - Refer an Employee

---

## Candidate Referrals
*Chunk ID: OHR-REC-0724 | Chapter: Candidate Referrals*

• Recruiting - Refer a Candidate
• Recruiting - Referred Candidates by Agency
• Recruiting - Submit Candidates by Agency
Here's how to create a rule for the Refer an Employee action.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Refer an Employee.
5. Click Add to create and configure a rule to display certain fields.
6. In the Basic Details section, enter the name, description, legal employer, and recruiting type.
7. In the Page Attributes section, set the Referral Descriptive Flexfield to visible.
8. Click the Edit icon if you want to further configure the flexfield.
9. Click Save and Close.

---

# Recruiting Campaigns

## Recruiting Campaigns
*Chunk ID: OHR-REC-0725 | Chapter: Recruiting Campaigns*

Set Up an Email Marketing Campaign
Recruiters use email marketing campaigns to advertise jobs to candidates to generate job applications and referrals.
They can also use campaigns to promote recruiting events and activities to invite candidates to respond to a request,
such as RSVP for an upcoming recruiting event or learn more about the company's benefits and corporate culture.
Here's what to do
1.
2.
3.
4.

---

## Create Campaign Opt In Statement
*Chunk ID: OHR-REC-0726 | Chapter: Recruiting Campaigns*

Add Campaign Opt In Option in Job Application Flow
Configure Campaign Settings
Run Scheduled Processes for Campaign Emails

---

## Create Campaign Opt In Statement
*Chunk ID: OHR-REC-0727 | Chapter: Recruiting Campaigns*

The Campaign Opt In Statement is a text displayed to candidates describing the candidate's agreement to receive
recruitment marketing communications.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library
2.
3.
4.
5.
6.

On the Recruiting Content Library page, click Create.
On the Create Content Item page, select Campaign Opt In Statement in the Category field.
Enter the text for the statement.
Complete the other fields.
Click Save and Activate.

For details, see Create a Content Item.

---

## Add Campaign Opt In Option in Job Application Flow
*Chunk ID: OHR-REC-0728 | Chapter: Recruiting Campaigns*

When you create a job application flow, select the Campaign Opt In option to ask candidates if they agree to receive
recruitment marketing communications. Candidates don't have to agree to proceed with their job application. The opt
in option appears with this short sentence "I agree to receiving marketing communications." If an active version of the
campaign opt-in statement is available in the content library, the sentence is displayed as a link that the candidate can
click to read the full statement.
For details, see Create an Application Flow.

---

## Configure Campaign Settings
*Chunk ID: OHR-REC-0729 | Chapter: Recruiting Campaigns*

You can configure several settings related to campaigns.
1. In the Setup and Maintenance work area, go to:

---

## Recruiting Campaigns
*Chunk ID: OHR-REC-0730 | Chapter: Recruiting Campaigns*

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Campaigns section and click Edit.
3. Configure these settings.
◦ Email Maximum Retry Count: Define the maximum number of retries for emails that failed to be sent.
Default value is 3.
◦ Don't send emails to candidates flagged as don't rehire: Select this option to automatically exclude
candidates from campaigns who aren't recommended to rehire.
◦ Don't send emails to audience members who already received emails in the last period: Select the
time period during which candidates received a primary email on another campaign to define which
candidates can be excluded from the campaign audience. Specify a time frame: 1 week, 2 weeks, 1 month.
◦ Exclude candidates who were included in a recent campaign: Select this option to enable a behavior
which allows the campaign manager to choose whether candidates who were sent at least one primary
email on another campaign are included in the audience. When enabled, by default those candidates
are excluded from the audience. The campaign manager can override this behavior to include these
candidates in the audience. When disabled, this capability doesn't appear to the campaign manager. This
capability provides you with the option to avoid sending candidates campaign emails at high frequency.
◦ Recent campaign period: This value is tied to the above setting where you indicate how recent the
campaign period is. If you select 1 week, it means that the audience members who were part of a
campaign in the last week won't receive campaign emails.
◦ Enable Rich Text Editor in Email Designer: You can enable the rich text editor for users creating campaign
emails.
4. Click Save.

---

## Run Scheduled Processes for Campaign Emails
*Chunk ID: OHR-REC-0731 | Chapter: Recruiting Campaigns*

These scheduled processes are used for campaigns. It's recommended to schedule these processes every 30 minutes.
• Prepare Campaign Email
• Send Campaign Email
• Track Campaign Email Delivery
For details, see Which scheduled processes are used in Recruiting?.

---

## Create Campaign Email Templates
*Chunk ID: OHR-REC-0732 | Chapter: Recruiting Campaigns*

Provide recruiters a selection of email templates so they can create visually engaging emails for their email marketing
campaigns. Recruiters can use the email as is, or they can use the design editor to personalize the content.
Templates are available for each campaign type, that is Respond to Request, Refer Job, Apply to Job. When recruiters
create a campaign, the email template appropriate to their campaign type is available for selection. Recruiters can use
the email as is, or they can use the design editor to personalize the content.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

---

## Recruiting Campaigns
*Chunk ID: OHR-REC-0733 | Chapter: Recruiting Campaigns*

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: HTML Email Templates
2. On the Manage HTML Email Templates page, click Add.
3. Enter a name for the template.
4. Select the template type called Campaign user email template.
5. Select a campaign purpose:
◦ Respond to Request

◦ Refer Job
◦ Apply to Job
6. Select one of the three default templates:
◦ Basic

◦ Blank
◦ Multi-Column
7. Click Save.
Results:
An editor opens in a new browser tab where you can personalize the template. You can personalize elements such as
background color, background image, branding text, fonts, font colors, rows, columns. You can also lock the template so
that users won't modify it.

---

## Add Assets to the Campaign Media Library
*Chunk ID: OHR-REC-0734 | Chapter: Recruiting Campaigns*

Manage an image library as a campaign administrator, and leverage those image assets in campaign email templates,
campaign emails, or landing pages as a campaign manager. Campaign administrators can upload and store images in
the media library so that they’re available to add to email templates and communications.
Campaign managers can then insert an image directly into an email by searching through a library of images. Campaign
administrators and campaign managers can either enter a URL for the image or choose an image from the library. To
upload an image:
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Manage Recruiting Media
2. Select Add and then click in the main area to upload.
3. Name the image.

---

## Recruiting Campaigns
*Chunk ID: OHR-REC-0735 | Chapter: Recruiting Campaigns*

4. Click Save and Activate or Save and Close. The Save and Close option saves the image in draft status. Once
activated, the image is available for use by others using the editor.
Filtering is also available on the Manage Images page. From the Actions menu, you can rename, download, or
activate or deactivate an image.
The media library stores the images and after you activate them. They’re available to insert into email
communications. Deactivating images doesn't remove them from email templates, campaign emails, or landing
pages where they're already being used.

---

# Recruiting Agencies

## Recruiting Agencies
*Chunk ID: OHR-REC-0736 | Chapter: Recruiting Agencies*

Agency Hiring
Agency hiring is designed to allow recruiters to invite agents to submit candidates that they manage to apply on
requisitions.
Here's how agency hiring basically works:
• The administrator creates a recruiting agency and associates one or more recruiting agents to it.
• The recruiter creates a job requisition, selects recruiting agents, and sends them an invitation to submit
candidates for the job.
• Agents receive the invitation by email. They access the agency hiring portal where they can view details about
the job requisition. They scan through candidates in the agency portal Talent section and submit candidates for
the job.
• Candidates receive an email notifying them that their profile was submitted for the job. They view the job
details and apply for the job.
• Recruiting agents go to the agency portal Referrals section to know how candidates they referred are
progressing.
• The recruiter goes back to the job requisition and views the list of job applications. An icon indicates which
applications were referred by agencies. The recruiter can also filter the list using the Referred by Agency filter.
When a candidate is referred by an agent, the information is tracked in the candidate file Source Information
section. You can see the source medium Agency Referral and the source which is the name of the agency that
submitted the candidate.

---

## Agency Portal
*Chunk ID: OHR-REC-0737 | Chapter: Recruiting Agencies*

Recruiting agents have access to an agency portal which provides a common area to manage their interactions with job
requisitions.
As a recruiting agent, you access the agency hiring portal from My Client Groups > Agency Hiring. The agency hiring
portal is organized into four areas:
• Invitations: You can view job requisitions for which you're invited to submit candidates. You can click the Submit
Candidate button to submit a candidate for a requisition. The list of candidates available for selection are
candidates not already submitted for the requisition and candidates who were sourced by the agency for a
specific period of time. Candidates are added to the requisition as prospects.
• Talent: You can view the list of candidates sourced by the agency. You can click the Add button to create a
candidate profile. When you save the information entered about the candidate, a check is done to verify if the
candidate already exists in the agency database. If no duplicate is found, you can continue with the creation

---

## Recruiting Agencies
*Chunk ID: OHR-REC-0738 | Chapter: Recruiting Agencies*

process. An email is sent to the candidate to inform them that a profile was created. The candidate accesses the
candidate self service area of the career site to review their profile and make changes, if any.
Note: If you add a document in the Internal Document section of a candidate profile, the recruiter can view
this document while viewing the candidate profile. When the candidate profile becomes a candidate job
application, the recruiter can no longer see the attached document. To see it, the recruiter needs to go in the
candidate profile and set the option Display Candidate Data to Yes.
• Referrals: You can view candidates you referred and their status. Note that when you add a candidate to a
job requisition and don't create a job application on behalf of the candidate, you can track the status of the
candidate in the Referrals tab. Whereas when you add the candidate to a job and create a job application on
behalf of the candidate, you can track the status of the candidate from the Job Applications tab. This also
means that as soon as the referred candidate applies through a career site (thereby creating a job application),
the candidate application is moved from the Referrals tab to the Job Applications tab.
• Job Applications: You can view job applications for talent sourced by the agency.

---

## Create a Recruiting Agency and Add Agents
*Chunk ID: OHR-REC-0739 | Chapter: Recruiting Agencies*

You can create a recruiting agency as an approved third-party entity and associate one or more agents to it so that
recruiters can invite agents to submit candidates to agency-enabled requisitions.

---

## Create an Agency
*Chunk ID: OHR-REC-0740 | Chapter: Recruiting Agencies*

1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Source Candidates
◦ Task: Recruiting Agencies
2. On the Agencies page, click Add.
3. On the Details page, enter the agency name, agency email, and main contact.
4. Specify the referral type.

◦ Job Specific: The agency gets a commission when a candidate gets hired for a requisition. This type of

agency usually doesn't have exclusive ownership of a candidate. If a candidate applies for another job
on the career site and gets hired, the agency doesn't generally get a referral commission. The exclusivity
setting isn't required for this type of referral.
◦ Person Specific: The agency gets a commission for placing a candidate at the company, regardless of
the referral. This type of agency usually has exclusive ownership of a candidate. If a candidate applies for
another job on the career site and gets hired, the agency still get a referral commission. The exclusivity
setting is required for this type of referral.
5. Specify the contract type.

◦ Transactional: This contract type is used when the agency submits an invoice and gets referral
◦
◦

commission for each successful referral.
Contingent: This contract type is used when the agency gets a commission for a defined number of job
applications within a defined period of time.
Retainer: This contract type is used when the agency gets a commission for a specific period of time,
regardless of the amount of job applications or successful referrals.

---

## Recruiting Agencies
*Chunk ID: OHR-REC-0741 | Chapter: Recruiting Agencies*

6. Set the exclusivity length. This is the amount of time that an agency has exclusive rights to represent a
candidate. When the exclusivity length is configured, if another agency creates a candidate profile that fails
the duplicate check during the exclusivity length period, a warning message is displayed indicating that the
profile already exists. The agency can't add the candidate profile. If another agency tries to create a candidate
profile that fails the duplicate check, and the date isn't within the exclusivity length period, a warning message
is displayed but the other agency is offered the option to move the candidate into their talent pool.
7. Indicate if you want to create a job application on behalf of candidate. If you select this option, agents
who submit candidates for a job requisition or add candidates to a job requisition can create a job
application instead of creating a prospect. Users need the privilege Create Candidate Job Application
(IRC_CREATE_CANDIDATE_JOB_APPLICATION) to see the "Create job application on behalf of candidate"
option when submitting candidates for job requisitions.
8. Enter notes.
9. Click Save and Close.

---

## Add Agents to the Agency
*Chunk ID: OHR-REC-0742 | Chapter: Recruiting Agencies*

1. On the Agencies page, click the agency you just created.
2. In the Agents section, click Add.
3. On the Details page, enter the following info:

◦ First Name, last name, and email of the agent.
◦ Job Family: You can add one or multiple job families to help recruiters find agents based on the
requisition's context. This field is also used as a filter on the agent detail panel.

◦ Responsible Location: You can add one or multiple locations to help recruiters find agents based on the
◦

requisition's context. Agents that have locations that match the location of the requisition will appear
first. All agents will appear in the advanced search, regardless their location. Note that the responsible
location isn't the location of the agent, but the locations the agent is responsible for.
Address

4. Click Save and Close.
The agent will receive an email with a link to change their password. The agent needs to change the password to have
access to the agency portal. If the agent doesn't receive the email to change their password or if they lose the email,
they can enter their email address and select the forgot password link to reset their password.
Note: When an agent is added to an agency, an account is automatically created with a user name and agent role
assigned. Don't change the email address or user name of the agent in the Security Console. Otherwise when the
agent goes to Hiring > Invitations, they won't be able to see the invitation for the specific job requisition.

---

## Hide Candidate Data to Recruiting Agents
*Chunk ID: OHR-REC-0743 | Chapter: Recruiting Agencies*

You can enable a setting to control how much candidate data recruiting agents can see.
If you enable the setting, agents will only view data in the candidate profile Attachments tab. If you don't enable the
setting, agents will view data in the candidate profile Details tab and Attachments tab.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management

---

## Recruiting Agencies
*Chunk ID: OHR-REC-0744 | Chapter: Recruiting Agencies*

◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Agency Hiring section and click Edit.
3. Select the option Hide Candidate Data.
4. Click Save.
Note: Initially, when an agent creates a candidate they can access the full candidate profile to provide complete
information about them. The create action only exposes a small set of fields. Once a candidate profile has been
created, agents are only able to access the subset of sections that are exposed to them.

Related Topics
• Agency Portal

---

## Enable Agent Actions
*Chunk ID: OHR-REC-0745 | Chapter: Recruiting Agencies*

You can enable a setting to give agents the ability to take actions on behalf of candidates to manage the application
process.
When this feature is enabled, agents have additional options available to them by clicking the ellipses icon in the
appropriate sections. Depending on the situation, agents can:
• Withdraw candidate job applications submitted by an agent after they received an invitation to submit
candidates for a job requisition.
• Withdraw candidate job applications.
• Withdraw prospects for a job requisition.
• View job offers on behalf of a candidate.
• Accept job offers on behalf of a candidate.
• Decline job offers on behalf of a candidate.
• View a candidates' scheduled interviews.
• Cancel interviews on behalf of a candidate.
Note: This feature is set at the global level, not at the agency level.

Note: There's auditing that records which agent took an action on behalf of a candidate.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Agency Hiring section and click Edit.
3. Select the Enable Agent Actions check box.
4. Click Save.

---

## Allow Internal Candidate Search by Recruiting Agencies
*Chunk ID: OHR-REC-0746 | Chapter: Recruiting Agencies*

You can enable a setting to allow recruiting agencies to search internal candidates using their email address.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Agency Hiring section and click Edit.
3. Select the option Allow Internal Candidate Search.
4. Click Save.
What to do next
You also need to enable a setting in the Source Candidates functional area.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Source Candidates
◦ Task: Recruiting Agencies
2.
3.
4.
5.

Open an agency.
In the Basic Information section, click Edit.
Select the option Allow Internal Candidate Search.
Click Save.

---

## Run Scheduled Processes for Agency Hiring
*Chunk ID: OHR-REC-0747 | Chapter: Recruiting Agencies*

You need to run these scheduled processes to use agency hiring:
• Import User and Role Application Security Data: This is a one time process that needs to be run when any new
role is delivered in a release.
• Retrieve Latest LDAP Changes: This process needs to be run every time a new agent is created. It should be
scheduled to automatically run on a frequent basis.
• Send Requisition Posting Expiration Date Notification: This process needs to be run daily. It sends a notification
to agents about the requisition posting expiration date.
Related Topics
• Which scheduled processes are used in Recruiting?

---

# Job Offer Letter Templates

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0748 | Chapter: Job Offer Letter Templates*

Job Offer Letter Template
A job offer letter is a formal written document given by an employer to a candidate. The letter confirms details of the
offer such as the proposed job title, proposed starting date, work location, salary, or other compensation.
To create offer letters for candidates, there should be at least one job offer letter template upon which to base the
offer letters. This template provides the formatting, branding, and most of the text that each candidate will see when
they receive their offer letter. It also may be configured to contain tokens that are replaced by specific values for each
person's offer letter. Some recruiters may be able to download and adjust the contents of each offer letter beyond the
template, which is useful for hard-to fill recruiting areas. Then, when each individual offer letter gets presented to the
candidate, this template always displays that candidate's specific job title, offer start date, location or any other selected
information within the template's format.
A company that uses significantly different text in their offers for different groups of candidates might consider having
more than one job offer letter template. Each template could act as a base for each different population of hires. Having
a targeted job offer letter template is useful, for example, for external candidates versus internal workers, for hourly
versus salaried people, or for offers for different countries. Within each job offer letter template, you can use conditions
that show or hide various sentences or area depending on each candidate's values, giving you even more granular
control of the content.

---

## Create a Job Offer Letter Template
*Chunk ID: OHR-REC-0749 | Chapter: Job Offer Letter Templates*

The Template Author creates the job offer letter template. The Template Author performs most of the work in Microsoft
Word, but must have a reasonable understanding of BI Publisher.
Before you start
To create a job offer letter template, you'll need the OTBI Publisher plugin. See How to Download and Use the Microsoft
Word BI Publisher Plugin (DOC ID 2478863.1)
Here's what to do
1.
2.
3.
4.
5.
6.
7.

Get the job offer letter template file.
Get the sample file.
Change text in the job offer letter template file.
Add tokens in the job offer letter template file.
Add conditions in the job offer letter template file.
Preview the job offer letter.
Prepare files to be uploaded in the Recruiting Content Library.
Watch video

---

## Get the Job Offer Letter Template File
*Chunk ID: OHR-REC-0750 | Chapter: Job Offer Letter Templates*

A job offer letter template is a rich text format (.rtf) file that contains formatting, images, text and tokens, conditions, or
other code which show or hide certain parts of the letter.
There are several ways to get a job offer letter template:
• Use the original sample provided by Oracle. Download it from BI Publisher (Shared Folders > Human Capital
Management > Recruiting > Job Offer > Job Offer Letter).
• If the Recruiting Content Library has content items of type Job Offer Letter Template, download one of the .zip
files. The .zip file contains a job offer letter template (.rtf file).
• Get an example from the Oracle community on Customer Connect (https://cloudcustomerconnect.oracle.com).
You can also create a job offer letter template from scratch by creating a text document that can be very simple or highly
formatted. Then, you can use the BI Publisher plugin for MS Office Word to insert tokens and conditions to personalize
the output for each candidate's job offer letter. The template must be saved in rich text (.rtf) format within Microsoft
Word. When you view the file in Word, tokens, conditions, and other code are highlighted in gray. Any users can view
these highlighted elements. However, you must have the BI Publisher plugin to modify the tokens.

---

## Get the Sample File
*Chunk ID: OHR-REC-0751 | Chapter: Job Offer Letter Templates*

The sample file is an extensible markup language (.xml) file that contains all the tokens available for the job offer letter
template. This file is necessary to author any new template because the tokens represent every field that can exist in a
candidate's offer letter. The sample file also contains a set of sample values for these tokens, taken from an example job
offer for an example candidate. These data values affect the preview that you can see of this job offer letter template.
But they have no effect on the real offer letters generated for candidates. Previewing the offer letter shows how it looks
with typical or unusual text, or tests how the conditions affect the display of various paragraphs.
There are several ways to get the sample file:
• You can download the sample provided in the product, from BI Publisher:
a. Go to Shared Folders > Human Capital Management > Recruiting > Job Offer > Data Models.
b. Click Edit.
c. Click the sample.xml link in the Attachment section.
d. Change the extension of the resulting file to .xml before using it.
• You can download your own sample file for your own typical job offer, from BI Publisher:
a. Decide on the ID of an existing job offer that will be used. Note the Offer ID of that offer.
- In the application, find the candidate's name and offer title.
- In BI Publisher, create an auxiliary data model, for instance in your My Folders area.
- In BI Publisher's Data Sets node, on the Diagram tab, create a new SQL Query data set, and enter a
query to retrieve offer information.
- In BI Publisher's Data tab, run that query and choose one of your existing offers from the results to
become your sample.
b. Generate the sample.xml file for that offer.
- Copy the data model JobOfferLetterDM from BI Publisher's Shared Folders area, for instance into
your My Folders area.
- In BI Publisher's Data Sets node, on the Data tab, provide the Offer ID as the second parameter, and
click View.

---

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0752 | Chapter: Job Offer Letter Templates*

- Click Export and provide a file name with the extension .xml.
• If the Recruiting Content Library has content items of type Job Offer Letter Template, you can download one
of the .zip files. If your recruiting administrator has uploaded both a job offer letter template (.rtf file) and a
relevant sample file (.xml file) into the .zip file, then you can use this sample file.
• You can get an example from the Oracle community on Oracle Cloud Customer Connect.
The sample file can also contain example values that might exist in job offer fields. When you view the sample file in
a simple editor such as Notepad, the sample.xml file contains the name of every token in brackets, and the example
value for each field if any. For example: <JOB_OFFER_TITLE>Sales Associate</JOB_OFFER_TITLE>. You can change the
values manually in the sample file, as long as the tokens within brackets remain unchanged. For example, changed to
<JOB_OFFER_TITLE>Assistant Teller</JOB_OFFER_TITLE>.

---

## Change Text in the Job Offer Letter Template File
*Chunk ID: OHR-REC-0753 | Chapter: Job Offer Letter Templates*

You can make simple updates to an existing job offer letter template without having the BI Publisher plugin, without
any connection to the database, and without using the sample file. This file is in rich text (.rtf) format, so you can simply
use Microsoft Word or any tool to change the existing text, formatting, images, and branding. Any tokens or conditions
present in the template can be seen, and can be deleted.
Note: If you plan to add images to the offer letter, you need to store images on a public-facing server that doesn't
require authentication. For example, this can be the same server that you use for your corporate public websites or
any publicly accessible website. Also, you can't store images in Oracle Recruiting Cloud (ORC).The URL can't contain
the customer's POD URL.

---

## Add Tokens in the Job Offer Letter Template File
*Chunk ID: OHR-REC-0754 | Chapter: Job Offer Letter Templates*

To add, view, and update tokens in the job offer letter template, the BI Publisher plugin must be installed in Microsoft
Word and the sample file must be loaded. When the sample file is loaded, Microsoft Word is aware of all available offerrelated fields and how they can be formatted. This work is done within Microsoft Word, which doesn't have to connect to
a database.
First, open the job offer letter template file (.rtf file) in Microsoft Word. Then, to load the sample file in Microsoft Word:
1. On the BI Publisher tab, click Sample XML.
2. Select the sample.xml file. When the file is loaded, the "Data loaded successfully" message is displayed.
To add offer fields in the job offer letter template:
1.
2.
3.
4.

On the BI Publisher tab, click Field. A window appears listing all the offer-related fields.
Place the cursor in the document where you want to insert a field.
Select the field.
Click Insert. The field appears in the template as a token .highlighted in gray.

---

## To see token properties, double-click a token. The BI Publisher Properties window appears and displays which field from
*Chunk ID: OHR-REC-0755 | Chapter: Job Offer Letter Templates*

the database will be shown in the offer letter. It also displays other properties which you can change. For instance, when
displaying fields of type date, a choice is offered among many different date formats.
Tokens that you can include in the job offer letter template are available in BI Publisher.
1.
2.
3.
4.

On the BI Publisher Home page, click the Catalog link.
In the Folders pane, navigate to Human Capital Management > Recruiting > Job Offer > Data Model.
Click Edit.
Select the data model named "JobOfferLetterDM".

---

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0756 | Chapter: Job Offer Letter Templates*

5. Click the Structure tab. You can view the list of tokens using the table view or the output view.
Note: Use the token <REQUISITION_TITLE> when you want to communicate the title of the requisition for which an
offer is made, instead of the token <OFFER_NAME>.

---

## Add Conditions in the Job Offer Letter Template File
*Chunk ID: OHR-REC-0757 | Chapter: Job Offer Letter Templates*

You can add conditions in the job offer letter template to make specific regions of the template shown or hidden
depending on a token's value in each job offer. For example, a template can generate a job offer letter that includes a
list of the candidate's promised bonuses and other compensation, but which omits this whole section for candidates
whose offer doesn't include any bonuses. Or a single template can include specific information about every possible
work location, and for each candidate's offer letter it will display only the one section that's appropriate to that offer's
promised work location. All these variations can be contained within a single job offer letter template file, using
conditions.
To work with conditions in the job offer letter template, the BI Publisher plugin must be installed in Microsoft Word and
the sample file must be loaded.
1. Highlight a region that you want to be displayed only in certain circumstances.
2. On the BI Publisher tab, click Conditional Region. This brings up a BI Publisher window.
3. On the Properties tab, specify which condition must be true for this section to appear.
◦ In the General section, select a value from the available tokens.

◦ In the Condition section, select a value from the available operations such as Equal to, Greater than, Less

than.
4. On the Advanced tab, use the Text to Display field to provide information to other users about the condition in
which this region will appear.
◦ By default, the letter C is displayed to indicate the start of a condition. You can replace this with a more
legible label to explain the specific condition. For example, you can replace the C with "Condition if Work
Location is New York". This label has no effect on the functionality of the condition.
5. Click OK.
6. At the end of the selected region a new tag labeled "EC" will now appear automatically. Click it to bring up a BI
Publisher window.
◦ In the Code field, the tag <?endif?> will appear indicating that the conditional region is finished and the
following sections of the offer will be shown to all viewers. Don't make any changes to this value.
◦ In the Text to Display field, you can provide information to other users about which condition is ending
here. For example, you can replace the default letters EC with a more legible label such as "End of
Condition about New York". This label has no effect on the functionality of the condition.
Note: To retain the value of the candidate type throughout the hiring process, use the token Candidate Type When
Applying.
You can configure the offer letter template to display information about who accepted the job offer and when, and
display the information that's gathered from the light electronic signature of the candidate if this was obtained.
Available fields include:
• E_SIGNATURE_SIGNATURE_DATE
• E_SIGNATURE_SIGNEE_IP_ADDRESS
• ACCEPTED_DATE

---

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0758 | Chapter: Job Offer Letter Templates*

• ACCEPTED_ON_BEHALF_BY
• OFFER_RECIPIENT/DISPLAY_NAME
• MOSTRECENTEXTENDEDDATE
To make the whole section appear only if the offer has been accepted, a condition such as the following can work:
<if:OFFER_DATES/MOSTRECENTOFFRWITHDRAWNDATE !="or ACCEPTED_ON_BEHALF_DATE !="or E_SIGNATURE_SIGNATURE_DATE !
="?>

Note that this also prevents showing the section if the offer was initially accepted but it's currently redrafted and not yet
re-accepted.

---

## Preview the Job Offer Letter
*Chunk ID: OHR-REC-0759 | Chapter: Job Offer Letter Templates*

You can generate a sample job offer letter to preview its content and see if the template is working as configured. The
job offer letter template is merged with a set of sample job offer values. These values are contained in the sample file
that was loaded into Microsoft Word. If you want different values, you can change the sample file and reload it into
Word. Then the preview replaces the tokens in the template with these sample data values, and conditional areas are
displayed or hidden based on the values for that sample offer.
To generate a preview of the job offer letter:
1. On the BI Publisher tab, in the Preview section, click the icon for the desired format to output the offer letter. For
example, PDF, RTF, HTML.
To experiment with different variations of the job offer letter, you can change the sample values in the sample.xml file.
You can change and delete the example values for the example candidate's job offer. However, don't change the offer
field names within brackets.
1.
2.
3.
4.

Open the sample.xml file in a simple editor such as Notepad.
Overwrite the desired values. For example, <JOB_OFFER_TITLE>Sales Associate</JOB_OFFER_TITLE>.
Save the file in .xml format again.
Load the new .xml file into Microsoft Word using the Sample XML button.

---

## Prepare Files to Be Uploaded in the Recruiting Content Library
*Chunk ID: OHR-REC-0760 | Chapter: Job Offer Letter Templates*

When you're satisfied with both the job offer letter template (.rtf file) and the sample file (.xml file), add them into a .zip
file. This allows both files to be uploaded at the same time in the Recruiting Content Library. The .zip file must not
exceed about 3 Megabytes to successfully be uploaded in the library.

---

## Upload the Job Offer Letter Template in the Content
*Chunk ID: OHR-REC-0761 | Chapter: Job Offer Letter Templates*

Library
When Oracle Fusion Cloud Recruiting gets deployed, there are no content items of type Job Offer Letter Template in the
Recruiting Content Library. The Recruiting Administrator must make job offer letter templates available to recruiters,
hiring managers, and other Offer Team members.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management

---

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0762 | Chapter: Job Offer Letter Templates*

◦ Task: Recruiting Content Library
2. Click Create.
3. Enter the following information:
◦ Name

◦ Code
◦ Category: Select Job Offer Letter Template.
◦ Visibility: A content item can be used for internal job offers only, external job offers only, or both.
◦ Start Date: Date and time when the item is available for use. You can select a time zone.
◦ Start on Activation: The content item becomes current as soon as it is made active.
4. Click Choose File to upload the .zip file containing the job offer letter template (.rtf file) and the sample file (.xml file).
5. Click Save and Activate to make the item available for use, or Save as Draft to edit and activate the item at a later
time.
Results:
As soon as the content item is active, Offer Team members can see it as an available choice while drafting candidate's
job offers.
Note: Once the job offer letter template (.rtf file) is uploaded, it automatically appears in the BI Publisher's Shared
Folders area for Job Offer Letters. Do not modify nor delete this file in BI Publisher.

---

## Versioning of Job Offer Letter Templates
*Chunk ID: OHR-REC-0763 | Chapter: Job Offer Letter Templates*

For each job offer letter template, only the current version is used in active candidate job offers. When a candidate's
offer is associated with an offer letter template, the candidate's letter is generated based on the currently-active version
of that template.
If you need to change the content or formatting in the offer letters of future candidates whose offers use a given
template, you need to inactivate the template in the Content Library and upload a new template to a new item in the
Content Library to avoid impacting active offers.
For example, let's say a given candidate's offer letter is drafted in December using the Content Library item named
Sales Offer Letter, which is currently version 1. Then in the Content Library you create a version 2 of the same Sales
Offer Letter, which is intended to be used starting in January. When the original candidate's offer gets extended and
candidates view their offer letter, the offer letter will be based upon the new January version 2, which is already the
current version of this Content Library item.
If that's not the behavior you want, you can instead create a new Content Library item, upload a new template into
it, and consider naming this new item Sales Offer Letter for the New Year. Then, you can inactivate the December
version or the original item named Sales Offer Letter so that it's not selected for new offers being drafted. But existing
offers that already use the original item will continue to use it. So the candidate whose offer was originally drafted in
December will always see the original offer letter, unless their offer gets redrafted and a new offer letter is selected from
the Content Library in the new year.

---

## Job Offer Letter Templates for Multiple Languages
*Chunk ID: OHR-REC-0764 | Chapter: Job Offer Letter Templates*

Candidates may apply for jobs in different countries and in different languages and each person's job offer letter should
reflect that same language.
This can be achieved in different ways depending on the complexity of the business requirements and depending on
whether your recruiters are adjusting candidate offer letters using the method of resolved tokens.

---

## Simple Use Case
*Chunk ID: OHR-REC-0765 | Chapter: Job Offer Letter Templates*

When an organization requires only one or a few different offer letter variations in a small number of languages, it's
possible to create each variation as a separate item within the Recruiting Content Library.
For instance, you may need a retail offer letter template and a headquarters offer letter template, and each of these
template may be needed in two languages: Spanish and English. Four separate items can be created in the Recruiting
Content Library to meet this need. The job offer letter template can be created as four separate documents (.rtf files):
Retail English, HQ English, Retail Spanish, HQ Spanish.
Then each job offer letter template (.rtf file) must be compressed into a .zip file, optionally along with a sample data
file (.xml file). Each compressed file must be attached to a Recruiting Content Library item with a single title in the
appropriate language and the date on which it's active and available to be used.
Ongoing maintenance is usually required over time. When any or all of these four letters need to be updated, the
administrator can download each of them from the Recruiting Content Library, make changes directly in each of the .rtf
files in the appropriate language, and then compress and re-upload it into its item in the Recruiting Content Library.
As each candidate's offer gets drafted, the recruiters would choose from a list of the currently-active offer letter
templates based on the item titles. It's the recruiter's responsibility to select the appropriate letter in the appropriate
language, for instance the English retail template or the Spanish headquarters template. If the recruiters have the right
to download and adjust these offer letters for individual candidates, they will see just the content which is relevant to
each candidate, in the single language which was used in that .rtf file.

---

## Complex Use Case
*Chunk ID: OHR-REC-0766 | Chapter: Job Offer Letter Templates*

Large organizations may require a larger number of offer letter templates, and this gets more complicated if they also
manage several different languages.
In this case, it may be preferable to combine the translations of each letter into a single item in the Recruiting Content
Library. So for instance, there would be one item for retail, one item for headquarters, and any other items which are
needed. Then within each of these templates, all necessary languages would be defined.
Within each single letter template, the same or similar text can be repeated several times, one time in each relevant
language. Each repetition within the letter can be configured to display only to candidates who applied in that language,
using conditions in the letter template. And if desired, the last repetition of the letter's contents can be conditionally
provided in the fallback language, in case candidates are allowed to apply in more languages than translations are
available.
This compound letter is authored and managed as just one template file (.rtf file), which is then compressed together
with one optional sample file (.xml file) into a .zip file and gets uploaded into an item in the Recruiting Content Library.

---

## If this letter's content needs to be updated later on, the administrator can download this .zip file from the item in
*Chunk ID: OHR-REC-0767 | Chapter: Job Offer Letter Templates*

the Recruiting Content Library, make changes to the text in all or any of the languages within its single .rtf file, then
compress and re-upload it into its item in the Recruiting Content Library.
As each candidate's offer gets drafted, the recruiters would choose from a list of the currently-active offer letter
templates based on the item titles. In this configuration, each single template would contain every relevant language
variation. It's the recruiter's responsibility to select the appropriate letter, but the language that will be generated for the
candidate is the language in which the candidate applied.
If the recruiter has the right to download and adjust these offer letters for individual candidates using the resolved
token method, they will see just the content which is relevant to each candidate, in the language in which the candidate
applied regardless of the language preferences of this recruiter. If they download these offer letters to adjust them using
the other method, the recruiter will see each repetition of the selected letter in each language. It's only necessary to
adjust the letter content in the appropriate language in which this particular candidate applied for the job; the other
languages' repetitions will not be displayed to the candidates themselves when the offer gets extended.

---

## Add Language-Related Conditions in the Job Offer Letter
*Chunk ID: OHR-REC-0768 | Chapter: Job Offer Letter Templates*

Template
The language condition is based on a standard token supported by BI Publisher named XDOLOCALE to which you add a
language.
Before you start
The BI Publisher plugin must be installed in Microsoft Word and the sample file (.xml) must be loaded.
Here's what to do
1. Open the offer letter template (.rtf file).
2. Highlight the region that contains the translation of the letter that you want to display to candidates using a given
language.
3. On the BI Publisher tab, click Conditional Region.
This brings up a BI Publisher window.
4. On the Properties tab, don't select any tokens from the offer-related list.
5. On the Advanced tab, in the Code field, insert the language condition with the language code to display the
paragraphs in the selected language. Here are examples:
◦ The tag for English is "en". You need to enter <?if:$_XDOLOCALE='en'?>

◦ The tags for regional variations use the hyphen (not an underscore) such as Canadian French fr-CA,
Brazilian Portuguese pt-BR, and simplified or traditional Chinese using zh-CN and zh-TW.

6. On the Advanced tab, in the Text to Display field, you can provide information to other users about the condition.
By default, the letter C is displayed to indicate the start of a condition. You can replace this with a more legible label
to explain the specific condition. For example, you can replace the C with the words "Conditional for English". This
label has no effect on the functionality of the condition and the candidate won't see it when viewing the offer.
7. Click OK.
8. At the end of the selected paragraphs, a new tag called "EC" will appear automatically. Click it to bring up a BI
Publisher window.
◦ In the Code field, the <?endif?> tag will appear indicating that the conditional region is finished and the
following sections of the offer will be shown to all viewers. Don't make any changes to this value.

---

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0769 | Chapter: Job Offer Letter Templates*

◦ In the Text to Display field, you can provide information to other users about which condition is ending

here. For example, you can replace the default letters EC with a more legible label such as "End of Condition
for English". This label has no effect on the functionality of the condition and the candidate won't see it
when viewing the offer.

9. Click OK.
What to do next
If you want a fallback language for candidates who applied in a language not listed in each conditional region's tags
above, you can highlight the region that contains this final translation of the letter.
1. On the BI Publisher tab, click Conditional Region. This brings up a BI Publisher window.
2. On the Properties tab, don't select any tokens from the offer-related list.
3. On the Advanced tab, in the Code field, insert the language condition with the language code but use the
exclamation point symbol to exclude all of the languages listed in other conditional regions above.
◦ For example: <?if:$_XDOLOCALE!='en' and $_XDOLOCALE!='es'?>
4. On the Advanced tab, in the Text to Display field, you can provide information to other users about the
condition. You can replace the default letter C with a more legible label, for example, "Conditional for Languages
Other Than English and Spanish".
5. Click OK.
6. At the end of the selected region, a new tag called "EC" will appear automatically. Click it to bring up a BI
Publisher window.
◦ In the Code field, the <?endif?> tag will appear indicating that the conditional region is finished and the
following sections of the offer will be shown to all viewers. Don't make any changes to this value.
◦ In the Text to Display field, you can provide information to other users about which condition is ending
here. For example, you can replace the default letters EC with a more legible label such as "End of
Condition for Languages Other Than English and Spanish". This label has no effect on the functionality
of the condition and the candidate won't see it when viewing the offer.
7. Click OK.

---

## Methods to Adjust the Content of an Offer Letter
*Chunk ID: OHR-REC-0770 | Chapter: Job Offer Letter Templates*

Every candidate will see a personalized offer letter, as long as their offer letter template was originally configured with
tokens such as their name, the offer start date, and the new work location.
If you need to add a longer personalized segment of content within the offer letter template, the tokens Additional
Text 1 and Additional Text 2 are available to be inserted within the offer letter template. In some cases, however, it's
necessary to make even bigger changes: to remove some information from the template, for instance, or to change part
of the letter's basic structure for an individual candidate. To meet this business need, users with the privilege Update
Candidate Job Offer Letter (IRC_UPDATE_CANDIDATE_JOB_OFFER_LETTER) can edit the entire offer letter before
extending it to a candidate.
There are two methods to adjust the content of offer letters for each specific candidate.
• Offer letter with all tokens (original method): If you didn't enable the option Download Offer Letter with
Resolved Token, then you're using the original method. The offer letter shows all of the tokens that will
represent the various field values for that candidate, and all the conditional sections that may or may not end
up being relevant to this candidate's situation. The recruiter make changes starting from the letter with all its
tokens. These tokens will be replaced with the current values in the offer fields about this candidate, whenever
a user or approver or the candidate views the offer letter after it's drafted. Some sections of the letter won't be

---

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0771 | Chapter: Job Offer Letter Templates*

shown to viewers because they're conditional, that is, they're dependent on specific values that might not end
up being relevant to the given candidate. Also, because there isn't anything yet entered into the Acceptance
and E-signature fields, that e-signature conditional section at the bottom of the template is full of tokens that
will be resolved later. They will be resolved if and when this offer gets accepted by the candidate.
• Offer letter with resolved tokens: You need to enable the option Download Offer Letter with Resolved Tokens.
With this method, all the tokens get replaced with values entered while creating or editing the offer. The
recruiter won't see any conditional sections, because everything that isn't relevant to this candidate as of right
now has been removed. Only the content that's currently appropriate for the candidate remains in the letter.
This also means there's no e-signature section because this draft offer is currently not accepted. The default esignature section will be added back to the bottom of the letter later, when the candidate accepts the offer. The
recruiter can make any changes to the candidate's offer letter from that starting point, and they can remove
anything not relevant. It's easier to understand what the candidate will see and make the necessary additions or
subtractions.

---

## Option to Download Offer Letter with Resolved Tokens
*Chunk ID: OHR-REC-0772 | Chapter: Job Offer Letter Templates*

Here's how you can enable the option Download Offer Letter with Resolved Tokens.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting and Candidate Experience Information
2. In the Offer Letter section, select the option Download Offer Letter with Resolved Tokens.

---

## Configure E-Signature on Accepted Offer Letters
*Chunk ID: OHR-REC-0773 | Chapter: Job Offer Letter Templates*

The e-signature section in the accepted offer letter can show content appropriate to the situation. The e-signature
configuration depends on whether or not your organization allows recruiters to adjust offer letters using the original
method or the resolved-tokens method.

---

## E-Signature Within Offer Letter Templates
*Chunk ID: OHR-REC-0774 | Chapter: Job Offer Letter Templates*

When candidates provide their full name to accept their job offer, the time, date, and IP address of their acceptance is
tracked. Many companies consider this level of validation and tracking to be a light electronic signature. If a recruiter
accepts a job offer on behalf of the candidate, similar information is also tracked: the name of the user and the time and
date of this acceptance. All of these values can be configured to become part of the offer letter, visible in an e-signature
section at the end of the letter when the candidate or any other user views the letter after it was accepted.
Conditional regions in the offer letter template (.rtf file) can be configured to display this acceptance-related information
as an e-signature section of each candidate's offer letter, only if the offer is accepted. For instance, one tailored
sentence or bullet point can state that the candidate provided their response from a given IP address. If that is accurate,
an alternate sentence or bullet point can state that a given member of the offer team recorded the candidate's
acceptance on a given date. The conditional configuration would ensure that only the appropriate one will be seen in a
given offer letter that has been accepted, and that neither will be displayed when users view the offer during the status
Offer - Extended, for instance, or after a redraft that returned the candidate to the status Offer - Draft.

---

## E-Signature in Multiple Languages
*Chunk ID: OHR-REC-0775 | Chapter: Job Offer Letter Templates*

If your organization maintains job offer letter templates in different languages, it would be appropriate to configure the
e-signature section to appear in each of the languages.
To better explain this scenario, let's use the use cases described in the topic Job Offer Letter Templates for Multiple
Languages.
• For the simple use case, two conditional sections or sentences should be added at the end of each of the
four job offer letter templates in the Recruiting Content Library. The two English offer letter templates would
contain two conditional English sentences explaining either the candidate's light e-signature acceptance or
the recruiter's acceptance on their behalf. The two Spanish offer letter templates would contain two similar
conditional Spanish sentences.
• For the complex use case, there might be a whole set of acceptance-related sections or sentences at the end of
each job offer letter template. In this situation, each sentence would specify the conditions in which it should
be displayed, driven by the candidate's or the recruiter's acceptance as well as by the language in which the
candidate applied to the job.

---

## E-Signature for Adjusted Offer Letter Content
*Chunk ID: OHR-REC-0776 | Chapter: Job Offer Letter Templates*

If your business requires offer letters' e-signature sections or sentences to contain any changes from the default seeded
template or any variations for different audiences or languages, there might be impacts depending on which method is
used for adjusting offer letter content.
• No adjustments to offer letters: If your organization doesn't allow recruiters to adjust offer letter content, it's
only necessary to configure the e-signature conditional section within all the offer letter templates (.rtf files)
that go into the Recruiting Content Library. When candidates view their offer letter and when users preview
them, the letter will display only the appropriate sentences or bullet points, based on the configured conditions
that are relevant for this candidate. These conditions can include multilingual requirements.
• Download offers without resolved tokens: If your organization allows recruiters to download and adjust offer
letters with all tokens (the original method), it's only necessary to configure the e-signature conditional sections
within all the offer letter templates (.rtf files) that go into the Recruiting Content Library. When a recruiter
selects and downloads the offer letter for a given candidate, they see all the tokens and conditional sentences
intended for all possible situations. As long as the recruiter doesn't remove these tokens and conditions, the esignature section remains in the letter as it gets re-uploaded. Then when candidates view their offer letter and
when users preview them, the letter will display only the appropriate sentence or section, in the appropriate
language variation if any.
• Download offers with resolved tokens: If your organization has configured the setting to download offer letters
with resolved tokens, it requires dual configuration to consistently display the light e-signature section if you
need any variations from the defaults. These variations can be driven by the need to display translations of
each sentence in different languages, for instance, or to include less formal wording for certain recruiting types.
First, the e-signature conditional section must be configured within all the offer letter templates (.rtf files) that
go into the Recruiting Content Library. This will be used for all candidates whose offer letter doesn't need to
get adjusted by any recruiter. Recruiters merely select the letter from the menu in the offer flow, and never
download them, so the template's e-signature related conditions don't get stripped out. So when candidates
view their offer letter and when users preview them, there will be an e-signature area displaying the appropriate
sentences or information.
Secondly, another e-signature conditional section can be configured in a shared, central place within BI
Publisher, not handled by the Recruiting Content Library. Based on functionality known as subtemplates, a
default e-signature area will get added to the end of any offer letter which was downloaded and adjusted

---

# Job Offers

## Job Offer Letter Templates
*Chunk ID: OHR-REC-0777 | Chapter: Job Offers*

by a recruiter. Within this e-signature subtemplate, administrators can configure any number of conditional
sentences or bullet points to be added to the end of any offer letter template as desired. This second esignature subtemplate configuration is necessary because when recruiters use the resolved-token method to
download and adjust offer letters, all tokens are resolved and all irrelevant conditions are eliminated from the
template. This allows the recruiter to see only the letter content that's appropriate for that given candidate as
of that moment. In the status Offer - Draft, there are no acceptance values yet, so the conditional sections for
e-signature are removed at the moment of downloading because they're currently irrelevant. Then when the
candidate views their offer letter and when users preview it, the adjusted letter without e-signature and the
subtemplate with e-signature will get combined.
If you have BI Publisher authoring capabilities, you can find the original e-signature subtemplate at Human
Capital Management > Recruiting > Job Offer > Job Offer Letter E-signature.
You can create your own version of this subtemplate if you need to display the appropriate flavor of e-signature
information for all candidate situations, including different languages according to how the candidate applied
to the job. Personalize the original subtemplate, editing it to repeat the desired sentences or bullet points
conditionally as many times as needed.

Job Offer Actions and Privileges
Users with specific privileges can perform several actions depending on the job offer state.

Action

---

## You create a job offer to detail the proposed assignment, salary, and other details to be used if and
*Chunk ID: OHR-REC-0778 | Chapter: Job Offers*

when the candidate accepts the offer and starts working in their new assignment.
If your tasks consist of selecting the right candidate for the requisition, drafting the job offer
completely, and sending it for approval, you need these privileges or duty roles:
• Initiate Job Offer (IRC_INITIATE_ JOB_OFFER_PRIV)
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• Update Job Offer (duty role) (ORA_IRC_UPDATE_JOB_OFFER)
• View Job Offer Salary (duty role) (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• Update Job Offer Salary (duty role) (ORA_IRC_UPDATE_JOB_OFFER_SALARY)
• View Job Offer Other Compensation (duty role) (ORA_IRC_VIEW_JOB_OFFER_OTHER_
COMPENSATION)
• Update Job Offer Other Compensation (duty role) (ORA_IRC_UPDATE_JOB_OFFER_OTHER_
COMPENSATION)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
However, if the above tasks are shared between two roles, a hiring manager and a recruiter, then
the hiring manager needs the Initiate Job Offer privilege to use the Create Offer action to move a
candidate's job application into the Offer - Draft status. The hiring manager can communicate any
intentions or notes to the recruiter and Offer Team using the Comment field. Then the recruiter
performs the other tasks.

---

## You edit a job offer to modify its content. The Edit Offer action is available for job offers in the Draft
*Chunk ID: OHR-REC-0779 | Chapter: Job Offers*

state.
Privileges or duty roles required for this action:
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• Update Job Offer (duty role) (ORA_IRC_UPDATE_JOB_OFFER)
• Any additional standard privileges
If you need to edit fields related to money, you also need these duty roles:
• View Job Offer Salary (duty role) (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• Update Job Offer Salary (duty role) (ORA_IRC_UPDATE_JOB_OFFER_SALARY)
• View Job Offer Other Compensation (duty role) (ORA_IRC_VIEW_JOB_OFFER_OTHER_
COMPENSATION)
• Update Job Offer Other Compensation (duty role) (ORA_IRC_UPDATE_JOB_OFFER_OTHER_
COMPENSATION)

Action

---

## You submit a job offer to have it approved by approvers. The Submit Offer action is available for job
*Chunk ID: OHR-REC-0780 | Chapter: Job Offers*

offers in the Draft state. The action is available while editing the offer.
Privileges or duty roles required for this action:
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• Update Job Offer (duty role) (ORA_IRC_UPDATE_JOB_OFFER)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)

---

## You use the Extend Offer action to communicate a job offer to a candidate. The Extend Offer action is
*Chunk ID: OHR-REC-0781 | Chapter: Job Offers*

available for job offers in the Approved state.
Privileges required for this action:
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)

---

## You use the Resend Offer action if the candidate deleted or misplaced the email that contains the
*Chunk ID: OHR-REC-0782 | Chapter: Job Offers*

link to reach a job offer on the career site. The Resend Offer action is available for job offers in the
Extended state.
Privileges or duty roles required for this action:
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)

---

## You use the Accept Offer action to accept the offer on behalf of the candidate. The Accept Offer
*Chunk ID: OHR-REC-0783 | Chapter: Job Offers*

action is available for job offers in the Extended state, or in the Approved state if the Extend state is
configured to be skipped.
Privileges required for this action:
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
To capture a negative response to an offer on behalf of a candidate, you use the Move Candidate
action.

---

## You use the Redraft Offer action to revise the job offer and start the Offer phase lifecycle again. When
*Chunk ID: OHR-REC-0784 | Chapter: Job Offers*

you redraft a job offer, the state of the offer changes to Draft so you can change the content.
You can redraft a job offer before the job application reaches the HR phase. In that case, you need
these privileges:
• Initiate Job Offer (IRC_INITIATE_ JOB_OFFER_PRIV)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
To redraft an offer after the job application has reached the HR phase, you need this privilege:
• Redraft Job Offer After HR Phase (IRC_REDRAFT_JOB_OFFER_AFTER_HR_PHASE_PRIV)
You can create a custom duty role and keep Redraft Job Offer After HR Phase (IRC_REDRAFT_JOB_
OFFER_AFTER_HR_PHASE_PRIV) if you don’t want to also inherit the privilege Cancel Job Offer (IRC_
CANCEL_JOB_OFFER_PRIV).

Action

---

## You can cancel a job offer for a candidate when the offer is rejected by the employer or the candidate
*Chunk ID: OHR-REC-0785 | Chapter: Job Offers*

has withdrawn. You can use the Cancel Offer action when the job applications are in the following
phases and states:
• Job Offer phase, with the Approved, Extended, or Accepted state.
• Custom phases after the Job Offer phase.
• HR phase, all states except Processed.
Duty role required for this action:
• Manage Job Offer by Recruiting Manager (ORA_IRC_MANAGE_JOB_OFFER_BY_RECRUITING_
MANAGER)
You can create a custom duty role and keep Cancel Job Offer (IRC_CANCEL_JOB_OFFER_PRIV) if you
don’t want to also inherit the privilege Redraft Job Offer After HR Phase (IRC_REDRAFT_JOB_OFFER_
AFTER_HR_PHASE_PRIV).

---

## Preview Offer
*Chunk ID: OHR-REC-0786 | Chapter: Job Offers*

You use the Preview Offer action to see how the job offer letter appears to the candidate.
Duty role required for this action:
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• BI Consumer Role
To see tokens resolved in the offer letter, you need these duty roles:
• View Job Offer Salary (duty role) (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• View Job Offer Other Compensation (duty role) (ORA_IRC_VIEW_JOB_OFFER_OTHER_
COMPENSATION)
• BI Author Role

---

## Move Candidate
*Chunk ID: OHR-REC-0787 | Chapter: Job Offers*

Use the Move Candidate action to change to states Withdrawn by Candidate or Rejected.
To perform the Move Candidate action to these inactive states while the candidate is in the Offer phase
(before the Extended state), this privilege is required: :
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
To perform the Move Candidate action to these inactive states while the candidate is in Extended or
Accepted state, or any subsequent custom phase, these privileges are required:
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)
To perform the Move Candidate action to these inactive states while the candidate is in the HR phase,
this action is done by the HR specialists who need this duty role:
• Address Job Offer (ORA_PER_ADDRESS_JOB_OFFER_DUTY)

---

## The Move to HR action is available for job offers in the Accepted state and in any subsequent
*Chunk ID: OHR-REC-0788 | Chapter: Job Offers*

custom phase that may be configured after the Offer phase. The action is always shown for external
candidates. If a custom phase is configured after the Offer phase and before the HR phase:
• The Move action will move the candidate forward into a state in that custom phase.
• The Move to HR action will skip the custom phase and go directly to the HR phase.
To perform the Move to HR action, you need this privilege:

---

## Job Offers
*Chunk ID: OHR-REC-0789 | Chapter: Job Offers*

Description and Privilege or Duty Role
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)

---

## The Delete Job Application action is available for job offers in the Withdrawn by Candidate or Rejected
*Chunk ID: OHR-REC-0790 | Chapter: Job Offers*

states.
Privilege required for this action:
• Delete Candidate Job Application (IRC_DELETE_JOB_APPLICATION_PRIV)
• View Candidate Job Application (ORA_IRC_VIEW_CANDIDATE_JOB_APPLICATION or ORA_IRC_
VIEW_NON_RESTRICTED_CANDIDATE_JOB_APPLICATION)

---

## When the duplicate check is configured during the Move to HR and when one or more duplicates have
*Chunk ID: OHR-REC-0791 | Chapter: Job Offers*

been identified, the View Duplicates action brings you to the list of possible duplicates. You don't need
any additional privilege to see this action.

---

## Provide Access to Job Offers to Users Not Part of the
*Chunk ID: OHR-REC-0792 | Chapter: Job Offers*

Offer Team
Users can view, update, communicate, move, and process job offers of candidates based on users' privileges, duty roles,
and data security. You can configure users' privileges so that users can see or edit only certain parts of the offers for
which they're specifically included on the offer team. Conversely, you can also configure much wider visibility so a given
user can oversee and manage everything about offers within a certain division or even across the entire enterprise
based on their person security profile.

---

## Job Offer Privileges and Duty Roles
*Chunk ID: OHR-REC-0793 | Chapter: Job Offers*

Users need specific privileges and duty roles to advance a candidate's job application through the rest of the selection
process after it has been selected for a job offer.
The standard role Hiring Manager is defined by default with some simple abilities to view and start drafting job offers.
The main work of creating and communicating job offers is handled by users with the Recruiter role, or the Recruiting
Manager role, which can perform all the actions of the recruiter and more. Then the final steps of the recruiting process
are performed by users with the standard role of HR Specialist.
For details on privileges and duty roles required to perform job offer actions, see Job Offer Actions and Privileges.

---

## Data Security to Access a Job Offer
*Chunk ID: OHR-REC-0794 | Chapter: Job Offers*

Specific data security is also required to access a candidate's job offer.
• A user can access a job offer within a candidate's job application or from the list of offers (My Client Groups
> Hiring > Job Offers or My Team > Hiring > Job Offers) if that user is part of the offer team in that offer's
list. The users can also access the job offer if its offer team includes any user who they supervise within their
management hierarchy. All users with roles based on the standard Hiring Manager and Recruiter roles can
access these offers, regardless of their person security profile within their data roles.
• A user can access a job offer within a candidate's job application or from the list of offers (My Client Groups
> Hiring > Job Offers or My Team > Hiring > Job Offers) if that candidate is within that user's person
security profile, without that user being named on the offer team or managing anyone on that team. This

---

## Job Offers
*Chunk ID: OHR-REC-0795 | Chapter: Job Offers*

capability is available to all users with roles based on the duty role Manage Job Offer by Recruiting Manager
(ORA_IRC_MANAGE_JOB_OFFER_BY_RECRUITING_MANAGER).
• A user can view job offers when they're requested to approve or reject a candidate's job offer. The user doesn't
need to be included in the offer team to see the details of this request. As long as the candidate is within the
user's data role's person security profile, the candidate's offer values will be visible to the user (within the
sections that are visible based on these privileges):

◦ View Job Offer (ORA_IRC_VIEW_JOB_OFFER)
◦ View Job Offer Salary (ORA_IRC_VIEW_JOB_OFFER_SALARY)
◦ View Job Offer Other Compensation (ORA_IRC_VIEW_JOB_OFFER_OTHER_COMPENSATION)
◦ View Job Requisition (ORA_IRC_VIEW_JOB_REQUISITION)
• An HR Specialist can access a candidate's job offer using the quick action Manage Job Offers in My Client
Groups; a candidate's job offer can be accessed if the candidate is within the data role's person security profile.
It's not relevant to be included in the offer team during this HR Phase.

---

## Example: How can a job offer approver see job offer info when they’re
*Chunk ID: OHR-REC-0796 | Chapter: Job Offers*

not part of the offer team and they don’t have the Recruiter or Recruiting
Manager role?
In such a case, when an approver receives a request to approve a job offer, the approver can’t see any job offer info. To
make job offer info visible, you’ll need to:
• Grant the duty role Manage Job Offer by Recruiting Manager
(ORA_IRC_MANAGE_JOB_OFFER_BY_RECRUITING_MANAGER)
• Grant the duty role View Job Requisition (ORA_IRC_VIEW_JOB_REQUISITION)
• Assign the Person Security Profile to All People.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.

In the Security Console, click the Users tab.
Search for the job offer approver.
Click the name of the approver.
In the Roles section, note the role assigned to the user.
Click the Roles tab.
On the Roles page, search for the role you noted and click it.
In the Search Result Count box, click the down arrow and select Edit Role.
On the Edit Role page, click Next until you reach the Role Hierarchy page.
Click Add Role.
In the Add Role Membership window, search for the duty role Manage Job Offer by Recruiting Manager.
Click Add Role Membership.
Search for the privilege View Job Requisition.
Click Add Role Membership.
Click Cancel to close the window.
Click Next then click Save and Close.

To assign the security profile:
1. In the Setup and Maintenance work area, search for the task Manage Data Role and Security Profiles and
click the task name.

---

## Job Offers
*Chunk ID: OHR-REC-0797 | Chapter: Job Offers*

2.
3.
4.
5.

On the Data Roles and Security Profiles page, search for the role you noted earlier.
Select the role and click Edit.
On the Edit Data Role page, click Next to view the Edit Data Role: Security Criteria page.
Select the View All option for each security profiles section. For example, select View All Job Requisitions in the
Job Requisition Security Profile section.
6. For the Person Security Profile, make sure you select the proper security.
7. Click Next, then Submit.

---

## Configure Job Offers When and Why Section
*Chunk ID: OHR-REC-0798 | Chapter: Job Offers*

The When and Why section is required when creating or editing a job offer, and can't be configured to be hidden.
All four fields in that section must have values to proceed, because they affect the subsequent fields and regions on
the offer page. If any of these fields are configured to be hidden, still they must receive values to proceed with the offer
process. If the fields Legal Employer and Worker Type didn't inherit values from the related requisition, for example, and
if they can't be filled manually by the user, then it will be impossible for the user to select an appropriate value for the
Action field.
Related Topics
• How You Configure Recruiting Pages Using Transaction Design Studio

---

## Configure Job Offers to Respect Requisition Headcount
*Chunk ID: OHR-REC-0799 | Chapter: Job Offers*

As candidates move through the lifecycle, the requisition is checked to ensure that an additional worker is still needed,
or to prevent that move if the opportunity is no longer available.
A requisition is considered to be at its limit of candidates when the number of openings is the same or less than the
number of candidates who are hired plus those who have an extended or accepted offer. Any candidate at or beyond
the Offer - Extended status is counted in this tally. Any of these candidates who later move into the state Rejected by
Employer or Withdrawn by Candidate are subtracted from this count.
Only users with the privilege Communicate Job Offer Ignoring Number of Openings
(IRC_COMMUNICATE_JOB_OFFER_IGNORING_NUMBER_OF_OPENINGS) can hire more candidates than the number
of openings on the requisition. These users can move forward as many job applications as they want through the Offer
phase, and no verifications against the requisition are done.

---

## When Are Offer Verifications Done Against Requisitions
*Chunk ID: OHR-REC-0800 | Chapter: Job Offers*

Here's when the requisition's remaining number of openings is checked in the job application's lifecycle:
• When users use the Submit button while creating or editing a job offer: A job offer can be drafted for a
candidate's job application regardless of any limits, but a validation occurs when the user is ready to submit
it into the approval cycle. When clicking the Submit button in the flow Create Offer or Edit Offer, the user

---

## Job Offers
*Chunk ID: OHR-REC-0801 | Chapter: Job Offers*

might receive an error message. The job offer can't be submitted if the requisition doesn't have any remaining
openings, counting both hired people and extended offers - unless the user has the privilege to ignore this
limit. This saves time for the approvers because there's little point in approving another offer if there's no room
for this candidate in the requisition.
• When using the Extend Offer action: By the time the user is ready to extend the draft job offer to the candidate,
it's possible that the requisition or position was updated or became filled, so that no room now remains for
this candidate. The same check is performed before the status can be moved to Offer - Extended, to prevent
notifying a candidate about a job offer for an opening that no longer exists. Only users with the privilege to
ignore this limit can extend the offer.
• Configurable when the Extend Offer action is triggered automatically: If the requisition's candidate selection
process is configured to extend job offers, either immediately or after a delay, the requisition's count of hired
candidates isn't checked by default. However, the automatic progression can be configured to check and
prevent the extend of the offer if the requisition is full. Note that the job application will only be available to be
extended if the requisition had enough openings to allow submitting the draft offer in the first place.
• Never Upon Accept: As long as the job offer is in the state Extended, the candidate isn't prevented from
accepting the offer. This is also true for the Recruiting user who might accept the offer on behalf of the
candidate. Even in the unlikely case that the requisition was updated or got more hires in the meantime, the
candidate and users aren't informed of these limits. It will be the responsibility of the HR specialists to reconcile
any problems after this point.
• Never upon Move to HR: When the candidate moves into the HR phase, no further validation is done for the
requisition's limits.

---

## Configure Job Offers to Respect Positions
*Chunk ID: OHR-REC-0802 | Chapter: Job Offers*

Businesses who use positions to control hiring have several ways to validate that there is enough room for each new job
offer, in addition to checking the requisitions' hiring limits.
An offer can be based on a position that has an approved hiring status, and its progress can be checked against the
position's headcount and FTE at many points.
You can configure the ways in which positions ensure offers don't exceed various limits.
• Check Position Hiring Status: This global profile setting controls whether or not offers and all other
assignments can be created based on positions in any hiring status, or only those with the hiring status of
Approved and not Proposed or Frozen. (This is unrelated to the position's status of Active or Inactive.)
• Number of Incumbents Validation: This global profile setting controls whether or not all positions' headcount
is enforced across your organization. When you enable this setting, many worker-related actions will verify
whether a new assignment's position still has enough open headcount and vacant FTE such as adding pending
workers, hiring new people, transferring internal workers, and managing candidate job offers, when any of
these are based on positions.
• Allow Overlap: This option is available for each position to control whether or not extra people can be hired
when that position's headcount and FTE limits have been reached.
When 's position's headcount and FTE limits considered to be reached? A candidate is considered to be an incumbent
as of their proposed start date, as soon as their job application has reached the Offer - Extended status in the recruiting
lifecycle (and all later states, except the states Withdrawn by Candidate or Rejected by Employer in any phase). These
incumbent candidates are added to all other incumbents as of the offer's proposed start date, to calculate whether or
not additional job offers should proceed through the recruiting lifecycle.

---

## Job Offers
*Chunk ID: OHR-REC-0803 | Chapter: Job Offers*

To expose the Check Position Hiring Status setting to check position hiring status for all position-based assignments,
including offers, you need to enable the profile option ORA_POS_HIRING_STATUS_FILTER at the Site level. Enter Y for
yes to perform the validation, or leave it null or enter N to disregard each position's hiring status.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
ORA_POS_HIRING_STATUS_FILTER.
6. Set the profile value at the Site level. Enter Y for yes to perform the validation, or leave it null or enter N to
disregard each position's hiring status.
7. Click Save and Close.
To expose the Number of Incumbents Validation setting for all position-based assignments, including offers:
1. In the Setup and Maintenance work area, search for the task Manage Extensible Flexfields.
2. On the Manage Extensible Flexfields page, search for the profile option code
PER_ORGANIZATION_INFORMATION_EFF.
3. In the Actions menu, click Edit.
4. Select the classification Enterprise in the Organization category.
5. In the Enterprise Details section, add the Add Position Incumbent page.
To enable the Number of Incumbents Validation setting for all position-based assignments, including offers:
1. In the Setup and Maintenance work area, search for the task Manage Enterprise HCM Information.
2. In the Position Incumbent Validation section, select the option Apply Incumbent Validation.
If the Number of Incumbents Validation settings isn't exposed or is exposed and unchecked, no validations will be
done for position-based offers and all other assignments that include a position. If the setting is exposed and checked,
validations will be performed across the suite, including Recruiting and any hiring actions directly within HR.

---

## When Are Offer Verifications Done Against Positions
*Chunk ID: OHR-REC-0804 | Chapter: Job Offers*

Here's when the requisition's remaining number of openings is checked in the job application's lifecycle:
• When drafting a job offer based on a position: Only positions whose hiring status is Approved (and not
Proposed nor Frozen) as of the offer's projected start date can be found in a search when creating a job offer, if
this field is configured to be checked.
• When users use the Submit button while creating or editing a job offer: A job offer can be drafted for a
candidate's job application regardless of how many incumbents its position has. When the user goes to submit
it into the approval cycle, they might receive a warning or error message. The draft offer can't be submitted if
its position doesn't have sufficient open headcount or sufficient vacant FTE as of its proposed start date (unless
the Number of Incumbents Validation is disabled). However, if the position is configured to allow overlap, the
user is warned that this candidate will be overfilling the position as of their offer start date, but they're given the
choice of continuing anyway and submitting the draft offer for approval.
• When using the Extend Offer action: By the time the user is ready to extend the draft job offer to the candidate,
it's possible that the position was updated or got additional incumbents. There isn't enough headcount or FTE
for this candidate. The same validations are performed before the status can be moved to Offer - Extended,
displaying the appropriate error or warning message according to the relevant setting and option above.
• When the Extend Offer action is triggered automatically: If the requisition's candidate selection process is
configured to extend job offers, either immediately or after a delay, the position's number of incumbents is
checked. The automatic action is successful if the position has sufficient open headcount and vacant FTE, or
if it allows overlap. If there is no room and the position doesn't allow overlap, then extend won't be successful,
and the candidate's job application will remain in the Offer - Approved status.

---

## Job Offers
*Chunk ID: OHR-REC-0805 | Chapter: Job Offers*

• Never Upon Accept: As long as the job offer is in the state Extended, the candidate isn't prevented from
accepting the offer. This is also true for the Recruiting user who might accept the offer on behalf of the
candidate. Even in the unlikely case that the position was updated or got more incumbents in the meantime,
the candidate and users aren't informed of these limits. It will be the responsibility of the HR specialists to
reconcile any problems after this point.
• Upon Move to HR, manually or triggered automatically: The move into the HR phase is always successful,
whether the recruiting user triggers it or, it was automatically triggered within the candidate selection process.
However, if the position will already have sufficient headcount or FTE as of the offer's proposed start date and
if overlap isn't allowed, the candidate will arrive in the HR phase in the state Error During Processing. It's the
responsibility of the HR specialist to handle this situation. But if the position allows overlap, even if it doesn't
have enough room, the candidate will be moved into the HR phase without a problem, and the warning will
remain visible in the Errors section of the Offer page.

---

## Configure Job Offers with a Payroll Section
*Chunk ID: OHR-REC-0806 | Chapter: Job Offers*

You can configure job offers to display the Payroll section.
The Payroll section is displayed by default for offers to internal candidates (employees). For external candidate offers,
you can decide to display it as well.
In some cases, the salary basis selected for an offer requires a payroll to be selected as well while the offer is being
drafted. The element linked with the salary basis could have been configured with element eligibility defined either on
a specific payroll or on all payrolls. This would be against the general recommendation of keeping the element eligibility
open. This means that the selected salary basis can only be used by certain payrolls, and if no payroll is selected while
drafting this offer, there will be an error in processing the candidate to become a worker.
Similarly, any individual compensation plan's eligibility can be configured to rely on either eligibility profiles or element
eligibility. It's recommended to configure eligibility profiles rather than payroll element level eligibility. But when payroll
eligibility is defined on a specific payroll or all payrolls, then the candidate's offer needs to specify a payroll in order for
this compensation plans to be displayed as available for that candidate.
When the Payroll section is displayed, several fields are visible by default depending on the country related to the legal
employer of the offer. These fields are shown due to rules in Transaction Design Studio that are delivered as part of the
solution by Oracle's localization teams. These rules are based on each country's legal regulations and ensure that the
necessary information can be gathered and displayed, for instance the field Tax Reporting Unit in such countries as
Canada, China, Ireland, Mexico, the United Kingdom, and the United States.
To display the Payroll section for your requirements, you need to create rules in Transaction Design Studio.
• While creating or editing a job offer, these rules might be useful to gather payroll attributes as needed.

◦ A rule to display the Payroll section while a new offer is getting create for an external candidate.
◦ One or more rules to display the Payroll section while editing existing offers. For example, you can add
◦

a rule to show the Payroll section for offers whose When and Why section specifies the actions Add
Pending Worker and Add Pending Work Relationship.
One or more rules to hide the Payroll section when it's not relevant, such as for internal mobility. For
example, you can add a rule to hide the Payroll section for offers whose When and Why section specifies
the actions Promote, Transfer, and similar actions.

• While viewing job offers within the Hiring area, you might want to configure a rule to show or hide the Payroll
section, based on the actions for external versus internal offers or any other attributes.

---

## Job Offers
*Chunk ID: OHR-REC-0807 | Chapter: Job Offers*

• While viewing job offers within the Manage Job Offers area, you might want to show or hide the Payroll section,
based on the same attributes.
To display the Payroll section while creating or editing an offer in status Offer - Draft:
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Create and Edit Job Offer to configure rules pertaining to entering job offer
values while in the offer is in status Offer - Draft.
5. Click Add to create a rule to display the Payroll section.
6. In the Basic Details section, enter a name and description for the rule. Complete the other fields as needed.

◦ To create a rule for external candidates, select values in the Action field such as Add Pending Worker and
◦

Add Pending Work Relationship.
To create a rule for internal candidates, select values in the Action field such as Promote and Transfer.

7. In the Show or Hide Regions section, you can make the Payroll Info region visible. You can also make it required
so that users always see this section as they create or edit each offer, without getting a choice of hiding it from
the questionnaire page.
8. In the Page Attributes section, select the Payroll Info region, and decide which fields to make visible and
mandatory. Because there are delivered rules that already display specific fields needed for specific countries,
you should check whether your business requires additional fields for those countries. If the delivered rules
suffice for your needs, it's not necessary to define anything further for Payroll in this Page Attributes section as
long as the region is configured to show above in the Show or Hide Regions section.
9. Click Save and Close.
To display the Payroll section while viewing the offer page within a job application and viewing it from the quick action
Manage Job Offers:
1. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
2. Click the Transaction Design Studio tab.
3. Select the action Recruiting - View Job Offer in Job Application or Recruiting - View and Manage Job
Offer.
4. Click Add to create a rule to display the Payroll section.
5. In the Basic Details section, enter a name and description for the rule. Complete the other fields if desired, such
as selecting all the actions which are relevant to external candidate offers like Add Pending Worker and Add
Pending Worker Relationship.
6. In the Page Attributes section, select the View Job Offer in Job Application or View and Manage Job Offer
region, and decide whether the section should be shown for this set of offers.
7. Click Save and Close.

---

## Populate Job Offer's Salary from Grade Ladder
*Chunk ID: OHR-REC-0808 | Chapter: Job Offers*

The value of a job offer's salary is populated based on the grade or grade ladder specified in the candidate's
assignment.
If the job or assignment section of the job offer defines a grade or a grade ladder with or without a step, then the
associated salary will get pre-filled by default in the Salary section of the job offer.
1. In the Setup and Maintenance work area, use the Progression Grade Ladders task.
2. When you create the progression grade ladder:

---

## Job Offers
*Chunk ID: OHR-REC-0809 | Chapter: Job Offers*

a. Set Include Salary Updates to Yes.
b. Set Salary Calculation Method to Use grade step rate.
3. This feature is relevant for any offers assigned to a salary basis with the salary basis type of Salary amount is
determined by user.
4. Include the Salary section in your offer flow.
5. Include the Grade Ladder, Grade, and Step attributes in the Assignment section of your offer flow. This will require
configuration using Transaction Design Studio, in HCM Experience Design Studio.
Exception: If your grades don't have steps, then you won't need to include the Step attribute.
Related Topics
• Basic Process to Default Salary Amounts from Grade Ladder Rates

---

## Configure Job Offers with an Other Compensation
*Chunk ID: OHR-REC-0810 | Chapter: Job Offers*

Section
You can select individual compensation plans to be awarded to candidates as part of their job offers.
By default, the Other Compensation region is shown and you can choose the eligible plans. You can award
compensation in addition to salary, such as bonuses, stock, car allowance, or other forms of compensation.
Recruiters can't see a specific plan during the Create and Edit Offer process due to the candidate being not eligible for
this plan or option combination, or due to an improper configuration in one of several areas. To identify the improper
configuration, check the below areas:
• Is the individual compensation plan in the state Active? Making the plan visible for the offer team to select in
the Offer process might be as simple as checking that the plan is active.
• Is the plan access configured for the offer's selected action in the When and Why section? Individual
compensation plans that grant access only to the actions Create Offer and Edit Offer won't be shown in the
offer, because these won't be preserved if and when the candidate moves to pending worker and eventually to
worker. Instead, you can configure the plan access to actions such as Add Pending Worker, Transfer, Promotion
to make it visible while drafting a relevant offer.
• Is the candidate eligible for the individual compensation plan's eligibility profile? Based on the offer that has
been drafted so far for this candidate, they're currently eligible for certain plans, and possibly not eligible for
others. This eligibility is calculated on the information about the offer's assignment, which, for instance, might
be in a certain group of the company, and isn't based on any other current or past assignment the candidate
might have had. So removing any eligibility profile from the individual compensation plan will remove this
restriction and make the plan visible to select while drafting this offer.
• Is the plan configured to be accessed by the appropriate actions? Some individual compensation plans are
intended to be awarded to new hires but not for rehires; others could be reserved for internal mobility processes
only. In the configuration for the individual compensation plan, you can decide not to restrict plan access to
make the plan visible when drafting offers, or you can configure to use the appropriate actions that will limit
those actions only.
• Is the person eligible for the element itself? To ensure that the plans are available to be selected:

◦ Verify that the element and eligibility start dates are far enough in the past to encompass the date when
this offer was first drafted.

◦ Verify that the candidate's offer is eligible per the element eligibility. It's recommended to define open
◦
◦

eligibility at the element level, to remove this restriction.
Verify that the element is attached to the legal employer and legislative data group in which this offer is
being drafted, and that the element exists in the legislative data group.
Verify that the payroll relationship mapping is defined for the following person types: Employee
Candidate (Candidate Standard), Contingent Worker Candidate (Candidate Element Entries Only),
Pending Employee (Pending Worker Standard).

---

## Note: To view the Other Compensation section in a job offer, make sure that these payroll relationships are added
*Chunk ID: OHR-REC-0811 | Chapter: Job Offers*

using the Configure Legislations for Human Resources task in the Setup and Maintenance work area.
System Person Type

---

## Configure Job Offers with Delayed Compensation
*Chunk ID: OHR-REC-0812 | Chapter: Job Offers*

You can configure job offers with individual compensation plans allocated on the projected start date or after a delay.
You can promise individual compensation plans to the candidate on the same day that their new assignment begins, or
a certain number of days or weeks after that.
You can synchronize individual compensation plan start and end dates with the projected hire date defined in the
offer. Then whenever recruiters change the projected hire date in the offer and then go to the individual compensation
section, the plan dates will adjust automatically. For example, the projected start date of an offer is January 1, 2022 and
the plan allocation starts the same day. Later the projected hire date changes to February 1, 2022. When you get to the
individual compensation section, the existing plan start date adjusts to February 1, 2022, to align with the new projected
hire date.
Alternatively, you can set a delay. When the offer is drafted, the plan start and end dates are automatically set using the
projected hire date and the specified delay. For example, an offer includes a sign-on bonus to start 1 month after the
projected hire date. Since the current projected hire date is February 1, 2022, the start date of the bonus plan is set to
March 1, 2022 after you go to the individual compensation section.
You can let recruiters override the calculated plan start date, end date, or both when they include the plan in their
draft offers. But when the recruiter overrides the dates, the synchronization can no longer happen automatically and
they have to manually intervene for every change in the projected start date. Their intervention involves deleting the
awarded individual compensation and adding it again, not correcting the dates of the existing plan.

---

## Force Users to Access Sections While Creating Job Offers
*Chunk ID: OHR-REC-0813 | Chapter: Job Offers*

When you create or edit rules for the Recruiting - Create and Edit Job Offer action in Transaction Design Studio, you can
define if sections within a job offer must be accessed or not by users.
When sections are configured as required, users who create or modify job offers need to access and open these
sections in the offer to be able to save the offer or submit it for approval. If fields within a required section are
configured as Required, users won’t be able to leave the section until those required fields are filled. Also, if users don’t
access required sections, an error message is displayed indicating which ones need to be accessed to proceed with the
selected action.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the actions Recruiting - Create and Edit Job Offer.
5. Click Add to create a rule to display certain sections and fields. You can also modify an existing rule.
6. In the Basic Details section, enter a name and description for the rule. You can select a role name, recruiting type,
and country.
7. In the Show or Hide Regions section, set the Show questionnaire page to Yes to display the Required/Not Required
configuration option for all sections of the requisition.
8. You can change the value of the Required/Not Required configuration option for all sections, except the How
section. This section must be visible every time a new requisition is created. When you set a section as Required, it's
automatically set as Visible.
9. Click Save and Close.

---

## Configure Job Offer Flexfields
*Chunk ID: OHR-REC-0814 | Chapter: Job Offers*

Different types of flexfields are available within a job offer, and they're shown in different sections of the Offer page.
Offer flexfields (IRC_OFFERS_DFF) are shown on the Offer page, in the Additional Info section.
You can define the following flexfields, for both global segments and context-sensitive segments:
• 90 text flexfields
• 30 number flexfields
• 10 date flexfields
• 10 time flexfields
Here's what to do
1. Configure Job Offer Flexfields
2. Display Job Offer Flexfields

---

## Configure Job Offer Flexfields
*Chunk ID: OHR-REC-0815 | Chapter: Job Offers*

You first need to configure job offer flexfields.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Job Offers
◦ Task: Job Offer Descriptive Flexfields
2. On the Job Offer Descriptive Flexfields page, select Job Offer Descriptive Flexfield.
3. In the Actions menu, click Edit.
4. The Global Segments section shows flexfields available to all offers regardless of context. Each row may display
a value set to control the available answer options, and a prompt to label them on the page. Click the Create
icon to add any new global flexfields that are needed.
5. The Context Segment section shows flexfields available to certain offers after the user selects their desired
context. Each row may display a value set and a prompt. Click the Create icon to add any context flexfields that
are needed. Change the context by selecting another value in the menu at top of this section, so that additional
sets of flexfields will be shown and can be augmented as needed.
6. Click Save and Close.
7. When you're back on the Job Offer Descriptive Flexfields page, click Deploy Flexfield.

---

## Display Job Offer Flexfields
*Chunk ID: OHR-REC-0816 | Chapter: Job Offers*

You use Transaction Design Studio to create rules to display offer flexfields using these offer actions:
• Recruiting - Create and Edit Job Offer displays offer flexfields while drafting job offers in the Hiring work area.
• Recruiting - View Job Offer in Job Application displays offer flexfields on the Offer tab of job applications in the
Hiring work area.
• Recruiting - View and Manage Job Offer displays offer flexfields on the offers in the Manage Job Offers quick
action.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select one of these action:

◦ Recruiting - Create and Edit Job Offer
◦ Recruiting - View Job Offer in Job Application
◦ Recruiting - View and Manage Job Offer
5.
6.
7.
8.

Click Add to create and configure a rule to display offer flexfields.
In the Basic Details section, enter the name and description for the rule.
In the Show or Hide Regions section, make sure Additional Info is set to Visible.
In the Page Attributes section, Additional Info is selected by default. Set the Job Offer Descriptive Flexfield to
Visible to display any selected offer flexfields.
9. Click the Edit icon.

◦ Flexfield Content Code: Select the global context or any specific contexts.
◦ Flexfield Attributes: Select specific flexfields.

---

## Job Offers
*Chunk ID: OHR-REC-0817 | Chapter: Job Offers*

◦ Configure if you want to make the field visible and required to be filled.
10. Click Done.
11. Click Save and Close.

---

## Configure Job Offer Assignment Flexfields
*Chunk ID: OHR-REC-0818 | Chapter: Job Offers*

Different types of flexfields are available within a job offer, and they're shown in different sections of the Offer page.
Assignment flexfields (PER_ASG_DF) are shown on the Offer page, in the Assignment Info section. The values become
available on each candidate's assignment if and when this offer assignment is accepted and processed and becomes
their real assignment.
Note: When a field is populated in the Assignment Info section, it updates the assignment as expected. When a field
is left blank, the value from the previous assignment is retained.
You can define the following flexfields, for both global segments and context-sensitive segments:
• 50 text flexfields
• 20 number flexfields
• 15 date flexfields
Here's what to do
1. Configure Job Offer Assignment Flexfields
2. Display Job Offer Assignment Flexfields

---

## Configure Job Offer Assignment Flexfields
*Chunk ID: OHR-REC-0819 | Chapter: Job Offers*

You first need to configure job offer assignment flexfields.
1. In the Setup and Maintenance work area, search for the task Manage Descriptive Flexfields.
2. On the Manage Descriptive Flexfields page, search for the flexfield code PER_ASG_DF. The flexfield
Assignment Attributes is displayed.
3. In the Actions menu, click Edit.
4. The Global Segments section shows flexfields available to all assignments and offer assignments regardless of
context. Each row might display a value set to control the available answer options, and a prompt to label them
on the page. Click the Create icon to add any new global flexfields that are needed.
5. The Context Segment section shows flexfields available to certain assignments and offer assignments after
the user selects their context. Each row might display a value set and a prompt. Click the Create icon to add
any context flexfields that are needed. Change the context by selecting another value so that additional sets of
flexfields will be shown and can be augmented as needed.
6. Click Save and Close.
7. When you're back on the Job Offer Descriptive Flexfields page, click Deploy Flexfield.

---

## Display Job Offer Assignment Flexfields
*Chunk ID: OHR-REC-0820 | Chapter: Job Offers*

You use Transaction Design Studio to create rules to display offer assignments flexfields using these offer actions:
• Recruiting - Create and Edit Job Offer displays offer flexfields while drafting job offers in the Hiring work area.

---

## Job Offers
*Chunk ID: OHR-REC-0821 | Chapter: Job Offers*

• Recruiting - View Job Offer in Job Application displays offer flexfields on the Offer tab of job applications in the
Hiring work area.
• Recruiting - View and Manage Job Offer displays offer flexfields on the offers in the Manage Job Offers quick
action.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select one of these action:

◦ Recruiting - Create and Edit Job Offer
◦ Recruiting - View Job Offer in Job Application
◦ Recruiting - View and Manage Job Offer
5.
6.
7.
8.
9.
10.

Click Add to create and configure a rule to display offer assignment flexfields.
In the Basic Details section, enter the name and description for the rule.
In the Show or Hide Regions section, make sure Assignment Info is set to Visible.
In the Page Attributes section, select Employment Details.
Set Assignment Attributes to Visible to display any selected assignment flexfields.
Click the Edit icon.

◦ Flexfield Content Code: Select the global context or any specific contexts.
◦ Flexfield Attributes: Select specific flexfields.
◦ Configure if you want to make the field visible and required to be filled.
11. Click Done.
12. Click Save and Close.

---

## Configure Job Offer Flexfields to Get Default Values
*Chunk ID: OHR-REC-0822 | Chapter: Job Offers*

You can configure any of the offer's flexfields to be created with default values pulled from existing information about
the candidate or about the requisition for which they're being recruited.
When you enable this feature, recruiters create job offers with initial flexfield values based on values from the
requisition or the candidate who's receiving the offer. This saves time and reduces errors made in manually entering the
information.
You need to configure which offer flexfields will get default values. Two parameters are available to create SQL queries
which affect these fields:
• SUBMISSION_ID, which refers to the job application and thus to the requisition
• PERSON_ID, which refers to the candidate who will be the offer recipient
To configure the defaulting behavior from the requisition or candidate into a newly-created offer, the offer's flexfields
must be defined as the same data type and value set as the fields from which their values will come. Then custom SQL
code can specify the initial default of any offer's flexfield based on the requisition field or person field.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience

---

## Job Offers
*Chunk ID: OHR-REC-0823 | Chapter: Job Offers*

◦ Functional Area: Job Offers
◦ Task: Job Offers Descriptive Flexfields
2. On the Job Offers Descriptive Flexfields page, select any existing flexfield and click the Edit icon.
3. In the Edit Segment page, in the Initial Default section, select the value SQL in the field Initial Default Type.
4. In the Default Value area, you need to configure the source of this flexfield's default value. These two
parameters are available to create an SQL query or Parameter query:

◦ SUBMISSION_ID, which refers to the job application and thus to the requisition
◦ PERSON_ID, which refers to the candidate who will be the offer recipient
5. Click Save and Close.
Here's an example of an SQL query which can be pasted into that Default Value area. The purpose of this example is to
identify the offer's related requisition, and then to pull the current value from its flexfield in Attribute Number 1 into the
current offer flexfield.
SELECT REQ.ATTRIBUTE_NUMBER1 FROM IRC_REQUISITIONS_B REQ, IRC_SUBMISSIONS SUB
WHERE REQ.REQUISITION_ID = SUB.REQUISITION_ID
AND SUB.SUBMISSION_ID = :{PARAMETER.SUBMISSION_ID}

---

## Make the Job Offer Letter Visible in Documents of
*Chunk ID: OHR-REC-0824 | Chapter: Job Offers*

Record
You can configure the job offer letter so that the HR specialist and the employee can view it in the Documents of Record
(DOR).
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Document Types.
4. Click the task name.
5. On the Document Types page, in the Category field, select Employment then click Search.
6. In the Search Results section, click Recruiting Job Offer Letters.
7. On the Edit Document Type: Recruiting Job Offer Letters page, in the Status field, select Active.
8. In the Document Record Preferences tab, make sure to set these options to No.
◦ Restrict Create

◦ Restrict Update
◦ Restrict Delete

9. Click Save and Close.

---

## Configure Job Offer Approval Rules
*Chunk ID: OHR-REC-0825 | Chapter: Job Offers*

You can configure approval rules for job offers in the same ways they're configured throughout the suite.

---

## For instance, one or two levels of approver might be appropriate depending on the business unit of the offer, based on
*Chunk ID: OHR-REC-0826 | Chapter: Job Offers*

the token Proposed Assignment Details.Business Unit.
The following subsections point out some specific offer fields that support particular rules that you might need.

---

## Configure Job Offer Approval Rules for Text in Offer Letters
*Chunk ID: OHR-REC-0827 | Chapter: Job Offers*

You can configure an approval cycle to be different for offers that have been drafted to diverge from the standard offer
letter templates, when the user has inserted additional text into a template or has adjusted or entirely replaced the
standard offer letter template.
• Configure rules for offers that include additional personalized text within the offer letter, using either or both
attributes Offer Details. Is OfferLetter Text1 Null and Offer Details.Is OfferLetter Text2 Null.
• Configure rules for offers whose offer letters were adjusted or replaced by the user who drafted it, when the
offer letter retains all its tokens (original method). These approval rules should use the token Offer Details.Is
Custom Offer Template, with the values of True and False.
• Configure rules for offers whose offer letters were adjusted or replaced by the user who drafted it, when the
offer letter's tokens were all resolved. These approval rules should use the token Offer Details.Is Custom
Resolved Template, with the values of "Y" or "N".

---

## Configure Job Offer Approval Rules Based on Flexfields
*Chunk ID: OHR-REC-0828 | Chapter: Job Offers*

You can configure the approval cycle for job offers based on flexfields defined as global segments on the offer and the
offer's assignment, and flexfields defined as both global and context-based segments on the requisition for which this
offer is hiring. You configure these approval rules within the Worklist, not using the Transaction Console.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.

On your Home page, click the Notifications icon.
On the Notifications page, click Show All.
Click Worklist.
In the menu next to your name, select Administration.
Click the Task Configuration tab.
Search for the task OfferApprovalHumanTask.
When the task is displayed, click the task name.
Click the Edit icon.
A message indicates that flexfields were changed. Click Start Synchronization.
When the synchronization is complete, click the OfferApprovalHumanTask task again.
Click the Assignees tab.
Click the blue dot in the Job Offer Approvers box to go to the rule.
When you click the SupervisoryRulesListSet, you can see the rule that you created.
In the IF section, go to Rule 1 and click the Search icon.
In the Condition Browser window, search for the flexfields. You can use:

◦ OfferDff
◦ RequisitionDff
◦ ProposedAssignmentDff
16. Create the condition.
17. Click Validate.

---

## Configure Job Offer Approval Rules Based on Job Requisition Information
*Chunk ID: OHR-REC-0829 | Chapter: Job Offers*

You can configure approval rules for job offers based on information about the job requisition for which the offer is
hiring. You configure these approval rules using the Transaction Console.
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

Go to the Tools work area.
Click Transaction Console.
Click the Approval Rules tab.
On the Transaction Manager: Rules page, select the Approve Job Offer process and click the Edit icon in the
Configure Rules column.
On the Approval Rules: Approve Job Offer page, click a rule then click the Edit icon in the toolbar.
Click the rule again and click the Edit Selection icon in the toolbar.
In the Approval Rules: Edit Condition Expression window, select the statement in the first menu.
In the second menu, select Requisition Details, and then choose any requisition-related fields from the related
menu.
In the third menu, select an operator. For example: > or < or == or contains or startsWith.
Select the rest of the expression for the approval rule.

---

## Configure Job Offer Approval Rules for Copied Job Offers
*Chunk ID: OHR-REC-0830 | Chapter: Job Offers*

If you have enabled users to create external job offers by copying all the values from an existing job offer in the same
requisition, you might want to define a shorter approval flow for these copied offers. Or you might choose to bypass
approval altogether for these copied offers if their original source offer was already approved. You can create these rules
in the Transaction Console as follows.
• You can configure an approval rule that only affects these copied job offers by specifying the string "Y" for yes
in the field Offer Details.Batch Creation Flag.
• You can configure a more specific approval rule that only affects offers that were copied from a source job offer
that was already approved. This type of rule must specify any of the acceptable states where the original offer
was, as of the moment when the copying was done. To create this rule, use the field Offer Details.Source State
Name and list all the state names or IDs where valid source offers might have been when they were copied:

Phase
Offer

State
• 1020 Draft
• 1021 Pending Approval
• 1028 Approval Rejected
• 1022 Approved
• 1023 Extended
• 1024 Accepted

HR

• 1033 Pending Automated Processing
• 1025 Pending Manual Processing
• 1034 Error During Processing
• 1026 Processing in Progress
• 1027 Processed

---

## Configure Representatives to Approve Job Offers
*Chunk ID: OHR-REC-0831 | Chapter: Job Offers*

You can add representatives as part of the list of approvers when configuring approval rules for job offers. The
candidate's proposed representative can be configured to provide approval for any candidates' offers, within the
Transaction Console.
1.
2.
3.
4.

Go to the Tools work area.
Click Transaction Console.
Click the Approval Rules tab.
On the Transaction Manager: Rules page, select the Approve Job Offer process and click the Edit icon in the
Configure Rules column.
5. Create a rule and set a Representative approver.
6. In the Representative section, set the fields as follows:
◦ Action Type: Approval required

◦ Representative Type: Recruiting
◦ Representative Of: Candidate's proposed representative

7. Click Submit.

---

## Use Case: Job Offer Completed But Still in Approval Pending
*Chunk ID: OHR-REC-0832 | Chapter: Job Offers*

Here's what you can do if a job offer is in Pending Approval state but the Transaction Console shows it's completed?
When a job offer is in Pending Approval state but the Transaction Console shows it's completed, you need to resubmit
the offer for approval.

---

## What Can I Do When a Job Offer is Approved but Shows
*Chunk ID: OHR-REC-0833 | Chapter: Job Offers*

as Pending Approval
A job offer has been approved but it shows as Pending Approval in Recruiting and as Completed in the Transaction
Console.
When a job offer is submitted for approval, a transaction gets created and a SOA instance is initiated. The SOA instance
takes some time (usually a few minutes) and during that time, the transaction remains in STUCK status. When the SOA
instance gets created, the transaction exits the STUCK state and enters the IN PROGRESS state. The job offer approval
process is then started. However, if a user terminates the transaction before the creation of the SOA instance, the job
offer remains in the Pending Approval state but in the Transaction Console the job offer shows as Completed.
Best Practices:
• It's recommended to wait at least 60 minutes before going ahead and terminating the transaction in STUCK
state.
To fix this situation, follow these steps.

---

## Job Offers
*Chunk ID: OHR-REC-0834 | Chapter: Job Offers*

1. Create the profile option HCM_TAC_RESUBMIT_ACTION so users have access to the Resubmit action in the
Transaction Console.
a. In the Setup and Maintenance work area, click Search.
b. Search for the task Manage Profile Options.
c. Click the task name.
d. On the Manage Profile Options page, click Create.
e. Complete the fields:
- Profile Option Code: HCM_TAC_RESUBMIT_ACTION
- Profile Display Name: HCM_TAC_RESUBMIT_ACTION
- Application: Global Human Resources
- Module: Global Human Resources
- Start Date: Pick a date in the past.
f. Click Save and Close.
g. On the Manage Profile Options page, select the Enabled and Updatable options for the Site level.
h. Click Save and Close.
2. Enable the profile option HCM_TAC_RESUBMIT_ACTION.
a. In the Setup and Maintenance work area, click Search.
b. Search for the task Manage Administrator Profile Values.
c. Click the task name.
d. On the Manage Administrator Profile Values page, search for the profile option code
HCM_TAC_RESUBMIT_ACTION.
e. In the Profile Values section, click the Add icon.
f. In the Profile Values section, select the Site profile level and enter TRUE in the Profile Value field.
g. Click Save and Close.
3. Resubmit the transaction in the Transaction Console:
a. In the Navigator menu, go to Tools, then Transaction Console.
b. In the Transaction Manager page, search for the transaction ID.
c. Select the transaction and click the Actions menu.
d. Select Resubmit to resubmit the transaction.
4. Once the transaction is resubmitted and the issue is resolved, disable the profile option
HCM_TAC_RESUBMIT_ACTION.
a. In the Setup and Maintenance work area, click Search.
b. Search for the task Manage Administrator Profile Values.
c. Click the task name.
d. On the Manage Administrator Profile Values page, search for the profile option code
HCM_TAC_RESUBMIT_ACTION.
e. In the Profile Values section, select the Site profile level and enter FALSE in the Profile Value field.
f. Click Save and Close.
Results:
To validate that the solution will resolve this situation, run the below query and verify the results include the impacted
record.
SELECT
h.transaction_id,
h.object_id ,
d.state ,
d.status ,

---

## Job Offers
*Chunk ID: OHR-REC-0835 | Chapter: Job Offers*

o.submission_id ,
RS.SUB_PROCESS_ID
FROM irc_submissions s ,
irc_offers o ,
HRC_TXN_CONSOLE_ENTRY c,
hrc_txn_header h ,
hrc_txn_data d ,
(
SELECT transaction_id,
object_id
FROM
(
SELECT last_h.transaction_id,
last_h.object_id ,
last_h.creation_date ,
RANK() OVER(PARTITION BY last_h.object_id ORDER BY last_h.creation_date DESC
) rnk
FROM fusion.hrc_txn_header last_h
WHERE last_h.object = 'IRC_OFFERS'
)
WHERE rnk = 1
)
last_trx ,
irc_processes_b p,
irc_routing_steps_b rs
WHERE h.TRANSACTION_ID = c.TRANSACTION_ID
AND h.transaction_id = d.transaction_id
AND h.transaction_id = last_trx.transaction_id
AND s.submission_id = o.submission_id
AND o.offer_id = h.object_id
AND h.object = 'IRC_OFFERS'
AND s.current_state_id = 1021
AND s.process_id = p.process_id
AND rs.process_id = p.process_id
AND rs.phase_id = 14
AND rs.step_status = 'ACTIVE'
AND c.status_category = 'COMPLETED'

---

## Configure the Management Hierarchy for Job Offer
*Chunk ID: OHR-REC-0836 | Chapter: Job Offers*

Approvals
In HCM, each employee can have multiple assignments, and each assignment has its own management chain. All the
assignments for the employee appear in the Directory work area (Me > Directory).
Every assignment can have its own management hierarchy used for approval instead of always relying on primary
assignment as before. As an administrator, you can decide to use the primary assignment or other assignments for the
offer approval process. Also, you can select the recruiter in the approval chain for offer approvals.
1. Go to the Tools work area.
2. Click Transaction Console.
3. Click the Approval Rules tab.
4. Select the Approve Job Offer process and click the Edit icon.
5. Click the Management Hierarchy box.
6. Go to the Management Hierarchy section at the bottom of the page.
7. In the Approval Chain Of field, select one of these options:

---

## Job Offers
*Chunk ID: OHR-REC-0837 | Chapter: Job Offers*

◦ Hiring Manager
◦ Requester
◦ Recruiter
◦ User
8. If you select Hiring Manager or Recruiter, you can select an assignment type:
◦ Use primary assignment hierarchy (default value)

◦ Use current assignment hierarchy

---

## Configure Notifications for Job Offer Approvers
*Chunk ID: OHR-REC-0838 | Chapter: Job Offers*

Approvers receive email notifications seeking their decision about job offers drafted for candidates. These notifications
are generated for each approver by BI Publisher, just like all other approvals.
The standard notification for offer approval includes all the pertinent information about the job offer, including the
proposed assignment details, salary, other compensation, and the requisition for which the candidate applied.
From a security standpoint, approvers need to have these duty roles and aggregate privileges to view respective
sections in the notification:
• View Job Offer (ORA_IRC_VIEW_JOB_OFFER)
• View Job Offer Salary (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• View Job Offer Other Compensation (ORA_IRC_VIEW_JOB_OFFER_OTHER_COMPENSATION)
• View Job Requisition (ORA_IRC_VIEW_JOB_REQUISITION)
Approvers don't need to be included in the offer team to see the details of the approval request. As long as the
candidate is within the user's data role's person security profile, the candidate's offer values will be visible to the user.
The standard notification also contains a link enabling approvers to view the offer letter which will be extended to the
candidate. The specific tokens are:
• P_OFFERLETTERTEMPLATENAME: This token shows the name of the selected offer letter from the list, or if the
candidate's offer was adjusted by a recruiter then it will show the custom-uploaded offer letter file name.
• P_OFFERLETTERDEEPLINK: This token contains the URL for the deep link to the offer letter. It can be displayed
as a URL to approvers, or it can be constructed in the notification as the link destination when the approver
clicks the name of the letter.

---

## Configure Collaborator Types Defaulted in Job Offers
*Chunk ID: OHR-REC-0839 | Chapter: Job Offers*

You can configure which collaborator types must be defaulted into the offer team for job offers in addition to the hiring
manager and recruiter.
When users create a job offer and the Offer team is defaulted from the job requisition:
• The hiring manager and recruiter are defaulted from the requisition. This is the current behavior.

---

## Job Offers
*Chunk ID: OHR-REC-0840 | Chapter: Job Offers*

• Users who are part of one of the selected collaborator types of the requisition are defaulted into the job offer’s
offer team, into the same collaborator type.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. On the Enterprise Recruiting and Candidate Experience Information page, expand the Offer section and click Edit.
3. Configure the Requisition Collaborators Added to Offers setting. You can select:
◦ All collaborator types. This is the default value to preserve the current behavior for existing customers.

◦ Specific collaborator types.
◦ None of the collaborator types. No collaborator will be defaulted on the job offer's offer team.
4. Click Save.

---

## Automatically Extend Job Offers to Candidates
*Chunk ID: OHR-REC-0841 | Chapter: Job Offers*

You can use the Extend Offer action in a candidate selection process to automatically extend job offers to candidates
once the offers have been approved. Offers are extended automatically to candidates when their job applications reach
the Offer - Approved status. You can add multiple Extend Offer actions to a candidate selection process so that you can
extend offers using different conditions and configurations.
Note: If you enable the Bypass Extending Offer option, the Extend Offer action isn't available.

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2.
3.
4.
5.
6.

7.
8.
9.
10.

On the Candidate Selection Process Configuration page, click a process.
On the process page, click the Offer phase.
In the States for Phase section, select the Approved state.
Select the Extend Offer action in the Actions menu, and select Add.
Define the delay in number of hours before extending the offer automatically. If you enter 0, the action is
performed immediately when each candidate reaches the status Offer - Approved. When an offer is set to be
extended with a delay, a banner message is displayed to users on the offer, showing the date and time when
the offer will be automatically extended. When that time arrives, the offer gets extended unless a user changed
it. For example, if the recruiter rejects the candidate or redrafts the offer in the meantime, the offer won't be
extended automatically and the banner will no longer be shown. If the redrafted offer is approved again, a new
automatic extend will be scheduled.
Click Continue.
As for other actions, you can define conditions that must be met for the Extend Offer action to be performed.
Enter a unique name for the action.
Click Save and Close.

---

## Limit the Automatic Extend of Offers
*Chunk ID: OHR-REC-0842 | Chapter: Job Offers*

Offers are extended automatically even when enough hires have been made on the requisition to match the number of
openings. If you want to prevent automatically extending an offer based on the number of hires on the requisition, you
could use a fast formula with a condition. By default, the automated progression to extend job offers will not check how
many candidates have been hired for the requisition. However, the requisition's count will be checked when these offers
are initially submitted for approval, which greatly reduces the likelihood of extending offers to too many candidates. To
configure a fast formula to limit the automatic extend of offers, consider these available methods:
• Define a condition using database items (DBI): If the requisition's number of
openings (IRC_CSP_REQ_NUMBER_TO_HIRE) is more than its current hires
(IRC_CSP_REQUISITION_NUMBER_OF_HIRES).
• Define a condition using a function: If the number of job applications that went through the state Accepted is
less than the requisition's number of openings.

---

## Automatically Extend Copied Job Offers to Candidates
*Chunk ID: OHR-REC-0843 | Chapter: Job Offers*

You can configure the candidate selection process to automatically extend all newly-copied offers to candidates once
the offers have been approved. You need to create a fast formula of the Recruiting Candidate Selection Process formula
type and use the database item IRC_CSP_JOBOFFER_BATCH_COPIED_FLAG which is used to indicate if the job offer
was created using a batch process. When you configure the candidate selection process, you select that fast formula
while defining conditions for the process.

---

## Bypass Extending Offers to Candidates
*Chunk ID: OHR-REC-0844 | Chapter: Job Offers*

You can configure a candidate selection process to bypass extending offers to candidates. When this candidate
selection process is used in a job requisition, the Offer Team will indicate if the offer is accepted or declined without the
need for any online communication to or from the candidate.
There are different reasons why your organization might decide to enable this feature. One could be that there are many
different languages used by candidates and they prefer to communicate directly with candidates instead of having to
translate all the notifications used in the regular offer process. Or your organization wants to avoid having back and
forth written communications with candidates during the offer process.
As soon as an offer reaches the Approved state, the Offer Team can tell the candidate about the offer. If the candidate
tells the Offer Team that they accept the offer, the Offer Team will use the Accept Offer action as long as there are still
available openings on the job requisition and if any related position has sufficient open headcount. The offer goes from
Offer - Approved directly to Offer - Accepted.. If the candidate tells the Offer Team that they decline the offer, the Offer
Team will use the Move action to change the status to Offer - Withdrawn by Candidate.
Because the offer is never extended to the candidate, no automated notification is sent to the candidate, inviting
them to view and accept their offer. And no offer letter is displayed to the candidate. It’s the responsibility of the hiring
manager, recruiter, or anyone in the Offer Team to discuss the details directly with the candidate and to record whether
or not they accept the offer.
When this feature is enabled, here's what it means for candidates:
• The candidates don't receive any automated notification informing them that an offer was extended.

---

## Job Offers
*Chunk ID: OHR-REC-0845 | Chapter: Job Offers*

• The candidates can't see their offer before responding to it.
• The candidates tell someone on the Offer Team whether they accept or decline the offer.
• The candidates don't receive a notification confirming that their response was received, unless this is
configured.
When the offer is accepted, no automated notification is sent to the candidate. But if you want, you can configure
notifications to inform others.
Also, recruiting users don’t need to select an offer letter template while drafting the offer. If recruiting users do select
an offer letter template, they can preview the candidate's offer letter, and it will get stored in the worker's Document
Records when the candidate accepts the offer. If the selected offer letter is configured to track e-signature, it will not
show that the candidate e-signed it; but it can show the name of the user who accepted the offer on behalf of the
candidate, the date, and time.

---

## Configure the Candidate Selection Process to Bypass
*Chunk ID: OHR-REC-0846 | Chapter: Job Offers*

Extending Offers
You can configure a candidate selection process to bypass extending offers to candidates. When this candidate
selection process is used in a job requisition, the Offer Team will indicate if the offer is accepted or declined without the
need for any online communication to or from the candidate.
Here's what to do
1.
2.
3.
4.

---

## Configure the Candidate Selection Process to Bypass Extending Offers
*Chunk ID: OHR-REC-0847 | Chapter: Job Offers*

Associate the Candidate Selection Process to Requisitions
Configure a Notification for Offer Acceptance
Provide an Accepted Offer Letter to the Candidate

---

## Configure the Candidate Selection Process to Bypass Extending Offers
*Chunk ID: OHR-REC-0848 | Chapter: Job Offers*

You need to configure the candidate selection process to skip the standard offer extended capabilities.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2.
3.
4.
5.
6.

On the Candidate Selection Process Configuration page, create a process or open an existing one.
Click the Offer phase.
Click Edit next to Phase Details: Offer.
Select Yes for the option Bypass Extending Offer.
Click Save.

---

## Associate the Candidate Selection Process to Requisitions
*Chunk ID: OHR-REC-0849 | Chapter: Job Offers*

To enable a given job requisition to not send any communication to candidates, recruiting users need to select a
candidate selection process which is set to bypass extending offers. This is done in the Configuration section of a job
requisition. When this candidate selection process is used in a requisition, every candidate on that requisition will move

---

## Job Offers
*Chunk ID: OHR-REC-0850 | Chapter: Job Offers*

from Offer - Approved directly to Offer - Accepted. The Offer Team will indicate whether the offer is accepted or not
without the need for any online communication to or from the candidate.

---

## Configure a Notification for Offer Acceptance
*Chunk ID: OHR-REC-0851 | Chapter: Job Offers*

When a job application's lifecycle is configured to bypass extending offers and to allow the Offer Team to control all
offer-related communications directly with candidates, no standard notifications are sent when extending nor accepting
the job offer. But recruiting users might want to inform other users when each acceptance is recorded, or might even
want to thank the candidate directly. Both of these notifications can be configured as follows.
Notify the recruiter or hiring manager: In the candidate selection process, you can configure an alert to be sent to the
recruiter or hiring manager, or both. The standard job application review message from the Alerts Composer tool is sent
once a day informing these recipients that there are new job applications to review that have reached the status Offer Accepted, and including a hyperlink to reach the list of them.
Note: This alert can be triggered to review other job applications reaching other phases and states too. So it might
not be desirable to configure the content of this message to mention offers specifically.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration

2.
3.
4.
5.

On the Candidate Selection Process Configuration page, click a process.
Click the Offer phase.
In the States for Phase: Offer section, add the Send Notification action to the Accepted state.
On the Action: Send Notification page, select the members of the Hiring Team who will receive the notification:
Recruiter, Hiring Manager, or both. They will receive the standard review notification as configured in Alerts
Composer.
6. Click Continue.
7. Add any conditions.
8. Click Save and Close.

---

## Notify the candidate: In the candidate selection process, you can configure an offer-related notification to be sent to
*Chunk ID: OHR-REC-0852 | Chapter: Job Offers*

the candidate after the offer is accepted. Reaching the desired phase and state triggers sending a specific message that
you configure in the Recruiting Content Library. You first create a notification, then define when each candidate will
receive that alert within the candidate selection process.
To create the notification:
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Content Library

2. On the Recruiting Content Library page, click Create.
3. On the Create Content Item page, enter a name and a code, select the category Automated Job Application
Notification, and indicate if the notification is for internal candidates, external candidates, or both.
4. Enter the subject and text for the message. Rich text features are available to format the text. You can insert
tokens such as the name of the requisition (which is preferable to the name of the offer), the work location, the
proposed start date if you want.

---

## You can use the token JobOfferDetailsCandidateDeepLinkURL to view the offer letter online. You insert this
*Chunk ID: OHR-REC-0853 | Chapter: Job Offers*

token only if the recruiting users will be configuring an offer letter in each offer for each candidate, otherwise
the candidate will have a broken link when they receive this message.
5. Click Save and Activate.
To define who will receive the notification:
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2.
3.
4.
5.
6.
7.
8.

On the Candidate Selection Process Configuration page, click a process.
Click the Offer phase.
In the States for Phase: Offer section, add the Send Notification action to the Accepted state.
Select the notification you created for the internal candidates and external candidates.
Click Continue.
Add any conditions.
Click Save and Close.

---

## Provide an Accepted Offer Letter to the Candidate
*Chunk ID: OHR-REC-0854 | Chapter: Job Offers*

When a job application's lifecycle is configured to bypass extending offers, the offer is never extend to the candidate.
The candidate doesn't have online access to any information about their job offer, and must rely on the recruiter or
Offer Team to learn the details of their offer and to provide their response. However, you can provide an offer letter to
the candidate for reference after they have accepted the offer.
If an offer letter was configured when the offer was drafted, you can still provide access for candidates to that letter
from a hyperlink in a notification. If that offer letter was configured to include a light e-signature section, the candidate
will see that it was accepted on their behalf by the user who moved their job application from the state of Approved to
Accepted. Internal candidates after they accept an offer can see any associated offer letter in the Me > Current Jobs >
Job Offers work area or by clicking the link in the notification they received. External candidates can only access their
offer using the link in the notification.

---

## Keep Active Job Applications Upon Move to HR
*Chunk ID: OHR-REC-0855 | Chapter: Job Offers*

You can keep active job applications of a candidate after the candidate is moved to the HR phase. This is useful to
prevent other job applications to be automatically withdrawn.
By default, job applications are automatically withdrawn.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. On the Enterprise Recruiting and Candidate Experience Information page, expand the Offer section and click Edit.
3. Clear the option Withdraw candidates from all other active job applications when they move to the HR phase.

---

## Define Reasons to Decline Job Offers
*Chunk ID: OHR-REC-0856 | Chapter: Job Offers*

You can gather feedback when candidates decline job offers. Candidates can select a reason from a list of reasons, if this
is configured, and enter any comments they want to provide.
With that information, your organization can gather valuable data for the recruiting teams, both immediate and
long-term. Recruiters can get notified right away when a candidate declines their job offer, which withdraws their job
application. The notification can contain enough information for the recruiter to take immediate action for the candidate
if desired. Longer term, these responses build up a picture of the decisions and concerns of your organization's selected
candidates. Why didn't your top candidates accept your job offers? Capturing this information and analyzing it to
understand trends can greatly improve your organization's future offers and future hiring strategies.
Here's what to do
• Define Reasons
• Configure the Candidate Selection Process
• Add the Candidate Selection Process to Job Requisitions
• Configure Notifications

---

## Define Reasons
*Chunk ID: OHR-REC-0857 | Chapter: Job Offers*

You first need to define reasons for declining job offers. You can use the reasons that already exist and which are used
at various points in the candidate lifecycle. You can also create new reasons, then place these reasons into a Reason
Group.
For details, see Define Reasons to Reject and Withdraw Job Applications.

---

## Configure the Candidate Selection Process
*Chunk ID: OHR-REC-0858 | Chapter: Job Offers*

You need to enable the Allow Candidate Reason and Comment on Withdraw option in the candidate selection process.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2.
3.
4.
5.

Open an existing process.
Click the Offer phase.
Go to the Phase Details: Offer section and click the Edit icon.
Set the option Allow Candidate Reason and Comment on Withdraw to Yes so that candidates can provide a
free-text comment as they decline their job offer. Candidates are declining to be considered any further for this
job and thereby moving themselves to the state Withdrawn by Candidate.
6. Click Save.
7. Go to the States for Phase: Offer section.
8. (Optional) Click the Reason Group menu for the Withdrawn by Candidate state and select the group that
contains the reasons to decline the offer. If you don't associate any reason group with the Withdrawn by

---

## Job Offers
*Chunk ID: OHR-REC-0859 | Chapter: Job Offers*

Candidate state, no list of reasons will be shown but the candidate will still have the opportunity to enter freetext comments as they decline the offer.

---

## Add the Candidate Selection Process to Job Requisitions
*Chunk ID: OHR-REC-0860 | Chapter: Job Offers*

For job offers to gather the reasons why candidates declined the offers, offers need to be associated with requisitions
whose candidate selection process is configured to accept this feedback.

---

## Configure Notifications
*Chunk ID: OHR-REC-0861 | Chapter: Job Offers*

Standard notifications can be sent to the offer team when a candidate declines their job offer:
• IRC_JobOffer_Declined_Internal
• IRC_JobOffer_Declined_External
You may want to configure this notification to include the feedback provided by the candidate. If so, add the following
tokens:
• JobOfferCandidateDeclineReason
• JobOfferCandidateDeclineComment

---

## Cancel and Redraft Job Offers Using a One-Step Process
*Chunk ID: OHR-REC-0862 | Chapter: Job Offers*

You can enable a profile option to let recruiting users cancel and redraft job offers using a simple one-step process.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_OFFER_CANCEL_REDRAFT_ENABLED.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.
What to do next
You need to grant users the following privileges so they can view the Cancel Offer action and Redraft Offer action after a
job application has reached the HR phase.
• Cancel Job Offer (IRC_CANCEL_JOB_OFFER_PRIV), using the delivered or custom duty role.
• Redraft Job Offer After HR Phase (IRC_REDRAFT_JOB_OFFER_AFTER_HR_PHASE_PRIV), using the delivered or
custom duty role.
These two privileges are granted by default to the Human Resource Specialist role through the Address Job Offer duty
role, and to the Recruiting Manager role through the Manage Job Offer by Recruiting Manager duty role. You should
grant those duty roles, or create a reduced custom version to fit your needs. For example, if you want to allow users to
redraft job offers but not cancel them, you need to copy the appropriate duty role and remove the elements you don't
want to include. You then need to resubmit your data role after including the appropriate duty role in your hierarchy, and

---

## Job Offers
*Chunk ID: OHR-REC-0863 | Chapter: Job Offers*

the appropriate data security policies will be generated. Remember that the Recruiting Manager role has a data security
policy based on the person security profile in addition to the policies for the Recruiter, based only on ownership and
subordinate hierarchy.

---

## End Dating Offer Assignments
*Chunk ID: OHR-REC-0864 | Chapter: Job Offers*

You can prevent old completed and terminated job offers from being redrafted or canceled by configuring settings.
Before you start
You first need to set the profile option ORA_IRC_OFFERS_TERMINATE_ASG_ENABLED to Y using the Manage
Administrator Profile Values task in the Setup and Maintenance work area.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Offer section and click Edit.
3. In the End Dating Offer Assignments section, configure the settings by indicating the number of days in the field.
Don’t leave the field blank as this would mean that there's no end date for offer assignments.
◦ After Reaching the Final Successful State (HR – Processed): Use this setting to indicate how many days is
appropriate to allow recruiting users to redraft or cancel job offers that have reached the final status HR –
Processed. Default value is 30 days.
◦ After Reaching Any Final Unsuccessful State (Rejected by Employer or Withdrawn by Candidate) in
the Offer Phase or Any Later Phase: Use this setting to indicate how many days is appropriate to allow
recruiting users to redraft job offers that have reached the inactive states Rejected by Employer or
Withdrawn by Candidate. Default value is 30 days.
4. Click Save.
Results:
Once the pending worker is converted into an employee or contingent worker, you can't cancel nor redraft the offer,
regardless of the value you entered in the above setting.
Note: If you want to end date an offer assignment for a specific requisition or candidate, don't add any parameters
while running the Perform Recruiting Candidate Selection Process Offer Actions scheduled process. This scheduled
process is responsible for several different Move to HR related functionalities (including assignment end-dating) and
the input parameters are applicable for other functionalities and not end-dating offer assignments. Offer assignments
end dating is applied to all eligible offers as per configuration.

Related Topics
• Create and Edit Profile Options

---

## Restrict Candidates to Respond to Job Offers After the
*Chunk ID: OHR-REC-0865 | Chapter: Job Offers*

Expiration Date
You can restrict candidates to accept or decline their job offers after the offer’s expiration date.
This is done by disabling the option called Allow candidates to accept or decline job offers after the offer’s expiration
date. This setting is enabled by default so that you can experience the current behavior.
When you disable the setting:
• Candidates can’t respond to the job offer when the expiration date has passed.
• Candidates get a message when they click the job offer link embedded in the Extend Job Offer notification.
• The Accept and Decline buttons are disabled.
• Candidates need to contact the Recruiting team for the job offer to be re-extended.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience
2. Expand the Offer section and click Edit.
3. Clear the option Allow candidates to accept or decline job offers after the offer’s expiration date.
4. Click Save.

---

## Enable Copy Job Offers
*Chunk ID: OHR-REC-0866 | Chapter: Job Offers*

You can allow recruiters to quickly create one or more job offers for external candidates on a requisition by copying an
offer that’s already been created for another external candidate.
This help recruiters to save time by quickly creating consistent offers for new hires and rehires, without the possibility of
any manual error by typing in each field value.
When you enable the feature, only users with the privilege Copy Job Offer (IRC_COPY_JOB_OFFER) can see the Copy
Offer action on the list of job applications for a given requisition.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_ALLOW_COPY_JOB_OFFER.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.

---

## Job Offers
*Chunk ID: OHR-REC-0867 | Chapter: Job Offers*

What to do next
You can configure approval rules for these copied offers, if your organization thinks for instance that the new offers
copied from existing offers might need less-thorough approval.
You can also configure these copied offers to be moved quickly forward through the recruiting lifecycle. A candidate
selection process can rely on fast formulas to automatically progress these job applications forward into any status,
such as from Offer - Approved to Offer - Extended, or from Offer - Accepted into the HR phase. Each job application
with an offer has a database item (DBI) to indicate whether or not its offer was created by the batch offer copy process.
The indicator IRC_CSP_JOBOFFER_BATCH_COPIED_FLAG indicates a copied offer if its value is Yes. You can configure
this DBI into a fast formula which can then be used in an auto-progression rule within any two states in the candidate
selection process.
Related Topics
• Configure Job Offer Approval Rules
• Fast Formulas for Candidate Selection Processes
• Create and Edit Profile Options

---

## Streamlined Internal Candidate Processing for HR
*Chunk ID: OHR-REC-0868 | Chapter: Job Offers*

Specialists
You can enable a set of features which give HR specialists a few ways to streamline the processing of most internal
candidates, allowing them to move quickly, efficiently, and flexibly into their new assignments in the HR system.

---

## Automatically Process Internal Candidates in the HR Phase
*Chunk ID: OHR-REC-0869 | Chapter: Job Offers*

Internal candidates who accepted their job offer and were moved to the HR phase can be automatically processed into
their new roles in the HR system as their proposed start date approaches.
When the automated processing capabilities are enabled, most internal candidates reach the HR phase in the state
Pending Automated Processing. When their proposed start date approaches, the new assignment is automatically
created from their offer. Each candidate’s state becomes Processing in Progress when the assignment is successfully
created, and becomes Processed when the assignment is approved and committed as the candidate’s new job.
Every internal candidate will be automatically processed when their assignment’s proposed start date is 7 days or fewer
from today, by default. You can configure the desired number of days in advance of the start date.
If some problem arises while automatically processing the offer into the new assignment, the candidate’s job application
will automatically move from the state Pending Automated Processing into the state Error During Processing. These
errors can occur for the usual reasons, such as the offer’s intended position suddenly has a hiring status of Frozen, or
the offer’s promised location has been inactivated. If the situation causing the error can be resolved, the recruiting user
can try processing the candidate again, using either the manual process or the Quick Process Offer action. However this
offer will not get automatically processed again, regardless of its approaching start date.
For internal candidates in a complex hiring situation, they still go into the state Pending Manual Processing and the
recruiting user will still need to manually process them. Any candidates in complex hiring situations usually arrive in the
HR phase in the state Pending Manual Processing, even if the automated processing feature is enabled. These offers will
not be automatically processed; they need to be manually processed as usual.

---

## Quickly Process Internal Candidates in the HR Phase
*Chunk ID: OHR-REC-0870 | Chapter: Job Offers*

The HR specialists can use the Quick Process Offer action in the Manager Job Offers page to process most internal
candidates into their new assignment with a single click after they were moved to the final HR phase of the recruiting
life cycle. The HR specialists can process candidates as early as they want, as they don’t have to wait for the automatic
processing date to arrive for each candidate. This process ensures consistent values from each offer into each new
assignment and salary.
When the HR specialists use the Quick Process Offer action, they don't review all the offer information while creating
the new assignment and they can’t change any values. This ensures consistent information from each accepted offer is
copied identically into each new assignment and salary.
The HR specialists can use the Quick Process Offer action for most internal candidates in the following states of the HR
phase:
• HR - Pending Automated Processing
• HR - Pending Manual Processing
• HR - Error During Processing
The Quick Process Offer action isn’t available for candidates in complex hiring situations, even if this feature is enabled.
These offers need to be manually processed as usual.

---

## Change the Proposed Start Date
*Chunk ID: OHR-REC-0871 | Chapter: Job Offers*

HR specialists can change the proposed start date for internal candidates after they’ve accepted their job offer, in case
the intended date in their offer now needs to be adjusted before their new assignment is processed.
HR specialists can use the Change Start Date action to fix the agreed-upon start date that was in the job offer. This new
date will be used when transforming the offer into the new assignment either by using the automatic processing option,
or the Quick Process Offer action, or by using the method where an HR specialist clicks through the guided process to
review all the values from the offer. This changed date won't affect the candidate's job offer letter which was already
accepted.

---

## Actions and HR States
*Chunk ID: OHR-REC-0872 | Chapter: Job Offers*

When the automated processing capabilities are enabled, the HR specialist can use the Redraft Offer, Rejected by
Employer, and Withdrawn by Candidate actions from the Manage Job offers page.
Redraft Offer, Reject Candidate, and Withdraw Candidate actions are available in the below HR states:
1. Pending Automated Processing
2. Error During Processing
3. Pending Manual Processing
The Redraft Offer action is also available in these 2 states:
• Rejected by Employer
• Withdrawn by Candidate

---

## Configure Streamlined Processing of Internal Candidates
*Chunk ID: OHR-REC-0873 | Chapter: Job Offers*

by HR Specialists
You can configure a profile option which will enable a set of features for HR specialists to streamline the processing of
most internal candidates, allowing them to move quickly, efficiently, and flexibly into their new assignments in the HR
system.
These capabilities affect all internal candidates that arrive in the HR phase of the lifecycle, except those who are in
complex hiring situations. A complex situation includes an internal candidate who already has two or more assignments
before this job offer, or who will already be terminated before their new job offer starts, or whose situation changes
while their offer is underway.
To enable streamlined processes so that the Quick Process Offer action and the Change Start Date action are available
to HR specialists, you need to enable the profile option ORA_IRC_AUTO_PROCESS_INTERNAL_OFFERS at the Site level
and configure the option Automatically Process Internal Offers to Assignments.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_AUTO_PROCESS_INTERNAL_OFFERS.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.
This profile option displays the Automatically Process Internal Offers to Assignments functionality in the Setup and
Maintenance work area.
8. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
9. Expand the Offer section and click Edit.
10. In the Automatically Process Internal Offers to Assignments section, configure the timing of when the automatic
processing of internal job offers will occur. By default, the value of the Days Before Proposed Start Date field is set
to 7 days. This means that the assignment will be created 7 days before the proposed start date on the offer. If you
set the value to 0, the assignment will processed on the same day as the proposed start date.
11. Click Save.
Related Topics
• Create and Edit Profile Options

---

## Candidate Duplicate Check and Merge After Job Offers
*Chunk ID: OHR-REC-0874 | Chapter: Job Offers*

After a candidate accepts a job offer and is moved to the HR phase, a check can be automatically done to verify if the
candidate is a duplicate of any person in the database.
When moving into the HR phase, each external candidate can be checked against all workers, ex-workers, contingent
workers, ex-contingent workers, and even against contacts and beneficiaries who have information in the database.
This duplicate check complements another duplicate check that is done earlier in the recruiting lifecycle. This earlier
check searches for potential duplicates by comparing a candidate against all other candidates and ex-workers, but not
against any current workers. This earlier check can be initiated by users or can be configured to happen automatically in
the candidate selection workflow.
Before creating a job offer for an external candidate, the recruiting user can merge the candidate's record and job
applications with any ex-worker or candidate. This is important if the user determines that the candidate already has
an additional separate record in the database. After a job offer has been created, however, the duplicate check and
merging capability is automated. The check is performed against workers and ex-workers, and the criteria used are
slightly different.

---

## Candidates and National Identifier Uniqueness
*Chunk ID: OHR-REC-0875 | Chapter: Job Offers*

The enterprise profile option National Identifier Uniqueness Validation Mode is available to check the uniqueness of
national ID numbers for all workers and people throughout your company. Checking this value prevents mistakenly
tracking the same person twice using the same national identifier. When creating or updating pending workers and
workers the national identifiers must be unique when this option is configured, but candidates aren't affected.
In Recruiting, candidates can provide their national identifier, if this is part of their job application process, or a Hiring
Team member with the necessary privilege can provide it for them. Any national ID number can be entered, even if
it isn't unique. A non unique national identifier likely means that this candidate already has a record in the database,
either as an ex-worker or even as a current worker. The flow of the job application won't be interrupted and there is no
request to correct the number entered, even if it's configured as a required field.
However, if the profile option National Identifier Uniqueness Validation Mode is enabled, then candidates who are
selected to be hired can't get transformed into pending workers using a non unique ID number. A candidate can
become a pending worker without providing a national ID number. But this number is likely configured to be required to
complete the pending worker record and convert them into a worker. If the new pending worker's ID number is entered
as a duplicate of an existing person, this value can't be saved in their pending worker record. The HR specialists will
need to handle the situation manually.

---

## Duplicate Checking and Person Creation
*Chunk ID: OHR-REC-0876 | Chapter: Job Offers*

If an external candidate is discovered to be a duplicate of an ex-worker or candidate before any job offer has been
created, the user can decide to merge the candidate's record and job applications with that person. This is important if
the user determines that the candidate already has an additional separate record in the database. But after a job offer
has been created, the duplicate checking and merging capability is slightly different to preserve the details of the job
offer.
If you decide to use this automated feature to check for duplicates after the job offer, consider requiring external
candidates to provide date of birth or national identifier during their job application process. These values will allow the
duplicate check, if configured, to find better matches with any existing people in the database before creating a pending
worker.

---

## Job Offers
*Chunk ID: OHR-REC-0877 | Chapter: Job Offers*

National identifier and date of birth are sensitive fields, so you might want to configure the application process to gather
these fields in a custom phase after the candidate has accepted their offer. But after the job offer, the only opportunity
to merge this candidate with a duplicate record is during the Move to HR.
At the moment of moving into the HR phase, this feature can check whether the candidate is a potential duplicate
of any existing person in the database, relying upon the configured definition of a duplicate record. If one or more
possible matches are identified, the candidate's job application will not move smoothly into the status HR - Processing
In Progress. Rather users will be notified that it has moved into the status HR - Error During Processing. A user must
decide whether or not to act upon the information by:
• Merging the candidate record with a newly discovered duplicate person record and recreating the candidate's
offer on the pre-existing worker. Or,
• Proceeding with the original candidate by creating a pending worker.
If this check doesn't identify any possible matches, then the external candidate will be transformed into a pending
worker upon their move to HR, on their way to becoming a new worker.
In case a duplicate exists but isn't found at this moment, perhaps due to incomplete or incorrect candidate information,
then an HR specialist will need to handle the situation manually. This might include creating a new assignment
directly on the existing person's record that resembles the candidate's offer, withdrawing this unneeded candidate job
application from consideration, perhaps deleting the candidate record, and possibly closing the requisition manually as
well.

---

## HR Specialist VS Recruiter Privileges
*Chunk ID: OHR-REC-0878 | Chapter: Job Offers*

Users who have the equivalent of the seeded HR Specialist role can see candidate job applications in the status HR
- Error During Processing, can read the banner explaining that they might be a duplicate, and can reach the list of
possible duplicates. To perform the merge with a selected existing person record, these users need to be granted the
following:
• Functional privilege Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE_PRIV )
• Role for tracking purposes Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE_PRIV_OBI)
After performing a merge, these HR specialists will rely on Recruiting users to recreate the job offer for the merged
person, because by default HR specialists don't have the necessary additional privileges or duty roles such as Update
Job Offer (ORA_IRC_UPDATE_JOB_OFFER). HR users will return to the main list of job offers in the Manage Job Offers
work area after they perform a candidate merge, and an alert can be sent automatically to inform the recruiter that a
draft offer is waiting to be reviewed.
Related Topics
• How National Identifiers are Validated
• How Person Records Are Matched

---

## Configure the Candidate Duplicate Check for Candidates
*Chunk ID: OHR-REC-0879 | Chapter: Job Offers*

Moving to the HR Phase
To check for duplicates in Recruiting when moving an external candidate into the HR phase, you need to configure two
settings:
• The enterprise profile option Person Creation Duplicate Check, which checks when people are created outside
of recruiting processes.
• The recruiting setting Duplicate Check in Move to HR, which applies this check to the end of the recruiting
lifecycle.

---

## Configure the Person Creation Duplicate Check Setting
*Chunk ID: OHR-REC-0880 | Chapter: Job Offers*

First you must define what kind of overlapping information about existing person records will be considered as a
possible duplicate when comparing it to a candidate record. Do this by ensuring that the enterprise profile option Person
Creation Duplicate Check is configured. This option is already used to find duplicates when managers, HR specialists,
or other users are directly hiring or updating employees, entering or updating contingent workers, or using HCM
Data Loader. Now it governs checking duplicates of Recruiting candidates in the action Move to HR as well, if this is
configured.
1. On your Home page, go to My Client Groups > Quick Actions > Show More.
2. Click Manage Enterprise HCM Information.
3. In the Enterprise Information section, configure the setting Person Creation Duplicate Check.
The table presents the options available when configuring the Person Creation Duplicate Check option.

Option

---

## If the candidate's national identifier matches
*Chunk ID: OHR-REC-0881 | Chapter: Job Offers*

the person's within the same country and type.
Note that if the candidate's value is null, no
duplicates are found.

---

## If the candidate's national identifier matches
*Chunk ID: OHR-REC-0882 | Chapter: Job Offers*

the person's within the same country and type,
regardless of whether or not the names or birth
dates match.
Alternately, if the last name and the initial of the
first name do match, and if the candidate's birth
date matches the person's or either birth date is
null, regardless of whether the NID matches or
doesn't match or is null.

---

## Will Find Duplicates If
*Chunk ID: OHR-REC-0883 | Chapter: Job Offers*

regardless of whether or not the names or birth
dates match.
Alternately, if the last name and the initial of the
first name do match, and if the candidate's birth
date matches the person's or either birth date is
null, regardless of whether the NID matches or
doesn't match or is null.

---

## The duplicate check results depend on the info
*Chunk ID: OHR-REC-0884 | Chapter: Job Offers*

provided by the candidate. If the candidate
provided all 4 attributes, matching is based
on the 4 attributes. If the candidate provided
2 attributes, matching is based on the 2
attributes. Last name and first name are
required, while gender and DOB are optional.
Here are examples:
• Candidate provided last name, first name,
DOB, gender. The duplicate check brings
data only if all 4 attributes match with a
person in the system.
• Candidate provided last name, first name,
DOB. The duplicate check brings data
matching these 3 attributes.
• Candidate provided last name, first name,
gender. The duplicate check brings data
matching these 3 attributes.
• Candidate provided last name, first name.
The duplicate check brings data matching
these 2 attributes.
• Candidate provided national identifier,
type, country along with last name, first
name. The duplicate check brings data
matching national identifier, type, country.
Also, it brings data matching last name,
first name.

NID

---

## Similar behavior as option 2, except if national
*Chunk ID: OHR-REC-0885 | Chapter: Job Offers*

identifiers for different countries have matching
numbers then additional duplicates might be
found.

---

## Last Name, First Initial, Date of Birth or National Similar behavior as option 3, except if national
*Chunk ID: OHR-REC-0886 | Chapter: Job Offers*

ID
identifiers from different countries have
matching numbers then additional duplicates
might be found. Note this is the default
behavior when no option has been explicitly
selected for this setting.

---

## Similar behavior as option 4, except if national
*Chunk ID: OHR-REC-0887 | Chapter: Job Offers*

identifiers for different countries have matching
numbers then additional duplicates might be
found.

Option

---

## Similar behavior as option 5, except if national
*Chunk ID: OHR-REC-0888 | Chapter: Job Offers*

identifiers for different countries have matching
numbers then additional duplicates might be
found.

---

## Configure the Duplicate Check in Move to HR Setting
*Chunk ID: OHR-REC-0889 | Chapter: Job Offers*

To extend the enterprise's Person Creation Duplicate Check to external candidates who get moved into the HR phase,
a second setting within Recruiting must also be enabled. This will prevent creating a Pending Worker or a Pending
Work Relationship automatically for new hire or rehire candidates if they have potential duplicates according to these
definitions, until a user can make a decision on how to proceed with the end of their recruiting process.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Move to HR section and click Edit.
3. In the Duplicate Check in Move to HR section, choose one of these options:
4.
◦ None - no duplicate validation

◦ Use Person Creation Duplicate Check setting for all candidates
◦ Use Person Creation Duplicate Check setting only for candidates with date of birth and national identifier

5. Click Save.

---

## Include as Potential Duplicates
*Chunk ID: OHR-REC-0890 | Chapter: Job Offers*

You can specify the person types to be included in the duplicate search when you move a candidate to the HR phase.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Move to HR section and click Edit.
3. In the Include as Potential Duplicates section, choose one of these options:
4.
◦ All person types

◦ Only person types supported in recruiting: You can exclude person types other than Employee, Ex-

Employee, Contingent Worker, Ex-Contingent Worker, and Pending Worker from duplicate matching.
5. Click Save.

---

## Configure the Automatic Processing of Internal Offers
*Chunk ID: OHR-REC-0891 | Chapter: Job Offers*

When the automatic processing of internal candidates is enabled, job applications follow a slightly different path
through the states in the HR phase. Internal candidates go into the state Pending Automated Processing until the

---

## Job Offers
*Chunk ID: OHR-REC-0892 | Chapter: Job Offers*

appropriate date arrives. On that number of days before each candidate's proposed start date, the worker's new
assignment and salary are automatically created by the scheduled process Perform Recruiting Candidate Selection
Process Offer Actions. Users don’t need to take any action.
By default, internal candidate offers get transformed into their new assignments 7 days before their proposed start date.
When the profile option ORA_IRC_AUTO_PROCESS_INTERNAL_OFFERS is enabled, you can configure the timing of
when the automatic processing of internal job offers will occur.
Note: If your organization is using Payroll-based Salary Basis in their offers, or has salary element eligibility defined
on Payroll, the Payroll section should be populated during the offer creation to avoid any errors when the job
application of the internal candidate is moved to HR phase.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Offer section and click Edit.
3. In the Automatically Process Internal Offers to Assignments section, set the number of days.
4. Click Save.

---

## Remove Hired Candidates from Consideration
*Chunk ID: OHR-REC-0893 | Chapter: Job Offers*

When candidates move to the HR phase, you may want to remove them from consideration for other job applications or
pools.
This automates the process of removing candidates from active pools where they might continue be nurtured, or
withdraws them from other job applications where they are under consideration.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Offer section and click Edit.
3. Click the Withdraw candidates from all other job applications when they move to the HR phase check box.
4. Click the Remove candidates from candidate pools when they move to the HR phase check box.
5. Click Save.

---

## Move Candidates Automatically to HR Phase
*Chunk ID: OHR-REC-0894 | Chapter: Job Offers*

At the end of the whole recruiting lifecycle, candidates need to be progressed either manually or automatically into the
final HR phase of the candidate selection process.

---

## When you configure a candidate selection process, you can automate the Move to HR action so that job applications are
*Chunk ID: OHR-REC-0895 | Chapter: Job Offers*

automatically moved to the HR phase once they reach a specific point in the candidate selection process and selected
conditions are met. For instance, candidates could be automatically moved forward after the background check.
Before you start
You can add the Move to HR action only on:
• The Offer - Accepted phase and state.
• Any non-terminal states of custom phases included between the Offer and HR phases.
• Phase-level events of custom phases included between the Offer and HR phases.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration
2. On the Candidate Selection Process Configuration page, create a selection process and select an existing draft
process.
3. Add the Move to HR action to Offer - Accepted or to a custom phase between the Offer and HR phases, or any nonterminal state of that phase.
4. On the Action: Move to HR page, add conditions.
a. Click Add Predefined to select predefined conditions.
b. Click Add Fast Formulas to select fast formulas used as conditions.
5. Click Save and Close.
Results:
There might be issues when trying to automatically move candidates forward into the HR phase. When the move
is performed manually, recruiters can see if any error occurred. When the move is configured to be automatic, a
notification can be sent automatically when the candidate's job application has a problem and falls into the state Error
During Processing. This standard notification is available in Alerts Composer:
• IRC_Move_To_HR_Error: Error During Move to HR
You can configure this notification. For instance, the notification is sent to the recruiters by default but you could add
other recipients such as an HR specialist who knows the most about resolving these unusual situations. These tokens
are used in the notification to display specific details of each error:
• OfferErrorMessageText
• OfferErrorDetailText
Also, you might want to send the user to the quick action called Manage Job Offers, which is available to users with the
seeded role of HR Specialist. If this notification is configured to go to a recipient who has the privileges to reach this
quick action area, then you can add these tokens:
• HRJobOfferListDeepLinkURL: This token takes the users to the offers list.
• HRJobOfferDetailDeepLinkURL: This token takes the user directly to the specific offer that's in error.

---

## Hire Date Filter on the Manage Job Offers Page
*Chunk ID: OHR-REC-0896 | Chapter: Job Offers*

A profile option controls the behavior of the Hire Date filter on the Manager Job Offers page.
You can configure the profile option ORA_IRC_OFR_HRLIST_MANDATE_DATE_FILTERS using the Manage Administrator
Profile Values task in the Setup and Maintenance work area. Two values are available:
• N: This is the default value. The Hire Date filter on the Manager Job Offers page is displayed only when a job
offer is in terminal state (Withdrawn by Candidate, Rejected, Processed). For example, if a user wants to see job
offers in the Withdrawn by Candidate state they can't unless they apply the Hire Date filter.
• Y: The Hire Date filter on the Manager Job Offers page is displayed at all times. Without applying the filter no
results will be fetched for any state in the HR phase.
The Hire Date filter offers these values:
• Next 30 days (default value)
• Next 7 days
• Last 7 days
• Last 30 days
• No Date Yet
• Range (Specify): Maximum range is 90 days.

---

## Revisit the Offer and Lifecycle After a Candidate is
*Chunk ID: OHR-REC-0897 | Chapter: Job Offers*

Merged with a Duplicate
Recruiters and HR specialists can decide to combine the candidate with any employee, ex-employee, contingent worker,
or ex-contingent worker who was identified as a possible match.
Note that they can't automatically perform the merge with other person types who may be identified as a duplicate. If
the application identifies a person of type contact, beneficiary, or others as a possible match, the HR specialist will need
to manage this job application manually.
After the decision to merge, the candidate profile information gets merged with the selected person record, and the
candidate's existing job applications get transferred to the selected person. This includes the job application for which
the current job offer was created, approved, and accepted.
The candidate's job offer details must be recreated on the transferred job application, and all its details must be revisited
to ensure that everything remains appropriate for the selected person. Any required changes must be made in the
offer's values in case they were specifically appropriate only for external candidates or other eligibility criteria were
defined. After the user reviews the offer, various choices are available to decide whether to bypass some or all of the
remainder of the lifecycle:
1. Upon submitting each recreated job offer, the user can decide whether to proceed directly back to the HR phase
of the lifecycle, bypassing every intervening state and any custom phases.
2. If they decide not to bypass the lifecycle for this person's new offer, offer approval rules can be configured to
treat these recreated offers differently. The field MERGE_FLAG exists for use in the approval area, indicating

---

## Job Offers
*Chunk ID: OHR-REC-0898 | Chapter: Job Offers*

that the offer is the result of this merge process after a duplicate record was identified. Approval rules can be
configured to send these offers through an alternate set of approvers, or no approvers at all.
3. Similarly, these recreated offers can be more quickly moved into the HR phase even if the individual users
decide not to bypass the lifecycle. The field MERGE_FLAG exists for use in fast formulas, indicating that the
offer is the result of this merge process after a duplicate record was identified. Within the candidate selection
process, automatic progressions can be configured for these merged candidates who had already moved to HR
before their duplication was discovered. For example, their recreated offers can be configured to be extended
immediately after approval, and they can be moved directly into the HR phase as soon as they have accepted
their revised offers.
Note: The requisition on which the candidate applied may have already been filled before anyone realizes that they're
a duplicate of an existing person. In that case, when the recruiter tries to merge the two records, an error message will
instruct them that the requisition must be reopened first. As soon as the newly-created offer gets moved into the HR
phase again, this merged person will again fill the opening that the original candidate had taken.

---

## Understanding Job Offers and Journeys
*Chunk ID: OHR-REC-0899 | Chapter: Job Offers*

Journeys are sets of standard tasks to be performed when there are changes in personal circumstances, for instance
when a candidate reaches the end of their recruiting process and prepares to begin their new assignment.
Allocating a journey too early in a candidate's lifecycle isn't effective. External candidates can't access any journeys
allocated to them until after they become a pending worker. Internal mobility candidates might end up accepting the
offer as the recruiting process continues. So an appropriate time in the recruiting lifecycle to allocate a journey is near
the end, when the candidate's job application moves into the HR phase. There are many actions that occur around this
point in the candidate's lifecycle, and the appropriate one might be the action named Move to HR.

---

## Allocating Journeys When Candidates Move to the HR Phase
*Chunk ID: OHR-REC-0900 | Chapter: Job Offers*

Every successful candidate eventually gets moved into the HR phase of the recruiting lifecycle.
When an external candidate is progressed to the HR phase, both the actions Move to HR and Add Pending Worker are
triggered for a new hire. In the case of a rehire, both the actions Move to HR and Add Pending Work Relationship are
triggered. It's recommended that you don't configure a journey based on the Move to HR action for external candidates.
Instead configure journeys for external candidates based on the actions Add Pending Worker and Add Pending Work
Relationship. This configuration is helpful in case the candidate gets delayed in the state Error During Processing after
they're moved to the HR phase. The journey will be allocated only after the issue gets resolved when the pending worker
or work relationship can be created.
When an internal candidate gets moved into the HR phase, their job application arrives in the status HR - Pending
Manual Processing and they wait for an HR specialist to process them in the Manage Job Offers work area. The HR
specialist will transform the offer's values using the action that was originally selected in the offer, such as Transfer,
Global Transfer, or Promote. If any journey is configured for these actions, it will get allocated for the internal person
only after the HR specialist has submitted this process based upon the offer. If you need your internal candidates to
perform journey tasks before their actual internal change becomes effective, then you would need to configure the
journey for the action of Move to HR.

---

## Note: Although the code for the action named Move to HR is ORA_IRC_ACCEPT_JOB_OFFER, the moment of
*Chunk ID: OHR-REC-0901 | Chapter: Job Offers*

triggering this action isn't when the candidate accepts the job offer. After an offer is accepted and before the Move to
HR action, time might elapse and any custom-configured phases can intervene. So despite its code which mentions
acceptance, the action Move to HR is triggered when the candidate's job application first changes to any state in the
HR phase.
Configuring eligibility profiles can ensure that only one journey gets allocated to a candidate at this point in their
recruiting lifecycle. For instance, you might want to ensure that the action Move to HR is configured to trigger a journey
only for internal candidates, so that external new hires and rehires can receive journeys based on the actions Add
Pending Worker and Add Pending Work Relationship respectively.
Journeys intended to be triggered upon the Move to HR action should not be configured with tasks allocated to the
initiator of the journey. That's because the action Move to HR usually has no initiator, when it's performed automatically
within the candidate selection process or even when it's performed manually by a user.
Note: These offer-related actions aren't appropriate for allocating journeys:
• The action Create Offer (code EMPL_OFFER_CREATE) is likely premature, as there are many reasons that a
newly-drafted offer might not result in a newly-hired or newly-transferred worker.
• The action Update Offer (code EMPL_OFFER_CHANGE) isn't used in Recruiting today, as all changes to offers
are corrections instead of updates.

---

## Journeys and Redrafted Offers
*Chunk ID: OHR-REC-0902 | Chapter: Job Offers*

Occasionally it's necessary to make changes to a job offer or offer letter after the job application has moved into the
HR phase, or even after a pending worker or worker was created for the candidate. This can be done by canceling the
transaction and then redrafting the job offer.
When a pending worker or worker transaction is canceled, their record is removed and the person becomes only a
candidate once again. This means it's no longer possible for them or any other users to access any journey that was
allocated to that person. However, this journey isn't removed, and any completed tasks on that journey still retain all
information.
If and when the redrafted offer and its job application get moved to the HR phase once again, a new pending worker
and worker will again be created. Now that journey, which remained active, becomes accessible once again for that
pending worker or worker, and all of its tasks can get continued and completed.
Note: If you intend to cancel a pending worker or worker who has an active journey and you don't want that journey
to remain active, consider deleting the journey before canceling the pending worker or worker. If the person gets
canceled first, managers and other users no longer have any way to access the still-active journey from the user
interface.

Related Topics
• How You Use Journeys

---

# Grid Views

## Grid Views
*Chunk ID: OHR-REC-0903 | Chapter: Grid Views*

Enable Grid View
A grid view is available to view job applications for a requisition, candidates in a candidate pool, and candidates in a
candidate search results list. With grid view, data is displayed in a columnar layout.
1. Create a Profile Option to Enable Grid View
2. Assign Grid View Privileges

---

## Create a Profile Option to Enable Grid View
*Chunk ID: OHR-REC-0904 | Chapter: Grid Views*

The Grid View feature is disabled by default. You need to create and enable a profile option to enable the feature.
You need to create a profile a profile option called IRC_SUBMISSION_LIST_GRID_VIEW_ENABLED.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Profile Options.
4. Click the task name.
5. On the Manage Profile Options page, click the New icon.
6. On the Create Profile Option page, create the profile option by entering these values:
◦ Profile Option Code: IRC_SUBMISSION_LIST_GRID_VIEW_ENABLED

◦ Profile Display Name: Grid View
◦ Application: Recruiting
◦ Module: Recruiting Common
◦ Description: Enable the grid view feature.
◦ Start Date: Today's date
7. Click Save and Close.
What to do next
When the profile option is created, you need to enable it at the Site level.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
IRC_SUBMISSION_LIST_GRID_VIEW_ENABLED.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.

Related Topics
• Create and Edit Profile Options

---

## Assign Grid View Privileges
*Chunk ID: OHR-REC-0905 | Chapter: Grid Views*

You can assign privileges to control the user's ability to create and manage grid views.
When the Grid View feature is enabled, all users have access to the Summary view and they can set their default view
using views created for them.
Here are the privileges that you can assign.
Personalize Candidates Lists (IRC_PERSONALIZE_CANDIDATE_JOB_APPLICATION_LISTS):
• Users with this privilege can create and manage their own personal grid views. Users without this privilege can
only define their default view, from the set of seeded and customer created views they can see.
Manage Candidates Lists (IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS):
• Users with this privilege can create and manage views that other users will have access to. Site level views are
available to all users; role-based views are available to users depending on their user roles.
• Users can create compound fields.
• Users can define data masking for the grid view.

---

## Default Summary View in Grid View
*Chunk ID: OHR-REC-0906 | Chapter: Grid Views*

This table lists the columns and fields displayed in the Summary view of the grid view. The Summary view is the default
view for all users. Columns will vary depending on where the grid view is used.

Column

Field

Candidate

---

## Candidate Number
*Chunk ID: OHR-REC-0907 | Chapter: Grid Views*

Candidate Location
Candidate Email Address: When you click the
email address, it opens the email automatically.
You need the privilege View Person Email for
Recruiting Data (IRC_VIEW_ PERSON_EMAIL_
FOR_RECRUITING_DATA) to view the field.
Candidate Phone Number: You need the
privilege View Person Phone for Recruiting
Data (IRC_VIEW_PERSON_PHONE_FOR_
RECRUITING_DATA) to view the field.
Person Number: For external candidates, the
person number is created during the HR phase.
If the person number isn't yet available, a blank

---

## Compound Field Content
*Chunk ID: OHR-REC-0908 | Chapter: Grid Views*

value appears on the grid view. For internal
candidates, the person number is always
shown.

Details

---

## Recent Certifications (up to 3 most recent
*Chunk ID: OHR-REC-0909 | Chapter: Grid Views*

entries)

Certification Name, Issue Date, Issued By,
State/Province Code, Country Name

---

## Work Preferences (candidate responded Y)
*Chunk ID: OHR-REC-0910 | Chapter: Grid Views*

Travel Domestically, Travel Internationally,
Willing to Relocate, Consider Temporary
Assignment, Consider Part Time Work, Flexible
To Work

---

# Recruiting Activity Center

## Recruiting Activity Center
*Chunk ID: OHR-REC-0911 | Chapter: Recruiting Activity Center*

Set Up the Recruiting Activity Center
When you set up the Recruiting Activity Center, recruiters and hiring managers have a place to easily access and
manage recruiting activities related to the job requisitions, job applications, and job offers they own.
For details, see How do I set up the Recruiting Activity Center?

---

## Recruiting Features Configuration Report
*Chunk ID: OHR-REC-0912 | Chapter: Recruiting Activity Center*

24 Recruiting Features Configuration Report
Set Up the Recruiting Features Configuration Report
You can use the Recruiting feature configuration report to review the features that are enabled, their associated settings,
the profile options to enable the features and the value of these profile options, and metrics on the required processes
scheduled in the customer's environment.
With this report:
• You can take advantage of a quick analytical view to understand the recruiting features enabled in your
environment out of available features.
• You can track the configuration progress during implementation.
• You can track and report the progress of new features addition on a periodic basis.
• You'll get a smooth transition of configuration ownership from system implementation partner to your
administrator during sustenance phase.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Feature Configuration Report
2. On the Recruiting Features Configuration Report page, select a functional area and a release version.
◦ Functional Area: This menu is populated with all the features available in the environment. If you select
Base Features, key features available before release 20B are selected. If you select All Features, you'll get
the base features plus features available for individual releases.
◦ Release Version: If you select Base, releases available before release 20B are selected. If you select All, you'll
get the base releases plus individual releases.
Note: When you select Base Features or All Features in the Functional Area menu, the Release Version menu is
empty. Release Version isn't supported for these use cases.
3. Click Create Report.
Results:
The report is generated and available in a downloadable PDF format.

---

## Recruiting Features Configuration Report
*Chunk ID: OHR-REC-0913 | Chapter: Recruiting Activity Center*

25 Oracle AI Apps in Recruiting
Welcome to Oracle AI Apps for Talent Management
Oracle AI Apps for Talent Management uses artificial intelligence and machine learning algorithms to provide features
to the HR specialists, recruiters, candidates, employees, and managers.
Here's a summary of the AI Apps features, along with activation and ingestion scheduled processes details:

Feature

Product

---

## Synchronize Recruiting Candidates
*Chunk ID: OHR-REC-0914 | Chapter: Recruiting Activity Center*

Data for Candidate
Recommendations
Synchronize
Talent Data for AI
Recommendations

---

## Synchronize Recruiting Recruiters
*Chunk ID: OHR-REC-0915 | Chapter: Recruiting Activity Center*

Data for Candidate
Recommendations
Synchronize
Talent Data for AI
Recommendations

---

## Suggest skills to
*Chunk ID: OHR-REC-0916 | Chapter: Recruiting Activity Center*

recruiters so that
they can quickly add
the required skills
to a requisition and
enhance the job
description.

---

## Scheduled Processes
*Chunk ID: OHR-REC-0917 | Chapter: Recruiting Activity Center*

for Ingestion

Audience

Description

managers to add to
succession plans.
Skills Center

---

## Synchronize Recruiting Employees
*Chunk ID: OHR-REC-0918 | Chapter: Recruiting Activity Center*

Data for Candidate
Recommendations
Managers
Synchronize
Talent Data for AI
Recommendations

---

## Provides a centralized
*Chunk ID: OHR-REC-0919 | Chapter: Recruiting Activity Center*

place for employees
and managers to
manage skills and
suggest actions to
drive personal and
organizational growth.

---

## Provide AI suggestions
*Chunk ID: OHR-REC-0920 | Chapter: Recruiting Activity Center*

for skills for recruiters
to enter skills for job
profiles.

Synchronize
Talent Data for AI
Recommendations
Skills Advisor for
Position Profiles

---

## Synchronize Recruiting Gig creators
*Chunk ID: OHR-REC-0921 | Chapter: Recruiting Activity Center*

Data for Candidate
(Recruiters, managers)
Recommendations
Candidates
Synchronize
Talent Data for AI
Recommendations

---

## Provide skill
*Chunk ID: OHR-REC-0922 | Chapter: Recruiting Activity Center*

suggestions that
gig creators can
associate with their
gigs. Provide an ability
for candidates to see
the skills comparison
of the gig against their
own skills.

---

## Suggest appropriate
*Chunk ID: OHR-REC-0923 | Chapter: Recruiting Activity Center*

skills to set as learning
outcomes when
configuring a course
or specialization.

Learning
administrators

---

## Suggest relevant skills
*Chunk ID: OHR-REC-0924 | Chapter: Recruiting Activity Center*

for HR administrators
to create and maintain
a targeted position
specification.

Note: The AI Apps features work only when the environment uses English as the operation language.
To activate AI Apps for Talent Management, see Activate Oracle AI Apps for Talent Management.

---

## Activate Oracle AI Apps for Talent Management
*Chunk ID: OHR-REC-0925 | Chapter: Recruiting Activity Center*

As part of configuring the AI Apps features, you will need to activate Oracle AI Apps.
These steps apply to all features except time to hire. To activate the Time to Hire feature, see Set Up Time to Hire.
Before you start

---

## Oracle AI Apps in Recruiting
*Chunk ID: OHR-REC-0926 | Chapter: Recruiting Activity Center*

To complete these activation steps, you must:
• Either have the predefined role Application Implementation Consultant (22D and above)
• Or have a custom role that inherits the predefined role Adaptive Intelligence Applications Administrator (22C
and above)
Note:
• When you activate Dynamic Skills, you must also activate AI Talent Best Match.
• If you were recently granted either the Application Implementation Consultant role or the Adaptive Intelligence
Applications Administration role, you might be denied access while activating an app, or the status of the
app may appear as Unavailable. Try signing into the application with another user who had the Application
Implementation Consultant role granted to them a while ago.

Here's what to do
1. Sign into your Oracle Fusion Application.
2. On the home page, click the Tools tab and then click the quick action AI Apps Administration.
The Application Administration page displays a list of apps and their current activation status.
3. Click the row for the app you want to activate, for example, Dynamic Skills.
4. On the app page, click Activate App.
The status changes to Processing, and then will change to Active. It may take about 5 to 20 minutes for the status to
change from Processing to Active.

---

## Ingestion Steps for AI Apps Features
*Chunk ID: OHR-REC-0927 | Chapter: Recruiting Activity Center*

These steps apply to all Oracle AI Apps features except time to hire, and are meant for the implementation user.
Note: You must complete these steps to make sure that all the AI features work as expected.

---

## These scheduled processes extract data from your Oracle HCM and transfer the data to the connected AI Apps
*Chunk ID: OHR-REC-0928 | Chapter: Recruiting Activity Center*

environment. This data will then be processed by machine learning pipelines to build custom machine learning models.
See the table in the topic Welcome to Oracle AI Apps for Talent Management to understand the AI application to activate
and the processes for data ingestion.
Here are a few things to keep in mind:
Here's what to do
•
•
•

These steps are required for all the AI features except time to hire.
You must not proceed further unless you completed the steps outlined in the previous sections.
You must set the ORA_HRT_AI_SKILLS_ASSISTANT profile option and/or the ORA_HRD_AI_BEST_ROLES
profile option to Yes to integrate with AI Apps.
a.
b.
c.
d.

Sign into your Oracle HCM application and navigate to the Setup and Maintenance work area.
Search for and click Manage Administrator Profile Values.
Search for and select the profile option ORA_HRT_AI_SKILLS_ASSISTANT or ORA_HRD_AI_BEST_ROLES.
In the Profile Values section, make sure that the Profile Level is set to Site.

•

•

•

---

## Oracle AI Apps in Recruiting
*Chunk ID: OHR-REC-0929 | Chapter: Recruiting Activity Center*

e. Set the Profile Value field to Yes.
f. Click Save and Close.
If you're following these steps in a nonproduction environment, set the jobs to run just once. If you're setting
this up in a production environment, you must set up a recurring schedule. Oracle recommends that you run
these scheduled processes once a week initially and then decide if you need to do it more often. For example,
you might need to do it more often if you've a significant hiring cycle, if you revised competencies, and so on.
The first execution of these scheduled processes will take significantly longer because the scheduled process
will try to extract historical data. Subsequent runs will be faster because the process extracts only incremental
changes since the last run.
After the scheduled processes complete, anonymized data from HCM Cloud will have been exported to the
AI cloud service. Processing of this data will begin automatically and is expected to take about 8-12 hours
to complete, depending on the volume of data. You can expect to start seeing recommendations after this
process completes.
If AI Talent Best Match is already activated and you’re now activating Dynamic Skills, these scheduled
processes might already be running in your environment. You might not need to run the processes again.

---

## Synchronize Recruiting Data for Candidate Recommendations
*Chunk ID: OHR-REC-0930 | Chapter: Recruiting Activity Center*

Schedule the Synchronize Recruiting Data for Candidate Recommendations job only if you’re live on Oracle Recruiting.
You must also be using one of the AI features for Recruiting.
1. Sign in as an admin user with the PER_RUN_HR_PROCESSES_PRIV privilege.
2. Select Scheduled Processes from either the Tools tab or from the navigator.
3. Click Schedule New Process.
4. Search for the Synchronize Recruiting Data for Candidate Recommendations scheduled process.
You must select the check box for the appropriate AI feature in Oracle Recruiting. See Enable Intelligent Matching
Features. For Dynamic Skills in Recruiting, you must select the feature Recommended Skills. If you don’t complete
this step, you won't find the scheduled process Synchronize Recruiting Data for Candidate Recommendations.
5. From the Entity Type list, select All.
6. Leave the From Date field blank.
7. Click Submit.
8. Click the Refresh icon to track recently submitted jobs.
What to do next
There will be a parent job and one or more child jobs depending on the parallel threads in action.
After the job completes successfully, you can check the scheduled process logs to get more details like the ingested file
names, ingestion path, the number of profiles and so on. These logs also record any errors that may occur.

---

## Synchronize Talent Data for AI Recommendations
*Chunk ID: OHR-REC-0931 | Chapter: Recruiting Activity Center*

If you’re live on Career Development, Succession Management, or Dynamic Skills, then you need to schedule the
Synchronize Talent Data for AI Recommendations process to view AI-based suggestions.
1. Sign in as an admin user with the PER_RUN_HR_PROCESSES_PRIV privilege.
2. Select Scheduled Processes from either the Tools tab or from the navigator.

3. Click Schedule New Process.
4. Search for the job Synchronize Talent Data for AI Recommendations.
5. Provide the parameters according to this table.
Parameter

Value

---

## AI Feature
*Chunk ID: OHR-REC-0932 | Chapter: Recruiting Activity Center*

◦ If you’re activating AI Talent Best Match, select Best Profile Matches.
◦ If you’re activating Dynamic Skills, select Skills Suggestions.
you’ve activated both these applications, run two different scheduled processes, one with the
◦ Ifvalue
Best Profile Matches, and another for Skills Suggestions.

---

## Talent Object
*Chunk ID: OHR-REC-0933 | Chapter: Recruiting Activity Center*

Select All to ingest all object types. You may optionally choose to ingest one talent object at a time.

---

## From Date
*Chunk ID: OHR-REC-0934 | Chapter: Recruiting Activity Center*

Indicates the date from which we want the Talent Object data to be pushed to AI cloud.
When left blank, an incremental ingestion will pick the Talent Object data from the last successful
run.

---

## Select the number of parallel java processes to run during ingestion. Use the default value unless
*Chunk ID: OHR-REC-0935 | Chapter: Recruiting Activity Center*

you've a specific reason to select a different value.
Default: 8, Minimum: 1, Maximum: 20

---

## Submission Notes
*Chunk ID: OHR-REC-0936 | Chapter: Recruiting Activity Center*

Provide optional comments regarding the current scheduled process.

6. Click Submit.
7. Use the refresh icon to track recently submitted jobs.
What to do next
There will be a parent job and one or more child jobs depending on the parallel threads in action.
After the jobs complete successfully, you can check the scheduled process logs to get more details like the ingested file
names, ingestion path, the number of profiles, and so on. These logs also record any errors that may occur.

Set Up Matching Features: Suggested Candidates,
Similar Candidates, Similar Jobs, Recommended Jobs
You can enable intelligent matching features such as Suggested Candidates, Similar Candidates, Similar Jobs,
Suggested Jobs. These features use Oracle AI Apps matching algorithms to provide suggestions.
• Suggested Candidates: Recruiters use the Suggested Candidates feature to review the suggested candidates for
an open job requisition.
• Similar Candidates: Recruiters use the Similar Candidates feature to find candidates that have similar traits with
an existing candidate.
• Similar Jobs: Recruiters use the Similar Jobs feature to suggest similar jobs based on a specific job requisition.
• Suggested Jobs: Candidates use the Suggested Jobs feature to review jobs based on their profile.

---

## Oracle AI Apps in Recruiting
*Chunk ID: OHR-REC-0937 | Chapter: Recruiting Activity Center*

To use matching features, your organization must meet the following criteria:
• The Recruiting environment must NOT be on a government pod.
For best results, it's strongly recommended to also meet these criteria:
• The Recruiting environment must be live in production for at least 6 months or have prior production data of at
least 6 months to benefit from high quality recommendations and prediction results.
• The Recruiting environment must use English for their operation language.
Suggested Candidates, Similar Candidates, Similar Jobs, and Recommended Jobs are automatically activated and
don’t require any Oracle AI Apps activation steps. You need to run the Synchronize Recruiting Data for Candidate
Recommendations scheduled process for ingestion.
1. Create the Profile Option for Intelligent Matching
2. Enable Intelligent Matching Features
3. Run the Scheduled Process for Candidate Recommendations

---

## Grant Permission to View AI-Based Candidate Suggestions
*Chunk ID: OHR-REC-0938 | Chapter: Recruiting Activity Center*

Grant security permissions for users to view classic AI-based features.
1. Go to Navigator > Tools > Security Console.
2. On the Roles tab, search for the Adaptive Intelligence Applications Administrator
(ORA_HRC_AI_APPLICATIONS_ADMINISTRATOR_JOB) role.
3. In the Basic Information train stop, select Enable Permission Groups.
4. In the Enable Permission Groups dialog box, select Enable Permission Groups.
5. Go to the Summary train stop.
6. Select Save and Close.
7. Create a role mapping and associate the admin user role with the Adaptive Intelligence Applications Administrator
(ORA_HRC_AI_APPLICATIONS_ADMINISTRATOR_JOB) role.

---

## Create the Profile Option for Intelligent Matching
*Chunk ID: OHR-REC-0939 | Chapter: Recruiting Activity Center*

You need to create and enable a profile option for intelligent matching called IRC_AI_INTELLIGENT_MATCHING.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Profile Options.
4. Click the task name.
5. On the Manage Profile Options page, click the New icon.
6. On the Create Profile Option page, create the profile option by entering these values:
◦ Profile Option Code: IRC_AI_INTELLIGENT_MATCHING

◦ Profile Display Name: Intelligent Matching Features Enabled
◦ Application: Recruiting
◦ Module: Recruiting Common

---

## Oracle AI Apps in Recruiting
*Chunk ID: OHR-REC-0940 | Chapter: Recruiting Activity Center*

◦ Description: Enable or disable AI features in the Setup and Maintenance work area.
◦ Start Date: Today's date
7. Click Save and Close.
What to do next
When the profile option is created, you need to enable it at the Site level.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
IRC_AI_INTELLIGENT_MATCHING.
6. Set the profile value at the Site level to Y.
7. Click Save and Close.

Related Topics
• Create and Edit Profile Options

---

## Enable Intelligent Matching Features
*Chunk ID: OHR-REC-0941 | Chapter: Recruiting Activity Center*

You enable intelligent matching features to make them available to users in Oracle Recruiting.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the AI Feature Integration section and click Edit.
3. Select the matching feature you want to enable: Suggested Candidates, Similar Jobs, Suggested Jobs, Similar
Candidates.
4. Click Save.

---

## Run the Scheduled Process for Candidate Recommendations
*Chunk ID: OHR-REC-0942 | Chapter: Recruiting Activity Center*

When matching features are enabled, you need to run the Synchronize Recruiting Data for Candidate
Recommendations scheduled process to push data from Oracle Recruiting to the Oracle AI Apps.
1. In the Navigator menu, go to Tools > Scheduled Processes.
2. On the Overview page, click Schedule New Process.
3. Search for the process Synchronize Recruiting Data for Candidate Recommendations.
4. Click OK.
5. On the Process Details page, click Advanced Options.
6. Configure these fields:
◦ Entity Type: Select All or leave the field blank. For initial or incremental data ingestion, you need to select All
to ingest all the entities.

◦ From Date: You can leave the field blank to pull all data, or you can select a date when to start the data
extraction.

---

## Note: When you leave the From Date field blank, the process extracts all the data during the first run
*Chunk ID: OHR-REC-0943 | Chapter: Recruiting Activity Center*

and only extracts incremental date from the next run. Oracle recommends that you run a complete data
extract the first time. You must set all the scheduled subsequent runs to extract only incremental data.

◦ We recommend a recurring schedule to be performed every 1 hour. On a testing environment, you can
schedule on a need basis. Click the Schedule tab and set up a schedule.

7. Click Submit.
Results:
When the scheduled process is completed, anonymous requisition and candidate data will have been exported to the
AI Cloud service and will then be processed. You can expect to see recommendations for AI Apps after 8 to 12 hours
depending on the volume of data.

---

## Data Used for Suggestions in Matching Features
*Chunk ID: OHR-REC-0944 | Chapter: Recruiting Activity Center*

Suggested Candidates, Similar Candidates, Similar Jobs, and Suggested Jobs use Oracle AI Apps matching algorithms
to provide suggestions based on the data presented in this table.

Feature

---

## Suggested Jobs
*Chunk ID: OHR-REC-0945 | Chapter: Recruiting Activity Center*

• Description
Similar Jobs

• Education Level
• Job Function
• Job Family
• Qualifications
• Responsibilities

---

## Suggested Candidates
*Chunk ID: OHR-REC-0946 | Chapter: Recruiting Activity Center*

Suggested Jobs
Similar Candidates

Candidate Profile Data:
• Work History (Previous Employment)
Title

◦
◦ Achievements
◦ Responsibilities

• Degrees (Education)
Degree

◦
◦ Major
◦ Education Level
• Skill
Name

◦
◦ Description

---

## Hide Suggested Candidates in Job Requisitions
*Chunk ID: OHR-REC-0947 | Chapter: Recruiting Activity Center*

You can define a list of countries for which the Suggested Candidates and Similar Candidates features aren't displayed.
If the posting location of a job requisition is part of the list of countries you defined:
• The Suggested Candidates section in the job requisition isn’t displayed.
• When users refine the list of suggested candidates by locations, candidates located in the countries defined by
you won’t show up in the list of suggested candidates.
• The Similar Candidates tab in candidate profiles, prospect records, and candidate pool members isn’t displayed.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. On the Enterprise Recruiting and Candidate Experience Information page, expand the AI Feature Integration
section and click Edit.
3. Select the option Manage AI recommendations based on countries.
4. Select one or several countries for which you want to exclude suggestions.
5. Click Save.

---

## Set Up Time to Hire
*Chunk ID: OHR-REC-0948 | Chapter: Recruiting Activity Center*

You can enable the Time to Hire feature so that recruiters get estimates about the time it will take to make a first hire for
a job requisition. Time to Hire uses Oracle AI Apps matching algorithms to estimate the time for a first hire, based on
previous similar job requisitions.
The Time to Hire estimate provided by this feature represents the estimated time it will take for a requisition in the
Open phase to have a first hired candidate (a candidate being moved to the HR phase). The system learns from the
time to hire of past requisitions, identifying similar requisitions over different attributes such as the title, description,
location, recruiting type, job function, education level. An estimated time to hire is then provided, based on the time to
hire of similar past requisitions. For the very first requisitions, there won’t be sufficient data for the system to provide
an estimate, so there won't be any estimate displayed. It’s recommended to disable the feature until the system has
enough history to use to provide an estimate. When you think you have enough data, you can enable the feature in a
testing environment and try it out to see if a time to hire estimate can be provided.

---

## Oracle AI Apps in Recruiting
*Chunk ID: OHR-REC-0949 | Chapter: Recruiting Activity Center*

To use Time to Hire, your organization must meet the following criteria:
• The Recruiting environment must NOT be on a government pod.
For best results, it's strongly recommended to also meet these criteria:
• The Recruiting environment must be live in production for at least 6 months or have prior production data of at
least 6 months to benefit from high quality recommendations and prediction results.
• The Recruiting environment must use English for their operation language.
Here's what to do:
1. Activate Time to Hire
2. Create the Profile Option for Time to Hire
3. Set Up Time to Hire
4. Display the Estimated Time to Hire Section in Job Requisitions

---

## Grant Permission to View AI-Based Candidate Suggestions
*Chunk ID: OHR-REC-0950 | Chapter: Recruiting Activity Center*

Grant security permissions for users to view classic AI-based features.
1. Go to Navigator > Tools > Security Console.
2. On the Roles tab, search for the Adaptive Intelligence Applications Administrator
(ORA_HRC_AI_APPLICATIONS_ADMINISTRATOR_JOB) role.
3. In the Basic Information train stop, select Enable Permission Groups.
4. In the Enable Permission Groups dialog box, select Enable Permission Groups.
5. Go to the Summary train stop.
6. Select Save and Close.
7. Create a role mapping and associate the admin user role with the Adaptive Intelligence Applications Administrator
(ORA_HRC_AI_APPLICATIONS_ADMINISTRATOR_JOB) role.

---

## Activate Time to Hire
*Chunk ID: OHR-REC-0951 | Chapter: Recruiting Activity Center*

You need to activate AI Services to start training a machine learning model and bring up the Time to Hire prediction
services.
Before you start
To complete these activation steps, you need to:
• Either have the predefined role Application Implementation Consultant (22D and above).
• Or have a custom role that inherits the predefined role Adaptive Intelligence Applications Administrator (22C
and above).
Here's what to do
1. On the home page, click the Tools tab and then click the quick action AI Apps Administration.
The Application Administration page displays a list of apps and their current activation status.
2. Click the row for Time to Hire.

---

## Oracle AI Apps in Recruiting
*Chunk ID: OHR-REC-0952 | Chapter: Recruiting Activity Center*

3. On the Time to Hire page, click Edit Connection.
4. In the Edit BIP Connection dialog box, enter the user name AIAPPS_BIP that you previously created and the
password for this user account.
5. Click Apply.
This saves the credentials to a secure vault in OCI. These credentials will be used only to retrieve historical job
requisition data and use this to train a machine learning model.
6. On the Time to Hire page, click Activate.
This initiates an automated flow that will retrieve the data, train a model, and bring up prediction services for time to
hire.

---

## Create the Profile Option for Time to Hire
*Chunk ID: OHR-REC-0953 | Chapter: Recruiting Activity Center*

You need to create and enable the profile option called IRC_AI_TIME_TO_HIRE.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Profile Options.
4. Click the task name.
5. On the Manage Profile Options page, click the New icon.
6. On the Create Profile Option page, create the profile option by entering these values:
◦ Profile Option Code: IRC_AI_TIME_TO_HIRE

◦ Profile Display Name: Time to Hire Enabled
◦ Application: Recruiting
◦ Module: Recruiting Common
◦ Description: Enable or disable AI features in the Setup and Maintenance work area.
◦ Start Date: Today's date
7. Click Save and Close.
What to do next
When the profile option is created, you need to enable it at the Site level.
1.
2.
3.
4.
5.
6.
7.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code IRC_AI_TIME_TO_HIRE.
Set the profile value at the Site level to Y.
Click Save and Close.

Related Topics
• Create and Edit Profile Options

---

## Enable Time to Hire
*Chunk ID: OHR-REC-0954 | Chapter: Recruiting Activity Center*

You enable the Time to Hire feature to make it available to users in Oracle Recruiting.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the AI Feature Integration section and click Edit.
3. Select the option Time to Hire.
4. Click Save.

---

## Display the Estimated Time to Hire Section in Job Requisitions
*Chunk ID: OHR-REC-0955 | Chapter: Recruiting Activity Center*

You need to create a rule in Transaction Design Studio to display the Estimated Time to Hire section in job requisitions.
You can use these actions to create the rule:
• Recruiting - Create Job Requisition
• Recruiting - View and Edit Job Requisition
You can configure the visibility of the three requisition attributes which can be modified in the Estimated Time to Hire
section:
• Education Level
• Requisition Title
• Locations
Related Topics
• Create a Rule to Configure a Page in Recruiting

26 Dynamic Skills in Recruiting
Overview of Dynamic Skills
To better understand and grow your organization’s talent with an always-current, well-defined, and tailored skills data
set, use Oracle Dynamic Skills. It uses your organizational data to automatically identify, infer, and recommend skills
for people, jobs, and other skills related resources. You've a continuously updated view into the ever-evolving skills to
effectively connect people to opportunities.
Here's a summary of the Dynamic Skills features.
Product

Features

Recruiting

---

## You can use Dynamic Skills on Break Glass environments. For details, see Can AI Apps be enabled in Fusion Break Glass
*Chunk ID: OHR-REC-0956 | Chapter: Recruiting Activity Center*

pods.
US Government Cloud customers can use Dynamic Skills functionality without AI support.
In addition to Dynamic Skills support for European Union Restricted Access (EURA), Dedicated Region Cloud Customer
(DRCC), and UK government pods, the following HCM AI features are also supported:
• Suggested Candidates
• Similar Candidates
• Time to Hire
• Recommended Jobs
• Similar Jobs

---

## Enable Skills Advisor for Candidates and Job
*Chunk ID: OHR-REC-0957 | Chapter: Recruiting Activity Center*

Requisitions
When you enable Skills Advisor for candidates, candidates can select suggested skills for a specific job. When you
enable Skills Advisor for job requisitions, recruiters can add required skills for a job requisition using suggested skills,
thereby enhancing the richness of the job description.
1. Create the Profile Option for Skills Assistant
2. Set Up the Skill Content Section for Person Profiles
3. Set Up the Skill Content Section for Job and Position Profiles
4. Configure the Skills Section in the Job Application Flow
5. Display the Skills Section in Job Requisitions
6. Enable Recommended Skills

---

## Create the Profile Option for Skills Assistant
*Chunk ID: OHR-REC-0958 | Chapter: Recruiting Activity Center*

You need to create and enable the profile option called ORA_HRT_AI_SKILLS_ASSISTANT.
When the profile option is created, you need to enable it at the Site level.
Related Topics
• Create and Edit Profile Options

---

## Set Up the Skill Content Section for Person Profiles
*Chunk ID: OHR-REC-0959 | Chapter: Recruiting Activity Center*

You create a new content section using the Skill template to capture Skills Center skills or convert an existing Skills
content section for Skills Center use.
1. Navigate to My Client Groups > Profiles > Profile Types > Person.
2. To make the content section available for Skills Center, select Skills Center as a subscriber.
Either Skills Center or Talent Profile can subscribe to a Skill Content section.
◦ If Skills Center is the subscriber, it appears only in Skills Center. The Skills Center can subscribe to only one
Skill content section. After you start adding skills to the content section, you can't cancel the Skills Center
subscription to the content section.
◦ If Talent Profile is the subscriber, the skills content is available only in the Skills and Qualifications page.
3. If you're using specific applications to integrate with Skills Center as a subscriber for the content section, select
subscribers such as Learning Outcomes and Career Development.
4. If you want to enable the usage of skill levels on skills, associate a rating model to the Skill Level attribute and make
sure that the attribute isn’t hidden.

---

## You can turn off skill levels later by hiding the attribute in the content section. You can create and use an N-level
*Chunk ID: OHR-REC-0960 | Chapter: Recruiting Activity Center*

rating model as long as it has numerically increasing level values. The level ID with the highest numeric value is
considered as the highest rating, and the level ID with the lowest numeric value is the lowest rating. The rating level
ID can only go up to 9. It is set to Unspecified until the skill level is assigned. You can’t change the rating model used
in a Skills Center content section once you start adding skills in the content section.

---

## Set Up the Skill Content Section for Job and Position Profiles
*Chunk ID: OHR-REC-0961 | Chapter: Recruiting Activity Center*

You can add the Skills Center content section to the job and position profile type the same way as you would add any
other content section. It will enable the content section to define skill requirements for a job and other tasks such as
creating learning item prerequisites.
Skills Advisor can be enabled for use in Job Profiles by enabling the profile option ORA_HRT_AI_SKILLS_ASSISTANT.
When the profile option is created, you need to enable it at the Site level.
Related Topics
• Create and Edit Profile Options

---

## Configure the Skills Section in the Job Application Flow
*Chunk ID: OHR-REC-0962 | Chapter: Recruiting Activity Center*

You need to configure the Skills section in the job application flow so that the skill recommendations appear when the
feature is enabled.
If it’s not already configured, you need to add the Skills block in a job application flow. This enables candidates to view
the Skills section to manually enter or bring in the skills as part of profile import.
1. 1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience
◦ Task: Job Application Flow Configuration
2. Select an application flow.
3. Create a new version of the flow.
4. Add the Skills block.
5. Click Save and Activate.
Related Topics
• Create an Application Flow

---

## Dynamic Skills in Recruiting
*Chunk ID: OHR-REC-0963 | Chapter: Recruiting Activity Center*

You need to create a rule in Transaction Design Studio to display the Skills section in job requisitions. This will enable
recruiting users to view the Skills section in requisitions and add skills relevant to the requisition. You can use these
actions to create the rule:
In Transaction Design Studio, mark the Skills section as visible for both these actions:
You use these actions to create the rule:
• Recruiting - Create Job Requisition
• Recruiting - View and Edit Job Requisition

Related Topics
• Create a Rule to Configure a Page in Recruiting

---

## Enable Recommended Skills
*Chunk ID: OHR-REC-0964 | Chapter: Recruiting Activity Center*

You enable recommended skills to make them available to users in Oracle Recruiting.
1. In the Setup and Maintenance work area, go to:
a. Offering: Recruiting and Candidate Experience
b. Functional Area: Recruiting and Candidate Experience Management
c. Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the AI Feature Integration section and click Edit.
3. Select the Recommended Skills option.
4. Click Save.

---

## Public Skills Content Section
*Chunk ID: OHR-REC-0965 | Chapter: Recruiting Activity Center*

You can add Skills Center as a subscriber to a skill content section, which makes the section a Public Skills content
section.
Any skill that’s added or updated in a Public Skills content section reflects in various pages in the Recruiting application
and career sites in these scenarios:
• When a candidate adds or updates a public skill while applying for a job in external or internal career sites, the
recruiter can view the updated skills in the Public Skills content section of the job application. Based on this
new skill, the recruiter can also filter job applications from the Advanced Filters page, if you’ve enabled Oracle
Search for job applications. The updated skill also appears in the Skills Center page after the candidate converts
to an employee.
• When a candidate becomes an employee and adds or updates a public skill in Skills Center, the skill appears in
the content section of the candidate’s profile. The recruiter can also search for the candidate based on the new
skill.
• When a recruiter adds or updates a skill in the Public Skills content section of a candidate’s job application, and
the candidate becomes an employee, the skill appears in the employee’s Skills Center page and in Connections.
• When a recruiter adds or updates a skill in a Public Skills content section of a job requisition (which can be done
in the details page of the requisition), it appears on the job details page in external and internal career sites and

in the Agency portal. Note that only the skill name appears in these three areas, but not other skill attributes
such as comments or skill description.
The table presents the configurations that are recommended and supported:

---

## You don't have a Public
*Chunk ID: OHR-REC-0966 | Chapter: Recruiting Activity Center*

Skills content section set
up in Person Profile, but
you have other skill content
sections set up. You want
to add Recruiting as a
subscriber to one or more
of these content sections.

---

## Since you don’t use Skills
*Chunk ID: OHR-REC-0967 | Chapter: Recruiting Activity Center*

Center, you can add
Recruiting as a subscriber
to one or more skill content
sections.

Yes

Yes

No

---

## You have only one Public
*Chunk ID: OHR-REC-0968 | Chapter: Recruiting Activity Center*

Skills content section set
up in Person Profile. You
want to add both Skills
Center and Recruiting as
subscribers to the Public
Skills content section.

---

## You have a Public Skills
*Chunk ID: OHR-REC-0969 | Chapter: Recruiting Activity Center*

content section set up in
Person Profile. You also
have other skill content
sections set up. You want
to add Skills Center as a
subscriber to the Public
Skills content section. You
want to add Recruiting as
a subscriber to the Public
Skills content section as
well as to the other skill
content sections.

---

## You have a Public Skills
*Chunk ID: OHR-REC-0970 | Chapter: Recruiting Activity Center*

content section set up in
Person Profile. You also
have other skill content
sections set up. You want
to add Skills Center as a
subscriber to the Public
Skills content section. You
want to add Recruiting as a
subscriber to the other skill
content sections, but not
to the Public Skills content
section.

---

## Configure Public Skills Content Section
*Chunk ID: OHR-REC-0971 | Chapter: Recruiting Activity Center*

You can add Skills Center as a subscriber to a skill content section, which makes the section a Public Skills content
section.

---

## Before you start
*Chunk ID: OHR-REC-0972 | Chapter: Recruiting Activity Center*

• To ensure that a new skill added to a skill content section in a job requisition appears in the job details page
as well as in external and internal career sites, create the skill content section in both the Job Profile Type
configuration and Person Profile configuration pages. Then add Skills Center and Recruiting as subscribers to
this content section, as described earlier.
• While job requisitions can show multiple skill content sections in a Job Profile Type configuration, it's strongly
recommended to use a single skill content section in the Job Profile Type configuration so that a single skill
content section is displayed in requisitions. Also, if you use the Skills Center product, it should subscribe to
this single skill content section in a Job Profile Type configuration. This will help simplify the uptake of future
improvements to skills support related to requisitions.
Here's what to do
1. Go to My Client Groups and click Profiles.
2. On the Profiles page, click Profile Types.
3. On the Profile Types page, click Person.
4. On the Edit Profile Type: Person page, click Add Content Section.
5. Select a template for the content section. You can use these templates:
◦ Certification

◦ Education
◦ Language
◦ Skill
◦ Work History
◦ Work Preferences (multiple sections isn't supported)
6. On the Add Content Section page, enter a section name and a description.
7. Select the Active option.
8. In the Content Section Properties section, set the Skill Level field to Hide.
You can decide which other attributes you want to display or hide as per your business needs.
The Skill Level field in a skill content section isn't supported in Recruiting. Enabling it is an invalid configuration and
can’t be used in Candidate Experience job application flows. The configuration of rules using Transaction Design
Studio overrides the administrative setup here in Profiles. When you configure the field visibility in Transaction
Design Studio, it’s applied to all skill content sections. Therefore, if you configure a field such as Skill Level to be
visible in Transaction Design Studio, it becomes an invalid configuration when the same field isn’t configured in a
content section.
9. Scroll down to the Subscriber section and select Recruiting and Skills Center to add them as subscribers to this
content section.
10. Click Save and Close.

---

# Opportunity Marketplace

## Opportunity Marketplace
*Chunk ID: OHR-REC-0973 | Chapter: Opportunity Marketplace*

What Is Opportunity Marketplace
Opportunity Marketplace allows organizations, and employees (internal candidates) to connect to ensure that
organizations are getting the most out of their talent. It also gives employees the ability to work on stretch assignments
to help them leverage and grow their skills, and to grow their network.
Jobs are long term opportunities that can be offered to employees or external candidates. Gigs are intended for
employees only. They're short term opportunities that use the skills and talents that employees might be using during
their day-to-day job. For example, perhaps your team needs someone for a short period of time to create a web page.
Gigs help employees improve the skills they already have, or gain skills they want to have.
Within Opportunity Marketplace there are:
• Creators - Employees who create gigs or internal jobs. These users can create opportunities, update them,
review candidate applications, assign candidates to opportunities, and close the opportunities.
• Seekers – Employees or external candidates who search for opportunities (gigs or jobs). They can browse and
search Opportunity Marketplace for gigs or jobs, view details for various opportunities, bookmark them, and
apply for them.
As a creator you:
• Create jobs and gigs.
• Post jobs and gigs.
• Receive candidate applications.
• Review candidate applications.
• Assign candidates to jobs and gigs.
• Close jobs and gigs.
Seekers:
• Search for jobs and gigs and save their searches.
• Review jobs and gigs.
• Bookmark jobs and gigs.
• Apply for jobs and gigs.
• View their candidate application statuses.
Job seekers can access Opportunity Marketplace from Me > Quick Actions > Show More > Opportunity Marketplace. On
the Opportunity Marketplace landing page, job seekers can see either jobs, gigs, or both, depending on what's enabled
for their organization. Jobs and gigs are listed as:
• Recommended - Displays jobs and gigs matching the user's preferences like job type and location, recently
applied gigs or jobs, and jobs recently added to favorite jobs. The recommendations will show on the top of the
list.
• Trending - Displays active, internally posted jobs or gigs that the user applied to or added to favorites by
other seekers in the last three weeks. Trending displays only if the currently logged-in seeker has indicated

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-0974 | Chapter: Opportunity Marketplace*

a preferred job location for their job alerts, the job or gig's primary location matches the seeker's location
preference, and if the seeker hasn't yet applied to the job or gig.
• Favorites - Displays jobs and gigs shortlisted by the user when they bookmark them as their favorite. Users can
remove these from favorites at any time.
Note: When you enable gigs, users will see a splash screen the first time they sign in to Opportunity Marketplace.
Once they save their preferences, this splash screen doesn't display again.

---

## Enable Opportunity Marketplace
*Chunk ID: OHR-REC-0975 | Chapter: Opportunity Marketplace*

Set up Opportunity Marketplace to give employees and external candidates a place to easily search for new job or gig
opportunities.
For details see How do I set up Opportunity Marketplace?

---

## Hide the Current Jobs Menu Under Me
*Chunk ID: OHR-REC-0976 | Chapter: Opportunity Marketplace*

When Opportunity Marketplace is enabled, you can optionally hide the Current Jobs menu under Me for users who have
Opportunity Marketplace Seeker privileges.
Hiding the Current Jobs menu means that users will only be able to use Opportunity Marketplace to search for internal
jobs.
1. Access the Me section in structure configurations, and find the configuration for Current Jobs navigation.
2. Edit the current job navigation entry, and select the EL Expression option under the Show on Springboard field.
3. Edit the EL expression and include the following text:

#{Offerings.isFeatureEnabledForImplementation.ORA_IRC_RCE and!
((securityContext.userGrantedPermission['permissionClass=oracle.adf.share.security.authorization.MethodPermission;targ
action=invoke']) and(Profile.values.ORA_HCM_OPP_MARKET_PLACE_JOBS eq 'Y')) }

4. Save and close the edited navigation entry.

---

## Configure Job Segmentation
*Chunk ID: OHR-REC-0977 | Chapter: Opportunity Marketplace*

Use job segmentation configurations to control which internal users and employees can see specific jobs in the list of
job requisitions in Opportunity Marketplace.
Using job segmentation you can:
• Create an eligibility profile to categorize the group of internal employees for whom the visibility of the jobs
needs to be restricted.
• Create job segmentation configurations to filter the jobs for which you need to control the visibility.
• Assign the eligibility profiles to the created job configurations.

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-0978 | Chapter: Opportunity Marketplace*

• Activate and deactivate the configurations as needed.
• Enable or disable the job segmentation configurations overall for your corporation as needed.

---

## Enable the Profile Options
*Chunk ID: OHR-REC-0979 | Chapter: Opportunity Marketplace*

Before you begin, enable the Job Configurations profile option via the following profile option under Recruiting
application in the Manage Administrator Profile Values task.
• Name: Opportunity Marketplace Job Configurations Enabled
• Code : ORA_HCM_OPP_MKT_JOB_CONFIG_ENABLED
To create job segmentation configurations you must also have the following privileges:
• BEN_MANAGE_BENEFIT_ELIGIBLITY_PROFILE_PRIV – This privilege allows users to create new eligibility
profiles for opportunity marketplace usage.
• BEN_REST_SERVICE_ACCESS_BENEFITS_LOVS_PRIV – This privilege allows users to select the Opportunity
Marketplace eligibility profiles while creating job configurations.

---

## Create Opportunity Marketplace Eligibility Profiles
*Chunk ID: OHR-REC-0980 | Chapter: Opportunity Marketplace*

Create eligibility profiles to group employees.
1. In the Setup and Maintenance Area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience Management
◦ Task: Select All Tasks from the Show drop-down list
2. Select Opportunity Marketplace Eligibility Profiles.
3. Click Create > Create Participant Profile.
4. Enter the appropriate information to create the Eligibility Profile Definition and Eligibility Criteria.
Note: Select Opportunity Marketplace from the Profile Usage drop-down list if it is not already selected.

---

## Create Opportunity Marketplace Jobs Configurations
*Chunk ID: OHR-REC-0981 | Chapter: Opportunity Marketplace*

Create Opportunity Marketplace jobs configurations so that you can link them to eligibility profiles.
1. In the Setup and Maintenance Area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience Management
◦ Task: Select All Tasks from the Show drop-down list

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-0982 | Chapter: Opportunity Marketplace*

2. Scroll down and select Opportunity Marketplace Jobs Configurations. This page lists all the active and draft
configurations defined so far. The configurations are listed in the order of priority.
Note: When a user logs in, the first active configuration that matches their eligibility profile is applied
to them. Only the matching requisitions from that job configuration are displayed in the Opportunity
Marketplace dashboard.

3.
4.
5.
6.
7.
8.

---

## You can create new job configurations and select the filters for the job requisitions that fall under that
*Chunk ID: OHR-REC-0983 | Chapter: Opportunity Marketplace*

job configurations. You can also map this jobs configuration against a specific eligibility profile of usage
opportunity marketplace.
Click Create.
Enter a configuration code.
Type a configuration name.
Select the eligibility profile. Only one Opportunity Marketplace eligibility profile can be mapped against a jobs
configuration.
Add the appropriate requisition filters.
Click Save and Close.

Related Topics
• How Eligibility Works With Other Objects

---

## Configure Job Alerts for Opportunity Marketplace
*Chunk ID: OHR-REC-0984 | Chapter: Opportunity Marketplace*

Configure periodic alerts that recommend available opportunities to internal candidates. These alerts match the
preferences set by internal candidates.
Job alerts are prioritized in the following order:
1. Explicit preferences selected on the Update Interest page.
2. Recently applied to and jobs added to favorites.
3. Employees' current job ID and location.
Within the Update Interest page preferences bucket, job ID and job family are given the highest priority. The threshold
is implemented in such a way that if a job matches only the location, organization, or skill, or a combination of these,
then the job won't be recommended. For a job to be recommended to a user, the job must match the job ID or the job
family preference. If the job ID or job family matches, then the other parameters come into play to boost the matches.
This means that a job matching both the job ID and location preference will be ranked higher than the job matching only
the job ID preference. A job matching only the location alone won't be recommended at all.
Watch video

1. Configure the Frequency of Opportunity Marketplace Email Notifications.
2. Configure the Opportunity Marketplace Email Template and make sure that the email template is active.
3. Ensure the following scheduled processes are scheduled and running successfully. The recommended frequency is 30
minutes.

◦ Send Campaign Email
◦ Prepare Campaign Email

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-0985 | Chapter: Opportunity Marketplace*

4. Make sure internal candidates have set their preferences. If a job requisition matches the candidate's primary or other
work location preferences, they'll receive an alert.
5. Verify with your internal candidates that they're receiving the email based on the frequency set for an internal job
posted matching the preference.
Note: The translation used in the body of the notification is based on the language preference settings for the
user who's running and scheduling the scheduled process, and not the user receiving the notification.

Related Topics
• Job Alert for New Job Opportunities

---

## Configure Manager Approval for Gigs
*Chunk ID: OHR-REC-0986 | Chapter: Opportunity Marketplace*

In Opportunity Marketplace, you can add an approval step to the application process to require manager approval
before employees can work on gigs. Once the approval process is set up, gig applications are automatically routed to
managers for approval when a gig creator assigns a gig to an applicant.
For gig creators, a gig application status is set to Pending for Approval until it's either approved or rejected by an
applicant's manager. You can't assign a gig to another person until a manager rejects the assigned employee's
application.
For gig seekers, gigs display with a status of Pending for Approval on their dashboards to let them know that they're
awaiting manager approval.
Managers approve or reject gig by clicking Approve and Reject buttons in either:
• Email notification
• Bell notification (Alerts Icon)
Once managers approve or reject a gig request, both gig creators and seekers are notified.
If a gig is canceled before the approval from line manager, then the Approve and Reject buttons won't be clickable.
1. Go to the Tools work area.
2. Click Transaction Console.
3. Click the Approval Rules tab.
4. Select the Approve Gig Assignation process and click the Edit icon.
5. Clear the Bypass Approvals check box to indicate that gig applications should go through approval process. If you
select Bypass Approvals, then gig applications will not go to the manager approval process when the gig is assigned
by the gig manager to the gig applicant.

---

## Notifications for Gigs
*Chunk ID: OHR-REC-0987 | Chapter: Opportunity Marketplace*

Notifications are sent when gigs are assigned to gig seekers.

Gig notifications are sent via email and the worklist application (bell icon notifications).
Here are the rules which govern which notification is sent. The notifications are available in Recruiting Content Library.
Scenario

---

## Notification sent to a gig seeker's manager
*Chunk ID: OHR-REC-0988 | Chapter: Opportunity Marketplace*

approval flow is enabled, the seeker's manager

requesting their approval to allow the gig

receives an approval request.

seeker to accept the gig assignment.

---

## A gig that a user was assigned to is canceled by
*Chunk ID: OHR-REC-0989 | Chapter: Opportunity Marketplace*

ORA_OM_GIG_CANCELED

Notification sent when a gig is canceled.

ORA_OM_GIG_NOT_APPROVED

---

## Notification sent to a gig seeker when a
*Chunk ID: OHR-REC-0990 | Chapter: Opportunity Marketplace*

the gig creator.
A gig seeker's manager rejects the gig
assignment.
A gig seeker isn't selected for a gig, and the gig

manager rejects a gig assignment.
ORA_OM_GIG_NOT_SELECTED

they applied to is completed.

---

## Notification sent when a gig seeker isn't
*Chunk ID: OHR-REC-0991 | Chapter: Opportunity Marketplace*

selected for a gig and the gig they applied to is
completed.

Related Topics
• Recruiting Content Library

---

## Enable Skills Advisor for Gigs
*Chunk ID: OHR-REC-0992 | Chapter: Opportunity Marketplace*

If you have set up Dynamic Skills, you can enable skills advisor for gigs so that gig creators can associate skills related to
a gig.
Skills advisor for gigs:
• Provides AI recommendations for skills that are related to gig titles and descriptions, which you can then add as
you create gigs.
• Helps attract gig seekers who are interested in those relevant skills so that they can apply to a gig, grow their
skill set, or further develop and attain skills they'd like to have.
• Utilizes location and skills as part of a matching algorithm to recommend gigs for the employees through the
Opportunity Marketplace dashboard.
Before you start
Enable Skills Center for Dynamic Skills
Here's what to do
1. Set Up the Skill Content Section for Person Profiles
2. Set Up the Skill Content Section for Job and Position Profiles
3. Enable the Use of AI Suggestions
4. Set Up Skills Recommendation for Gigs Profile Option

---

## Set Up the Skill Content Section for Person Profiles
*Chunk ID: OHR-REC-0993 | Chapter: Opportunity Marketplace*

You create a new content section using the Skill template to capture Skills Center skills or convert an existing Skills
content section for Skills Center use.
1. Navigate to My Client Groups > Profiles > Profile Types > Person.
2. To make the content section available for Skills Center, select Skills Center as a subscriber.
Either Skills Center or Talent Profile can subscribe to a Skill Content section.
◦ If Skills Center is the subscriber, it appears only in Skills Center. The Skills Center can subscribe to only one
Skill content section. After you start adding skills to the content section, you can't cancel the Skills Center
subscription to the content section.
◦ If Talent Profile is the subscriber, the skills content is available only in the Skills and Qualifications page.
3. If you're using specific applications to integrate with Skills Center as a subscriber for the content section, select
subscribers such as Learning Outcomes and Career Development.
4. If you want to enable the usage of skill levels on skills, associate a rating model to the Skill Level attribute and make
sure that the attribute isn’t hidden.
You can turn off skill levels later by hiding the attribute in the content section. You can create and use an N-level
rating model as long as it has numerically increasing level values. The level ID with the highest numeric value is
considered as the highest rating, and the level ID with the lowest numeric value is the lowest rating. The rating level
ID can only go up to 9. It is set to Unspecified until the skill level is assigned. You can’t change the rating model used
in a Skills Center content section once you start adding skills in the content section.

---

## Set Up the Skill Content Section for Job and Position Profiles
*Chunk ID: OHR-REC-0994 | Chapter: Opportunity Marketplace*

You can add the Skills Center content section to the job and position profile type the same way as you would add any
other content section. It will enable the content section to define skill requirements for a job and other tasks such as
creating learning item prerequisites.
Skills Advisor can be enabled for use in Job Profiles by enabling the profile option ORA_HRT_AI_SKILLS_ASSISTANT.
When the profile option is created, you need to enable it at the Site level.
Related Topics
• Create and Edit Profile Options

---

## Enable the Use of AI Suggestions
*Chunk ID: OHR-REC-0995 | Chapter: Opportunity Marketplace*

You perform these steps to ensure that the AI skill suggestions are presented accurately to users.
Before you start
You must have the HRT_VIEW_SKILL_RECOMMENDATIONS_PRIV privilege to display AI skill suggestions on the Skills
Center page.

---

## Note: The ORA_PER_EMPLOYEE_ABSTRACT role is shipped with the HRT_VIEW_SKILL_RECOMMENDATIONS_PRIV
*Chunk ID: OHR-REC-0996 | Chapter: Opportunity Marketplace*

privilege. If you don’t want certain users to access AI suggestions, make sure that they don’t have the
HRT_VIEW_SKILL_RECOMMENDATIONS_PRIV privilege.

Here's what to do
1. Create a custom role based on the ORA_PER_EMPLOYEE_ABSTRACT role.
2. Remove the HRT_VIEW_SKILL_RECOMMENDATIONS_PRIV privilege in this role.
3. Assign the new custom role to those specific users who shouldn’t view the AI suggestions.
Oracle recommends that your users have a job association to get the best skill suggestions. An HR Specialist can:
a. Navigate to My Client Groups > Person Management.
b. Search and edit the configuration for the user.
Related Topics
• Set Up Security for Skills Center

---

## Set Up Skills Recommendation for Gigs Profile Option
*Chunk ID: OHR-REC-0997 | Chapter: Opportunity Marketplace*

You need to enable the profile option ORA_IRC_AI_GIG_SKILL_RECOMMENDATIONS to enable Skills Advisor in the gig
creation page, in Opportunity Marketplace.
1. In the Setup and Maintenance work area, click the Tasks icon.
2. Click Search.
3. Search for the task Manage Administrator Profile Values.
4. Click the task name.
5. On the Manage Administrator Profile Values page, search for the profile option code
ORA_IRC_AI_GIG_SKILL_RECOMMENDATIONS.
6. In the Profile Values section, set the Profile Level field to Site.
7. Set the Profile Value field to Y.
8. Click Save and Close

---

## Display Custom Content in a Content Card
*Chunk ID: OHR-REC-0998 | Chapter: Opportunity Marketplace*

You can display custom content in a content card on the Opportunity Marketplace home page. The content card
presents content in the form of a guided journey providing guidance to users such as welcome videos, promotional
videos about the company, links to company policies, tutorials, and so on.
By default, no content card is displayed. To enable this feature, your administrator needs to:

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-0999 | Chapter: Opportunity Marketplace*

1. Enable the profile option ORA_PER_GUIDED_JOURNEYS_ENABLED.
a. Click Search.
b. Search for the task Manage Administrator Profile Values.
c. On the Manage Administrator Profile Values page, search for the profile option code
ORA_PER_GUIDED_JOURNEYS_ENABLED.
d. Set the profile value at the Site level to Y.
e. Click Save and Close.
2. Create a guided journey using a checklist template.
The checklist template is used to configure the data displayed in the content card. You need the function privilege
Manage Journey (PER_MANAGE_CHECKLIST_TEMPLATE_PRIV) to work on checklist templates.
a.
b.
c.
d.
e.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Checklist Templates.
On the Checklist Templates page, click the Create button.
On the Create Checklist window, enter a name and code for the checklist. Select the Guided Journey
category. Complete the other fields as needed.
f. Click OK.

3. Use business rules in Visual Builder Studio to display the content card on the home page.
Related Topics
• Overview of Guided Journeys
• Overview of Redwood Application Extension

---

## Configure Gig Segmentation
*Chunk ID: OHR-REC-1000 | Chapter: Opportunity Marketplace*

Use gig segmentation configurations to control which employees can see specific gigs in Opportunity Marketplace.
When a user logs in, the first active configuration that matches their eligibility profile is applied to them. Only the
matching requisitions from that gig configuration are displayed in the Opportunity Marketplace dashboard.
Before you start
For creating job segmentation configurations, you must have the following privileges:
• BEN_MANAGE_BENEFIT_ELIGIBLITY_PROFILE_PRIV – This privilege allows users to create eligibility profiles for
opportunity marketplace usage.
• BEN_REST_SERVICE_ACCESS_BENEFITS_LOVS_PRIV – This privilege allows users to select the Opportunity
Marketplace eligibility profiles while creating job configurations.
To enable and use this feature you need to:
1. Enable a profile option.
2. Create eligibility profiles (if you haven't already done so).
3. Create gig configurations by linking to eligibility profiles.

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-1001 | Chapter: Opportunity Marketplace*

Note: If you've already set up active gig configurations then, upon enabling the profile option for gig configurations,
the gigs will be restricted to users based on their eligibility profiles that match the available gig configurations.

---

## Enable Profile Option
*Chunk ID: OHR-REC-1002 | Chapter: Opportunity Marketplace*

Enable the ORA_HCM_OPP_MKT_GIG_CONFIG_ENABLED profile option. By default, the profile option is set to N,
meaning the feature is disabled by default.
To enable the profile option:
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
On the Search page, search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
ORA_HCM_OPP_MKT_GIG_CONFIG_ENABLED.
6. In the Profile Values section, set the profile value to Y.
7. Click Save and Close.

---

## Create Eligibility Profiles
*Chunk ID: OHR-REC-1003 | Chapter: Opportunity Marketplace*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience Management
◦ Task: Select All Tasks from the Show drop-down list, or search for "gig" from the Search Tasks field.

2.
3.
4.
5.
6.

Select the Opportunity Marketplace Eligibility Profiles task.
Click Create.
Enter the appropriate information to create the Eligibility Profile Definition and Eligibility Criteria.
Select Opportunity Marketplace from the Profile Usage drop-down list if it's not already selected.
Click Save and Close.

---

## Create Gig Configurations by Linking to Eligibility Profiles
*Chunk ID: OHR-REC-1004 | Chapter: Opportunity Marketplace*

You can create gig configurations and link them to eligibility profiles. You can select the filters for the gig requisitions
that fall within that gig configuration.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Experience Management
◦ Task: Select All Tasks from the Show drop-down list, or search for "gig" from the Search Tasks field.

2.
3.
4.
5.
6.

Click Opportunity Marketplace Gigs Configurations.
Click Create.
Enter a configuration code.
Type a configuration name.
Select an eligibility profile.
Note: Only one Opportunity Marketplace eligibility profile can be mapped against a gig configuration.

7. Add the appropriate requisition filters.

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-1005 | Chapter: Opportunity Marketplace*

8. Click Save and Close.
Related Topics
• How Eligibility Works With Other Objects

---

## Configure Descriptive Flexfields as Search Filters and
*Chunk ID: OHR-REC-1006 | Chapter: Opportunity Marketplace*

Facets
Configure descriptive flexfields as filters and facets so that candidates can use them to browse jobs in Opportunity
Marketplace.
To use this feature you must enable the flexfields you want for Opportunity Marketplace.
1. Create the flexfields you want to use.
2. Navigate to Manage Search Indexes page and select the flexfields for ingestion.
3. Run ingestion Job called “ESS Job to create index definition and perform initial ingest to OSCS”. This ensures that
all jobs and gigs that already exist in the application are fully indexed for search. Specify “fa-hcm-requisition” in the
Index Name to Reingest field.
4. Once ingested successfully, Navigate to Search Views in the Quick Actions menu, and click My Client Groups >
Search More > Search Views.
5. Select Opportunity Marketplace Jobs View.
6. Click the Filters tab.
7. Scroll down if needed to see the flexfields.
8. Select the fields you want to use.
9. Indicate whether you want to display them as filters or facets (or both).
Related Topics
• Overview of Flexfields

---

## Configure Descriptive Flexfields as Filters and Facets
*Chunk ID: OHR-REC-1007 | Chapter: Opportunity Marketplace*

You can also configure descriptive flexfields as filters and facets so users can use them to browse gigs in Opportunity
Marketplace.
Before you start
• To access the Search Views page, you must have the following privilege: HRC_MANAGE_SEARCH_VIEWS_PRIV.
• To use advanced search filters on the Opportunity Marketplace Jobs page, you must have the following
privilege HRC_ACCESS_HCM_COMMON_COMPONENTS_PRIV.
This feature provides another ways for gig creators to capture data and for gig applicants to search for gigs.

---

## Opportunity Marketplace
*Chunk ID: OHR-REC-1008 | Chapter: Opportunity Marketplace*

Here's what to do
1. Create the flexfields you want to use.
2. Run the ingestion job called “ESS Job to create index definition and perform initial ingest to OSCS”. This ensures that
all jobs and gigs that already exist in the application are fully indexed for search. Specify “fa-hcm-requisition” in the
Index Name to Reingest field.
3. Navigate to My Client Groups > Quick Actions > View More > Search Views.
4. Select Opportunity Marketplace Gigs View.
5. Click the Filters tab, and scroll down if needed to see the flexfields.
6. Indicate whether you want to display them as filters or facets (or both).
7. Click Save and Close.
The following validation types are supported for the gig descriptive flexfields:

◦ Gig Create/Edit and Details page: Format only, Independent and Table
◦ Gig Filters and Facets: Independent and Table
◦ Gig VBStudio Customization: Format Only, Independent, Table
Related Topics
• Overview of Flexfields

---

# Lookups

## Configure Career Roles and Career Paths
*Chunk ID: OHR-REC-1009 | Chapter: Lookups*

When you set up career roles and career paths, employees can search and browse through them using the Career Roles
and Career Paths facets. They can also view the career paths defined for a role from the career role details page.
Complete the following tasks to set them up in Opportunity Marketplace:
• Enable Career Roles in Opportunity Marketplace
• Display Career Roles Based on Jobs, Positions, or Both
• Display Jobs in Career Roles
• Display Role Guides for Career Roles
• Configure Career Role Recommendations
• Configure Career Role Filters Using Search Views
• Configure Career Paths in Opportunity Marketplace

Recruiting Lookups
Lookups are lists of values in applications. You use lookups to provide validation or a list of values for a user input field
in a user interface.
You can use these tasks in the Setup and Maintenance work area to manage lookups for Oracle Fusion Cloud Recruiting:
• Recruiting and Candidate Experience Lookups
• Manage Common Lookups
You can update lookups that have an extensible configuration level to suit your organization's requirements.
The lookup type name for Oracle Recruiting all start with ORA_IRC.
Here are a few examples.

Task

---

## List of block usage
*Chunk ID: OHR-REC-1010 | Chapter: Lookups*

values.

System

ORA_INTERNAL

Internal

ORA_EXTERNAL

External

ORA_BOTH

Both

ORA_REC_CAMPAIGN

---

## On call job
*Chunk ID: OHR-REC-1011 | Chapter: Lookups*

ORA_ACTIVE

Active

ORA_INACTIVE

Inactive

ORA_DRAFT

Draft

ORA_CAMPUS

Campus

ORA_CONTINGENT

Contingent

ORA_EXECUTIVES

Executive

ORA_HOURLY

Hourly

---

# Geography Hierarchies

## Lookup Code
*Chunk ID: OHR-REC-1012 | Chapter: Geography Hierarchies*

Description

ORA_PROFESSIONAL

Professional

Related Topics
• Overview of Lookups

Using Geography Hierarchies and Geography Hierarchy
Structure
A geography hierarchy is a business object that defines a limited universe of geographies, organized in parent-child
relationships.
Oracle Fusion Cloud Recruiting uses geographies managed in HCM, which typically exist in large numbers. To simplify
the use of geographies, two additional configurations related to geographies are available:
• Geography Hierarchy Structure
• Geography Hierarchies

---

## Geography Hierarchy Structure
*Chunk ID: OHR-REC-1013 | Chapter: Geography Hierarchies*

The geography hierarchy structure defines the structure of geography levels from which a geography hierarchy can be
built. It also defines the geography levels to be used when searching using locations in areas such as job search and
candidate search.
The configuration of the geography hierarchy structure is done in the Setup and Maintenance work area, using the
Geography Hierarchy Structure task.
The Geography Hierarchy Structure page lists the current structure for all countries available within the master
geography hierarchy. If a new country is added to the master geography hierarchy, it's automatically displayed on the
Geography Hierarchy Structure page.
A geography hierarchy structure can have a maximum of three levels. The topmost level represents the country. For
each country, a maximum of two geography sublevels can be defined:
• Level 1
• Level 2
It's not necessary to define sublevels for a country. You can define one sublevel, two sublevels, or none. If a hierarchy
structure isn't defined for a country, the list of locations presented to candidates when they search for a job in the career
site only includes the country with no sublevels. Also, it's not possible to add geographies other than the country in a
geography hierarchy.
The table presents the default geography hierarchy structure for the United States and Canada. Customers must define
the structure for all other countries.

Country

---

## Level 2
*Chunk ID: OHR-REC-1014 | Chapter: Geography Hierarchies*

Note: As a best practice, your Geography Hierarchy should include only those locations where hiring activities occur,
such as cities with physical offices. Including only relevant locations helps recruiters and managers to more easily
select the desired locations when performing recruiting tasks.
To improve the performance of the search in the geography, you can enable the profile option
ORA_PER_ORACLE_SEARCH_LOCATIONSLOV_ENABLED. When you set the profile option to Y, you need to create a
new index "fa-hcm-irc-geography-nodes" by running the scheduled process called ESS job to create index definition
and perform initial ingest to OSCS, with the value fa-hcm-irc-geography-nodes in the Index Name to Reingest field.

---

## Edit a Geography Hierarchy Structure
*Chunk ID: OHR-REC-1015 | Chapter: Geography Hierarchies*

You edit the geography hierarchy structure using the Geography Hierarchy Structure task in the Setup and Maintenance
work area.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Geography Hierarchy Structure

2. On the Geography Hierarchy Structure page, click a country name.
3. In the Geography Hierarchy Structure window, select a value for Level 1 and Level 2.
4. Click OK.
Results:
For some countries, the Not Available value can appear for Level 1 and Level 2. This means that the structure for this
country wasn't defined within the master geography hierarchy. It's also possible that a value appears for Level 1, but
Level 2 displays the Not Available value. This means that the structure for this country only includes one level within the
master geography hierarchy.

---

## Deactivate Countries in a Geography Hierarchy Structure
*Chunk ID: OHR-REC-1016 | Chapter: Geography Hierarchies*

You can deactivate countries in the geography hierarchy structure to prevent those countries from being available
throughout Recruiting.
Deactivating countries from the geography hierarchy structure prevents these countries from being used in geography
hierarchies, but also removes these countries from areas defining available geographies based on the geography
hierarchy structure directly.
When you deactivate a country, you can activate it again to add it back to the geography structure. Changes you make
to the countries of a geography hierarchy structure don’t impact the currently active geography hierarchy; inactive

---

## Geography Hierarchies
*Chunk ID: OHR-REC-1017 | Chapter: Geography Hierarchies*

countries remain available in the current geography hierarchy. However, you won't be able to activate a new geography
hierarchy which contains inactive countries.
When you deactivate countries, you should activate a new geography hierarchy to avoid having inactive countries in
the current geography hierarchy. Otherwise, there could be situations where candidates would experience inconsistent
behaviors where they search for jobs using locations which will never return any results.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Geography Hierarchy Structure

2. On the Geography Hierarchy Structure page, click a country name.
The Geography Hierarchy Structure window opens. The currently selected levels are displayed, if any
3. On the Geography Hierarchy Structure window, set the status to Inactive.
4. Click OK.
5. Click Save and Close.

---

## Geography Hierarchy
*Chunk ID: OHR-REC-1018 | Chapter: Geography Hierarchies*

A geography hierarchy represents a universe of locations.
Recruiters typically hire candidates in the same areas and therefore post job requisitions in the same set of locations. To
facilitate the selection of the appropriate locations when recruiters create job requisitions, the Recruiting Administrator
can define a geography hierarchy.
To create a geography hierarchy, in the Setup and Maintenance work area, go to:
• Offering: Recruiting and Candidate Experience
• Functional Area: Recruiting and Candidate Experience Management
• Task: Geography Hierarchies
The Geography Hierarchies page lists the geography hierarchies that were created. The geography names are displayed
in the user's session language. For example, Spanish is installed in the environment. If you sign in Spanish, you can view
geographies in Spanish. Several geography hierarchies can be created but only one geography hierarchy can be current
at any given time. You can create, duplicate, edit, and delete geography hierarchies.
A geography hierarchy is composed of a list of countries where geographies are added, following the geography
hierarchy structure defined for each country. For example, if for United States, the structure is United States > State >
City, the geography hierarchy could contain:
• United States > California
• United States > California > San Francisco
• United States > Florida
• United States > Florida > Miami
A geography hierarchy can have one of the following statuses:
• Draft: The geography hierarchy can be edited and activated when ready.

---

## Geography Hierarchies
*Chunk ID: OHR-REC-1019 | Chapter: Geography Hierarchies*

• Current: The geography hierarchy is being used and cannot be edited. Only one geography hierarchy can be
current at any given time.
• Future: The geography hierarchy is scheduled to be used at a later time. It can be edited.
• Ended: The geography hierarchy was used in the past and has been replaced by another one. It cannot be
edited.
Geography hierarchies are used in the following recruiting functionality:
• Job requisition and job requisition template: When recruiters select the Primary Location and Other Locations
of a job requisition or job requisition template, only values from the currently active geography hierarchy can be
selected.

---

## Create a Geography Hierarchy
*Chunk ID: OHR-REC-1020 | Chapter: Geography Hierarchies*

You create a geography hierarchy to ease the selection of the appropriate locations when hiring managers and
recruiters create job requisitions.
Before you start
As a best practice, only add locations where your company has physical offices. This will help hiring managers and
recruiters find the appropriate locations. It will also prevent performance issues.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Geography Hierarchies
2. On the Geography Hierarchies page, click the Create icon.
3. On the Create Geography Hierarchy, provide a name for the geography hierarchy.
4. Enter the start date when the geography hierarchy will be available for use.
If you select the option Start on Activation, the geography hierarchy becomes available as soon as it's made active.
5. To add a country to the geography hierarchy:
a. In the Geography Hierarchy section, click the Plus icon.
b. In the Add Country window, search for the country you want to add, select it, and add it to the list of
selected countries using the arrow.
c. Click OK.
You can select many countries at once by selecting a country and holding the Shift or Ctrl key while you select other
countries.
6. To add geographies to a country:
a. In the Geography Hierarchy section, select the country and click the Add Sublevels button.
b. In the Add Sublevels window, search for the geography you want to add, select it, and add it to the list of
selected items using the arrow.
c. Click OK.
You can select many geographies at once by selecting the geography name and holding the Shift or Ctrl key while
you select other geographies. Use the Show filter to filter down the list of geographies to only show Level 1 or Level 2
geographies.

---

## Displaying the Correct Location Filter Values in
*Chunk ID: OHR-REC-1021 | Chapter: Geography Hierarchies*

Candidate Search
Consider this info to ensure the Location filter is showing the correct locations.
• When the geography hierarchy structure of a country is modified, run the Load and Index Master Geography
Hierarchy scheduled process for that country.
• When you define the geography hierarchy structure of a country, don't use postal code. Postal codes aren't
supported in Oracle Fusion Cloud Recruiting.
• The Location filter can't work without the Level 2 or StateCode field populated in Core HR. The TownOrCity
field in the Core-HR table is read only when the StateCode field is populated. No location will be indexed
for candidates that don't have a State populated in the Address section of their profile. This means that the
Location filter won't be available in Candidate Search.
Example: The Saudi Arabia location isn't displayed in the Location filter. The customer's system was configured to work
on Tax and Reporting Address format. Here's how to fix the issue.
1. Define the geography validation for Saudi Arabia and set the address style to "Saudi Arabia Tax and Reporting
Address Format".
2. Create the correct mapping (governorate to city, and regions to state).
3. Run the Load and Index Master Geography Hierarchy scheduled process.
4. Create a candidate or edit an existing one.
5. Add the address of the candidate (state and city).
6. Run the Maintain Candidates and Job Requisitions for Search scheduled process.
7. The Location filter now displays the Saudi Arabia location.

---

## Optimize Obsolete Geography Hierarchies
*Chunk ID: OHR-REC-1022 | Chapter: Geography Hierarchies*

You can optimize your geography hierarchies.
This feature isn't intended for unauthorized use by customers. Instead, it's a specialized tool that should only be used
when recommended by the Oracle Support team in specific circumstances. The Oracle Support team will guide the
customer on its proper use. Testing in a non production pod will be necessary to validate the desired outcomes are
achieved. This will ensure the feature is used effectively and in the right context to address the customer needs.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Geography Hierarchies

2. On the Geography Hierarchies page, click Optimize Hierarchies.
3. Select one of these options:

---

## Geography Hierarchies
*Chunk ID: OHR-REC-1023 | Chapter: Geography Hierarchies*

◦ Update Objects to Latest Nodes: Use this action to update Recruiting objects using hierarchies, so that
◦

these objects use geography nodes from the active hierarchy instead of nodes from ended hierarchies
when possible. Objects will be updated only if the active hierarchy contains a node referring to the same
geography.
Delete Unused Hierarchies: Use this action to delete hierarchies which aren't used by any objects. These
hierarchies will be deleted. Only hierarchies which are ended (no longer active) and which none of the
geography nodes are referenced by Recruiting objects will be deleted. Draft hierarchies aren't deleted.

Results:
To determine if a Recruiting object uses geography nodes from a hierarchy, the system looks for such nodes in gigs, job
requisitions, and job requisitions from Workforce Modeling. These are the only Recruiting objects keeping references to
geography nodes.

30 Fast Formulas for Recruiting
Overview of Recruiting Fast Formulas
Oracle Fast Formula is a simple way to write formulas using English words and basic mathematical functions. You can
use information from your database in formulas without learning the database structure or a programming language.
In Recruiting, you can create fast formulas for these formula types:
• Recruiting Candidate Selection Process: Fast formulas used as conditions in a candidate selection process.
Conditions are used to determine if an automated action will be done to move job applications.
• Recruiting Job Requisition: Fast formulas used as conditions to automatically unpost job requisitions.
• Recruiting Job Application Computed Field: Fast formulas to calculate computed fields based on the data
collected on job applications.
Fast formulas are created in the Setup and Maintenance work area, using the Fast Formulas task.
Related Topics
• Overview of Using Fast Formulas

---

## Fast Formulas for Candidate Selection Processes
*Chunk ID: OHR-REC-1024 | Chapter: Geography Hierarchies*

You can create fast formulas of the Recruiting Candidate Selection Process formula type and use them as conditions in
a candidate selection process. Conditions are used to determine if an automated action will be performed to move job
applications.
Note: When a job application is moved, the system processes the actions configured on the destination phase or
state before updating the job application status with the new phase and state. For this reason, if within a Fast Formula
associated to an action on the destination phase or state you make use of the job application’s current phase and
state, this will reflect the phase and state the job application was on before moving.
This table presents the areas where fast formulas of the Recruiting Candidate Selection Process type can be used.

---

## Defines a condition that must be met for the
*Chunk ID: OHR-REC-1025 | Chapter: Geography Hierarchies*

action to be executed. The action is executed or
not depending on the formula's return value.

---

## A formula used as a condition on a Move
*Chunk ID: OHR-REC-1026 | Chapter: Geography Hierarchies*

action. The job application is moved only if the
job application is from an internal candidate.

---

## Defines a condition that must be met for a job
*Chunk ID: OHR-REC-1027 | Chapter: Geography Hierarchies*

application to be allowed to move out of its
current state (move to a different state). The job
application can move or not depending on the
formula's return value.

---

## A formula used as a Move Condition on the
*Chunk ID: OHR-REC-1028 | Chapter: Geography Hierarchies*

Offer - Accepted state. Users can move the job
application only if a background check has been
requested and completed.

---

## Fast Formulas for Recruiting
*Chunk ID: OHR-REC-1029 | Chapter: Geography Hierarchies*

The return value of Recruiting Candidate Selection Process formulas must be set in the CONDITION_RESULT variable.
Formulas of the Recruiting Candidate Selection Process type must return a value indicating if the condition is met or
not. Use the following variables in the return statement:
CONDITION_RESULT variable contains the result of the formula, which indicates if the condition is met or not.
• To indicate that the condition is met, the CONDITION_RESULT variable must contain one of the following values
(case insensitive):

◦ y
◦ yes
◦ true
◦ 1
• Any other value will consider the condition as not being met.
CONDITION_MESSAGE is an optional part of the result, it doesn't have to be returned. Maximum size is 255 characters.
• The message is used for logging purposes only.
CONDITION_RESULT = 'N'
CONDITION_MESSAGE = ''
...
return CONDITION_RESULT, CONDITION_MESSAGE

---

## When you create a fast formula of type Recruiting Candidate Selection Process, you can use information related to
*Chunk ID: OHR-REC-1030 | Chapter: Geography Hierarchies*

a specific job application within this formula. For example, the job application itself, the job requisition to which the
candidate applied, assessments initiated for the job application, the prescreening score of the candidate for the job
application.

---

## Sample Formula
*Chunk ID: OHR-REC-1031 | Chapter: Geography Hierarchies*

Here's an example of a fast formula to determine if a candidate is external.
DEFAULT FOR IRC_CSP_JOBAPP_INTERNAL IS 'N'
CONDITION_RESULT = 'N'
...
RESULT = IRC_CSP_JOBAPP_INTERNAL
IF (RESULT = 'N' THEN
CONDITION_RESULT = 'Y'
return CONDITION_RESULT

Here's an example of a fast formula based on assessment result.
DEFAULT_DATA_VALUE FOR IRC_CSP_ASSMNT_PARTNER_NAME IS 'N/A'
DEFAULT_DATA_VALUE FOR IRC_CSP_ASSMNT_PACKAGE_CODE IS 'N/A'
DEFAULT_DATA_VALUE FOR IRC_CSP_ASSMNT_PACKAGE_NAME IS 'N/A'
CONDITION_RESULT = 'Y'
i = 1
WHILE IRC_CSP_ASSMNT+PARTNER+NAME.EXISTS(i) LOOP
(
partner_name = IRC_CSP_ASSMNT_PARTNER_NAME[i]
package_status_code = IRC_CSP_ASSMNT_PACKAGE_CODE[i]
/* ORA_INITIATED, ORA_REQUESTED, ORA_COMPLETED_PASS, ORA_COMPLETED_FAIL */

---

## IF package_status_code != 'ORA_REQUESTED' THEN
*Chunk ID: OHR-REC-1032 | Chapter: Geography Hierarchies*

CONDITION_RESULT = 'N'
i = i + 1
)
return CONDITION_RESULT

Here's an example of a fast formula based on a candidate interview being completed.
CONDITION_RESULT = 'N'
CONDITION_MESSAGE = 'Debug: '
l_interview_operation = get_context(IRC_INTRVW_OPERATION, 'UNDEFINED')
CONDITION_MESSAGE = CONDITION_MESSAGE || l_interview_operation
IF(l_interview_operation = 'INTERVIEW_COMPLETED') THEN
CONDITION_RESULT = 'Y'
return CONDITION_RESULT, CONDITION_MESSAGE

Here's an example of a fast formula to return true if a job application citizenship is Canada and Active. Possible values
for this database item are the country codes defined in the "NATIONALITY" lookup type.
DEFAULT FOR IRC_CSP_CANDIDATE_CITIZENSHIP_LEGISLATION_CODE IS 'N/A'
CONDITION_RESULT = 'N'
IF (IRC_CSP_CITIZENSHIP_LEGISLATION_CODE = 'CA' AND IRC_CSP_CANDIDATE_CITIZENSHIP_STATUS = 'A') THEN
CONDITION_RESULT ='Y',
RETURN CONDITION_RESULT

Contexts
The following contexts are available to the Recruiting Candidate Selection Process formula type:
• SUBMISSION_ID
◦ ID of the job application
• LANGUAGE
◦ Language for which to retrieve multilingual information
For fast formulas used on actions performed as part of the Interview Updated event, additional context information is
available to describe what interview update caused the event to be triggered. The available context information is:
• IRC_INTRVW_SCHEDULE_ID: The ID of the interview schedule related to the interview update.
• IRC_INTRVW_ID: The ID of the interview related to the interview update.
• IRC_INTRVW_REQUEST_ID: The ID of the interview request related to the interview update.
• IRC_INTRVW_OPERATION: The interview operation which triggered the event. The possible values for
IRC_INTRVW_OPERATION are:
◦ INTERVIEW_REQUEST_SENT

◦ INTERVIEW_SCHEDULED
◦ INTERVIEW_CANCELLED
◦ INTERVIEW_RESCHEDULED
◦ INTERVIEW_UPDATED

◦ INTERVIEW_COMPLETED

---

## Database Items
*Chunk ID: OHR-REC-1033 | Chapter: Geography Hierarchies*

Database items related to requisitions, job applications, candidate profiles, interview feedback, assessments,
background checks, tax credits, rehire eligibility, request information flow, prescreening are available for the formula
type Recruiting Candidate Selection Process.
For a complete list of database items, see the spreadsheet Database Items for Oracle Recruiting Cloud Fast Formulas on
My Oracle Support (MOS ID 2723251.1).
Some database items are associated to multilingual values. Multilingual database items will return their value based on
the job application language. If you need to retrieve a value in a specific language, you can change the context of the
formula accordingly:
DEFAULT FOR IRC_CSP_REQ_BUSINESS_UNIT_NAME IS 'NONE'
l_locale = 'US'
CHANGE_CONTEXTS (LANGUAGE= l_locale)
name = IRC_CSP_REQ_BUSINESS_UNIT_NAME

Functions
These functions are available to support more complex calculations.

---

## Determines if a job requisition's
*Chunk ID: OHR-REC-1034 | Chapter: Geography Hierarchies*

locations are at a lower or equal
level of a geography in the
geography hierarchy. For example,
New York location is within the
country US.

---

## Parameter 1: IRC_CSP_REQ_
*Chunk ID: OHR-REC-1035 | Chapter: Geography Hierarchies*

NUMBER: Number of the
requisition. It's not required to use
this database item to provide the
requisition number. As long as a
requisition number is provided.

---

## The formula will return a Y if
*Chunk ID: OHR-REC-1036 | Chapter: Geography Hierarchies*

the geography of the requisition
is the same as the possible
location levels. For example, if a
requisition's geography is Germany
and you call the function with only
the Germany geography (as in the
example below), this will return Y.

---

## Parameters 2 to 11: Possible
*Chunk ID: OHR-REC-1037 | Chapter: Geography Hierarchies*

location levels. Level 1 is always the
Country; the other levels represent
sub-levels. If you don't want to
define the sub-levels, you can use
ANY.
Parameter 12: Y/N if you want to
consider the requisition's other
locations (Y) or only the primary
location (N).
Parameter 13: The locale to use for
loading the location names.

---

## DEFAULT FOR IRC_CSP_REQ_NUMBER IS 'NONE'
*Chunk ID: OHR-REC-1038 | Chapter: Geography Hierarchies*

CONDITION_RESULT = 'N'
l_locale = 'US'
CHANGE_CONTEXTS(LANGUAGE=l_locale)
CONDITION_RESULT = IS_REQ_BELOW_IN_GEO_HIERARCHY(IRC_CSP_REQ_NUMBER, 'Germany', 'ANY','ANY', 'ANY', 'ANY',
'ANY', 'ANY', 'ANY', 'ANY', 'ANY', 'N',l_locale)

return CONDITION_RESULT

---

## Determines if a job requisition's
*Chunk ID: OHR-REC-1039 | Chapter: Geography Hierarchies*

organization is at a lower or equal
level of an organization in the
organization tree.

---

## Parameter 1: IRC_CSP_REQ_
*Chunk ID: OHR-REC-1040 | Chapter: Geography Hierarchies*

ORGANIZATION_NAME: Name
of the organization used in the
requisition. It's not required to use
this database item to provide the
name of the organization. As long
as the name of the organization is
provided.

---

## Parameter 2: The name of the
*Chunk ID: OHR-REC-1041 | Chapter: Geography Hierarchies*

organization which you want
to know if the organization in
parameter 1 is below or equal to.
Parameter 3: The locale to use for
loading the organization names.

---

## DEFAULT FOR IRC_CSP_REQ_ORGANIZATION_NAME IS 'NONE'
*Chunk ID: OHR-REC-1042 | Chapter: Geography Hierarchies*

CONDITION_RESULT = 'N'
l_locale = 'US'
CHANGE_CONTEXTS(LANGUAGE=l_locale)
CONDITION_RESULT = IS_REQ_BELOW_IN_ORG_TREE(IRC_CSP_REQ_ORGANIZATION_NAME, 'Vision
Administration',l_locale)
return CONDITION_RESULT

Related Topics
• Overview of Writing Formulas
• Database Items for Oracle Recruiting Cloud Fast Formulas

---

## Fast Formulas for Job Requisitions
*Chunk ID: OHR-REC-1043 | Chapter: Geography Hierarchies*

You can create fast formulas of the Recruiting Job Requisition formula type and use them as conditions in job
requisitions. Conditions are used to determine if job requisitions will be automatically unposted from career sites.
This table presents the area where fast formulas of the Recruiting Job Requisition type can be used.

---

## Defines a condition that must be met for the
*Chunk ID: OHR-REC-1044 | Chapter: Geography Hierarchies*

job requisition to be unposted from the internal
career site, the external career sites, or both.

---

## A formula used as a condition to automatically
*Chunk ID: OHR-REC-1045 | Chapter: Geography Hierarchies*

unpost a job requisition. The job requisition is
automatically unposted when a given number
of job applications have been received.

The return value of Recruiting Job Requisition formulas must be set in the CONDITION_RESULT variable.

---

## Formulas of the Recruiting Job Requisition type must return a value indicating if the condition is met or not. Use the
*Chunk ID: OHR-REC-1046 | Chapter: Geography Hierarchies*

following variables in the return statement:
CONDITION_RESULT variable contains the result of the formula, which indicates if the condition is met or not.
• To indicate that the condition is met, the CONDITION_RESULT variable must contain one of the following values
(case insensitive):

◦ y
◦ yes
◦ true
◦ 1
• Any other value will consider the condition as not being met.
CONDITION_MESSAGE is an optional part of the result, it doesn't have to be returned. Maximum size is 255 characters.
• The message is used for logging purposes only.
CONDITION_RESULT = 'N'
CONDITION_MESSAGE = ''
...
return CONDITION_RESULT, CONDITION_MESSAGE

---

## When you create a fast formula of type Recruiting Job Requisition, you can use information related to a specific job
*Chunk ID: OHR-REC-1047 | Chapter: Geography Hierarchies*

requisition within this formula. For example, the requisition's recruiting type, organization, number of confirmed job
applications.

---

## Sample Formula
*Chunk ID: OHR-REC-1048 | Chapter: Geography Hierarchies*

Here's an example of a fast formula to automatically unpost a job requisition based on the number of confirmed job
applications on the requisition.
DEFAULT FOR IRC_REQ_JOBAPP_COUNT_CONFIRMED IS 0
CONDITION_RESULT = 'N'
...
COUNT = IRC_REQ_JOBAPP_COUNT_CONFIRMED
IF (COUNT > 500) THEN
CONDITION_RESULT = 'Y'
return CONDITION_RESULT

Contexts
The following contexts are available to the Recruiting Job Requisition formula type:
• IRC_JOB_REQUISITION_ID

◦ ID of the job requisition.
• IRC_JOB_LANGUAGE

◦ Language for which to retrieve multilingual information.

---

## Database Items
*Chunk ID: OHR-REC-1049 | Chapter: Geography Hierarchies*

Database items related to requisitions are available for the formula type Recruiting Job Requisitions.
For a complete list of database items, see the spreadsheet Database Items for Oracle Recruiting Cloud Fast Formulas on
My Oracle Support (MOS ID 2723251.1).

Functions
These functions are available to support more complex calculations.

---

## Counts the number of active job
*Chunk ID: OHR-REC-1050 | Chapter: Geography Hierarchies*

applications which are currently
in a given phase or state for a job
requisition.

---

## Parameter 1: IRC_REQ_
*Chunk ID: OHR-REC-1051 | Chapter: Geography Hierarchies*

REQUISITION_NUMBER: Number
of the requisition. It's not required
to use this database item to
provide the requisition number.
As long as a requisition number is
provided.

---

## Parameter 2: Phase name. The
*Chunk ID: OHR-REC-1052 | Chapter: Geography Hierarchies*

name of the phase for which to
count the active job applications.
Parameter 3: State name. The
name of the state, within the
phase provided as the previous
parameter, for which to count the
active job applications. If you want
to count the job applications for all
states within the phase, you can
use ANY.
Parameter 4: The locale to use
for loading the phase and state
names.

---

## DEFAULT FOR IRC_REQ_REQUISITION_NUMBER IS 'none'
*Chunk ID: OHR-REC-1053 | Chapter: Geography Hierarchies*

CONDITION_RESULT = 'N'
...
COUNT = COUNT_JOBAPPS_ACTIVE_IN_PHASE_STATE(IRC_REQ_REQUISITION_NUMBER, 'New', 'To be Reviewed', 'US')
IF (COUNT > 300) THEN
CONDITION_RESULT = 'Y'
return CONDITION_RESULT

---

## Counts the number of job
*Chunk ID: OHR-REC-1054 | Chapter: Geography Hierarchies*

applications which were previously
or are currently in a given phase or
state for a job requisition.

---

## Parameter 1: IRC_REQ_
*Chunk ID: OHR-REC-1055 | Chapter: Geography Hierarchies*

REQUISITION_NUMBER: Number
of the requisition. It's not required
to use this database item to
provide the requisition number.
As long as a requisition number is
provided.

---

## Parameter 2: Phase name. The
*Chunk ID: OHR-REC-1056 | Chapter: Geography Hierarchies*

name of the phase for which
to count the number of job
applications.
Parameter 3: State name. The
name of the state, within the
phase provided as the previous
parameter, for which to count the
job applications. If you want to
count the job applications for all
states within the phase, you can
use ANY.
Parameter 4: The locale to use
for loading the phase and state
names.

---

## DEFAULT FOR IRC_REQ_REQUISITION_NUMBER IS 'none'
*Chunk ID: OHR-REC-1057 | Chapter: Geography Hierarchies*

CONDITION_RESULT = 'N'
...
COUNT = COUNT_JOBAPPS_PAST_PHASE_STATE(IRC_REQ_REQUISITION_NUMBER, 'New', 'To be Reviewed', 'US')
IF (COUNT > 300) THEN
CONDITION_RESULT = 'Y'
return CONDITION_RESULT

Related Topics
• Overview of Using Fast Formulas
• Database Items for Oracle Recruiting Cloud Fast Formulas

---

## Candidate Data Archiving and Disposal
*Chunk ID: OHR-REC-1058 | Chapter: Geography Hierarchies*

31 Candidate Data Archiving and Disposal
Archive Candidate Search
You use candidate search archiving to track candidate searches ran by recruiters. Search result archiving supports
requirements from the Office of Federal Contract Compliance Programs (OFCCP).
When you enable candidate search archiving, you can track and record the following information:
• User who ran the candidate search
• Criteria used for the search
• Date and time when the candidate search was run
• Candidates returned in search results
• Action taken on candidates by the user from search results
Candidate search queries are saved for a period of two years. A search query can contain a maximum of 500
candidates. Search queries returning no candidate are also archived.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information

2. Expand the Search section and click Edit.
3. Select the option Candidate Search Archiving.
4. Click Save.
Results:
Data is available in Oracle Transactional Business Intelligence reporting solution in the Recruiting - Recruiting Real Time
subject area, Candidate Search dimension.
What to do next
You need to run the Convert Candidate Search Logs for Reporting Purposes scheduled process.

---

## Set Up Candidate Data Disposal
*Chunk ID: OHR-REC-1059 | Chapter: Geography Hierarchies*

You can manage the disposal of candidate data to meet data protection requirements of individuals and organizations.
Candidate data is collected through various ways. It can be provided by candidate themselves or collected by recruiters
or agencies. Candidate data can include personally identifiable information (PII).
To initiate candidate data disposal, you use the Remove Person Information tool in the Data Exchange work area. Two
options are available:
• Configure Person Information Removal Policies: You can configure the business objects and their components
that you want to remove and mask required attributes.

---

## Candidate Data Archiving and Disposal
*Chunk ID: OHR-REC-1060 | Chapter: Geography Hierarchies*

• Remove Person Information: You can remove person information for specified people from this page. When
you submit the person information removal process, the data is removed according to the configuration
defined in the associated person information removal policy.
To access the Remove Person Information tool, you need these privileges:
• Configure Person Information Removal Policies (HRC_CONFIGURE_PERSON_INFO_REMOVAL_POLICIES_PRIV)
• Remove Person Information (ORA_HRC_REMOVE_PERSON_INFORMATION)
Note: Before you initiate the Remove Person Information process to obfuscate data, the corresponding candidate
must be deleted in Oracle Recruiting. This delete is a soft delete that can be done from within recruiting or with HCM
Data Loader. Here's an example: Examples of Loading Candidates

---

## Configure Person Removal Policy
*Chunk ID: OHR-REC-1061 | Chapter: Geography Hierarchies*

1. In My Client Groups, click the Data Exchange work area.
2. In the Remove Person Information section, click Configure Person Information Removal Policies.
3. Click Create to create a template. Complete these fields:

◦ NAME: The name of the template.
◦ CODE: The template code, defaults to the name of the template.
◦ CATEGORY: The Business Object the template is created for. Select Candidate.
◦ DESCRIPTION: You can enter a description.
4.
5.
6.
7.
8.
9.

Click OK.
On the Components page, in the Business Objects, select the Candidate option.
Click Save.
On the Components page, in the Components, select all the components.
Click Save.
Click the Rules tab to configure policies. Most objects are configured for deletion, so no specific rules are
needed for those objects. You can configure rules for objects if they contain attributes that can only be
obfuscated and cannot be deleted. Candidate details are masked in several areas such as emails, phone
numbers, candidate job applications, attachments, interactions. Here is how values are masked:

◦ NUMBER columns = 0000
◦ VACHAR columns = OBF_ZZZ
◦ CHAR columns = 0
◦ DATE columns = 1900-01-01
◦ TIMESTAMP columns = 1900-01-01 00:00:00
10. Click Enable Template.
It's recommended to define Person Information Removal policy in line with your business requirement. Define policies
specific to candidate types, for example two different policies to obfuscate external candidate data and ex-employees
or ex-contingent workers. In ex-employee and ex-contingent workers policy, exclude the deletion and obfuscation
of Candidate Name, Candidate Address, Candidate Phone, Candidate Email, Candidate Extra Information, Candidate
National Identifier, and any other information as per your business requirement. Delete or obfuscate ex-employee or excontingent workers data in the Worker category.

---

## Submit the Remove Person Information Process
*Chunk ID: OHR-REC-1062 | Chapter: Geography Hierarchies*

1.
2.
3.
4.
5.

In My Client Groups, click the Data Exchange work area.
In the Remove Person Information section, click Remove Person Information.
Locate the rule that you created.
Click Submit Process.
On the Submit Process page, enter the process name, select the template you just created, enter candidate
numbers, and select the Remove process mode.
6. Click Submit.

---

## The process appears on the Remove Personal Information page. Here's what you will see on the page after you submit
*Chunk ID: OHR-REC-1063 | Chapter: Geography Hierarchies*

the process:
• STATUS: Success or Error.
• PROCESS MODE: Remove mode or Report mode.
• SUBMITTED BY: The user who submitted the process.
• SUBMISSION DATE: The date the process was submitted.

---

## Summary of Candidate Data Being Disposed
*Chunk ID: OHR-REC-1064 | Chapter: Geography Hierarchies*

Here's a summary of candidate data that can be disposed to meet data protection requirements of individuals and
organizations.

---

## Attribute or Entity
*Chunk ID: OHR-REC-1065 | Chapter: Geography Hierarchies*

Candidate

Name
Address
Email
Phone
Attachments
Languages
Referral, Endorsement
Regulatory Information
Flexfields
National Identifiers
Preferences
Preferred Job Family
Preferred Location
Preferred Organization

by Users

---

## Additional Text 1 and 2
*Chunk ID: OHR-REC-1066 | Chapter: Geography Hierarchies*

Flexfields
Attachments

Referral

Notes
JSON

Questions

Responses

Interactions

Candidate
Job Application

e-Signature

Name

---

## Purge Recruiting Campaign Data
*Chunk ID: OHR-REC-1067 | Chapter: Geography Hierarchies*

You can configure data retention duration for recruiting campaign email metrics.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Enterprise Recruiting and Candidate Experience Information
2. Expand the Data Purging section and click Edit.
3. Enter the number of days you want to retain campaign email metrics.
The default value is 180 days. Maximum value is 1000 days.
4. Click Save.
5. You need to run the scheduled process Purge Processed Internal Recruiting Data.
Results:
The database is cleaned up after the number of days you entered in the campaign email metrics setting.

---

# Third Party Integration

## Third Party Integration
*Chunk ID: OHR-REC-1068 | Chapter: Third Party Integration*

Integrating Third Party Services
Your organization might decide to integrate and use third-party services based on their business needs and business
processes.
Here are the available third-party services:
• Assessment
• Background check
• Direct Apply
• Job distribution
• Profile import
• Tax credits
Note: For details on the integration enablement done by partners, see the Partner Integration documentation on My
Oracle Support (ID 2627681.1).

Assessment
Assessments are used to assess and measure the knowledge, skills, abilities, and attributes of candidates for a job.
Assessments are conducted using Oracle's assessment partner services. When an assessment service is enabled, the
Recruiting Administrator can configure at which state and phase of the candidate selection process the assessment is
initiated.

---

## Background Check
*Chunk ID: OHR-REC-1069 | Chapter: Third Party Integration*

Background checks are run on candidates as part of their candidate selection process to ensure that their background
is verified before hiring them. Background checks are conducted using Oracle's background check partner services.
When a background check service is enabled, the Recruiting Administrator can configure at which phase and state of
the candidate selection process the background check is automatically triggered.

---

## Direct Apply
*Chunk ID: OHR-REC-1070 | Chapter: Third Party Integration*

With Direct Apply, candidates who navigate to the career site of an approved partner can apply for a job and provide
required information while staying on the partner’s site.

---

## Job Distribution
*Chunk ID: OHR-REC-1071 | Chapter: Third Party Integration*

Job requisitions can be posted on job boards using job distribution partner services.

---

## Profile Import
*Chunk ID: OHR-REC-1072 | Chapter: Third Party Integration*

When a profile import partner service is enabled, the Profile Import block becomes available in the job application flow.
When external candidates apply for a job, they can upload their resume. A call is made to the partner's web service and
the data returned by the partner is used to populate the candidates' job application. This is called resume parsing.
Note: For the Apply with LinkedIn and resume parsing functionality, only default sections are imported.

---

## Tax Credits
*Chunk ID: OHR-REC-1073 | Chapter: Third Party Integration*

Tax credit screenings are used to validate tax credit eligibility of candidates. Candidates can be eligible to various
federal, state, and other tax credits. Tax credit screenings are conducted using Oracle's partner services. When a tax
credit service is enabled, the Recruiting Administrator can configure at which phase and state of the candidate selection
process the tax credit screening is triggered.
Related Topics
• Partner Integration Guides on My Oracle Support

---

## Set Up Partner Enablement
*Chunk ID: OHR-REC-1074 | Chapter: Third Party Integration*

Partner enablement consists in contacting the partner to obtain the implementation project .zip file and to import it in
Oracle HCM Cloud.
A user with the Application Implementation Administrator role
(ORA_ASM_APPLICATION_IMPLEMENTATION_ADMIN_ABSTRACT) and Recruiting Administrator role
(ORA_PER_RECRUITING_ADMINISTRATOR_JOB) performs the following steps.
1.
2.
3.
4.
5.
6.

In the Setup and Maintenance work area, click the Tasks icon then click Manage Configuration Packages.
On the Manage Configuration Packages page, in the Search Results section, click Upload.
Select the implementation project .zip file provided by the partner.
Click Get Details to verify that the selected file is correct. If needed, click Update to select a different file.
Click Submit.
When the warning message appears, click Yes. The upload process starts. Once the upload is done, the status
changes to Completed successfully.

Note: Click the Refresh icon to update the status.
Once the upload is done, you need to import setup data.
1. Select the row where Upload - Completed Successfully appears and click the Import Setup Data button.
2. If needed, click the Refresh icon to update the status.
3. Once the import is done, the status changes to Completed successfully.
The partner is now provisioned. If you go to the Recruiting Category Enablement task and Recruiting Category
Provisioning and Configuration task, you can see that the status of the partner is set to Provisioned.

---

## Set Up Partner Integration Provisioning
*Chunk ID: OHR-REC-1075 | Chapter: Third Party Integration*

To use a partner's service, the Recruiting Administrator needs to provision and activate a supported integration. The list
of supported integrations is published on Oracle's Cloud Marketplace.
Here's what to do:
1.
2.
3.
4.
5.
6.
7.

---

## Configure the Integration
*Chunk ID: OHR-REC-1076 | Chapter: Third Party Integration*

Provide User Account Credentials
Export and Import the Integration Provisioning Files
Enter the Reference Key
Activate the Integration
Enter a User Account for the Partner
Run Scheduled Processes

---

## Configure the Integration
*Chunk ID: OHR-REC-1077 | Chapter: Third Party Integration*

The Administrator configures the integration in a testing environment.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Category Provisioning and Configuration page, find the integration partner and click the Edit icon.
3. Complete the fields. For details, see Fields to Complete for Partner Integration Configuration.
4. Click Save.

---

## Provide User Account Credentials
*Chunk ID: OHR-REC-1078 | Chapter: Third Party Integration*

The Administrator provides the user account credentials to the partner for data synchronization. The partner uses this
user account for authentication with HCM when updating the data.
This is done in a testing environment. A separate account is required for the testing environment and the production
environment.
The table lists the privileges required to provide user account credentials to a partner. For details on privileges, see the
Security chapter in each of the partner integration guide on My Oracle Support (ID 2627681.1).

Service

Privilege

Assessment

---

## Use REST Service - Candidate Background Checks
*Chunk ID: OHR-REC-1079 | Chapter: Third Party Integration*

(ORA_IRC_REST_SERVICE_ACCESS_CANDIDATE_BACKGROUND_CHECKS)
Choose Application Reference Territory Data (PER_CHOOSE_APPLICATION_REFERENCE_TERRITORY_
DATA)

Service

Privilege

---

## Job Site REST Services Duty (ORA_IRC_JOB_SITE_REST_SERVICES_DUTY)
*Chunk ID: OHR-REC-1080 | Chapter: Third Party Integration*

Job Site REST Services Duty (ORA_IRC_JOB_SITE_REST_SERVICES_DUTY_CRM)
Manage Person Disability by Worker (PER_MANAGE_PERSON_DISABILITY_BY_WORKER_PRIV_OBI)

---

## Export and Import the Integration Provisioning Files
*Chunk ID: OHR-REC-1081 | Chapter: Third Party Integration*

When the Administrator has tested the integration on a testing environment, a user with the Application
Implementation Administrator role (ORA_ASM_APPLICATION_IMPLEMENTATION_ADMIN_ABSTRACT) and Recruiting
Administrator role (ORA_PER_RECRUITING_ADMINISTRATOR_JOB) performs the following steps.
Note: The enablement file must be previously loaded if it's not a refresh of the configuration. You do this using the
partner's .zip file as explained above or it can be exported from a test environment using the task Recruiting Category
Enablement instead of the task Recruiting Category Provisioning and Configuration.
To export the file, you first create an implementation project:
1. In the Setup and Maintenance work area, click the Tasks icon then click Manage Implementation Projects.
2. In the Implementation Projects page, click the Plus icon to create an implementation project.
3. On the Create Implementation Project page, provide the following information:

◦ Name: Enter a unique name.
◦ Code: Enter a unique code.
◦ Description: Provide a brief description, if desired.
◦ Assigned To: Assign the project to a user, if desired.
◦ Start Date: Enter the date when the project will start.
◦ Finish Date: Enter the date when the project will finish.
4.
5.
6.
7.
8.

Click Save and Open Project.
On the newly created implementation project page, click the Plus icon.
On the Task Lists and Tasks page, search for the task Recruiting Category Provisioning and Configuration.
Select the Recruiting Category Provisioning and Configuration task, click Apply, then click Done.
Exit the Implementation Projects page.

You then create a configuration package:
1. On the Manage Configuration Packages page, click the Plus icon to create a configuration package.
2. On the Create Configuration Package page, provide the following information:

◦ Name: Select the implementation project you just created.
◦ Export: Select the option Setup task list and setup data.

---

## Note: Fields in the Configuration Package Details section are automatically populated with data from the
*Chunk ID: OHR-REC-1082 | Chapter: Third Party Integration*

implementation project, except for the Client ID and Client Secret.
3. Click Next.
4. On the Create Configuration Package: Select Objects to Export page, keep the Export option selected for the
Partner Service Provisioning.
5. In the Partner Service Provisioning: Scope section, click the Plus icon.
6. On the Partner Integration Provisioning page, select the partner service you want to add, click Apply, then click
Save and Close.
7. On the Create Configuration Package: Select Objects to Export page, click Submit.
8. When the warning message appears, click Yes. The export process starts. Once the export is done, the status
changes to Completed successfully.
Note: Click the Refresh icon to update the status.
9. Once the export is successfully completed, click the Download icon and select Download Configuration
Package. An implementation project .zip file is created.
To import the file:
1. In the Setup and Maintenance work area, click the Tasks icon then click the Manage Configuration Packages
task.
2. On the Manage Configuration Packages page, in the Search Results section, click Upload.
3. Choose the implementation project .zip file.
4. Click Get Details to verify that the selected file is correct. If needed, click Update to select a different file.
5. Click Submit.
6. When the warning message appears, click Yes. The upload process starts. Once the upload is done, the status
changes to Completed successfully.
Note: Click the Refresh icon to update the status.

---

## Enter the Reference Key
*Chunk ID: OHR-REC-1083 | Chapter: Third Party Integration*

The Administrator enters the reference key in the provisioning screen in the production environment. The key is
provided by the partner.
Here's the list of supported special characters for the reference key:
• ~
• !
• *
• (
• )
• • _
• .
Note: There must be no space and no & character in the reference key.

---

## Activate the Integration
*Chunk ID: OHR-REC-1084 | Chapter: Third Party Integration*

The Administrator activates the integration in the production environment.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Category Provisioning and Configuration page, find the partner and click the Edit icon.
3. Click Activate.
Once the integration is active, the status changes from Provisioned to Active.

---

## Enter a User Account for the Partner
*Chunk ID: OHR-REC-1085 | Chapter: Third Party Integration*

The Administrator enters user accounts to be used by recruiting users for the partner on the production environment.
Those accounts must exist already on the partner side.
1. In the Setup and Maintenance work area, go to the following:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Category Provisioning and Configuration page, click the Edit icon for a partner.
3. Click Assign User Account.
4. Enter a user name and description. The description is useful, for example, for recruiters posting a job
requisition to partners or selecting a package for background check.
5. Click OK.
Packages associated with the user account are retrieved upon user account activation.
• For background checks, the administrator can also edit and save the account. This will refresh the list of
associated packages.
• For assessments and tax credit screenings, deactivating and reactivating the account will refresh the list of
packages associated with such account.
• Note that refreshing packages can also be done at any point of time by the partner using the account packages
update service.

---

## Run Scheduled Processes
*Chunk ID: OHR-REC-1086 | Chapter: Third Party Integration*

You need to run theses scheduled processes:
• Perform Recruiting Candidate Selection Process Actions
• Send Candidate Screening Requests to Partners
For details, see Which scheduled processes are used in Recruiting?.

---

## Note: You can use location-based access (LBAC) to control user access to tasks and data based on their roles and
*Chunk ID: OHR-REC-1087 | Chapter: Third Party Integration*

computer IP addresses. If you activated LBAC, it might prevent access from external locations (IP). As a result, you're
responsible to provide a Public custom role for the partner user calling the REST services. If the role isn't public, the
REST services can't be called from outside the firewall. For details, see Overview of Location-Based Access

Related Topics
• Partner Integration Guides on My Oracle Support

---

## Fields to Complete for Partner Integration Configuration
*Chunk ID: OHR-REC-1088 | Chapter: Third Party Integration*

The tables list the fields you need to fill when configuring an integration partner.

Assessment
Assessment Field

Description

---

## This key is separate for each instance. The partner provides a separate reference key for the customer's
*Chunk ID: OHR-REC-1089 | Chapter: Third Party Integration*

test instance and for the production instance.
Note: There must be no space in the reference key.

---

## Client ID
*Chunk ID: OHR-REC-1090 | Chapter: Third Party Integration*

Client ID provided by the partner. Used with the Client Secret to get the OAuth token.

---

## Client Secret
*Chunk ID: OHR-REC-1091 | Chapter: Third Party Integration*

Client Secret provided by the partner. Used with Client ID to get the OAuth token.

---

## Capture PII Data from Partner
*Chunk ID: OHR-REC-1092 | Chapter: Third Party Integration*

When you select this option, partners can send back the National Identifier and date of birth.

---

## This key is separate for each instance. The partner provides a separate reference key for the customer's
*Chunk ID: OHR-REC-1093 | Chapter: Third Party Integration*

test instance and for the production instance.
Note: There must be no space in the reference key.

---

## Client ID
*Chunk ID: OHR-REC-1094 | Chapter: Third Party Integration*

Client ID provided by the partner. Used with the Client Secret to get the OAuth token.

---

## Client Secret
*Chunk ID: OHR-REC-1095 | Chapter: Third Party Integration*

Client Secret provided by the partner. Used with Client ID to get the OAuth token.

---

## This key is separate for each instance. The partner provides a separate reference key for the customer's
*Chunk ID: OHR-REC-1096 | Chapter: Third Party Integration*

test instance and for the production instance.
Note: There must be no space in the reference key.

---

## Client ID
*Chunk ID: OHR-REC-1097 | Chapter: Third Party Integration*

Client ID provided by the partner. Used with the Client Secret to get the OAuth token.

---

## Client Secret
*Chunk ID: OHR-REC-1098 | Chapter: Third Party Integration*

Client Secret provided by the partner. Used with Client ID to get the OAuth token.

---

## Reference Key
*Chunk ID: OHR-REC-1099 | Chapter: Third Party Integration*

Reference key provided by the partner.
Note: There must be no space in the reference key.

---

## This key is separate for each instance. The partner provides a separate reference key for the customer's
*Chunk ID: OHR-REC-1100 | Chapter: Third Party Integration*

test instance and for the production instance.
Note: There must be no space in the reference key.

---

## Client ID
*Chunk ID: OHR-REC-1101 | Chapter: Third Party Integration*

Client ID provided by the partner. Used with the Client Secret to get the OAuth token.

---

## Client Secret
*Chunk ID: OHR-REC-1102 | Chapter: Third Party Integration*

Client Secret provided by the partner. Used with Client ID to get the OAuth token.

---

## Profile Import: Fields Imported from LinkedIn and Indeed
*Chunk ID: OHR-REC-1103 | Chapter: Third Party Integration*

The table lists fields imported from LinkedIn and Indeed when you use the Profile Import feature.
Fields are imported for the blocks enabled in the job application flow. For example, if the Education block isn't part of
the application flow, the education content won't be imported.
Note: For the Apply with LinkedIn and resume parsing functionality, only default sections are imported.

Section

Field

---

## School Name
*Chunk ID: OHR-REC-1104 | Chapter: Third Party Integration*

School Location (Indeed only)
Degree
Field of Study/Major
Start Date
End Date

Experience

---

## Company Name
*Chunk ID: OHR-REC-1105 | Chapter: Third Party Integration*

Company Type
Job Title
Start Date
End Date
Current Indicator
Summary/Description

Section

Field

---

## Licenses and Certifications
*Chunk ID: OHR-REC-1106 | Chapter: Third Party Integration*

Name
Description (Indeed only)
Issuing Authority (LinkedIn only)
Number (LinkedIn only)
Start Date
End Date

Languages

---

## Set Up Background Check Package Selection Within
*Chunk ID: OHR-REC-1107 | Chapter: Third Party Integration*

Recruiting
You can configure background checks so that recruiters select background check packages directly within Recruiting,
without having to go on the partner's site.
Before you start
To enable background check package selection within Recruiting, the partner needs to support the feature.
Here's what to do
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Enablement
2. On the Partner Enablement page, go to the Background Check section and click the Edit icon next to a partner.
3. These two options are available. Verify with the partner if they support those options before modifying them.
◦ Local Package Selection: Select this option to enable the selection of a packages directly in Recruiting. By
default, this option is disabled, which means packages are selected on the partner's portal using the Go to
Partner Portal link.
◦ Multiple Phases or States: Select this option if you want to allow users to send multiple background check
requests at different phase or state. You can choose this option only if you selected the Local Package
Selection option. By default, this option is disabled.
4. Click Save and Close.

---

## Send Additional Requisition Flexfields to Screening
*Chunk ID: OHR-REC-1108 | Chapter: Third Party Integration*

Partners
You can create rules in Transaction Design Studio to display additional requisition flexfields to partners.
Discuss with your screening partners if they want to support additional requisition flexfields. If that’s the case, use these
actions to create the rules and enhance the standard screening integrations:
• Recruiting – Additional Fields for Assessment
• Recruiting – Additional Fields for Background Check
• Recruiting – Additional Fields for Direct Apply
• Recruiting – Additional Fields for Job Distribution
• Recruiting – Additional Fields for Tax Credit
Note: LinkedIn is using its own posting mechanism even though LinkedIn appears in the list of partners.
You will need to select which flexfields pair, field, and value will be added to the candidate details payload for each
partner. Those flexfields can be activated at the global context level and only one context per partner. A single partner
can’t receive flexfields configured in more than a single specific context in addition to the global one. Up to 25 flexfields
can be activated per partner.
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select these actions:
◦ Recruiting – Additional Fields for Assessment

◦ Recruiting – Additional Fields for Background Check
◦ Recruiting – Additional Fields for Direct Apply
◦ Recruiting – Additional Fields for Job Distribution
◦ Recruiting – Additional Fields for Tax Credit
5. Click Add to create a rule.
6. In the Basic Details section, enter a name and description for the rule. Select a recruiting partner
7. In the Page Attributes section, set Job Requisition Descriptive Flexfield to Visible.
8. If you want to fill and send individual flexfields to the partner, click the Edit icon. Select a flexfield content code and a
flexfield attribute. Set the field as being visible.
9. Click Save and Close.
Results:
These activated flexfields will be visible in the job requisition. These fields are shared with specific partners and will
be included in the candidate details payload requested by the partners. This is additional content from recruiting to
partner.

---

## Send Additional Screening Results Using Job Application
*Chunk ID: OHR-REC-1109 | Chapter: Third Party Integration*

Flexfields
You can allow your screening partners to send additional screening results using candidate job application flexfields.
Discuss with your assessment, tax credit, and background check screening partners if they want to support additional
job application flexfields for screening results. If that’s the case, you need to configure these additional job application
flexfields for the result payload per partner.
When the flexfields are configured, the additional results and values are displayed in the job application’s Screening
Results tab. Recruiters can add these additional fields to the job application grid view and filters. The fields aren’t
available in the candidate detail’s view, where only assessment standard fields are displayed. In the grid view Compound
Field section, all segments including hidden ones are displayed when the context is selected.
Here's what to do:
1.
2.
3.
4.

---

## Create Multi-Row Flexfield Context for Job Candidate Application Usage
*Chunk ID: OHR-REC-1110 | Chapter: Third Party Integration*

To support additional results, you need to create a multi-row flexfield context using the extensible flexfield called
Person EIT Information.
• You can only select one multi-row context per partner.
• You need to create the hidden fields PROVISIONING_ID and PACKAGE_RESULT_ID to support the partner and
package.
• You can create up to 25 additional result fields for each context.
• You can only use text, number, and date format:
◦ Date time isn’t supported.

◦ Date must be sent by the partner using the ISO-8601 format YYYY-MM-DD

1.
2.
3.
4.
5.
6.
7.
8.
9.

In the Setup and Maintenance work area, search for the task Manage Person Extensible Flexfield.
On the Manage Person Extensible Flexfield page, select the extensible flexfield called Person EIT Information.
Click the Edit icon.
On the Manage Person Extensible Flexfield page, click Manage Contexts.
On the Manage Contexts page, you create one multi-row context per partner supporting those additional result
fields.
In the Context Usages tab, click the Create icon and select the usage Usage code for candidate application.
In the Context Sensitive Segments section, click the Create icon.
Create the mandatory segments in the context using values provided in the following table.
Click Save and Close.

Note: PROVISIONING_ID and PACKAGE_RESULT_ID must be configured as hidden.

Code

Partner
Name

---

## Value Set
*Chunk ID: OHR-REC-1111 | Chapter: Third Party Integration*

Prompt

PROVISIONING_
provisioningId No
ID

Yes

NUMBER

PEI_
PartnerNameLovValueSet
Partner
INFORMATION_
Name
NUMBER1

Hidden

Package
Result
Identifier

PACKAGE_
RESULT_ID

packageResultId
Yes

Yes

NUMBER

PEI_
15 Digit
INFORMATION_Number
NUMBER2

Hidden

Package
Name

PACKAGE_
CODE

packageCode No

Yes

---

## CHARACTER PEI_
*Chunk ID: OHR-REC-1112 | Chapter: Third Party Integration*

BGCPackageNameLovValueSet
Package
List of
INFORMATION1or
Name
values

Package
Result
Identifier

Display
Type

AssessmentPackageNameLovValueSet
or
TaxCreditsPackageNameLovValueSet

In addition, you can create up to 25 result fields, using those 3 supported formats:
• Date Segments: You can use the ORA_FND_FLEX_DEFAULT_FORMAT_ONLY_DATE value set, or you can define
your own value set with minimum and maximum date validation. Date time isn’t supported. The partner needs
to send date data in the ISO-8601 format YYYY-MM-DD.
• Number Segments: You can use the FND_NUMBER15 value set, or you can define your own with different
precision/scale to support integer and decimal numbers.
• Char Segments: You can use the FND_CHAR100 value set, or you can define your own value set. The maximum
number of characters allowed is 150.

---

## Create Value Sets
*Chunk ID: OHR-REC-1113 | Chapter: Third Party Integration*

You need to create value sets for the Partner Name, Package Name, Package Result Identifier.
1.
2.
3.
4.

In the Context Sensitive Segments section, select the context sensitive segment you created and click Edit.
Click Create Value Set.
Enter the required values as indicated in the following tables.
Click Save and Close.

---

## FROM Clause
*Chunk ID: OHR-REC-1114 | Chapter: Third Party Integration*

(SELECT DISTINCT A.PACKAGE_CODE,A.PACKAGE_NAME,B.PROVISIONING_ID FROM FUSION.IRC_
ASMT_ACCT_PACKAGES A,FUSION.IRC_TP_PARTNER_ACCOUNTS B WHERE A.ACCOUNT_
ID=B.ACCOUNT_ID) PKG,FUSION.IRC_ASMT_PARTNER_CONFIG PC

---

## PC.PROVISIONING_ID =PKG.PROVISIONING_ID AND PC.RESULTS_FLEX_CONTEXT_CODE=’ASMT_
*Chunk ID: OHR-REC-1115 | Chapter: Third Party Integration*

FLEX_CONTEXT’
Note: ASMT_FLEX_CONTEXT is the context code for which you are creating Segments. It will vary
depend on the context code you created.

---

## FROM Clause
*Chunk ID: OHR-REC-1116 | Chapter: Third Party Integration*

(SELECT DISTINCT A.SCR_PKG_CODE,A.SCR_PKG_NAME,B.PROVISIONING_ID FROM FUSION.irc_bc_
acct_sp_assgmnts A,FUSION.IRC_TP_PARTNER_ACCOUNTS B WHERE A.ACCOUNT_ID=B.ACCOUNT_
ID) PKG,FUSION.IRC_BC_ACTIVATION_CONFIG PC

---

## Tax credit partner package LOV value set for TaxCreditsPackageNameLovValueSet
*Chunk ID: OHR-REC-1117 | Chapter: Third Party Integration*

FROM Clause

(SELECT DISTINCT A.PACKAGE_CODE,A.PACKAGE_NAME,B.PROVISIONING_ID FROM FUSION.IRC_
TC_ACCOUNT_PACKAGES A,FUSION.IRC_TP_PARTNER_ACCOUNTS B WHERE A.ACCOUNT_
ID=B.ACCOUNT_ID)PKG, FUSION.IRC_TC_PARTNER_CONFIG PC

---

## Associate Context to Partner
*Chunk ID: OHR-REC-1118 | Chapter: Third Party Integration*

When the context configuration is done, you need to associate the context to the partner.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Partner Integration Provisioning page, locate the partner and click the Edit icon.
3. Select the context in the Context for Additional Results field.
4. Click Save.

---

## Input Payload for Partners
*Chunk ID: OHR-REC-1119 | Chapter: Third Party Integration*

With this newly associated context, the partner can start to send additional results into those defined segments. For
details, see the Partner Integration guides available on My Oracle Support (ID 2627681.1).
Related Topics
• Partner Integration Guides on My Oracle Support

---

## Integration with Direct Apply
*Chunk ID: OHR-REC-1120 | Chapter: Third Party Integration*

Direct Apply allows candidates who navigate to the career site of an approved partner to apply for a job and provide
required information while staying on the partner’s site. The information is received in Oracle Recruiting, a job
application is created and a candidate is created or updated (if they already exist). The candidate doesn’t have to
navigate back to the career site of the customer to submit their application. The partner can query on the status of the
candidate as they go through the job application process.
The Direct Apply partner category is available in Oracle Marketplace.

---

## Third Party Integration
*Chunk ID: OHR-REC-1121 | Chapter: Third Party Integration*

Below are the touchpoints of the integration initiated by the partner.
• Partner retrieves the list of posted jobs.
• Partner retrieves requisition details.
• Partner retrieves application flow details.
• Partner verifies if the candidate exists.
• Partner creates candidate if needed.
• Partner creates job application.
• Partner retrieves job application statuses.
• Oracle sends notifications to the partner based on the candidate selection process configuration.
The Direct Apply third party integration category is used by external partners like the other existing categories
(assessment, background check, tax credit, profile import, job distribution).
The steps to enable the Direct Apply category are similar to the ones of other partner categories. You obtain the .zip file
from the partner, you upload the .zip file in the partner enablement page to obtain the partner key, you configure the
user, and you enter the secret code. Note that some partners might have their own activation mechanism.
The administrator then configures the integration using the Recruiting Category Provisioning and Configuration task in
the Setup and Maintenance work area.
Note:
• If you already use a primary partner site where most of your candidates are sourced from, the Direct Apply
category might be a good solution for you. You can use it with as many approved partners as you want. Also,
when a single category must be used for a specific case, like resume parsing for a single language, with Direct
Apply you could use multiple partners to create job applications for a single job requisition, there's no limit.
• Verify with your Direct Apply partner if they can send the ID from your list of values or if they send free text.
If they send free text for degrees, certifications, and establishments, you might want to review the impact of
using a predefined list of values (because normally, you capture one or the other).
• Direct Apply only fills default sections.
• The zip file import isn't needed for LinkedIn integration, managed in the Profile Import configuration section.

Related Topics
• Set Up Partner Enablement
• Set Up Partner Integration Provisioning

---

## Send Status Notifications to Direct Apply Partners
*Chunk ID: OHR-REC-1122 | Chapter: Third Party Integration*

You can send notifications to Direct Apply partners to inform them of the status of their job applications.
You can configure a candidate selection process to automatically send notifications to Direct Apply partners when their
job applications are moved to a phase or state. You can select one of these delivered reference partner statuses:
• New
• Under Consideration
• Screening
• Interviewing
• Offer Extended
• Background Check
• Hired
• Rejected
• Withdrawn
Note: The New status might not be of any use for job applications, since the status of newly created job applications
is set to New. However, the New status can be used when partners create prospects. Validate with your partners if
they’ll use that scenario.
Here are special use cases for specific partners.
• Indeed is a partner in Profile Import. The Direct Apply activation is done separately. The Direct Apply partner
provides a .zip file.
• LinkedIn is a partner in Profile Import. However, the Direct Apply configuration is done in the Profile Import
area. LinkedIn requires customers to configure the notifications service to use this integration and they need to
have up-to-date job application statuses.
• For all other Direct Apply partners, you need to verify if they support job application notifications and upload
the appropriate .zip file accordingly.
• You don't need to map all phases and states, only those that are meaningful to partners and only at the entry
point, to avoid generating redundant traffic. For example, the mapping to the Offer Extended phase can be
done at the Extended state only, no need to map other states in the Offer phase, except for Withdrawn by
Candidate and Rejected by Employer states. If you're not always entering a phase with the first state, you can
place the notification trigger at the “When Entering Phase” level but keep the Rejected and Withdrawn status at
the specific Rejected by Employer and Withdrawn by Candidate state.
• You need to run the scheduled process “Send Candidate Screening Requests to Partners” to send notifications
to the partners.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration

---

## Third Party Integration
*Chunk ID: OHR-REC-1123 | Chapter: Third Party Integration*

2. On the Candidate Selection Process Configuration page, click an existing process.
3. Click a phase of the candidate selection process.
4. In the When Entering Phase menu or the Actions menu of a state, select Add Action > Send Direct Apply
Notification.
5. On the Action: Send Direct Apply Notification page, select a reference partner status.
6. Click Continue.

---

## Integration of Direct Apply with LinkedIn Apply Connect
*Chunk ID: OHR-REC-1124 | Chapter: Third Party Integration*

Direct Apply with LinkedIn Apply Connect allows job seekers to apply for jobs without leaving LinkedIn.
Job seekers can view jobs posted on LinkedIn. To apply for a job, they use the Easy Apply button on the job posting.
After clicking the Easy Apply button, LinkedIn presents an easy job application experience to job seekers. They can
upload their resume and respond to questions. They can review their job application and submit it on the LinkedIn
site. When job seekers submit their job application, their application is sent to the customer on Oracle Recruiting. Job
seekers can check the status of their job application on the LinkedIn site.
Recruiters can view the job application submitted by the candidate on the LinkedIn site within Oracle Recruiting. When
recruiters click LinkedIn preview, they can view the candidate profile which includes the LinkedIn applicant highlights.
They can also progress the candidate job application. The job application status is sent to LinkedIn as configured in the
candidate selection process.

---

## Set Up Direct Apply with LinkedIn Apply Connect
*Chunk ID: OHR-REC-1125 | Chapter: Third Party Integration*

Direct Apply with LinkedIn Apply Connect allows job seekers to apply for jobs without leaving LinkedIn.
Here's what to do
1.
2.
3.
4.
5.

Set up a default recruiting type in the candidate selection process.
Add the Send Direct Apply Notification action in the candidate selection process.
Request or update the LinkedIn integration.
Activate Apply Connect in Oracle Recruiting.
Run scheduled processes.

---

## Important Info
*Chunk ID: OHR-REC-1126 | Chapter: Third Party Integration*

To use Direct Apply with LinkedIn Apply Connect, the Automated Job Posting is required for staffing customers and
recommended for non-staffing customers.
• If Automated Job Posting isn't yet enabled:
◦ Enable Apply Connect in Oracle Recruiting.

◦ Wait 24 hours and then enable the Automated Job Posting in LinkedIn Recruiter. For details, see LinkedIn
Automated Jobs Set-Up for Apply Connect Note: Waiting 24 hours allows jobs to be synced using Apply
Connect API, at which point your automated job postings request can be done.

• If Automated Job Posting is enabled:
◦ Enable Apply Connect in Oracle Recruiting.

---

## Third Party Integration
*Chunk ID: OHR-REC-1127 | Chapter: Third Party Integration*

◦ Make sure the connection status of your Oracle Recruiting API source is "Posting active". For details,

see step 7 in LinkedIn Automated Jobs Set-Up for Apply Connect. Note: When connected, you can close
your manual jobs. This will help prevent duplicate jobs and ensure that all jobs are directly collecting
applications into Oracle Recruiting using Apply Connect.

---

## Set Up a Default Recruiting Type in a Candidate Selection Process
*Chunk ID: OHR-REC-1128 | Chapter: Third Party Integration*

You need to set up a default recruiting type in a candidate selection process. This is done while editing the properties of
the selection process.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Candidate Job Applications
◦ Task: Candidate Selection Process Configuration

2.
3.
4.
5.

On the Candidate Selection Process Configuration page, click an existing process.
On the process page, click Edit Process Properties.
In the Context Information section, add a recruiting type and set it as Default.
Click Save and Close.

---

## Add the Send Direct Apply Notification Action in a Candidate Selection
*Chunk ID: OHR-REC-1129 | Chapter: Third Party Integration*

Process
When a candidate applies for a job on LinkedIn using Easy Apply, LinkedIn sends the job application to Oracle
Recruiting. Once Oracle Recruiting receives the job application, LinkedIn needs to be informed of the status of the
candidate application in Recruiting.
You need to decide for which statuses you want to send a status notification to LinkedIn. This is done by adding the
Send Direct Apply Notification action to the state of a phase. You can add that action to any state within phases.
1. Click a phase of the candidate selection process.
2. In the States for Phase section, click the Actions menu next to a state, then select Add Action > Send Direct
Apply Notification.
3. On the Action: Send Direct Apply Notification page, select a reference partner status.
4. Click Continue.
5. Click Save and Close.
Once this is configured, the recruiter will need to select a candidate selection process with a default recruiting type and
the Send Direct Apply Notification action.
Note: It's recommended to configure all candidate selection processes with the Send Direct Apply Notification action
at all appropriate phases and states so that candidates can view their progress on LinkedIn.

---

## Request or Update the LinkedIn Integration
*Chunk ID: OHR-REC-1130 | Chapter: Third Party Integration*

1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration

---

## Third Party Integration
*Chunk ID: OHR-REC-1131 | Chapter: Third Party Integration*

2. On the Category Provisioning and Configuration page, go to the Profile Import section and click Edit.
3. On the Profile Import Partners page, go to the LinkedIn section.
4. If the LinkedIn application isn't created, click Request Integration.
a. Complete the fields.
b. Click Start Activation. The Client ID and Client Secret fields are populated.
5. If the LinkedIn application already exists, click Update Integration.
a. Select the contract name.
b. Select the Enable Apply Connect check box and save changes.

---

## Activate Apply Connect in Oracle Recruiting
*Chunk ID: OHR-REC-1132 | Chapter: Third Party Integration*

1. Identify the integration user name to be used for Apply Connect integration and confirm the user has access to
the Direct Apply services.
◦ Confirm the job role assigned is enabled for access from all IP addresses by selecting the check box if you
have enabled Location Based Access Control.
Note: For details on the duty role and privileges required, see the User Security chapter in the Direct Apply
Partner guide on My Oracle Support (ID 2627681.1).
2. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration

3. On the Category Provisioning and Configuration page, go to the Profile Import section and click Edit.
4. On the Profile Import Partners page, go to the Apply Connect section. Update integration will launch the
onboarding widget where you turn on Apply Connect on LinkedIn to get the widgets.
5. Enter the Oracle Recruiting integration user name and password.
6. Select the Enable Easy Apply check box.
7. Select the Active check box.
8. Click Save.

---

## Run Scheduled Processes
*Chunk ID: OHR-REC-1133 | Chapter: Third Party Integration*

You need to run these schedules processes:
• Synchronize LinkedIn Data. This is used to synchronize data between LinkedIn Recruiter System Connect,
Direct Apply, and Oracle Recruiting. The recommended frequency is every hour.
• Send Candidate Screening Requests to Partners: This is used to send requested candidate assessments and tax
credit screening to selected partners. Sends screening notifications to partners supporting notifications. The
recommended frequency is every 10 minutes.
Note: It's recommended to run an end-to-end test after enabling the integration to confirm Easy Apply is enabled
for the jobs posted on LinkedIn, and the apply for the job and confirm application delivery from LinkedIn to Oracle
Recruiting is successful.

---

## Tips and Considerations
*Chunk ID: OHR-REC-1134 | Chapter: Third Party Integration*

• It's recommended to configure all candidate selection processes with the Send Direct Apply Notification action
at all appropriate phases and states so that candidates can view their progress on LinkedIn.

---

## Third Party Integration
*Chunk ID: OHR-REC-1135 | Chapter: Third Party Integration*

• Easy Apply from LinkedIn supports these application flow blocks: Contact Information, Supporting Documents,
Education, Experience, Job Application Questions.
• It's recommended to configure the Request Information flow to collect more information using the Contact
Information, Address, Sensitive Personal Information, Diversity, Disability, Veteran blocks. These blocks can be
presented to candidates several times.
• Skills required for a job requisition are included in the job data synced with LinkedIn.
• Source tracking is enhanced to capture the source medium as job aggregator and source name as LinkedIn
Direct Apply. It's recommended to use source tracking information to configure the Request Information flow to
collect more information.
• Requisition description that has a minimum of 100 characters and requisitions in English or with English
translations are synced with LinkedIn.
• Requisition status in Open - Posted are synced with LinkedIn.
• Requisition must not be confidential to publish the job on LinkedIn (the setting Allow candidates to apply when
not posted in the requisition is set to No).
• Supported question types are Text, Single Choice, and Multiple Choice.
• The No Response question type isn't supported. Alternately, you can configure a single choice question with a
single value like Yes, Accept, Confirm.
• Text question type with rich text response isn't supported. Alternately, you can define the response type as text.
• Text question type with response type as text and min and max length isn't supported. Alternately, you can
remove the min and max restrictions.
• Text question type with response type as date and min and max date isn't supported. Alternately, you can
remove the min and max restrictions.
• Multiple Choice question type with min and max response isn't supported. Alternately, you can split to multiple
questions of single choice.

Related Topics
• Partner Integration Guides on My Oracle Support

---

## Set Up Direct Apply with LinkedIn Apply Connect in NonRecruiter Mode
*Chunk ID: OHR-REC-1136 | Chapter: Third Party Integration*

You can set up the non-recruiter mode for the Direct Apply with LinkedIn Apply Connect. This is done by adding your
company URL when setting up the integration and posting jobs on LinkedIn using that URL.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration

2. On the Category Provisioning and Configuration page, go to the Profile Import section and click Edit.
3. On the Profile Import Partners page, go to the LinkedIn section.
4. In the Application Name field, enter a name for the application.

---

## Third Party Integration
*Chunk ID: OHR-REC-1137 | Chapter: Third Party Integration*

5. Click Start Activation Process. When the activation is complete, the Apply Connect section is populated.
6. In the Apply Connect section, enter the company URL.
7. Select the Enable Easy Apply check box if you want the Easy Apply feature to be available on LinkedIn.
8. Select the Send notification to candidate check box to send candidate notifications on the LinkedIn site.
9. Enter a user name and password.
10. Select the Active check box.
11. Click Save.
12. Run the Synchronize LinkedIn Data scheduled process.

---

## Integration with LinkedIn Recruiter System Connect
*Chunk ID: OHR-REC-1138 | Chapter: Third Party Integration*

Your organization might decide to integrate with Recruiter System Connect for sharing transactional recruiting data
between Oracle Fusion Cloud Recruiting and LinkedIn Recruiter.
In LinkedIn Recruiter, recruiters can:
• See if LinkedIn members have a candidate profile in Oracle Recruiting.
• See if LinkedIn members have already applied to jobs.
• View job applications of those members and their progression within the selection process.
• Use the Send InMail feature to interact with prospects. These emails also appear in Oracle Recruiting.
• Use the Notes feature to enter comments. These notes also appear in Oracle Recruiting.
• View interview status and dates, recommendations, and reason for rejection using the In-ATS indicator.
• Export LinkedIn member profiles to Oracle Recruiting and attach them to specific requisitions as prospect.
• Review the Recommended Matches who match your job description. Recommended Matches are candidate
recommendations tailored to an open job requisition and optimized based on recruiting team members'
feedback.
• Use the 1-Click Export feature to export a candidate that isn't in Oracle Recruiting and create a prospect for
a specific job requisition. When a recruiter exports a candidate, LinkedIn sends some basic information like
first name, last name, email, phone based on what's available and shared by the candidate. Because of the
continuous sync process on Oracle Recruiting side, if the candidate provides email or phone to LinkedIn, that
data will be synced as such at that time.
Note: When syncing candidates from Oracle Recruiting to LinkedIn, all candidates' external profile will be directed to
the career site URL.
In Oracle Recruiting, recruiters can:
• View the LinkedIn profile of candidates.
• Create candidates using basic profile data from InMails.
• Access InMails and Notes, within Interactions, sent to candidates from LinkedIn Recruiter. In addition, Prospects
Interactions are available from Recruiting activity as part of LinkedIn profile widget.
Below are requirements that need to be satisfied for a job requisition to be available in Export to ATS.
• Requisition status is Open - Posted.

---

## Third Party Integration
*Chunk ID: OHR-REC-1139 | Chapter: Third Party Integration*

• Requisition isn't confidential (the setting Allow candidates to apply when not posted in the requisition is set to
No).
• Requisition description has a minimum of 100 characters.
• Recruiter signed in in LinkedIn is part of the Hiring team.
• Recruiter is mapped to one of the Recruiter LinkedIn seat.
If you have questions about the integration, see the document FAQs for LinkedIn Recruiter System Connect Integration
on My Oracle Support (ID 2693159.1).
Related Topics
• FAQs for LinkedIn Recruiter System Connect Integration

---

## Enable the Integration with LinkedIn Recruiter System
*Chunk ID: OHR-REC-1140 | Chapter: Third Party Integration*

Connect
You can integrate with Recruiter System Connect for sharing transactional recruiting data between Oracle Fusion Cloud
Recruiting and LinkedIn Recruiter.
To enable the LinkedIn Recruiter System Connect integration, you need to have your own LinkedIn application (client_id)
for each environment you need to test. This ensures that the data isn't damaged across environments (staging, test,
production).
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2.
3.
4.
5.
6.

On the Category Provisioning and Configuration page, click the Edit icon next to Profile Import Partners.
On the Profile Import Partners page, go to the LinkedIn section.
By default, the Create LinkedIn Customer Application option is selected.
Enter the application name.
Click Start Activation Process. The LinkedIn app is created using the LinkedIn API, which creates the app and
returns the Client ID and Client Secret. The Client ID and Client Secret are displayed and can't be modified.
You now need to configure LinkedIn Administration settings.
1. Go to http://www.linkedin.com and navigate to LinkedIn Recruiter > Profile Picture > Administration
settings > ATS tab.
2. Find the partner service you just created.
3. Ensure that the ATS client name on the screen is identical to the Application Name created in Oracle Recruiting
Cloud.
4. Ensure that the following settings are enabled. The LinkedIn Recruiter System Connect partner service in Oracle
Recruiting can't be enabled if these two settings are disabled.

◦ Contract Level access (for every seat on this contract).
◦ Company Level access (for every contract in your company).
5. When LinkedIn Recruiter is successfully enabled, the integration status in Oracle Recruiting displays Enabled.

Note: Below are requirements for a job requisition to be available in Export to ATS:
• Requisition posted date must be after 1-1-70.
• Requisition shouldn't be a pipeline requisition.
You need to map at least one LinkedIn Recruiter to a Recruiting user to enable and start the one-time full
synchronization process.
1.
2.
3.
4.
5.

Go to LinkedIn Recruiter System Connect Contracts and click Map Seats.
Click Request Recruiter Seats to fetch all the recruiter seats.
Assign LinkedIn recruiter seats to Oracle Recruiting users and click Save.
When users are mapped, activate the contract and accept the terms and conditions.
Enable the LinkedIn Profile Import and LinkedIn Recruiter System Connect at the same time. LinkedIn Profile
Import or LinkedIn Recruiter System Connect can't be activated alone.
6. Save the configuration to active the integration.
7. Schedule and start the process called Synchronize LinkedIn Data. This will start the full synchronization of
data between Oracle Recruiting and LinkedIn Recruiter. Based on the volume of the data, the synchronization
will take between 6 hours to a few days. When the full synchronization is complete, users can start using the
integration features both in LinkedIn RSC and Oracle Recruiting. The frequency of the scheduled process is
every hour.
LinkedIn Recruiter System Connect API helps to synchronize jobs, candidate applications, and candidates between
Oracle Recruiting and LinkedIn. The following synchronization settings are optimized for data transfer. We strongly
recommend to not change these settings.

---

## Prospect Interactions Synchronization
*Chunk ID: OHR-REC-1141 | Chapter: Third Party Integration*

Frequency in Hours

4 hrs (Oracle Recruiting will fetch prospect interactions based on this setting)

---

## LinkedIn might change these API limits from time to time and we encourage you to review LinkedIn RSC documentation
*Chunk ID: OHR-REC-1142 | Chapter: Third Party Integration*

for more information.
By default, all jobs are sent as private and are only visible in your LinkedIn products. The setting Send Job Requisitions
as Private controls this behavior. If you want jobs to be set as public and appear to job seekers on LinkedIn.com, you
need to disable the setting.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience

---

## Third Party Integration
*Chunk ID: OHR-REC-1143 | Chapter: Third Party Integration*

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration
2. On the Category Provisioning and Configuration page, click the Edit icon next to Profile Import Partners.
3. On the Profile Import Partners page, go to the LinkedIn Recruiter System Connect under Social Media, and click
Synchronization Settings.
4. To have jobs appear on LinkedIn, deselect the setting Send Job Requisition as Private.
Note: LinkedIn doesn't have a staging or testing environment. All the testing of the Recruiter System Connect
functionality is done in LinkedIn production, which means jobs synchronized as public will be available on
LinkedIn.com, all Recruiter System Connect features enabled on a particular contract will be visible to all users on that
contract. Recruiter System Connect is a ready-to-use activation. To test the Recruiter System Connect functionality,
you need to contact your LinkedIn CSM.
If you have enabled Location Based Access Control, you must allow a set if IP ranges provided by LinkedIn. This is
required for 1 click export to send limited information from LinkedIn member profiles to Oracle Recruiting. For the set of
LinkedIn IP addresses, see the FAQs for LinkedIn Recruiting System Connect Integration document (DOC ID 2693159.1)
available on My Oracle Support.
It's possible to delete the LinkedIn application and reset the settings using the Delete Application profile option. This
isn't intended for regular use and must be used only in the case of data corruption (for example due to Productionto-Test - P2T). As a general practice, you should have a separate LinkedIn application key across the environments. By
default, the Delete Application profile option isn't visible in the LinkedIn Application area. To use it, you need to create a
profile option and enable it.
Note: An error will occur in the Profile Import Partner page if a recruiter is mapped on two different LinkedIn
contracts at the same time.
1.
2.
3.
4.
5.

In the Setup and Maintenance work area, click the Tasks icon.
Click Search.
Search for the task Manage Administrator Profile Values.
Click the task name.
On the Manage Administrator Profile Values page, search for the profile option code
IRC_RSC_ALLOW_DELETE.
6. When it appears in the Search Results section, select it.
7. Click the New icon to add a new profile value.
8. Select the Site profile level.
9. Enter Y in the Profile Value field.
10. Click Save and Close.
You can enable the LinkedIn Recommended matches feature.
1. In the Setup and Maintenance work area, go to:
◦ Offering: Recruiting and Candidate Experience

◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Category Provisioning and Configuration

2. On the Category Provisioning and Configuration page, click Edit next to Profile Import Partners.
3. In the Recommended Matches section, select the Active option.
Related Topics
• FAQs for LinkedIn Recruiter System Connect Integration (DOC ID 2693159.1)

---

## Enable the LinkedIn Embedded Candidate Search
*Chunk ID: OHR-REC-1144 | Chapter: Third Party Integration*

You can configure the candidate search in Recruiting so that recruiters can find more candidates using the LinkedIn's
search functionality that is embedded in the Candidate Search page.
Before you start
The LinkedIn Recruiter System Connect (RSC) feature must be enabled, and the Full Synchronization status should bet
set to Completed.
Here's what to do
1. In the Setup and Maintenance work area, go to:
a. Offering: Recruiting and Candidate Experience
b. Functional Area: Recruiting and Candidate Experience Management
c. Task: Recruiting Category Provisioning and Configuration
2. On the Partner Integration Provisioning page, click Edit next to Profile Import Partners.
3. Select the Active check box in the LinkedIn Recruiter System Connect section.
4. Ensure that the Full Synchronization status shows as Completed.
Results:
The Search in LinkedIn Recruiter link is displayed on the candidate search results page. Clicking this link takes recruiters
to the LinkedIn search page, where they can search and browse for LinkedIn profiles.
If you searched using a set of keywords on the Candidate Search page, clicking the LinkedIn search link displays
candidate search results based on those same sets of keywords.
Note: When you click the LinkedIn search link, the Recruiter login page opens if you didn’t previously log in. Enter
your credentials and select the contract type to view the LinkedIn search page.

---

## Enable Chatbot
*Chunk ID: OHR-REC-1145 | Chapter: Third Party Integration*

You can use a digital assistant to interact with HCM and Oracle Recruiting Cloud by downloading skills available from the
Oracle Digital Assistant skill store.
Oracle Fusion Cloud Recruiting supports Candidate Experience, Internal Candidate Experience, and Hiring Skills.
• The Candidate Experience skill integrates with Oracle Recruiting. It enables candidates to search for jobs, check
their job application status, withdraw their job application, or delete their profile.
Note: The Candidate Experience skill must be hosted in its own digital assistant. It can't be combined with
any other skills because it's an external candidate focused skill.
• The Internal Candidate Experience skill integrates with Oracle Recruiting. It enables internal candidates to
search for jobs, check their job application status, or withdraw their job application. The Internal Candidate
Experience skill can be part of the digital assistant with other skills like Hiring and HCM.

---

## Third Party Integration
*Chunk ID: OHR-REC-1146 | Chapter: Third Party Integration*

• The Hiring skill integrates with Oracle Recruiting. It enables recruiters and the Hiring Team to check job
requisition status, candidate status, and review any pending job offers. The Hiring skill can be combined with
other skills like HCM and Approvals, and is part of the HCM Applications Digital Assistant.
Related Topics
• Introduction to Oracle Digital Assistant for HCM

---

## Scheduled Processes for Recruiting
*Chunk ID: OHR-REC-1147 | Chapter: Third Party Integration*

33 Scheduled Processes for Recruiting
Scheduled Processes in Oracle Recruiting Cloud
Scheduled processes are available for specific business needs in Oracle Recruiting Cloud. You can schedule and run
processes in the Scheduled Processes work area (Tools > Scheduled Processes). For details, see Which scheduled
processes are used in Recruiting?

---

# Security for Recruiting

## Scheduled Processes for Recruiting
*Chunk ID: OHR-REC-1148 | Chapter: Security for Recruiting*

Security in Oracle Recruiting Cloud
The security of Oracle Fusion Cloud Recruiting is consistent with the other Oracle Application Cloud offerings.
Specific roles are predefined and it's highly recommended that you use them as a starting point to create your own
versions of roles.
Data roles are mandatory to perform all recruiting activities. Without data roles, visibility of main objects will be
limited to ownership, while various list of values will be empty, preventing the creation of various entities. Properly
understanding and managing data roles is a crucial step of implementing Oracle Recruiting.
Related Topics
• Securing HCM
• Security Reference for HCM

---

## Recruiting Roles
*Chunk ID: OHR-REC-1149 | Chapter: Security for Recruiting*

The primary user roles in Oracle Fusion Cloud Recruiting are described below.
For more details about each of these roles, see the Security Reference for HCM guide available on docs.oracle.com.

Role

Description

---

## The Hiring Manager role has access to a limited set of recruiting features such as initiating the job
*Chunk ID: OHR-REC-1150 | Chapter: Security for Recruiting*

requisition creation process, approving the job requisition, viewing candidate applications, approving
job offers. The Hiring Manager accesses Hiring under My Team.
This role usually has limited visibility on objects based on ownership.

---

## The Recruiter role has a broader access to recruiting features, which includes tasks such as creating job
*Chunk ID: OHR-REC-1151 | Chapter: Security for Recruiting*

requisitions, managing candidate flows, creating job offers. The Recruiter accesses Hiring under My
Client Groups.
This role has limited visibility on objects but can get broader security profiles as defined by the security
administrator.

---

## Recruiting Manager - Job role
*Chunk ID: OHR-REC-1152 | Chapter: Security for Recruiting*

The Recruiting Manager role can perform all recruiting tasks.
This role inherits all capabilities of the Recruiter role but has a few more capabilities such as:
• Manage Candidate Job Application Lists
• Manage Job Requisition Interview Schedule Before Job Formatting Phase
• Update Candidate Job Offer Letter

---

## Security for Recruiting
*Chunk ID: OHR-REC-1153 | Chapter: Security for Recruiting*

Description
• Update Job Requisition After Draft Phase
• View Confidential Questionnaire Responses
• View External Candidate Sensitive Information
• Manage Job Offer by Recruiting Manager
• Recruiting Manager Reporting Duty
• Manage External Candidate Sensitive Information

---

## The Recruiting Administrator role performs functional configurations in the Setup and Maintenance
*Chunk ID: OHR-REC-1154 | Chapter: Security for Recruiting*

work area. This includes questions and requisition templates management.
• List of Values are moving toward REST services that are secured.

---

## Recruiting Agent - Job role
*Chunk ID: OHR-REC-1155 | Chapter: Security for Recruiting*

The Recruiting Agent role has access to the Agency Portal.
Creates candidate flows.

---

## None of these roles provides access to internal career sites. That access is assigned to the Employee and Contingent
*Chunk ID: OHR-REC-1156 | Chapter: Security for Recruiting*

Worker roles. Users who only have recruiting roles can't access internal career sites and therefore can't perform actions
such as apply to jobs, refer candidates, answer interview requests, and preview offer letters without direct access to
Recruiting.
Related Topics
• Role Types
• Security Reference for HCM

---

## Security Profiles Used in Recruiting Roles
*Chunk ID: OHR-REC-1157 | Chapter: Security for Recruiting*

The table describes the security profiles used for each recruiting role.
For more details about security profiles, see the Securing HCM guide available on docs.oracle.com.

---

## Candidate Selection Profile
*Chunk ID: OHR-REC-1158 | Chapter: Security for Recruiting*

• Applies only to candidate search.

Recruiter
Recruiting Manager

• Applies to search parameters of the
Rest service recruitingCandidates.
There's no data security when calling
the service using the candidate
number or the person ID.
• Only valid when the profile option
ORA_IRC_CANDIDATE_SECURITY_
ENABLED is set to Y.
Country Security Profile

---

## Job Requisition Security Profile
*Chunk ID: OHR-REC-1159 | Chapter: Security for Recruiting*

• To view job requisitions.
• The team and subordinate selections
on the security profile apply only
when this profile option is set to
Y. When set to N (default value),
team and subordinates are always
included.
Job Requisition Security Profile
• To delete job requisitions.

---

## Hiring Manager
*Chunk ID: OHR-REC-1160 | Chapter: Security for Recruiting*

Recruiter
Recruiting Manager

Recruiter
Recruiting Manager

• Only valid when the profile option
Requisition Update Data Security
Enabled is set to Y.
• The team and subordinate selections
on the security profile apply only
when this profile option is set to Y.
Job Requisition Security Profile
• To update job requisitions.

Recruiter
Recruiting Manager

• Only valid when the profile option
Requisition Update Data Security
Enabled is set to Y.
• The team and subordinate selections
on the security profile apply only
when this profile option is set to Y.
Organization Security Profile
• To select the recruiting organization.
• To select job requisition templates if
they have recruiting organizations.
• To select the business unit, legal
employer, and department in list of
values in various places, including
filters.

---

## Recruiting Manager
*Chunk ID: OHR-REC-1161 | Chapter: Security for Recruiting*

• To edit job offers.
Position Security Profile
• To select a position in a job
requisition.

---

## Security for Recruiting
*Chunk ID: OHR-REC-1162 | Chapter: Security for Recruiting*

Used by Role

• To select a position in a job offer.
Public Person Security Profile
• To select users in the hiring team.
• To select users in the offer team.
• To select users in filters.

---

## Hiring Manager
*Chunk ID: OHR-REC-1163 | Chapter: Security for Recruiting*

Recruiter
Recruiting Manager
Recruiting Administrator

Recruiter
Recruiting Manager

• For Redwood user experience only.

---

## Create the Recruiting Administrator View All Data Role
*Chunk ID: OHR-REC-1164 | Chapter: Security for Recruiting*

To implement Oracle Fusion Cloud Recruiting and before creating data roles for the various users, you must create a
Recruiting Administrator View All data role.
Prerequisite: You need to sign in as a TechAdmin user.
1. In the Setup and Maintenance work area, search for the task Assign Security Profiles to Role.
2. On the Data Roles and Security Profiles page, in the Search Results section, click Create.
3. On the Create Data Role: Select Role page, complete the fields as follows.
◦ Data Role: Recruiting Administrator View All

◦ Job Role: Recruiting Administrator
4. Click Next.
5. On the Create Data Role: Security Criteria page, select these predefined security profiles.
◦ Organization: View All Organizations

◦ Person: View All People
◦ Public Person: View All People
◦ Job Requisition: View All Job Requisitions
6. Click Review.
7. On the Create Data Role: Review page, click Submit.
8. On the Data Roles and Security Profiles page, search for the Recruiting Administrator View All data role to
confirm that it was created successfully.
9. In the Security Console, assign the data role to the user implementing Oracle Recruiting.
Related Topics
• Overview of Securing Oracle HCM Cloud

---

## Job Requisition Security Details
*Chunk ID: OHR-REC-1165 | Chapter: Security for Recruiting*

The aggregated privilege View Job Requisition (ORA_IRC_VIEW_JOB_REQUISITION) is assigned by default to the Hiring
Manager and Recruiter roles.
The ability to view job requisitions is also controlled by data security policies. There are two main dimensions to
understand:
• The job requisition's Hiring Team

◦ If you're a direct member, sometimes called "ownership of the requisition".
◦ If one of your subordinates is part of the Hiring Team.
• The job requisition's security profile

◦ This is an empty set by default, until a data role is created.
By default, the Hiring Manager role can only view job requisitions they own and job requisitions of their subordinates.
This also applies to the Recruiter role, although that role should have a data role with a properly defined job requisition
security profile so that additional requisitions be visible through it.
Security profiles are defined differently depending on the business object. For job requisitions, the security profile is
defined using these areas of responsibility dimensions:
• Recruiting Organization
• Recruiting Location
• Job Family
• Job Function
• Recruiting Type
These dimensions are defined at the requisition security profile level. The values they cover are defined for each
recruiter within their area of responsibilities. The data covered by the dimensions selected in the security profile is
redirected to each user with this data role and relies on the user's areas of responsibility.
If the ORA_IRC_REQUISITION_UPDATE_DATA_SECURITY_ENABLED profile option is set to Y, then the other options
for the role played in the job requisition, like recruiter, hiring manager, or collaborators, can be controlled as well as the
visibility of subordinate requisitions.
The same data security applies to the privilege Update Job Requisition (ORA_IRC_UPDATE_JOB_REQUISITION) when
the profile option is set to its default value N. This privilege is assigned to the Recruiter role by default. It's not assigned
to the Hiring Manager role. A data role that has both the View Job Requisition (ORA_IRC_VIEW_JOB_REQUISITION) and
Update Job Requisition (ORA_IRC_UPDATE_JOB_REQUISITION) privileges will edit the same set of job requisitions that
they can view.
As soon as the profile option is set to Y, then the Update Job Requisition (ORA_IRC_UPDATE_JOB_REQUISITION) and
Delete Job Requisition (ORA_IRC_DELETE_JOB_REQUISITION) function privileges are no longer sufficient; the system
relies on the aggregate privileges of the same name and the requisition security profile. This allows to create a different
set of updatable or deletable job requisitions.

---

## Job Requisition Template Security Details
*Chunk ID: OHR-REC-1166 | Chapter: Security for Recruiting*

There is no data security policy to view or update job requisition templates.
Requisition templates are managed in the Setup and Maintenance work area using the Job Requisition Templates task.
All templates are visible to users who can access this task. The task is controlled by the privilege Manage Recruiting
Administration (IRC_MANAGE_RECRUITING_ADMINISTRATION_PRIV), granted to the Recruiting Administrator role by
default.
To select a recruiting organization while creating a job requisition template, the user must be assigned a role with an
organization security profile.

---

## Job Application Security Details
*Chunk ID: OHR-REC-1167 | Chapter: Security for Recruiting*

The ability to view job applications is tied to both the job requisition visibility and the job offer visibility.
In general, the job requisition visibility is broader than the job offer visibility. Because the job requisition's Hiring Team
might be different from the job offer team, a user who can view a job offer might not have access to the original job
requisition where the job application was created. However, the user will be able to view the job application associated
with those offers.
A user with access to a set of job requisitions might not have access to any job applications. By default:
• The Hiring Manager role has the View Non-Restricted Candidate Job Application
(ORA_IRC_VIEW_NON_RESTRICTED_CANDIDATE_JOB_APPLICATION) aggregate privilege
• The Recruiter role has the View Candidate Job Application (ORA_IRC_VIEW_CANDIDATE_JOB_APPLICATION)
aggregate privilege
The difference is that if restricted phases are defined in the candidate selection process, the Hiring Manager role won't
see job applications until they're moved out of these phases.
There's no need to define data security policies to view job applications from the Requisitions list. Only the concept of
restricted phases applies. The conditions for those two aggregate privileges are:
• For unrestricted job applications for the job requisitions and job offers I can see
• For all job applications for the job requisitions and job offers I can see
These conditions will apply in all contexts where you can see job applications, including the Activity tab of candidates.

---

## Job Offer Security Details
*Chunk ID: OHR-REC-1168 | Chapter: Security for Recruiting*

The aggregate privilege View Job Offer (ORA_IRC_VIEW_JOB_OFFER) is assigned by default to the Hiring Manager,
Recruiter, and Recruiting Manager roles.
The Hiring Manager and Recruiter roles only have access to job offers for which they or their subordinates are part of
the job offer team. To view and update job offers for which they're not part of the offer team, a duty role is required:

Manage Job Offer by Recruiting Manager (ORA_IRC_MANAGE_JOB_OFFER_BY_RECRUITING_MANAGER). By default,
this duty role is assigned to the Recruiting Manager role.
Tip: You can define two data roles for a single user, one data role to view and one to edit, and have the view data role
based on a broader security profile. This would allow seeing many items and updating only a subset of them. This can
be done for all view and update data privileges.
Here's a summary of the job offer's aggregate privilege delivered by default to recruiting roles.

---

## Recruiting Manager
*Chunk ID: OHR-REC-1169 | Chapter: Security for Recruiting*

User
Subordinates
Based on the Person Security Profile (includes
viewing and updating the entire job offer and
job offer's salary and other compensation
sections as well as canceling and redrafting job
offers.)

---

## To view the content of job offers while approving them, the view conditions must be assigned to users. While the Hiring
*Chunk ID: OHR-REC-1170 | Chapter: Security for Recruiting*

Manager role can typically view at least the offers that their subordinates can access, users outside of the hierarchy may
not have access to any offers that they're asked to approve. If that's the case, you can assign the Manage Job Offer by
Recruiting Manager duty role or create your own duty role, to enable viewing offers for approval throughout the user's
person security profile.
Here are the steps to create your own duty role:
1. Click Navigator > Tools > Security Console.

---

## Security for Recruiting
*Chunk ID: OHR-REC-1171 | Chapter: Security for Recruiting*

2.
3.
4.
5.
6.
7.
8.

Click the Roles tab.
Search for the duty role Manage Job Offer by Recruiting Manager.
Click the Actions menu and select Copy Role.
Select Copy top role.
Click Copy Role.
Remove the update data security policies.
Assign this new duty role to approvers who aren't hiring managers so they can view the job offer content if
they're requested to approve it.
This view capability for users outside the offer team is important if:
• They need to review the job offer content before approving it, which is desirable.
• They need to click the link in the approval notification to view the candidate's offer letter.
These privileges and data access are required:
• View Job Offer, to see the recruiting and assignment content of the job offer.
• View Job Offer Salary, for the salary related info of the offer.
• View Job Offer Other Compensation, for any compensation plans and options of the offer.
• View Job Requisition, for any job requisition content that might be included in the notification.
• Internal career site access, so there is a landing page if there's a link to the job offer letter within the notification.
Note: For the Human Resource Manager role accessing job offers using the task Manage Job Offer, you need to
review the Address Job Offer aggregate privilege security.

Related Topics
• How You Secure Access to Candidates with Job Offers in Manage Job Offer Task

---

## Candidate Security Details
*Chunk ID: OHR-REC-1172 | Chapter: Security for Recruiting*

There is an optional candidate security profile needed to search candidates, if the profile option
ORA_IRC_CANDIDATE_SECURITY_ENABLED is enabled.
Consider the following:
• Candidates are always visible when the profile option is set to its default value of not being enabled. Once
enabled, the returned candidates will be limited to the candidate security profile definition.

◦ Users without access to the candidate search can only view candidates and candidate job applications in
their folders.

• Personal email, home phone, National ID, date of birth, and address are visible only for external candidates.

◦ For internal candidates, the work email, phone, and email are displayed
◦ This is also true in reporting.

---

## Candidate Pool Security Details
*Chunk ID: OHR-REC-1173 | Chapter: Security for Recruiting*

Candidate pool security is based on ownership. When you create a candidate pool, the pool is set to Private by default.
But the pool owner can grant other users access to the pool content.
To support data security for candidate pools and allow some roles to view, report, or select all pools, an aggregate
privilege is available: Manage Candidate Pool (IRC_MANAGE_CANDIDATE_POOL). This aggregate privilege contains
both the functional privilege and the data privilege.
You organization might need to give some specific people a super-user access to candidate pools so that they can
perform any action related to any candidate pools, though the person isn’t an owner of the candidate pool.
As an IT Security Manager, you can grant access to all pools through data security using the Security Console for
managing, selecting, or reporting candidate pools.
• Security business object: Candidate Pool
• Aggregate privilege: Manage Candidate Pool (ORA_IRC_MANAGE_CANDIDATE_POOL)
• Data privilege: Manage Candidate Pool Data (IRC_MANAGE_CANDIDATE_POOL_DATA)
• Data privilege: Choose Candidate Pool Data (IRC_CHOOSE_CANDIDATE_POOL_DATA)
• Data privilege: Report Candidate Pool Data (IRC_REPORT_CANDIDATE_POOL_DATA)
Using the Security Console, edit the data role to which you want to grant full access to candidate pools and create a new
data security policy. In the Create Data Security Policy, configure the fields as follows:
• Data Resource: Select Candidate Pool as the business object.
• Data Set: Select All values for the data set.
• Actions: Select the actions you want: Choose Candidate Pool, Manage Candidate Pool, Report Candidate Pool.

---

## Campaign Security Details
*Chunk ID: OHR-REC-1174 | Chapter: Security for Recruiting*

Campaigns are similar to candidate pools. Only the campaign owner can see the content of the campaign by default.
By default, the Recruiter and the Recruiting Manager roles have this aggregate privilege:
• View Recruitment Campaign (ORA_IRC_VIEW_RECRUITMENT_CAMPAIGN)
An orphan aggregate privilege granting access to all campaigns is available:
• View All Recruitment Campaigns (ORA_IRC_VIEW_ALL_RECRUITMENT_CAMPAIGNS)

---

## Approval Security Details
*Chunk ID: OHR-REC-1175 | Chapter: Security for Recruiting*

Approvals have the same data security constraints as viewing content. Users can approve job requisitions and offers
without seeing their content, which might not be desirable.

---

## If you want a role to approve job requisitions and offers while seeing their content, you need to assign the right
*Chunk ID: OHR-REC-1176 | Chapter: Security for Recruiting*

aggregate privileges and duty roles:
• View Job Offer (ORA_IRC_VIEW_JOB_OFFER)
• View Job Offer Salary (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• View Job Offer Other Compensation (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• View Job Requisition (ORA_IRC_VIEW_JOB_REQUISITION)

---

## Reporting Security Details
*Chunk ID: OHR-REC-1177 | Chapter: Security for Recruiting*

Reporting security is aligned with the product security most of the time. There are a few variations, but data access is
managed by reporting data privileges, not product data privileges.
For example, instead of the privilege View Job Offer Data (IRC_VIEW_JOB_OFFER_DATA), the role will need the privilege
Report Job Offer Data (IRC_REPORT_JOB_OFFER_DATA).

---

## Oracle BI Publisher Security Details
*Chunk ID: OHR-REC-1178 | Chapter: Security for Recruiting*

In general, BI Publisher reports are secured using the product security, not the reporting security. This is the case for
delivered data models.
As an example, the approval notification and the job offer letters are generated using BI Publisher through secured data
models.
BI Publisher report writers can create custom data models, secured or not, depending on the content. Standard BI
Publisher reports are secured based on the product and user access. If report writers create custom reports, you need
to check within them if the reports are secured or not and which objects are used when they're secured. Recruiting
and general HCM security will differ in some cases, mainly with Personal Identifiable Information. Personal email,
phone, and address are secured but unlocked for external candidates in Recruiting (that info is required in the recruiting
process), while it's highly protected in HCM. Make sure you know which data model is used and how it's secured.

---

## Personalization Using Transaction Design Studio
*Chunk ID: OHR-REC-1179 | Chapter: Security for Recruiting*

35 Personalization Using Transaction Design
Studio
How You Configure Recruiting Pages Using Transaction
Design Studio
You use Transaction Design Studio to create rules for configuring Recruiting pages. You can create rules to display or
hide sections and fields applicable to your business. You can change the required status of optional attributes.
When you create a rule, you perform these main steps:
• Select the action to configure a page.
• Provide basic details such as the name, description, recruiting type, country, role, legal employer. The fields
vary according to the action selected.

◦ When you select a recruiting type, the rule applies only to job requisitions, job applications, or job offers
◦

◦

with the same recruiting type.
When you select a country, the rule applies only to job requisitions for which one of the locations is part
of this country. The Primary Location or one of the Other Locations must be part of the selected country.
For example, you select the country "United States". A requisition's location is Pleasanton, California, US.
The rule applies to this requisition. In the case of job offers, when a rule is created for a specific country, it
applies to job offers for which the legal employer is part of the selected country.
When you select a role, the rule applies to the selected role. If you don't select a role, the rule applies to all
roles.

• Decide which sections, fields, and flexfields to display or hide on the page.
• Specify the status of fields as being required or optional.
• Make the rule active or inactive. You can have only one active rule for any action at any time.
Note: If you set a descriptive flexfield as being required, you can't decide on that field's visibility in particular
application areas using Transaction Design Studio. If you set a flexfield as being visible, the Visible indicator for the
field will be checked and disabled.

---

## Note: You can no longer configure the Job field in job requisitions using Transaction Design Studio. The Job field is
*Chunk ID: OHR-REC-1180 | Chapter: Security for Recruiting*

disabled. If you still want to change the configuration of the Job field, you'll need to use Page Composer.
When you create several rules for a specific action, the rules are listed in order of precedence. The first rule on the list
which applies to a given user is the rule being used, rather than the union of all rules that apply to the user. For rules
defined based on the roles of the users, only the first rule which applies to a given person is enforced. For instance, let's
say that for a given action, rule ABC is configured to show fields A, B, and C to recruiters, and rule BCD is configured to
show fields B, C, and D to HR specialists. Rule ABC appears first on the list of rules for this action. When a user who's
both a recruiter and an HR specialist accesses that page (action), they will only see fields A, B, and C but not D. If these
two rules were reordered to make rule BCD appear first on the list, then that same user would see only fields B, C, D on
that page and not A.

This table shows the actions that you can use to configure Recruiting pages.

Context

Action

Description

---

## Governs the job requisition descriptive
*Chunk ID: OHR-REC-1181 | Chapter: Security for Recruiting*

flexfields that can be used as a job search
results filters on the external career site.

---

## Governs the descriptive flexfields defined by
*Chunk ID: OHR-REC-1182 | Chapter: Security for Recruiting*

Oracle's worldwide teams for each country's
legislative requirements (PER_PERSON_
LEGISLATIVE_DATA_LEG_DDF)

---

## Enables defining which fields are required
*Chunk ID: OHR-REC-1183 | Chapter: Security for Recruiting*

from candidates in a given job application flow.
Setting is available for apply flow blocks using
profile content sections.

---

## Governs the sections and fields shown to
*Chunk ID: OHR-REC-1184 | Chapter: Security for Recruiting*

Recruiting users who view the offer page within
a candidate's application, in the Hiring work
area.

---

## Governs the sections and fields shown to HR
*Chunk ID: OHR-REC-1185 | Chapter: Security for Recruiting*

Specialists who view the offer during the HR
phase, in the Manage Job Offers quick action.

---

## Governs the sections and fields shown to
*Chunk ID: OHR-REC-1186 | Chapter: Security for Recruiting*

internal candidates when they're referring
external candidates to job requisitions.

---

## Governs the sections and fields shown to
*Chunk ID: OHR-REC-1187 | Chapter: Security for Recruiting*

internal candidates when they're referring
internal candidates to job requisitions.

---

## Create a Rule to Configure a Page in Recruiting
*Chunk ID: OHR-REC-1188 | Chapter: Security for Recruiting*

Here are examples of how to create rules in Transaction Design Studio to configure Recruiting pages.

---

## Example 1: Create a rule for the Recruiting - Create Job Requisition action
*Chunk ID: OHR-REC-1189 | Chapter: Security for Recruiting*

1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.
2. On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
3. Click the Transaction Design Studio tab.
4. Select the action Recruiting - Create Job Requisition.
5. Click Add to create a rule to display certain sections and fields.
6. In the Basic Details section, enter a name and description for the rule.
7. You can select a role, one or more recruiting types, and one or more countries for which the rule applies.

◦ If you don't select a role, the rule applies to all roles.
◦ When you select a recruiting type, the rule applies only to job requisitions with the same recruiting type.
◦ When you select a country, the rule applies only to job requisitions for which one of the location is part

of this country. The Primary Location or one of the Other Locations must be part of the selected country.
For example, you select the country "United States". A requisition's location is Pleasanton, California, US.
The rule applies to this requisition.
8. In the Show or Hide Regions section, select which sections you want to make visible.
9. In the Page Attributes section, select a region. Then select which fields are visible and which ones are required
to be filled.
10. Click Save and Close.

---

## Example 2: Create a rule for the Recruiting - Candidate Application
*Chunk ID: OHR-REC-1190 | Chapter: Security for Recruiting*

Additional Info action
1. Activate a sandbox and page editing at the Site layer in Settings and Actions Menu > Edit Pages > Activate a
sandbox.

2.
3.
4.
5.
6.
7.

---

## Personalization Using Transaction Design Studio
*Chunk ID: OHR-REC-1191 | Chapter: Security for Recruiting*

On your Home page, go to My Client Groups > Quick Actions > HCM Experience Design Studio.
Click the Transaction Design Studio tab.
Select the action Recruiting - Candidate Application Additional Info.
Click Add to create and configure a rule to display certain flexfields for certain countries.
In the Basic Details section, enter a name and description for the rule.
In the Page Attributes section, the region Additional Info is selected by default. Set the Person Legislative
Information field to Visible. Click the Edit icon. You can select any of the additional legislative flexfields
that have been defined by Oracle's worldwide teams for each country's legislative requirements
(PER_PERSON_LEGISLATIVE_DATA_LEG_DDF)

◦ Flexfield Content Code: Select the country/legal employer for which the rule applies.
◦ Flexfield Attributes: Select the specific field that has been configured in the lookups for that country/legal
◦

employer.
Select each field you want to make visible and which ones are required to be filled.

8. Click Save and Close.

---
