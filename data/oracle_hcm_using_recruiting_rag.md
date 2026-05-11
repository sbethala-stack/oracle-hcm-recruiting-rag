# Oracle HCM Cloud — Using Recruiting
## RAG Knowledge Base
> Source: Oracle Fusion Cloud Talent Management, Using Recruiting (2026)

---

# Job Requisitions

## Overview of Using Recruiting
*Chunk ID: OHR-USE-0001 | Chapter: Job Requisitions | Guide: Using Recruiting*

Recruiters and hiring managers can use the Hiring work area to find the best candidates for a job.
Oracle Fusion Cloud Recruiting provides tools to source and nurture candidates, create and manage job requisitions,
screen and select candidates, create and manage job offers, and onboard new employees into the organization. It also
provides career sites for employees and external candidates to search, discover, and apply to jobs using a smooth
application process.
Let's look at some of the key features.

You create job requisitions that contain the specific requirements for a job for which candidates are hired. A job
requisition can contain prescreening questionnaires and screening services such as background checks. You post job
requisitions on the career site that candidates visit as they search for jobs to apply for or refer people for the job.

---

## Recruiting Campaigns
*Chunk ID: OHR-USE-0002 | Chapter: Job Requisitions | Guide: Using Recruiting*

You create recruiting campaigns to advertise job requisitions and promote other recruitment initiatives. For example,
you can use campaigns to invite candidates to RSVP recruiting events, or advertise about the company's benefits and
corporate culture.

---

## Candidate Selection
*Chunk ID: OHR-USE-0003 | Chapter: Job Requisitions | Guide: Using Recruiting*

You search the database to find qualified candidates for current or planned jobs. You can match candidates to the job
requisitions. You can also put candidates in candidate pools and manage sourcing activities for current or future job
positions that you're currently recruiting for. You can move the candidate's job applications after they have applied to
the job requisitions during the selection process. The candidate selection process tracks and manages candidates from
the time their job application is confirmed to the time that they're hired.

You create job offers by providing details such as proposed start date, job assignment, salary, or other compensation.
You extend job offers to candidates. Candidates receive the offers, consider the content, and respond to the offers by
either accepting or declining them. When the candidate accepts the job offer, the candidate job application is handed
over to the HR specialist who finalizes the HR records for this worker.

2 Job Requisitions
Job Requisition Creation Process
There are three scenarios that you can use to create job requisitions. You'll have access to these scenarios depending on
your privileges and roles.
• Recruiter process: As a recruiter, you're responsible for the entire job requisition creation process. You initiate
the creation of the job requisition, you add details about the job requisition, and you submit the job requisition
for approval. When the job requisition is approved, you can enter job formatting information and post the job
requisition on career sites.
• Hiring manager process: As a hiring manager, you're responsible for the entire job requisition creation process.
You initiate the creation of the job requisition, you then enter details about the job requisition, and you submit
the job requisition for approval. When the job requisition is approved, you can enter job formatting information
and post the job requisition on career sites.
• Shared process: The process is shared between the hiring manager and the recruiter. The hiring manager
initiates the creation of the job requisition. The recruiter receives a notification to enter details about the job
requisition. The recruiter then submits the job requisition for approval. When the job requisition is approved,
the recruiter enters job formatting information and posts the job requisition on career sites.

---

## Job Requisition Phases and States
*Chunk ID: OHR-USE-0004 | Chapter: Job Requisitions | Guide: Using Recruiting*

A job requisition goes through different phases and states during its creation. You can see the phase and state of a job
requisition on the Requisitions list and also within the job requisition, in the Overview and Progress tabs.
The table lists the phases and states of a job requisition.

Phase

State

Draft

In Progress

Approval

Pending
Rejected
Canceled

---

## Create a Job Requisition
*Chunk ID: OHR-USE-0005 | Chapter: Job Requisitions | Guide: Using Recruiting*

You create a job requisition to specify the requirements of a job for which candidates are hired.
Here's what to do
1. Initiate the Creation of the Job Requisition
2. Enter Details About the Job Requisition
3. Submit the Job Requisition for Approval
4. Enter Job Formatting Information
During the job requisition creation process, you can view the progress of the job requisition in the Progress tab. You can
see the date when the job requisition was created, its phase and state, the start date of the phase, and the time spent on
the phase.

---

## Initiate the Creation of the Job Requisition
*Chunk ID: OHR-USE-0006 | Chapter: Job Requisitions | Guide: Using Recruiting*

You initiate the creation of a job requisition by selecting how you want to start off the creation process. You can initiate
the creation process from the Hiring work area, or using the Create Job Requisition quick action, or using the Create
Requisition action from within a workforce model.
Note: If you initiate the creation of the job requisition using a workforce model, when the workforce model is ready,
you can implement the model to create or update job requisitions within Hiring. The model is implemented if there are
no conflicts between the model and the existing job requisitions.
1. On the Job Requisitions page, click Add.
2. On the Create Job Requisition page, provide details on how you want to create the job requisition.
a. In the Requisition Type field, select Standard.
b. In the Use field, select how you want to start off the creation process.
- Blank Requisition: You create the requisition using a blank form.
- Existing Requisition: You create the requisition by duplicating an existing job requisition. Fields
(except the Requisition Number) in the new requisition are prepopulated with field values from the
source job requisition. If a job requisition template was used to create the source job requisition,

it's displayed in the Requisition Template field in the new job requisition. The new job requisition
considers only the values of the source job requisition fields and not the content of the template.
- Template: You create the requisition using a job requisition template. You'll find many of the
requisition fields prepopulated based on the selected template. The templates you can select
match the recruiting type and primary location of the requisition. Your access to the templates
displayed by the selector depends upon the organization selected on the templates and the
organization security profile of your data roles.
- Position: You create the requisition by selecting a position to base it upon.
- Job: You create the requisition by selecting a job to base it upon.
3. Click Continue.

---

## Enter Details About the Job Requisition
*Chunk ID: OHR-USE-0007 | Chapter: Job Requisitions | Guide: Using Recruiting*

You enter details about the job requisition by navigating to each section of the job requisition.

---

## Submit the Job Requisition for Approval
*Chunk ID: OHR-USE-0008 | Chapter: Job Requisitions | Guide: Using Recruiting*

When you're done entering all the details of the job requisition, use the Submit action to submit the job requisition for
approval.
By default, the job requisition is set to Job Formatting - In Progress, and an approval isn't required. In case the approval
process is enabled:
• The job requisition is set to Approval - Pending.
• The job requisition is routed automatically to the hiring manager's first-level manager, who's the first approver.
• If the hiring manager's first-level manager approves the job requisition, the job requisition is routed
automatically to the hiring manager's second-level manager, who's the second approver.
• If the hiring manager's second-level manager approves the job requisition, the job requisition is set to Job
Formatting - In Progress.
When you submit a job requisition for approval, the banner "Approval in progress. See how it's going." is displayed
and you can click the link in the banner to see complete transaction details. This link is only available to the approval
initiator.
After you submit a job requisition for approval, you can't edit most of the job requisition fields unless you have the
privileges Update Job Requisition (IRC_UPDATE_JOB_REQUISITION) and Update Job Requisition After Draft Phase
(IRC_UPDATE_JOB_REQUISITION_AFTER_DRAFT_PHASE). When the job requisition is approved, you can use the
Redraft Job Requisition action to return the job requisition to the draft status and change the values of the fields.
When you redraft a job requisition, the job requisition is set back to Draft - In Progress and the job requisition must be
submitted again to go through the approval process if required.
Your administrator might have configured if sections within a requisition must be accessed or not by users. When
sections are configured as required, when you create a job requisition or change a draft job requisition, you'll need
to access and open these sections in the requisition to save the requisition or submit it for approval. If you don't
access required sections, an error message is displayed indicating which ones you need to access to proceed with the
selected action. If you can only initiate job requisitions because you don't have the privilege Update Job Requisition,
the error message is displayed when you save the requisition. If you have the privilege Update Job Requisition
(IRC_UPDATE_JOB_REQUISITION) , the error message is displayed when you submit the requisition. You can save
changes in the requisition even if not all required sections have been visited, while making sure required sections are
visited before submitting.

---

## Enter Job Formatting Information
*Chunk ID: OHR-USE-0009 | Chapter: Job Requisitions | Guide: Using Recruiting*

When the job requisition is approved, the Job Formatting tab in the requisition becomes available. This is where you
select descriptions and media you want to share with candidates.
1.
2.
3.
4.
5.
6.
7.

On the Job Requisitions page, click the job requisition you just created.
In the Employer Description section, click Edit.
Select a predefined description of the employer and click Save.
In the Recruiting Organization Description section, click Edit.
Select a predefined description of the organization and click Save.
In the Media section, click Add.
You can select images and videos to be shown to the candidates. For example, images of the facilities, video
of the corporate history of the organization, video of testimonials from current employees. When you add a
URL for a video, by default the Thumbnail URL automatically points to a high-quality version of the video. It's
recommended that you add URLs of the type HTTPS to avoid displaying insecure items in a secure career site
page. You can select specific images and videos to be shown to the candidates who will receive job offers.

You can select the languages in which each media item is available and translate the media title in the
appropriate languages.
8. Click Save.
When you're done, you can use the Preview Job Requisition action to see how the information is shown to candidates
on the career site. When you're ready to post the requisition, use the Move to Posting or Open for Sourcing action to
post the job on a career site.
Related Topics
• Info About Job Requisition Fields
• Preview a Job Requisition
• Post a Job Requisition on a Career Site

---

## Create a Job Requisition Based on a Job
*Chunk ID: OHR-USE-0010 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can create a job requisition by selecting a job to base it upon.
Before you start
You need the privilege Initiate Job Requisition Using Job (IRC_INITIATE_JOB_REQUISITION_FROM_JOB).
Here's what to do
1. On the Job Requisitions page, click Add.
2. In the Requisition Type field, select Standard.
3. In the Use field, select Job.
4. Select a business unit to narrow down the list of jobs you can select.
5. Select a job available within your organization.
6. Click Continue.
7. Complete fields as for a standard job requisition.
8. Click Submit.

Results:
The following job field values are added by default to the job requisition. You can modify them.
• Job Family
• Job Function
• Regular or Temporary
• Management Level
• Full Time or Part Time
• Job
• Grade
If the job you selected has a job requisition template associated to it, you can modify the recruiting-specific fields that
are pre-populated by the template. For example, Recruiter, Hiring Team, Description.
If a profile is associated to the job, the following field values are defaulted from the profile associated to the job:
• All fields from the Work Requirements section
• Internal Description
• External Description
• Short Description: The short description is defaulted from the Profile
Description of the profile only if the appropriate profile option is set
(ORA_IRC_REQ_DEFAULT_SHORT_POSTING_DESC_FROM_PROFILE_DESC_ENABLED).
Note: The following configurations related to profile options are taken into consideration:
• PER_DEFAULT_GRADE_FROM_JOB_POSITION: The grade value is defaulted if requested with this profile
option.
• PER_ENFORCE_VALID_GRADES: If the profile option is set accordingly, you can only select grades which are
valid for this job or position.
Important info about translation. For the translated values of the profile to be defaulted on the job requisition, the
desired languages must be active when you create the requisition. To achieve this, a requisition template must be
selected on the job from which the requisition is created, and the desired languages must be selected on the requisition
template (which will enable these languages on the requisition being created). Translations must also be provided
on the requisition template for the translatable requisition values (the Source Language for each language row in
the translation editor must be set to the current language). By doing so, the translated values from the profile will be
defaulted on the requisition for the languages of the requisition.

---

## Create a Job Requisition Based on a Position
*Chunk ID: OHR-USE-0011 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can create a job requisition by selecting a position to base it upon.
When you create a job requisition based on a position, the template from the job is used if no template is available on
the position.
1. On the Job Requisitions page, click Add.

2. In the Requisition Type field, select Standard.
3. In the Use field, select Position.
4. Select a business unit.
The Business Unit field is required when you create a job requisition based on a position.
5. Select a position available within your organization.
6. The option Show Only Approved Positions is selected by default. This means that only positions with the Approved
hiring status are available for selection. If you clear this option, the list of positions will include active positions with
all hiring status values. If you select a position whose hiring status isn't Approved, a warning message is displayed so
that you can decide whether to continue the process or to select another position.
Note: Your administrator may have disabled this option.
7. Click Continue.
8. Complete fields as for a standard job requisition.
9. Click Submit.
Results:
The following position field values are added to the job requisition and you can modify them.
• Number of Openings / Unlimited Openings: The Number of Openings is defaulted to the available headcount
of the position. This is calculated by taking the headcount of the position from which we remove the number
of incumbents on that position (at the time of the requisition creation). If ever this calculation gives a negative
value or 0, the number of openings is defaulted to a value of 1.
• Regular or Temporary
• Full Time or Part Time
• Business Unit
• Department
• Primary Work Location
• Job
• Grade
• Requisition Title
Note: The Business Unit, Department, Legal Employer, and Primary Work Location are defaulted from the work
assignment of the Hiring Manager only if no such value was defaulted from the requisition template, position, job, or
the requisition template associated to the position or job. The values are coming from the position. If no value was set
on the position for one of these fields, the values coming from the work assignment of the Hiring Manager are used.
If the position you selected has a job requisition template associated to it, you can modify recruiting-specific fields such
as Recruiter, Hiring Manager, and Candidate Selection Process that are prepopulated by the template.
Information from the job associated to the position is also added to the requisition. You can modify these values in the
job requisition.
• Job Family
• Job Function
• Management Level

If a profile is associated to the position, the following field values are defaulted to the requisition. If no profile is
associated to the position, these field values are defaulted from the profile associated to the job that's associated to the
position (if there is one).
• All fields from the Work Requirements section
• Internal Description
• External Description
• Short Description: The short description is defaulted from the Profile
Description of the profile only if the appropriate profile option is set
(ORA_IRC_REQ_DEFAULT_SHORT_POSTING_DESC_FROM_PROFILE_DESC_ENABLED).
Note: The job description is set on the profile, and that description is defaulted in the requisition posting description.
Job requisition fields aren't sync with the position or anything that's associated with it. If you change the values of the
position, the job, the requisition template, or profile contained in that position, these changes have no effect on the job
requisition values.
Depending on the configuration selected by your administrator, some requisition behaviors will vary:
• You can select any position, regardless of the position's hiring status, or only those with a hiring status of
Approved.
• The grade value or the requisition may be defaulted from the job or position.
• Only grades valid for this job or position may be selected on the requisition.
Important info about translation. For the translated values of the profile to be defaulted on the job requisition, the
languages must be active when you create the requisition. To achieve this, a requisition template must be selected
on the position from which the requisition is created, and the languages must be selected on the requisition template
(which will enable these languages on the requisition being created). Translations must also be provided on the
requisition template for the translatable requisition values (the Source Language for each language row in the
translation editor must be set to the current language). By doing so, the translated values from the profile will be
defaulted on the requisition for the languages of the requisition.

---

## Create a Job Requisition When Requesting a New
*Chunk ID: OHR-USE-0012 | Chapter: Job Requisitions | Guide: Using Recruiting*

Position
When you request a new position or duplicate an existing position, you can select a requisition template and provide
details about the new requisition to create for this position.
1. In the Workforce Structures work area, click Request a New Position.
2. On the Request a New Position page, select Requisition Details and click Continue.
3. Complete the fields in the Requisition Details section.
Not all requisition fields are visible in the Requisition Details section, only a small subset of the standard requisition
fields are available. When you access the Requisition Details section for the first time, field values are defaulted to the
appropriate values, following the same logic as when creating a requisition based on a position:
◦ Position field values are pre-filled into the requisition fields.

◦ Fields coming from the requisition template are pre-filled into the requisition fields, if a template was
◦

selected.
Fields coming from other sources are pre-filled as usual.

4. Click Submit.
Results:
The job requisition is created only when the position is approved. While the position is pending approval, the requisition
isn't visible in Oracle Fusion Cloud Recruiting. If the user who submitted the position can submit job requisitions
for approval, the job requisition is submitted for approval automatically. If the job requisition can't be successfully
submitted (due to missing or invalid required information for example), the requisition will remain in the Draft In Progress status. If the user who submitted the position isn't allowed to submit job requisitions for approval, the
requisition will be in the Draft - In Progress status.
Note: When you're requesting a new position and have already accessed the Requisition Details section of the
Request a New Position flow, if you go back to an earlier section of the flow and change a position value, you will
get a warning letting you know that you need to refresh the requisition information. To do this, go to the Requisition
Details section. The existing requisition values will be removed and be replaced with the latest information defined
in the other position sections. The requisition information is only refreshed when accessing the Requisition Details
section. If you don’t return to the requisition section and submit the position, the requisition will be created using the
previously selected values.

---

## Info About Job Requisition Fields
*Chunk ID: OHR-USE-0013 | Chapter: Job Requisitions | Guide: Using Recruiting*

While you create job requisitions, consider the following info regarding specific fields.
Note: Profile descriptive flexfields (DFF) aren't visible in Recruiting. The DFF context will be populated on the profile
items as soon as the candidate is converted into a pending worker or employee.

Field

Description

---

## Requisition Number
*Chunk ID: OHR-USE-0014 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can use these characters for the job requisition number:
• alphanumeric characters
• period
• underscore
• dash
• space

Hiring Team

When you define the Hiring Team, the selectors for the Hiring Manager, Recruiter, and Collaborator
fields display all the assignments for a person, not only the primary assignment. The name,
email, business title, and person number are displayed on the list. The business title identifies the
assignment.

---

## Add Collaborator Type
*Chunk ID: OHR-USE-0015 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can add collaborator types to define hiring team roles more precisely and to better manage
communications with members of the job requisition's and offer's Hiring Teams. When you add a user
as a collaborator on a job requisition or job offer (regardless of the collaborator type), the user has the
required data security to view this requisition or offer.

Field

Description

Collaborator

When you define the Hiring Team, if you don't add yourself as the hiring manager or recruiter, you're
automatically added as a collaborator. This ensures that the user creating the requisition has access to
the requisition once it's created.

---

## Requisition Structure
*Chunk ID: OHR-USE-0016 | Chapter: Job Requisitions | Guide: Using Recruiting*

The field values in the Requisition Structure section are coming from the job requisition template.
Values are copied only if there are no values in the requisition. For example, the primary location set on
the job requisition template isn't copied in the job requisition if a value is defined in the requisition.

Organization

If you're a recruiter, you need to enter a value in the Organization field. If you're a hiring manager you
need not do so. When you display the Organization list of values, the name of the organization and its
type are displayed for each entry.
Values displayed in the Organization, Legal Employer, and Department selectors are controlled by the
organization security profile of your data roles.
What's the purpose of the Organization field compared to the Department field?
The Organization field has important functional implications which the Department field doesn't
provide.
The value selected in the Organization field can be used to drive the possible values to be selected for
other requisition fields (candidate selection process and prescreening questions for example). This
Organization value can also be used to drive data security, meaning it can be used to define which
requisitions a user is allowed to see.
The hierarchical nature of the Organization field (which is a value within the Organization tree) allows
taking into account where the selected Organization is placed within the tree.
However, the Department field in the Offer section is a simple selection which will be defaulted in an
offer created for this requisition. It doesn't impact anything else.

---

## Values for these fields are coming from the work assignment of the Hiring Manager only if no value
*Chunk ID: OHR-USE-0017 | Chapter: Job Requisitions | Guide: Using Recruiting*

was defaulted from the requisition template, position, job, or the requisition template associated to the
position or job. Also, the Business Unit field is required only when you create a job requisition based on
a position.

---

## Display in Organization Chart
*Chunk ID: OHR-USE-0018 | Chapter: Job Requisitions | Guide: Using Recruiting*

When you select this option, it indicates if the requisition is visible in the My Team work area and the
organization chart available in the Directory work area. Note that the responsive UI version of the
Directory work area doesn't display requisitions in the organization chart; only older versions of the
Directory are impacted by the value of this field.

---

## Posting Description
*Chunk ID: OHR-USE-0019 | Chapter: Job Requisitions | Guide: Using Recruiting*

This is where you define the posting description, short description, qualifications, and responsibilities
of the job posted on the internal carer site, external career sites, or both.
The short description appears on the career site job search results page. That page displays the name,
location, and brief description of the job. The Short Description field can contain a maximum of 1000
characters.
The description appears when a candidate clicks on a job to view the complete description of the
job requisition. You can specify a different description for the internal career site and the external
career site. Note that the internal short description is currently not used on the internal career site. The
description is only displayed within the requisition.

Skills

Skills you add to a job requisition are visible to external and internal candidates when they view the
details of the requisition on a career site and to recruiting agents when they view the job details in their
agency portal.
When additional skill attribute values are entered on requisitions, only the skill name is displayed to
candidates and recruiting agents viewing the requisition details. Other attributes aren't displayed.
Values in the Skills section might be defaulted depending on how you create the job requisition.
Skills aren't multilingual, it's not possible to translate the name of a skill in multiple languages. For this
reason, it's recommended to not use skills in multilingual job requisitions because the skill name will

Field

Description
always be displayed to candidates exactly as entered, regardless of the language in which candidates
are viewing the requisition.

Attachments

You can upload attachments to the requisition to provide additional information to users viewing the
requisition, typically members of the hiring team. These attachments aren't visible to candidates and
can't be made visible for them.

Workplace

You can define the workplace for a job:
• On-site
• Remote
• Hybrid

---

## Hot Jobs
*Chunk ID: OHR-USE-0020 | Chapter: Job Requisitions | Guide: Using Recruiting*

Promote certain job requisitions on external career sites by displaying a "Hot Job" tag in search results
lists, and on job details pages.
You can change the tag's visibility and styling for custom search results pages. You can also use it as a
criterion in the custom job list component.
Note: This tag is only visible on external career sites using the Minimal template.
To make the Hot Jobs field available, you need to first enable it in Transaction Design Studio for the
Recruiting - Create Job Requisition, and the Recruiting - View and Edit Job Requisition actions. Once
enabled, the field displays in the Configuration section.

Configuration

This is where you can select configuration options for the job requisition:
• Candidate selection process: You select the candidate selection process used for the requisition.
• External application flow: You select the application flow used for the requisition.
• Allow candidates to apply when not posted: You can invite candidates to apply on a job requisition
that's currently not visible to other candidates. This could be the case if your organization wants
to fill a high-level job or even a replacement and they want to keep it confidential.
• Automatically open requisition for sourcing: You can specify if the requisition is automatically
open for sourcing once it's approved, and post it on career sites.
• Automatically unpost requisition: You can specify if the requisition will be automatically unposted
from the internal career site, the external career sites, or both.
• Automatically fill requisition: When you enable this option, the status of the job requisition is
automatically changed to Filled once the number of hired candidates matches the number of
openings on the job requisition.

Job

The Job field has special logic attached to it. The field can be displayed in different sections of the job
requisition depending on how the requisition was created (this depends on the value selected in the
Use field while creating the requisition). The Job field is also not always editable (this also depends on
how the requisition was created). If you want to set a value for the Job field, it's recommended to create
the job requisition using a job. For details, see Create a Job Requisition Based on a Job.

---

## How Locations and Work Locations Work Together
*Chunk ID: OHR-USE-0021 | Chapter: Job Requisitions | Guide: Using Recruiting*

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

You create a job requisition from an
existing requisition.

• The values from the source requisition are used.

You create a job requisition from a
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

Scenario
You create a job requisition from a
position.

Result
• If a work location is defaulted from the position and no primary location is defaulted from the
template associated to the position, the primary location is defaulted to the geography associated
to the work location.
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

## Skills Advisor for Job Requisitions and Candidates
*Chunk ID: OHR-USE-0022 | Chapter: Job Requisitions | Guide: Using Recruiting*

To better understand and grow your organization’s talent with an always-current, well-defined, and tailored skills data
set, use Oracle Dynamic Skills. It makes use of your organizational data to automatically identify, infer, and recommend
skills for people, jobs, and other skills related resources. You have a continuously updated view into the ever-evolving
skills to effectively connect people to opportunities.
If your organization implemented Dynamic Skills, recruiters and candidates can take advantage if these features:
• Recruiters can add required skills for a job requisition using suggested skills, there by enhancing the richness of
the job description.
• Candidates can use the suggested skills for a specific job and their experience. It helps candidates to quickly
select the relevant skills and add details.
Related Topics
• Overview of Dynamic Skills

---

## Fields You Can Edit in Non-Draft Job Requisitions
*Chunk ID: OHR-USE-0023 | Chapter: Job Requisitions | Guide: Using Recruiting*

The fields you can edit in non-draft job requisitions will vary depending on your privileges.
If you have the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION), you can edit these fields:
• Requisition Title
• Other Requisition Title
• Language
• Comments
• Hiring Team
• Posting Description
• Attachments

• External Application Flow (you can't edit the field when the requisition is in the Open phase)
• Allow Candidates to Apply When Not Posted
• Automatically Open Requisition for Sourcing (you can only edit the field when the requisition is in the Draft or
Approval phase)
• Automatically Unpost Requisition
• Automatically Fill Requisition
• Prescreening Questionnaires (you can't edit the field when there are job applications on the requisition)
• Interview Questionnaires
If you have the Update Job Requisition (IRC_UPDATE_JOB_REQUISITION) and the Update Job Requisition After Draft
Phase (IRC_UPDATE_JOB_REQUISITION_AFTER_DRAFT_PHASE) privileges, you can edit most fields except these ones:
• Recruiting Type
• Requisition Template
• Requisition Number
• Position
• Organization
• Primary Location (you can edit the field if you have the privilege Update Job Requisition Posting Locations
(IRC_UPDATE_JOB_REQUISITION_POSTING_LOCATIONS). Also, there must be job applications and prospects
in the requisition.)
• Other Locations (you can edit the field if you have the privilege Update Job Requisition Posting Locations
(IRC_UPDATE_JOB_REQUISITION_POSTING_LOCATIONS). Also, there must be job applications and prospects
in the requisition.)
• Job Family
• Job Function
• Business Unit if the requisition is based on a position or job
• Job if the requisition is based on a position or job
• Candidate Selection Process
• Screening Services. There must be no job applications on the requisition.
• Application Flow (when there are job applications)
• Questionnaires (when there are job applications)

---

## Edit a Draft Job Requisition
*Chunk ID: OHR-USE-0024 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can modify the values of fields in draft job requisitions.
Before you start
You need the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
Note: On a draft job requisition, you can only change the value of the requisition template field if the requisition was
created using a blank requisition or a requisition template on which no job is selected.
Here's what to do

1. On the Job Requisitions page, click on a draft job requisition.
2. Modify field values as needed.
3. Click Save and Close.

---

## Edit a Non-Draft Job Requisition
*Chunk ID: OHR-USE-0025 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can modify the value of many fields in non-draft job requisitions.
Before you start
• You need the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
• If you have the privilege Update Job Requisition After Draft Phase
(IRC_UPDATE_JOB_REQUISITION_AFTER_DRAFT_PHASE), you will have additional editing capabilities.
Here's what to do
1. On the Job Requisitions page, click on a non-draft job requisition.
2. Click a tab on the left panel. The Edit button is displayed for sections you can modify.
3. Click Edit.
4. Modify field values as needed.
5. Click Save.

---

## Edit the Locations of a Job Requisition with Job
*Chunk ID: OHR-USE-0026 | Chapter: Job Requisitions | Guide: Using Recruiting*

Applications
You can modify the primary location and the other locations of job requisitions that you can no longer redraft because
they have job applications, prospects, or linked requisitions.
For example, you want to modify posting locations to reach out to candidates in more locations. Or you forgot to include
a location or included an incorrect one.
All operations that consider the locations of a job requisition will immediately consider the latest posting locations of
the requisition. For example, the requisition is posted or unposted from contextualized career sites based on the latest
posting locations.
When you change the posting locations of a job requisition, it won’t update other requisition values that are
contextualized such as the candidate selection process or prescreening questions. These values may not be aligned
with the new posting locations.
When you change the locations of a posted job requisition, it may cause a temporary mismatch of information until the
Maintain Candidates and Job Requisitions for Search scheduled process is run to update the search index. Everything
relying on the index will be outdated until the process is run. For example, a candidate looking at jobs on a career site
may notice a mismatch between the locations displayed in the job details of a job and the location facets for which this
job is returned.
Before you start

You need these privileges:
• Update Job Requisition (IRC_UPDATE_JOB_REQUISITION)
• Update Job Requisition Posting Locations (IRC_UPDATE_JOB_REQUISITION_POSTING_LOCATIONS)
Here's what to do
1. On the Job Requisitions page, click on a job requisition.
2. In the Requisition Structure section, click Edit.
3. Add, remove, or change the existing primary location and other locations as needed.
4. Click Save.

---

## Preview a Job Requisition
*Chunk ID: OHR-USE-0027 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can preview a job requisition to see how the information is shown to candidates on the career site.
1. On the Job Requisitions page, click on a job requisition.
2. In the Actions menu, select Preview Job Requisition.
3. In the Preview field, indicate if you want to preview the requisition as an internal or external candidate, on a desktop
computer or a mobile device.
Only active external career sites for which the requisition's context matches the filters of the site are available for
selection.
4. In the Language field, select the language to preview the requisition.
You can preview the information in the different languages that are active for the requisition.

---

## Suspend a Job Requisition
*Chunk ID: OHR-USE-0028 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can suspend activities associated with a job requisition and indicate that the requisition is currently on hold.
You may want to do that when there's a hiring freeze, or you want to postpone the hiring of candidates, or you want to
put an approved requisition on hold and reopen it without having to get a second round of approvals. Suspending a job
requisition prevents further actions on job applications until the requisition is resumed.
You can suspend a job requisition when it's in the Open phase. However, you can't suspend a job requisition when:
• The requisition is already on hold.
• The requisition is closed (Open - Canceled or Open - Filled).
• There are active job applications on the requisition which are on Offer - Draft status or later, but not in the HR
phase.
Before you start
You need the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
Here's what to do
1. On the Job Requisitions page, click on a job requisition.

2. In the Actions menu, select Suspend job Requisition.
Results:
When a job requisition is suspended:
• The requisition is moved to the Open - Suspended status.
• Current or scheduled posting on career sites are canceled. If the requisition is posted on job boards, you're
asked if it should be unposted from job boards or not.
• The option Allow Candidates to Apply When Not Posted is deselected.
• A notification is sent to the Hiring Team.
What to do next
Here's a list of actions you can and can't do when a requisition is suspended.
Actions you can do

---

## Redraft the job requisition. This action
*Chunk ID: OHR-USE-0029 | Chapter: Job Requisitions | Guide: Using Recruiting*

is only available when there are no job
applications on the requisition.

Add candidates to the requisition.

Close the job requisition.

Create an offer for a job application.

---

## Move a job application to the Rejected
*Chunk ID: OHR-USE-0030 | Chapter: Job Requisitions | Guide: Using Recruiting*

by Employer or Withdrawn by Candidate
state.

Move a job application to any state other than Rejected by Employer or Withdrawn by Candidate.

Collect feedback for a job application.

Schedule an interview.

Send emails to candidates.

Add interactions on job applications.

---

## Automated actions defined in the
*Chunk ID: OHR-USE-0031 | Chapter: Job Requisitions | Guide: Using Recruiting*

candidate selection process for job
applications are performed as usual.

Related Topics
• Resume a Job Requisition

---

## Resume a Job Requisition
*Chunk ID: OHR-USE-0032 | Chapter: Job Requisitions | Guide: Using Recruiting*

You use the Resume Job Requisition action to reactivate a job requisition that was put on hold.
Before you start
You need the privilege Update Job Requisition (IRC_UPDATE_JOB_REQUISITION).
Here's what to do
1. On the Job Requisitions page, click Show Filters.
2. Display suspended job requisitions using these filters: phase Open, state Suspended.
3. Open the suspended job requisition.
4. In the Actions menu, select Resume Job Requisition.
What to do next
The requisition is moved back to the state where it was before being suspended. However, the requisition won't be
posted back on career sites. Its status will be set to Open - Unposted if it was previously posted or scheduled to be
posted. Also, the job requisition won't get sent for a second round of approvals.

---

## Redraft a Job Requisition
*Chunk ID: OHR-USE-0033 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can redraft a job requisition when you realize that you need to change the values of fields after the job requisition
was submitted for approval.
Before you start
If the job requisition is posted, you'll have to unpost the job requisition before redrafting it. You can redraft a job
requisition as long as there are no job applications or draft job applications (job applications not yet completed by the
candidate) on the job requisition.
Here's what to do
1. On the Job Requisitions page, click on a job requisition.
2. In the Actions menu, select Redraft Job Requisition.
Results:
The job requisition status is put back to Draft and you can modify field values.
What to do next
When you're done redrafting the job requisition, you need to submit it again to go through the approval process, if
required.

---

## Reopen a Job Requisition
*Chunk ID: OHR-USE-0034 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can reopen a job requisition that was filled or canceled.

1. On the Job Requisitions page, click on a job requisition with the state Filled or Canceled.
2. In the Actions menu, select Reopen Job Requisition.
Results:
The job requisition's phase and state are reset to what they were before the requisition was filled or canceled. If the job
requisition was posted or scheduled before being canceled, its status is set to Open - Unposted after being reopened.
If the job requisition had candidate job applications that got rejected when it was filled or canceled, reopening the job
requisition has no effect on these candidate job applications. Any of these candidate job applications can be manually
returned to their prior phase and state in the selection process.

When to Delete or Cancel a Job Requisition
You may want to delete or cancel job requisitions depending on the situation and what you want to achieve.
If you want to remove a job requisition from the Job Requisitions list, use the Delete Job Requisition action. Note that
the requisition status must be Draft - In Progress.
If you no longer need a job requisition, use the Cancel Job Requisition action. The state of active candidates who
applied on the job requisition is changed to Rejected. You can use the Cancel Job Requisition action when the job
requisition is in one of these phases or states:
• Job Formatting
• Posting
• Open
• Approval - Rejected: If the approval was rejected, you can cancel the requisition or redraft it for editing and
resubmit it for approval later.
You can't cancel a job requisition while at least one candidate is in one of these statuses:
• Offer - Pending Approval
• Offer - Extended or later in the selection process (but not in the HR phase) which includes:

◦ Offer - Accepted
◦ Custom phases after the Offer phase, but not the terminal states Rejected by Employer, Withdrawn by
Candidate.

If you want to view job requisitions that were canceled, use the Include Inactive Requisitions filter on the Job
Requisitions list.

---

## Suggested Jobs
*Chunk ID: OHR-USE-0035 | Chapter: Job Requisitions | Guide: Using Recruiting*

When the Intelligent Matching features are enabled within your organization, candidates can use the Suggested Jobs
feature to review jobs based on their profile.
This feature helps candidates find relevant jobs based on their profile and therefore also discover jobs quickly. The
Suggested Jobs feature uses artificial intelligence (AI) and machine-learning algorithms.

---

## Similar Jobs
*Chunk ID: OHR-USE-0036 | Chapter: Job Requisitions | Guide: Using Recruiting*

When the Intelligent Matching features are enabled within your organization, you can use the Similar Jobs feature to
suggest similar jobs to candidates based on a specific job requisition.
This feature helps candidates find similar jobs quickly and apply for the right roles. The Similar Jobs feature uses
artificial intelligence (AI) and machine-learning algorithms.

---

## Overview of Suggested Candidates
*Chunk ID: OHR-USE-0037 | Chapter: Job Requisitions | Guide: Using Recruiting*

The AI Apps feature Suggested Candidates uses a machine learning model known as Intelligent Matching. The feature
can be independently enabled. It helps you to quickly identify candidates that could be a good fit for a job requisition.
Many jobs today receive hundreds of candidate applications, and it takes time for recruiters and hiring managers to find
relevant candidates who’ve the right skills, experience, and education required for the job. The Suggested Candidates
feature quickly compares and analyzes the details of candidate profiles with the details of an open job requisition. It
then finds relevant candidates to be reviewed and saves time during the sourcing process.
The Suggested Candidates feature doesn’t replace the normal hiring process. It only provides suggestions. It’s up to you
as the hiring manager or recruiter to decide which candidate is the best fit for the job through the hiring process.
Note: As with any artificial intelligence solution, the results shown are a machine’s best interpretation of the data. If
data is missing from the candidate profile or job requisition, this will result in less relevant suggestions for that job and
candidate.
Within Oracle Recruiting, the suggested candidates are displayed within the Suggested Candidates section of a job
requisition. The suggested candidate is displayed along with a set of criteria, Profile, Education, Experience and Skill
that help indicate why this candidate was suggested. This example shows that both candidates have a stronger match
on the experience required for this job, but lower matches for skill, education, and profile.

---

## How Suggested Candidate Works
*Chunk ID: OHR-USE-0038 | Chapter: Job Requisitions | Guide: Using Recruiting*

The Suggested Candidates feature is powered by machine learning algorithms that evaluate candidate data and job
requisition data to understand similarities across common words or phrases. The feature uses candidate and job
requisition data and converts it into mathematical representations to calculate similarities. The feature is more powerful
than a regular search because it uses Natural Language Processing (NLP) that can consider the context in which a word
or phrase is located within the data. That means that the terms don’t have to be an exact match for the feature to find
similarities in data.
Note: The Suggested Candidates feature doesn’t receive a copy of a candidate’s resume nor any PII data. Oracle
Recruiting pushes a subset of fields about a candidate to AI Apps to use.

---

## Considerations for Enabling Suggested Candidates
*Chunk ID: OHR-USE-0039 | Chapter: Job Requisitions | Guide: Using Recruiting*

To use the Suggested Candidates feature, your organization must meet the following criteria:
• The Recruiting environment must not be on a EUR or government pod.
• The Recruiting environment must be live in production for at least 6 months, or migrated 6 months’ worth of
data, to benefit from high-quality suggestions and prediction results.
• The Recruiting environment must use English for their operation language. If resumes, job applications, and
job requisitions are in languages other than English, the candidate suggestions might be unpredictable. We
recommend that you don't use this feature if you've data in languages other than English.

• The Suggested Candidates feature works best for job requisitions that require skilled labor (that is workers that
have a specialized set of skills and education to perform the job).

---

## View Suggested Candidates for a Job Requisition
*Chunk ID: OHR-USE-0040 | Chapter: Job Requisitions | Guide: Using Recruiting*

When the Oracle AI Apps Suggested Candidates feature is enabled within your organization, you can view a list of
suggested candidates for open job requisitions.

---

## Filter Suggested Candidates
*Chunk ID: OHR-USE-0041 | Chapter: Job Requisitions | Guide: Using Recruiting*

When you view the results in the Suggested Candidates section, the candidates are sorted by those with the strongest
profile match by default. You can further refine the results based on these filters. When you apply a filter, the Suggested
Candidates section refreshes to show candidates that meet the filter criteria.
• Location: If you select a city in the Location field, candidates within a 100 mile radius of that city are displayed in
the Suggested Candidates section. If you select a country, then candidates in that country are displayed.
• Years of Experience
• Degree
• Last Updated: This refines the list of suggested candidates based on the number of days or months the
candidate profile was last updated.
Note: The sorting on the UI is based on the overall score received by the candidate. The overall score consider all the
aspects for candidates like education, skills, achievements, responsibilities, past experience, titles. So the candidate
with evaluated overall score higher than other candidates will be shown first on the list.

---

## Remove Employees from Suggested Candidates
*Chunk ID: OHR-USE-0042 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can select the Exclude employees check box to exclude employees from the suggestions. By default, the option
isn’t selected, and all candidate suggestions are displayed.
If the job requisition includes non-English languages, the Suggested Candidates section in the requisition isn’t
displayed. The Suggested sort option on the job applications list is also not displayed.

---

## Dismiss Candidates from Suggested Candidates
*Chunk ID: OHR-USE-0043 | Chapter: Job Requisitions | Guide: Using Recruiting*

When you view the list of suggested candidates for a job requisition, you can dismiss a candidate suggestion from
the list. After you select the Dismiss action available in the Actions menu, you can provide a reason for dismissing the
candidate suggestion. Possible reasons are:
• Not a good match
• Appears repeatedly
• View other suggestions
The candidate is then removed from the list of suggestions and won’t be shown again as a suggested candidates for
that requisition.
Note: When you dismiss a candidate, the candidate is no longer suggested to you. Though, another recruiter could
see the suggested candidate.

---

## Exclude Suggestions for Specific Countries
*Chunk ID: OHR-USE-0044 | Chapter: Job Requisitions | Guide: Using Recruiting*

Candidate suggestions are enabled for all countries by default. However, if you’ve a business need, your administrator
can exclude certain countries from receiving candidate suggestions. When certain countries are excluded, here’s what
happens:
• The Suggested Candidates section doesn’t appear when requisitions are posted in the excluded list of
countries.
• Candidates whose address is in the excluded list of countries aren’t included in the list of suggested candidates.
So even if the posting location isn’t in the excluded list, when you refine the list of suggested candidates by
location, candidates located in the countries excluded aren’t included in the list of suggested candidates.

---

## Understand Top Candidate Suggestions
*Chunk ID: OHR-USE-0045 | Chapter: Job Requisitions | Guide: Using Recruiting*

The Intelligent Matching feature suggest candidates for a job requisition by matching candidates to the details of the
job requisition.
Candidate suggestions for a job requisition have four criteria that explain why a candidate is suggested. These four
criteria, Profile, Education, Experience and Skills, provide a representation of a candidate’s job application. Hiring
managers and recruiters can get a more nuanced understanding of how the candidate’s job application matches the
given job. Each criteria is represented by 0-3 stars indicating the relative match, with 0 indicating no match.
The artificial intelligence models use these fields from the candidate profile and the job requisition to suggest
candidates for a job:
Field Types

---

## Requisition Title
*Chunk ID: OHR-USE-0046 | Chapter: Job Requisitions | Guide: Using Recruiting*

Experience

• Skill (Skill Center Section)

• Posting Description

• Description (Skill Center Section)

• Education Level

• License or Certificate

• Job Function

• Title (Previous Employment)

• Job Family

• Issued By

• Qualifications

• Degrees

• Responsibilities

• Major
• Education Level (Education)
• Job Title (Previous Employment)
• Responsibilities (Previous Employment)
• Achievements (Previous Employment)

This table lists the criteria against which candidates are assigned stars, along with the fields from the candidate’s profile
that are used to derive the number of stars.

Criteria

Description

Profile

Considers the title and description in the candidate’s profile.

Skills

Considers skill data from skills fields as well as keywords found through machine learning.

Experience

---

## Considers the candidate's number of years of experience. It uses contextual words to assess the
*Chunk ID: OHR-USE-0047 | Chapter: Job Requisitions | Guide: Using Recruiting*

likelihood that the candidate is a manager.

Education

Considers the candidate’s most recent education.

So, for example, if a candidate’s title and description have a strong match to the job requisition, the candidate is
assigned 3 stars on profile. Candidate suggestions and the four criteria displayed are relative indicators that you can use
to assess a candidate's application to a given job requisition. For example, if a PHD is a requirement for a job, looking at
matches that have 3 stars for education can assist in the overall sourcing process.
Note: The suggested candidates and the stars don’t replace the general hiring process or the need to review a
candidate in more detail. For example, you've to continue to look through the resumes of the suggested candidates
before taking next steps.

---

## View Metrics on Job Applications for a Job Requisition
*Chunk ID: OHR-USE-0048 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can view various metrics regarding the job applications for a requisition. A section called Metrics is available in the
requisition’s Overview tab.
The Metrics section displays an OTBI report containing various info about the requisition. To display data specific to the
requisition, the Requisition ID is passed to the OTBI report. If your administrator created a custom report, it is possible to
replace the default report with that custom report using Page Composer.
The report displayed in the Metrics section contains these 3 tabs:
• Job Applications: In the Job Applications tab, you can display gender, ethnicity, and disability information for
the job applications on the requisition. The diagram displays the number of people who provided the info for
each phase of the candidate selection process.
• Source Tracking: In the Source Tracking tab, you can display the source medium and source name from which
candidates applied. You can see the number of candidate applications for a specific source medium or source
name as well as the percentage it represents out of the total number of applications.
• Candidate Type: In the Candidate Type tab, you can display job applications by candidate types such as all
external candidates, all internal candidates, employees, contingent workers, ex contingent workers and ex
employees. The diagram displays the candidate type for each phase of the candidate selection process.
The OTBI report only displays info to which you have access. Also, no info is displayed if there are less than 20 job
applications on the requisition. This is to avoid being able to easily identify which candidate is part of which group.

---

## Get Predictions About the Time Required for a First Hire
*Chunk ID: OHR-USE-0049 | Chapter: Job Requisitions | Guide: Using Recruiting*

When the Time to Hire feature is enabled within your organization, you can get predictions about the time it will take
to make a first hire for a job requisition. The Time to Hire feature uses Artificial Intelligence (AI) and machine-learning
algorithms to estimate the time for a first hire, based on previous similar job requisitions.
The Estimated Time to Hire section is available when you create a job requisition and edit a draft job requisition, so that
you can see the estimated time to hire before finalizing the details of the requisition.
When you start creating a job requisition, only the estimated time to hire is displayed. When the requisition reaches
the Open phase, another number is displayed to indicate the current number of days for which the requisition has been
open, letting you compare the current time with the estimated time to hire. After a first hire is made on the requisition,
the current number of open days is no longer displayed. It's replaced by the number of days it took for a first hire to be
made.
You can use the feature to model scenarios where the location or education required for that position is changed. For
example, you’ve posted a role for an Engineer in San Francisco and you view a prediction of 42 days to hire. You can
then model a scenario where you change the location to California to see how the days to hire prediction is impacted.
You can change the value of these 3 fields displayed in the Estimated Time to Hire section so you can see the impact it
has on the time to hire prediction.
• Requisition Title
• Education Level
• Locations
When you change these values, it has no impact on the actual requisition values. You need to change the corresponding
values in the requisition details if you want to keep them.

---

## How Time to Hire Works
*Chunk ID: OHR-USE-0050 | Chapter: Job Requisitions | Guide: Using Recruiting*

The Time to Hire model trains on all job requisitions that had a hire in the last 365 days, and each job requisition can
influence the prediction outcome. It not only considers the length of time that a job requisition was open, but also
considers factors such as the job location and title. Therefore, the time to hire predictions are more than just an average
of the time it took to close historical requisitions.
The Time to Hire feature uses a supervised machine learning model known as Random Forest. This classification
algorithm works by generating and comparing all the job requisition input data with all possible variations of that same
input data. After these computations are made for all possible variations, an average is taken across the entire set to
generate a prediction.
After every job requisition is closed, the model uses the days required to close the requisition to improve the quality of
future recommendations. The Time to Hire model trains on this and other new data once a week. So, if you’re hiring
within a short period of time, you can’t expect an immediate change in the predication.

---

## View Job Requisitions in a Position
*Chunk ID: OHR-USE-0051 | Chapter: Job Requisitions | Guide: Using Recruiting*

When you view the details of a position, you can see a list of requisitions created for this position.

Positions are available in the Position Details work area (My Client Groups > Quick Actions > Workforce Structures >
Position Details)
• Only active requisitions are displayed (requisitions that aren't Filled or Canceled).
• Only requisitions that you're allowed to see are displayed.
• Ten requisitions are listed. New requisitions are displayed first. You can load more if you want.
• For each requisition, the following information is displayed: Requisition Title, Requisition Number, Requisition
Status.
• You can navigate to the requisition to see more details.

---

## Pipeline Job Requisition
*Chunk ID: OHR-USE-0052 | Chapter: Job Requisitions | Guide: Using Recruiting*

You use pipeline requisitions when you have positions you always have a need to fill.
You can use pipeline requisitions to avoid having several very similar jobs on your career sites. You post a single pipeline
requisition on your career site to which candidates can apply. You can then review candidates on this pipeline requisition
and add relevant candidates to a linked standard requisition for which these candidates are a good fit, based on
experience, location, or any other criteria you see fit.
You can also use pipeline requisitions for jobs your organization is often hiring. You always have a requisition for
candidates to apply, even if no opening is currently available. Once an opening becomes available, you can create a
linked standard requisition and add the candidates from the pipeline requisition to the linked standard requisition.

---

## Create a Pipeline Job Requisition
*Chunk ID: OHR-USE-0053 | Chapter: Job Requisitions | Guide: Using Recruiting*

You create a pipeline job requisition when you have positions you always have a need to fill.
Before you start
You need the privilege Initiate Pipeline Job Requisition (IRC_INITIATE_PIPELINE_JOB_REQUISITION).
Here's what to do
1. On the Job Requisitions page, click Add.
2. In the Requisition Type field, select Pipeline.
3. Complete fields as for a standard job requisition.
Note that pipeline job requisitions use a candidate selection process different than the one used in standard job
requisitions. Only processes of type Pipeline can be selected on pipeline job requisitions.
4. Click Submit.
What to do next
Create a Standard Job Requisition Linked to a Pipeline Job Requisition
Related Topics
• Create a Job Requisition

---

## Create a Standard Job Requisition Linked to a Pipeline
*Chunk ID: OHR-USE-0054 | Chapter: Job Requisitions | Guide: Using Recruiting*

Job Requisition
When a pipeline requisition is created and approved, you can create a standard requisition that's linked to the pipeline
requisition.
You can create a linked requisition from a template, a position, an existing requisition, or from a blank requisition. The
default choice is to create it from an existing requisition and the pipeline requisition is selected by default. You use
this standard requisition to hire candidates who were initially gathered on a pipeline requisition. You can have several
standard requisitions linked to the same pipeline requisition.
1. Open the pipeline job requisition.
2. In the Linked Requisitions section, click Add.
3. Select Create Job Requisition.
4. Complete fields as for a standard job requisition.
5. Click Submit.
What to do next
Link a Job Requisition to a Pipeline Requisition

---

## Link a Job Requisition to a Pipeline Requisition
*Chunk ID: OHR-USE-0055 | Chapter: Job Requisitions | Guide: Using Recruiting*

You can link an existing standard job requisition to a pipeline requisition.
You can use the Link to Pipeline Requisition action available on the Job Requisitions page and requisition details page.
You can also use the Link Existing Requisition action in the pipeline requisition.
Before you start
You need the privilege Associate Job Requisition to Pipeline Requisition
(IRC_ASSOCIATE_JOB_REQUISITION_TO_PIPELINE_REQUISITION).
Here's what to do
1. On the Job Requisitions page, use the Pipeline criteria in the Requisition Type filter to easily locate the pipeline
requisition.
2. Open a pipeline requisition.
3. In the Linked Requisitions section, click Add then select Link Existing Requisition.
4. Select one or more standard requisitions.
5. Click Save and Close.
Results:
The requisition is added to the Linked Requisitions section. In that section, requisitions are sorted by Creation Date New to Old. You can use the filter to display all linked requisitions or just the active ones.
Related Topics
• Rules to Link a Job Requisition to a Pipeline Requisition

---

## Rules to Link a Job Requisition to a Pipeline Requisition
*Chunk ID: OHR-USE-0056 | Chapter: Job Requisitions | Guide: Using Recruiting*

When you link an existing standard job requisition to a pipeline requisition, you need to consider these rules.
Only requisitions matching the following criteria can be linked to a pipeline requisition:
• The requisition is a standard job requisition that isn't linked to a pipeline requisition.
• The requisition is active meaning it's not filled nor canceled.
• The requisition has no prospects nor job applications including draft job applications.
• The requisition isn't scheduled to be posted and isn't posted on an external or internal career site, or on a job
board.
• The requisition has no recruiting agent linked to it.
If the pipeline requisition matches one of these criteria, you can't link a standard requisition to it:
• The pipeline requisition is in the Draft phase.
• The pipeline requisition is in the Approval phase.
• The requisition if Filled.
• The requisition is Canceled.
When you link a standard job requisition to a pipeline job requisition, the standard requisition is adjusted so it's a valid
linked requisition:
• The value of the External Application Flow field is set to the value in the pipeline requisition.
• The value of the Allow Candidates to Apply When Not Posted field is set to No.
• The value of the Automatically Open Requisition for Sourcing field is adjusted as follows:

◦ If the field is set to Yes, posted internally, Yes, posted externally, or Yes, posted internally and externally,
◦

the field is set to Yes, not posted.
If the field is set to Yes, not posted or No, the field value is preserved.

• The value of the Automatically Unpost Requisition field is set to No.
• Screening services configuration related to application flows defined on the requisition are removed.
• If the requisition is currently in the Posting In Progress status, the status is changed to Job Formatting In
Progress.

---

## View a Pipeline Requisition to Which a Requisition is
*Chunk ID: OHR-USE-0057 | Chapter: Job Requisitions | Guide: Using Recruiting*

Linked
You can view the pipeline requisition to which a standard requisition is linked, even if the linked requisition is draft. The
View Pipeline Requisition action is available for all linked requisitions, but is especially useful for draft ones because this
is the only way to know to which requisition this is linked to.
Before you start

The View Pipeline Requisition action is available if the current requisition is a linked requisition and you have access to
the pipeline requisition.
Here's what to do
1. On the Job Requisitions page, use the Standard criteria in the Requisition Type filter to easily locate standard
requisitions.
2. Open a standard job requisition.
3. In the Actions menu, select View Pipeline Requisition.

---

## Add Candidate Job Applications to a Linked Requisition
*Chunk ID: OHR-USE-0058 | Chapter: Job Requisitions | Guide: Using Recruiting*

After the pipeline and linked standard requisitions are created, you can add candidate job applications of a pipeline
requisition to a linked standard requisition.
Before you start
You can only add confirmed job applications to a linked standard requisition.
Here's what to do
1. Open a candidate job application associated to a pipeline requisition.
2. In the Actions menu, select Add to Linked Requisition.
3. Select a job requisition.
4. Click Save and Close.
Results:
New job applications are automatically created on the linked standard requisition and candidates need not apply again
to the job requisition.
The source info on the new job applications indicates that the candidate was added to the job requisition, since the job
application was added by a user. The source medium indicates “Candidate added to job requisition” and the source
indicates “Job Requisition”.
Most of the information of the pipeline job application is copied to the linked standard job application, except the
following information:
• Interactions
• Screening services results
• Answers to prescreening questions
• Interview feedback

---

## View Pipeline Job Application Content in a Linked
*Chunk ID: OHR-USE-0059 | Chapter: Job Requisitions | Guide: Using Recruiting*

Requisition
You can view content that was captured on a job application for a pipeline requisition while viewing the job application
on a linked requisition.

All the information gathered on a pipeline job application is available directly in the linked job application, whether the
information was gathered before or after the candidate was added to a linked requisition. This applies to info in the
following tabs:
• Screening
• Prescreening
• Feedback
• Interactions
For example, when you're on the Interactions tab of a job application for a linked requisition, you can decide to display
interactions from the linked job application or from the pipeline job application.

---

## Pipeline Requisitions and Candidate Experience
*Chunk ID: OHR-USE-0060 | Chapter: Job Requisitions | Guide: Using Recruiting*

On the candidate self service page, if and only if the candidates are active on the pipeline requisitions or one of linked
standard requisitions, they can view their job applications on the pipeline requisitions. Job applications on linked
requisitions aren't displayed.
Note: Linked requisitions can't be posted on career sites. You need to make them open using the Open for Sourcing
action to add job applications to it from the pipeline requisition.
On the candidate self service page, the following statuses are displayed for job applications on pipeline requisitions:
• Under Consideration: The candidate has an active job application on the pipeline requisition or on one of the
requisitions linked to the pipeline requisition.
• Not Retained: The candidate has job applications on a terminal state (Rejected by Employer or Withdrawn by
Candidate) on the pipeline requisition and on all the requisitions linked to the pipeline requisition.
• Offer Accepted: The candidate has a job application on one of the requisitions linked to the pipeline requisition.
For one of these standard requisitions, the current phase is the HR phase and the current state isn't a terminal
state (Rejected by Employer or Withdrawn by Candidate).

---

## Job Requisition Multilingual Content
*Chunk ID: OHR-USE-0061 | Chapter: Job Requisitions | Guide: Using Recruiting*

Oracle Recruiting Cloud is available in multiple optional languages to deliver a multilingual recruiting experience.
When you sign in Oracle Applications, you can select your session language in your user preferences. American English
is the default session language for the first visit (the application remembers the last session language). The session
language you select defines the language of every label in a product. The session language is used as the creation
language. For example, Spanish is installed in the environment so when you sign in Spanish, you create job requisitions
in Spanish.
When you create a job requisition, you select the languages in which the job requisition is available. Note that you can't
remove the language used to create the job requisition. When the job requisition is created, you can then translate
the job requisition content in the selected languages. This makes it easier for you to translate job requisitions in the
preferred languages instead of translating them in all the activated languages in your organization.

You can provide translation at any point during the job requisition lifecycle, as long as the job requisition is active. This
means, if you make changes to the translation while the job requisition is posted, the changes are visible to candidates.
When you duplicate a job requisition, the multilingual content is copied from the source job requisition to the new
requisition. When you create a job requisition from a job requisition template, the multilingual content of the template
is copied to the new job requisition. When you duplicate a job requisition, the multilingual content is copied from the
source job requisition to the new requisition. When you create a job requisition from a job requisition template, the
multilingual content of the template is copied to the new job requisition.

---

## Translate a Job Requisition
*Chunk ID: OHR-USE-0062 | Chapter: Job Requisitions | Guide: Using Recruiting*

You use the Translate Job Requisition action to translate the content of the job requisition.
You can translate these values:
• Requisition Title
• Other Requisition Title
• Short Description for Internal Candidates
• Description for Internal Candidates
• Responsibilities for Internal Candidates
• Qualifications for Internal Candidates
• Short Description for External Candidates
• Description for External Candidates
• Responsibilities for External Candidates
• Qualifications for External Candidates
• Media title (in Job Formatting tab)

---

# Job Requisition Posting and Sourcing

## Job Requisitions in Workforce Modeling
*Chunk ID: OHR-USE-0063 | Chapter: Job Requisition Posting and Sourcing | Guide: Using Recruiting*

Workforce Modeling provides managers and human resources (HR) specialists with the ability to plan, model, and
perform workforce changes using a graphical tool.
You create models which include job requisitions, using the workforce modeling. When you create a workforce model,
existing job requisitions located in the hierarchy of the model's top-level manager are included as part of the default
data included in the model. Data security is enforced. Only job requisitions which you're allowed to see are included in
the model.
Within a workforce model, you can create new job requisitions. Requisitions created in a model only exist within the
model. You need the privilege Initiate Job Requisition (IRC_INITIATE_JOB_REQUISITION) to create job requisitions in a
model.
You can also view, edit, and move job requisitions within the workforce model hierarchy.

After the workforce model is ready, you can implement the model to create or update job requisitions within Oracle
Fusion Cloud Recruiting. The model is implemented if there are no conflicts between the model and the existing job
requisitions. In Oracle Recruiting, requisitions are created in the Draft - In Progress status.

3 Job Requisition Posting and Sourcing
Post a Job Requisition on a Career Site
When you're done creating and entering all the details of a job requisition, you can post the requisition on a career site
so candidates can apply to it.
1. On the Job Requisitions page, open a job requisition.
2. In the Actions menu, you can choose one of these actions:
◦ Move to Posting: Use this action to move the job requisition to the Posting phase.

◦ Open for Sourcing: Use this action to move the job requisition directly to the Open phase without posting
the job requisition first.

3. Click the Posting tab.
4. On the Posting page, decide if the job requisition is posted on the internal career site, on external career sites, or
both. Click the Edit button.
5. Select the posting schedule: Post Now, Post Later, or Do Not Post.
6. Depending on the posting schedule you selected, enter the start date, the expiration date, and the time zone.
7. Click Save.
Results:
Here's what happens after you click Save:
• If the job requisition is posted immediately, its status changes to Open - Posted.
• If the job requisition is posted later, its status changes to Open - Scheduled.
• If the job requisition status is Open - Scheduled, it's posted to the career sites when the start date is reached
and the status is changed to Open - Posted.
• If the posting expiration date is reached, the job requisition is removed from the career sites and the status is
changed to Open - Expired after the two postings (internal and external) have expired.
• Let's say posting jobs to Google is enabled within your organization and you post a job requisition to an
external career site. In such a case, Google is notified that a new job is available to be posted on Google.
Note: Jobs are posted to particular sites based on the context set for these sites, such as location, organization, job
category, job function, recruiting type, job requisition flexfields (refer to Implementing Recruiting for details).

---

## Job Requisition Info Visible to Candidates
*Chunk ID: OHR-USE-0064 | Chapter: Job Requisition Posting and Sourcing | Guide: Using Recruiting*

When a job requisition is posted on an external career site, some fields in the requisition are visible to candidates.
• Requisition title
• External short description

• Primary location and number of other locations
• External description (displayed as Job Description), responsibilities, and qualifications
• Employer description (displayed as About Us)
• Recruiting organization description (displayed as About The Team)
Additionally, in the Job Info section of a job details page, candidates can see the following details:
• Requisition number
• Job category
• Locations
• Posting start date
• Posting end date
• Degree level
• Job schedule
Note: These fields are exposed to candidates out-of-the-box. More fields can be exposed using site editor and
Design Studio capabilities.
Fields display in the order in which they were added during the configuration of the page.
Note: The Locations value varies depending on the job requisition configuration. If work locations were added for a
job, both Primary Work Location and Other Work Locations are visible in the Locations field. If work locations weren't
defined for the job, Primary Location and Other Locations are shown in that section.

---

## Post a Job Requisition on a Job Board
*Chunk ID: OHR-USE-0065 | Chapter: Job Requisition Posting and Sourcing | Guide: Using Recruiting*

If job distribution partner services are enabled within your organization, you can post job requisitions to job boards.
Before you start
Only jobs posted on external career sites can be posted on a job board.
Here's what to do
1. On the Job Requisitions page, open a job requisition.
2. Click the Posting tab.
3. In the Job Boards section, click Select job boards for posting.
4. Select the supplier, account, and language.
5. You're taken to the supplier's site where you select the job boards where you want to post the job requisition.
All the required job requisition fields are populated on the partner's portal. Let's say that the partner supports
multilingual postings and the job requisition is available in more than one language. In such a scenario, the job
requisition data in all the languages is also available on the partner's portal. You can simply enter any additional
information required and schedule the posting in multiple languages on the partner's portal.
6. Click Save.
What to do next

After the job requisition is posted on the partner's portal, you can review the status of the posted job requisition on the
job requisition's Posting tab.
You want to edit previously entered information, change posting dates, or post the job in an additional language? All
you need to do is to access the partner's portal and edit the job posting information provided the job requisition is
either already posted or scheduled to be posted. Furthermore, you can also remove a posting.
As soon as the job requisition posting ends, the job requisition status changes to Open - Expired and you're notified to
remove the job from the job boards. In case the job requisition is filled or canceled, it's automatically removed from the
job boards.

---

## Automatically Open a Job Requisition for Sourcing
*Chunk ID: OHR-USE-0066 | Chapter: Job Requisition Posting and Sourcing | Guide: Using Recruiting*

You can automatically open a job requisition for sourcing once it's approved, and post it on career sites.
1. On the Job Requisitions page, create a job requisition or open a draft requisition.
2. In the Configuration section, select the option Automatically Open Requisition for Sourcing.
3. Select one of these values:
◦ No: The requisition isn't automatically open for sourcing. This is the default value.

◦ Yes, not posted: The requisition is open automatically for sourcing, but it's not posted.
◦ Yes, posted internally: The requisition is open automatically for sourcing, but it's only posted on the internal
◦
◦

career site.
Yes, posted externally: The requisition is open automatically for sourcing, but it's only posted on external
career sites.
Yes, posted internally and externally: The requisition is open automatically for sourcing, and it's posted on
internal and external career sites.

4. When you set the requisition to be automatically open and posted, you can define the number of days after which
the requisition posting will expire. If the No Expiration option is selected, the posting won't expire.
5. Click Save and Close.
Results:
When you submit the requisition for approval and the requisition is approved, the configuration option you selected is
performed. The Job Formatting and Posting phases are skipped, the job requisition moves to the appropriate state of
the Open phase, and it's posted on the selected career sites if applicable.

---

## Automatically Unpost a Job Requisition
*Chunk ID: OHR-USE-0067 | Chapter: Job Requisition Posting and Sourcing | Guide: Using Recruiting*

When you create or update a job requisition, you can specify if the requisition will be automatically unposted from the
internal career site, the external career sites, or both.
Before you start
If the job requisition is currently not posted, it won't be possible to post it if the automatic unpost condition is currently
met.
Here's what to do

1. On the Job Requisitions page, open a job requisition.
2. In the Configuration section, set the Automatically Unpost Requisition field to one of these values:
◦ Yes, unpost internally only

◦ Yes, unpost externally only
◦ Yes, unpost internally and externally
3. In the Automatically Unpost Condition field, select the condition when the unpost will happen.

---

## Invite Candidates to Apply on Job Requisitions Not
*Chunk ID: OHR-USE-0068 | Chapter: Job Requisition Posting and Sourcing | Guide: Using Recruiting*

Posted
You can invite candidates to apply on a job requisition that's currently not visible to other candidates. This could be the
case if your organization wants to fill a high-level job or even a replacement and they want to keep it confidential.
1. On the Job Requisitions page, open a job requisition.
2. In the Configuration section, click Edit.
3. Select the option Allow Candidates to Apply When Not Posted.
4. Click Save.
5. You now need to add candidates to the job requisition using the Add Prospect action or the Add to Job Requisition
action.
Results:
Candidates receive an email containing a link to apply for the job. Candidates are redirected to an external or internal
career site depending on the candidate type. For a job that's not posted, using this link is the only way candidates can
apply for the job as it won't be there in the job list on the career site.
If the job requisition is posted externally and you enable the option Allow Candidates to Apply When Not Posted,
employees will be able to apply to the requisition because they can access the job details page on the internal career
site. Requisitions posted externally appear on the internal career site to allow employees to refer other people. If you
don't want employees to apply to the requisition, you need to disable the option.
You can change the value of the Allow Candidates to Apply When Not Posted option in all phases of the requisition
lifecycle except when the state of the phase is Canceled, Filled, or Rejected.

---

## Fill a Job Requisition Manually
*Chunk ID: OHR-USE-0069 | Chapter: Job Requisition Posting and Sourcing | Guide: Using Recruiting*

You can fill job requisitions manually when the required number of candidates was hired for the job, regardless of the
number of active candidates on the requisition.
You can't fill a job requisition if candidate job applications have these statuses:
• Offer - Pending Approval: To close the job requisition, the candidate job application must be withdrawn from
the offer approval cycle by the submitter or it must be rejected by the approver.

• Offer - Extended: The job requisition can't be filled if a job offer was extended to a candidate. To close the job
requisition, the candidate need to accept the job offer so that you can start the HR phase to hire the candidate.
Or, you can reject the candidate manually and inform the candidate.
• Offer - Accepted or other active states in any custom phase that's been configured after the Offer phase:
The job requisition can't be filled if a job offer was accepted by a candidate and is still active. To close the job
requisition, the candidate job application must either be moved into the HR phase where it's considered inactive
and successful, or moved into the state Rejected or Withdrawn by Candidate where it's considered inactive.
1. On the Job Requisitions page, open a job requisition that's in phase Open, except Open - Canceled and Open - Filled.
2. In the Actions menu, select Fill Job Requisition.
Results:
Here's what happens next:
• If the number of candidates is 50 or less, the fill action is done immediately.
• If the number of candidates is higher than 50, a message is displayed explaining that the requisition will soon
be filled. When the fill action is complete, you'll receive a notification containing info about the number of job
applications that were processed for each of theses statuses:

◦ Succeeded: Job applications that were successfully processed.
◦ Failed: Job applications that weren't successfully processed.
◦ Skipped: Job applications that didn't need to be processed.
While waiting for the requisition to be filled, you can continue working on the requisition and its job
applications. For instance, you can close the requisition manually, you can disposition job applications
manually.
• The job requisition is removed from the Job Requisitions list as it's filtered out by default. If you want to view
job requisitions that were filled, use the Include Inactive Requisitions filter on the Job Requisitions list.
• Active candidate applications who applied on the job requisition are moved to the predefined Rejected by
Employer state of the phase they're currently in.
What to do next
To view job requisitions that were filled, use the Include Inactive Requisitions filter on the Job Requisitions list.

---

# Prescreening Questionnaires

## Fill a Job Requisition Automatically
*Chunk ID: OHR-USE-0070 | Chapter: Prescreening Questionnaires | Guide: Using Recruiting*

You can automatically change the status of a job requisition to Filled once the number of hired candidates matches the
number of openings on the job requisition.
There are situations where the Automatically Fill Requisition option is enabled but job requisitions aren't automatically
filled. For example:
• The job application is in the Offer - Pending Approval status.
• The job application is in the Offer - Extended status or later status in the selection process (but not in the HR
phase) which includes:

◦ Offer - Accepted

◦ Custom phases after the Offer phase, but not the terminal states Rejected by Employer, Withdrawn by
Candidate. Job applications in terminal states don't prevent automatic filling.

• The job requisition includes a job application on a state which has a Move Condition which isn't met. The job
application won't be rejected and the job requisition won't automatically be filled.
This automatic filling is triggered when moving a job application to HR phase. The requisition won't automatically fill
at a later point if the necessary conditions are met at a later time. For example, if you have job applications in the Offer
phase when doing a Move to HR on another job application, this will prevent the automatic filling. Later rejecting the job
applications in the offer phase won't trigger the requisition to be automatically filled. The Fill a Job Requisition Manually
process will need to be used.
1. On the Job Requisitions page, open a job requisition.
2. Click the Details tab.
3. In the Configuration section, click Edit.
4. Set the Automatically Fill Requisition option to Yes.
Results:
Here's what happens next:
• If the number of candidates is 50 or less, the fill action is done immediately.
• If the number of candidates is higher than 50, a message is displayed explaining that the requisition will soon
be filled. While waiting for the requisition to be filled, you can continue working on the requisition and its
job applications. For instance, you can close the requisition manually, you can disposition job applications
manually.
• Active candidate applications who applied on the job requisition are moved to the predefined Rejected by
Employer state of the phase they're currently in.
• The job requisition is automatically unposted from all career sites and job boards.
• When the fill action is complete, you'll receive a notification containing info about the number of job
applications that were processed for each of theses statuses:

◦ Succeeded: Job applications that were successfully processed.
◦ Failed: Job applications that weren't successfully processed.
◦ Skipped: Job applications that didn't need to be processed.

4 Prescreening Questionnaires
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
*Chunk ID: OHR-USE-0071 | Chapter: Prescreening Questionnaires | Guide: Using Recruiting*

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

## Prescreening Question
*Chunk ID: OHR-USE-0072 | Chapter: Prescreening Questionnaires | Guide: Using Recruiting*

Prescreening questions are used to ask candidates about their career goal, job preferences, knowledge, and more. If a
prescreening question is configured as required, the candidate can't skip it while applying for the job.

---

## Here's an example of a prescreening question: "How good are your Java skills?"
*Chunk ID: OHR-USE-0073 | Chapter: Prescreening Questionnaires | Guide: Using Recruiting*

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

## Reorder Questions in a Prescreening Questionnaire
*Chunk ID: OHR-USE-0074 | Chapter: Prescreening Questionnaires | Guide: Using Recruiting*

You can define the order of prescreening questions displayed to candidates when they apply for a job.
Before you start
You can't reorder questions when the job requisition has the following status:
• Draft - In Progress
• Canceled state of any phase
• Open - Filled
Here's what to do
1. On the Job Requisitions page, open a job requisition.
2. Click the Details tab.
3. Expand the Questionnaires section.
4. Click Reorder to open the Reorder Questions page.

5. Use the Move question up and Move question down icons to change the order of questions in internal and
external prescreening questionnaires. You can reorder disqualification questions and prescreening questions added
automatically or by the user.
6. Click Save and Close.

---

## View the Overall Score of Prescreening Questions
*Chunk ID: OHR-USE-0075 | Chapter: Prescreening Questionnaires | Guide: Using Recruiting*

When a candidate applies for a job and answers prescreening questions, you can see the overall score to the
prescreening questions in the candidate's job application.
When you view the job applications for a job requisition, you can sort the applications using these two criteria:
• Score - High to Low
• Score - Low to High

---

# Screening Services

## View Job Applications Having a Specific Prescreening
*Chunk ID: OHR-USE-0076 | Chapter: Screening Services | Guide: Using Recruiting*

Question and Answer
If you want to see the list of job applications where a specific answer was provided for a prescreening question, use the
Question and Answer filter in the job applications list. This filter shows the following questions and responses:
• Questions from the internal prescreening questionnaire of the current requisition.
• Questions from the external prescreening questionnaire of the current requisition.
• Questions with responses of type Single Choice.
• Questions with responses of type Multiple Choice.

5 Screening Services
Background Check
You can use a background check during the candidate selection process to investigate a candidate's background before
hiring them.
A check on a candidate's background might include verifications such as employment history, education, criminal
records. After the background check is complete, candidates are ready to be moved to the next step in the recruiting
process.
Your administrator configures when the background check is automatically triggered during the candidate selection
process. The background check partner obtains the candidate's info and completes the background check. You then
receive a notification.
If you create a job requisition based on a template which contains background checks, the background checks are
added to the requisition. You can edit the selected background check packages. If you create a requisition using a blank
form, you can add background checks in the Screening Services section. You can add one or more background check
packages, usually many packages with a single screening.
Note: You can add background check packages to requisitions in draft state, or other states as long as there are no
job applications.
Depending on how background check was configured by your administrator, there are two possible ways to add
background check packages to a job requisition:
• From the partner's site: After you select a background check partner and a user account, you can click a link to
go to the partner's site to add the background check packages to the job requisition. You can also specify the
order in which the partner will run the screening packages. You can go to the partner's site to view details about
a candidate's background check results or to order additional screenings.
• Directly in Oracle Fusion Cloud Recruiting: After you select a background check partner and a user account, you
can select packages without having to go to a partner's site.
◦ If one background check trigger was configured in the candidate selection process, you can select one or
more packages for the phase or state that has the background check trigger.
◦ If many background check triggers were configured in the candidate selection process and the partner
supports multi phases and states, you can select one or more packages for the different phases and
states that have the background check trigger.
◦ If many background check triggers were configured in the candidate selection process and the partner
doesn't support multi phases and states, you can select one or more packages to one of the phase or
state.
When you go to the Screening section of job applications, you can view the background check partners and packages
that were copied from the job requisition to the job application. You can also view the status of the background check
and background check results. These statuses are displayed:
• Canceled
• Candidate Input Required
• Complete

• Completed - Pass
• Completed - Fail
• Completed - To Be Verified
• Declined By Candidate
• Error
• Initiated
• In Progress
• Not Triggered
Note: The status icon represents the last updated status from the partner. As an example, if the first partner update
is Completed - Fail and the second update is Completed - Pass, the green check mark icon is displayed.
You can edit background check packages in job applications if you meet these conditions:
• The package selection must be done within Oracle Recruiting. If you need to go to the partner's site, you can't
change packages at the job application level.
• You need the privilege Update Candidate Job Application Screening Package
(IRC_UPDATE_CANDIDATE_JOB_APPLICATION_SCREENING_PACKAGE).
• The job application isn't in Rejected state, Withdrawn state, or in HR phase.
• You can remove packages not yet triggered.
• You can add packages on triggers not yet reached.
Note: Partners aren't aware of job application status changes after they receive a request. As a result, it's possible for
candidates to take an assessment regardless of the job application status. Partners can also update the assessment
results regardless of the job application status.

Assessment
You use assessments to assess and measure the knowledge, skills, abilities, and attributes of candidates for a job.
When you create a job requisition, you add assessments in the Screening Services section. You can add one or more
assessment screening packages. After you select the assessment partner and user account, you need to decide if
candidates take the assessment when applying for a job, or during the candidate selection process, or both.
• For assessments during the job application, select the assessments for the internal job application flow, the
external flow, or both. A link is displayed in the candidate self-service and candidates can take the assessment
right after submitting their job application. If your administrator enabled inline assessments, candidates fill
the assessment before they submit their job application. When recruiters create job applications on behalf
of candidates, application flow level assessments aren't automatically triggered. If the candidate must fill
such assessment, the recruiter must manually trigger it. The partner will receive the request. If the candidate
must take the assessment after the application flow, the candidate will see a link to take the assessment in the
candidate self-service.
• For assessments during the selection process, select the phase and state when the assessment request is
sent to candidates, then select the assessments. When a job application is at the phase and state selected,
the assessment partner's service is called to initiate one or multiple assessments, based on its configuration.
The partner validates the user requesting the screening service and retrieves candidate and job requisition

information. After the partner receives all the information, the status of the assessment is set to "Started". The
partner then sends an email to the candidates with a link to take the assessments. The partner updates the
status to "In progress" when the candidates start the assessment process. After the candidates complete all the
assessments, the partner updates the status to Completed, Completed - Fail, Completed - Pass, Completed - To
be Verified and the overall assessment results are available in the candidate job applications.
Note: Partners aren't aware of job application status changes after they receive a request. As a result, it's possible for
candidates to take an assessment regardless of the job application status. Partners can also update the assessment
results regardless of the job application status.
You can view the status of the assessment and assessment results in the Screening section of the candidate job
application. You can also go to the partner's site to view additional details about a candidate's assessment results. When
the assessment is complete, candidates are ready to be moved to the next step in the recruiting process.
You can use these assessment filters when you view candidate search results, members of a candidate pool, prospects
for a job requisition, and job applications:
• Assessment Package
• Assessment Status
• Assessment Score

---

## Tax Credit Screening
*Chunk ID: OHR-USE-0077 | Chapter: Screening Services | Guide: Using Recruiting*

You use tax credit screenings to validate tax credit eligibility of candidates. Candidates can be eligible to various federal,
state, and other tax credits.
You add tax credit screenings in the job requisition Screening Services section. You can assign one tax credit screening
package with multiple screenings. You then select the desired partner and user account, and also a location package, if
needed. Indicate if the tax credit screening is triggered during the candidate application flow or the candidate selection
process. When you save the changes, you can see the selected screening packages on the job requisition Screening
Services section.
The tax credit screening is automatically triggered during the external job application flow or when candidates reach a
specific phase and state in the candidate selection process as configured by your administrator. The tax credit partner
receives the request and retrieves info from the job requisition, the location package, and the candidate. The partner
might invite the candidate to complete required forms, if needed. Once the tax credit screening is completed, you
receive a notification. You can view the status of the tax credit screening in the candidate job application Screening
section. You can also go to the partner's site to review the candidate's detailed results or access official forms.
You can view the status of the tax credit screening in the candidate job application Screening section. You can also go to
the partner's site to review the candidate's detailed results or access official forms.
Note: When you create a job requisition based on a template, screening packages selected for the requisition
template are added to the job requisition.

Note: If hiring confirmation is used for hiring requisitions associated to pipeline requisitions, the initiated tax credit
trigger should also be placed at the hiring requisition level. When no hiring confirmation is used, the trigger can be
defined at the pipeline job requisition level.

Note: Partners aren't aware of job application status changes after they receive a request. As a result, it's possible for
candidates to take an assessment regardless of the job application status. Partners can also update the assessment
results regardless of the job application status.

---

## Manually Initiate Screening Services
*Chunk ID: OHR-USE-0078 | Chapter: Screening Services | Guide: Using Recruiting*

You can manually initiate screening services without having to move candidates in the candidate selection process.
Before you start
You need the privilege Manually Trigger Screening Packages (IRC_MANUALLY_TRIGGER_SCREENING_PACKAGES).
Note: Your administrator may have configured the candidate selection process so that a screening service is initiated
automatically when a job application reaches a specific state in the candidate selection process. If you do decide
to manually initiate a request that's already been automatically requested, this request and the ones requested
automatically will all be initiated right away. You won't have to wait for the scheduled process to be completed, which
is recommended to be run every 10 minutes.
Here's what to do
1. Open a candidate a job application.
2. Click the Screening tab.
3. In the Actions menu, select Initiate Request.
4. For background check or assessment categories, you can select the screening service package you want to initiate.
You can select one or multiple packages. You can't select packages in status Completed and In Progress. For tax
credits, there is no package selection because multiple packages aren't supported.
5. Click OK.
What to do next
If later on you want to cancel a screening service, use the Stop Request action.

---

# Candidate Search

## Edit a Screening Service in a Job Requisition
*Chunk ID: OHR-USE-0079 | Chapter: Candidate Search | Guide: Using Recruiting*

You can change the configuration of screening services in job requisitions that are no longer in the draft phase.
As an example, you want to change a partner at the end of a contract or add packages due to new legislation.
If you have the Update Job Requisition (IRC_UPDATE_JOB_REQUISITION) and Update Job Requisition After Draft
Phase (IRC_UPDATE_JOB_REQUISITION_AFTER_DRAFT_PHASE) privileges, you can edit the configuration of screening
services in a requisition as long as there are no job applications on the requisition. You can edit screening services when
the requisition is in any of these phases:
• Approval
• Job Formatting
• Posting
• Open

The configuration of these screening services is possible: background checks, assessments, tax credits.
Note that some of the screening services configurations might show as being deactivated if the action is deactivated in
the candidate selection process:
• When your administrator modifies actions of a candidate selection process that generates additional
configuration on job requisitions, the configuration of the job requisition or requisition template using this
process is updated accordingly.
• When a job requisition uses a candidate selection process with deactivated actions, these actions are still visible
on the job requisition configuration, but there is an indication that they're deactivated.
• For actions that are waiting to receive information by a candidate (interview invite), the information will be
accepted even if the corresponding action has been deactivated. The fact that the action is deactivated only
impacts its triggering, not the reception of information after.

6 Candidate Search
You use the candidate search to find qualified candidates for current or planned open positions.
When you search for candidates, you can enter keywords, use boolean expressions, advanced search criteria, LinkedIn
search, basic filters, and perform actions on the candidates that are retrieved. Each time a criteria is selected, the Total
Candidates number gets updated to provide feedback on the results.

---

## Find a Known Candidate
*Chunk ID: OHR-USE-0080 | Chapter: Candidate Search | Guide: Using Recruiting*

You can quickly look up known candidates using the Find a Candidate feature. Select Find a Candidate from the Search
Action menu. Enter the appropriate information and click Search to start the search. When using this search method,
take the following into consideration:
• Phone number searches must have a country code, area code, and the complete number with no dashes.
• Email searches must contain full email addresses.
• Keyword search doesn't support search by email address or phone number.
Phone number searches must have a country code, area code, and the complete number with no dashes.

---

## Keyword Search
*Chunk ID: OHR-USE-0081 | Chapter: Candidate Search | Guide: Using Recruiting*

When you search for candidates, you can enter a keyword in the Search field. As you enter letters in the Search field,
words matching the characters you typed are displayed. The list continues to narrow as you enter more characters. You
can select an item from the list and click the Search icon.
Keywords are searched in the following fields of the candidate file:
• Candidate Number
• Degree
• Employer Name
• Full Name
• Job Title
• Language
• Last Name
• License
• Major
• Medium
• Resume Text (resumes containing footers aren't parsed)
• School
• Skill
• Source

If you search for a candidate by entering their full name in the Keyword Search field, the search results will display
candidates having the same full name at the top of the results list. Candidates having the same first name or last name
will be displayed after them.

---

## Boolean Search
*Chunk ID: OHR-USE-0082 | Chapter: Candidate Search | Guide: Using Recruiting*

A boolean search is a type of search where you can combine keywords with operators such as AND, OR, NOT, and
parenthesis to produce more relevant results.
When you do a boolean search, consider the following:
• AND, OR, NOT and parenthesis "()" are the supported boolean operators.
• You can search in different languages but the boolean operators remain the same (AND, OR and NOT).
• Anything between the operators will be considered as a full quoted text. Example: business analyst AND
"marketing manager" is the same as business analyst AND marketing manager.
• Wild card searches "*" aren't supported.
• Multi-level parenthesis aren't supported. Example: (manager AND (analyst OR associate)) isn't supported. But
manager AND (analyst OR associate) AND (computer OR electronics) is supported.
The table provides a detailed explanation of the boolean operators and examples.

Operator

Description

AND

---

## Use the AND operator to join keywords or different aspects of product marketing AND manager
*Chunk ID: OHR-USE-0083 | Chapter: Candidate Search | Guide: Using Recruiting*

search. Use AND to find candidate profiles that include both
search phrases. When you use AND in a search, it essentially business AND economics
narrows your results to the intersection of the two search
phrases or terms. Every candidate profile result will contain
sales AND marketing
both terms and typically limits your search results.

OR

---

## Use the OR operator to broaden the keywords or different
*Chunk ID: OHR-USE-0084 | Chapter: Candidate Search | Guide: Using Recruiting*

aspects of search that mean the same or similar thing. Use
OR to broaden your search by connecting two or more
synonyms. When you use OR in a search you can find
candidate profiles that include one term, the other term, or
all terms. The more search terms you enter connected by OR,
the more candidate profile results you get.

business analyst OR systems analyst

---

## Use the NOT operator to exclude a particular term from your
*Chunk ID: OHR-USE-0085 | Chapter: Candidate Search | Guide: Using Recruiting*

candidate search. Type NOT immediately before the term.
Candidate profile search results will exclude any profile that
contains that term.

business analyst NOT manager

NOT

Example

developer OR designer OR programmer
project OR program OR portfolio

bachelors NOT masters
developer NOT manager

()

---

## Use parenthesis "()" when you want to run complex search
*Chunk ID: OHR-USE-0086 | Chapter: Candidate Search | Guide: Using Recruiting*

queries combining the logical sections of the query. The
terms and operators inside the operators will be searched
first.

(Sales OR Marketing) AND (Vice President OR
Director)
(Company A OR Company B) NOT Company C

---

## Advanced Search Criteria
*Chunk ID: OHR-USE-0087 | Chapter: Candidate Search | Guide: Using Recruiting*

When you search for candidates, you can use these advanced search criteria to narrow down your search results and
improve the quality of your results:
• Candidate Details: Name, Language, Skill, Contact Info, Source, Source Medium
• Location: Postal Code, Location
• Education: School, Degree, Major
• Experience: License, Job Title, Years of Experience
• Company: Current Company, Past Company
When you use an advanced search criteria, the Total Candidates number is updated. When you see a * (star) next to the
Total Candidates number, it indicates that advanced search criteria were used.
Advanced search criteria are saved within the same session. If you search candidates using a criteria, go to some other
screen and come back, the criteria will still be available in that session.

---

## LinkedIn Search
*Chunk ID: OHR-USE-0088 | Chapter: Candidate Search | Guide: Using Recruiting*

You can find more candidates using LinkedIn’s search functionality, which is embedded in the Candidate Search page.
This provides a unified experience by allowing you to search and browse LinkedIn profiles from within Oracle Fusion
Cloud Recruiting. When you search for candidates on the Candidate Search page, the Search in LinkedIn Recruiter link is
displayed on the results page. Clicking this link takes you to the LinkedIn search page, where you can search and browse
for LinkedIn profiles. If you searched using a set of keywords on the Candidate Search page, clicking the LinkedIn search
link displays candidate search results based on those same set of keywords.
Note: When you click the LinkedIn search link, it takes you to the Recruiter sign in page, if you didn’t previously sign
in. You need to provide your credentials and select the contract type to view the LinkedIn search page.

---

## Search Results
*Chunk ID: OHR-USE-0089 | Chapter: Candidate Search | Guide: Using Recruiting*

When you click Search, candidates matching your search criteria are displayed.
You can use filters to narrow down the list of candidates.
You can use the grid view to display candidate data in a columnar layout. You can set your view to understand where
candidates are currently active on job applications, by viewing job applications and interactions information. You can
view a candidate's 3 most recent job applications, and the 3 most recent interactions taken against job applications. The
first 120 characters display for each interaction, but you can hover over them to see more content. If there are more than
3 applications, the number of applications is displayed at the bottom of the list in parenthesis. You can log an interaction
against a candidate profile, or against a pool member, but only job-specific interactions are shown.
Unconfirmed candidates don't appear in search results. To appear in search results, candidates must confirm their email
address or phone number. Deleted candidates don't appear in search results, but they're still available for reporting
purposes.
If your organization set up security based on the recruiting type, candidates with the Withdrawn by Candidate status
won't appear in search results.
In the search results page, the result indicates candidate profiles found using advanced search criteria and basic filters.
For example, if the search result is Candidates (7 of 15*) 15 candidates were found using advanced filters, and 7 using
basic filters.

---

## Actions on Retrieved Candidates
*Chunk ID: OHR-USE-0090 | Chapter: Candidate Search | Guide: Using Recruiting*

From the candidates list, you can perform several actions on candidates. Available actions are:
• Add to Requisition
• Add to Candidate Pool
• Add Interaction
• Send Message
• Delete Candidate
• Create a Candidate

---

# Prospects and Candidates

## Apply Bulk Actions to Candidates
*Chunk ID: OHR-USE-0091 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can apply a bulk action to up to 500 candidates on the Candidate Search page. This means you can send a message
to a maximum of 500 candidates at a time, or move up to 500 candidates at a time to a pool.
1. On the Candidate Search page, search for candidates, and filter the results if necessary until there are 500 or fewer
candidates in the results list.
2. Click Select All.
This check box only becomes available for use when the search results contain 500 or fewer results.
Clicking Select All selects all items in the search results, even if they're not immediately available on the page. You
can click Load More Items to show more.
3. Select an action from the Action menu.
4. Click Save and Close.
Results:
When the action is applied to 50 or fewer candidates, it's performed synchronously (immediately). If it's applied to
51-500 candidates, the process runs asynchronously. This means the action is added to a batch queue, and you'll be
notified on the bell icon when the batch is ready.

7 Prospects and Candidates
What's a Prospect
Prospects are people who were referred for a job requisition or added to a job requisition but who haven't yet completed
their job application.
When a person is referred for a job, a prospect record is created and associated to the job requisition. When you use the
Add to Requisition action for a candidate, a candidate record is also created and associated to the job requisition.
You can access prospects associated to a job requisition from several places such as the Job Requisitions list and the
job requisition details view. You can also access the referred prospects from the job requisition Overview tab. When you
view the list of prospects for a job requisition, you can:
• Navigate through the list of prospects.
• Sort and filter prospects.
• Search for specific prospects.
• Take actions on prospects such as send an email, send a reminder invitation to apply to a job, add prospects to
other job requisitions and candidate pools, add interactions, indicate that prospects aren't interested in the job,
delete prospects, convert a prospect into a candidate job application.
• See which prospects were referred and which ones were added to the job requisition.
• See which prospects you didn't yet view. A blue dot appears next to the prospect name.
When you open a prospect record, you can see details about the prospect such as personal information, previous
employment, degrees, certifications and licenses, endorsements, attachments, and any other recruiting activities the
candidate is associated with like candidate pools or other job requisitions.
Note: Documents attached by a referrer are saved in the candidate profile’s Key Highlights section (not in the
Attachments section). Only one document (the most recent one) is displayed. Documents uploaded by the candidate
while applying for a job using the referral link are saved in the Attachments section of their job application.
The count of prospects for a job requisition is displayed on the Job Requisitions list and within the job requisition. The
number of prospects displayed varies depending on where you view it:
• On the Job Requisitions list, the number of prospects represents the active prospects added and referred to the
job requisition.
• In the job requisition Overview tab, the number of referred prospects is displayed. When you click the number,
you're taken to the prospects list where you can filter the list to see referred and added prospects.

---

## Invite a Prospect to Apply for a Job
*Chunk ID: OHR-USE-0092 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

When prospects are added to a job requisition or referred, an invitation to apply is automatically sent to the prospects.
You can use the Send Invite action to manually resend an invitation to the prospects. The prospects receive an email
inviting them to apply for the job. If prospects are interested in learning more about the job, they can click the link in the

email to access the job description and complete their job application. The email also includes a Not Interested link that
the prospects can use to update their prospect record accordingly.

---

## Indicate a Prospect Isn't Interested by a Job
*Chunk ID: OHR-USE-0093 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

If a prospect isn't interested in applying for a job, you can use the Update to Not Interested action on the Prospects list
or the prospect record.
The prospect record status is automatically updated to Not Interested. A prospect marked as not interested doesn't
prevent the candidate from applying for the job.

---

## Delete a Prospect
*Chunk ID: OHR-USE-0094 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You delete a prospect when you no longer want to see them in the prospects list of a job requisition.
1. On the Job Requisitions page, click the Prospects link for a specific requisition.
2. On the Prospects page, select a prospect.
3. In the Actions menu, select Delete Prospect.
Results:
• The prospect no longer appears in the prospect list of the job requisition and in the list of referrals submitted by
the referrer.
• The prospect can be added to the job requisition again. The prospect can be endorsed for the same job
requisition.
• The prospect can't be referred for the job requisition again.

---

## Convert a Prospect into a Candidate Job Application
*Chunk ID: OHR-USE-0095 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can convert an existing prospect record into a candidate job application.
Before you start
You need the privilege Create Candidate Job Application (IRC_CREATE_CANDIDATE_JOB_APPLICATION).
Here's what to do
1. Go to the Job Requisitions list.
2. Click the Prospects link for a specific requisition.
3. On the Prospects page, select one or multiple prospects.
You can select up to 10 prospects.
4. In the Actions menu, select Convert Prospect.
Results:

When the prospect record is converted, it no longer appears on the Prospects list. It appears as a confirmed job
application.
What to do next
You can use the Candidate Application filter on the job application list to find those applications which were created on
behalf of the candidate.
Note: The Candidate Application filter isn't displayed in the Filters panel by default. You need to add it using the
Personalize Filter action.
If the candidate attempts to apply using their invite to apply email, the candidate will get an error and won't be able to
apply because the job application was created (on their behalf) with the Convert Prospect action.

---

## Supported Candidate Types
*Chunk ID: OHR-USE-0096 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

These candidate types are supported in Oracle Recruiting.
• Employees
• Contingent workers
• Ex-employees
• Ex-contingent workers
• Candidates (External)

---

## Create a Candidate Profile
*Chunk ID: OHR-USE-0097 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You create a candidate profile to quickly capture candidate information.
There are various reasons why you may want to create a candidate profile. For example, a candidate was referred to you
and you want to quickly capture contact details of the candidate to coordinate and schedule a conversation with the
candidate. Or, you're attending a university event or career fair where you meet potential candidates, and you want to
quickly capture candidate information to contact the candidate or potentially screen the candidate later.
You can create a candidate profile from the Candidate Search page, from within a candidate pool, and from the prospect
candidate list. Let's say you're on the Candidate Search page:
1. On the Candidate Search page, click Add.
2. On the Create Candidate page, enter basic info about the candidate like name, email address, phone number, and the
source where the candidate originated.
When capturing source information, the domain name of the source is captured along with the long URL. The
domain name appears in the interface as the display name, whereas the long URL is available in the database for
reporting purposes. If a job was posted to LinkedIn using the copy link functionality, the source is categorized as
jobshare/linkedin. If the job was posted to LinkedIn in any other way, the source is categorized as social/linkedin.
3. Decide if you want to display data to the candidate.
◦ If you select Yes, the candidate will see the talent profile data you entered when they go through a job
application flow, a request information flow, or a talent community flow. Some fields will be prefilled and
the candidate will have the ability to edit those values.

◦ If you select No, talent profile data, phone number, address, and attachments will be hidden, and the

candidate will see empty fields when going through a job application flow or a request information flow. If
the candidate leaves these fields empty, the info previously supplied (by the Recruiting user) is deleted and
now empty.

4. Add attachments such as resumes, cover letters, or miscellaneous documents.
5. Click Save and Close.
Results:
When you save the information, the application checks if the email address entered already exists in the database. If
that's the case, you need to enter an alternate email address to create this candidate.
If no duplicate is found, you're presented with a message asking you if you want to go to the candidate profile page
to fill in more information about the candidate such as previous work employment, education, licenses, certifications,
spoken languages. If you say no, the create page closes and you're taken back to the page where you initiated the create
action.
When the candidate for whom you created a profile applies for a job, the candidate reuses the profile you created so that
information you entered is kept. For example, if you added the candidate to a job requisition or a candidate pool, the
information remains. However, any data supplied by the candidate overwrites the data you entered.

---

## Delete a Candidate Profile
*Chunk ID: OHR-USE-0098 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can delete candidate profiles that have unconfirmed or inactive job applications. You can also delete candidate
profile that have active job applications as long as they don't have any active job offers. Deleted profiles are no longer
visible in the application, but they're still available for reporting purposes.
1. On the candidate search results page, select a candidate.
2. In the Actions menu, select Delete Candidate.

---

## Candidate Source Tracking
*Chunk ID: OHR-USE-0099 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

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

## UTM Code
*Chunk ID: OHR-USE-0100 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Campaign

Email

The candidate applied from a
campaign email or from social
media channels.

utm_source=email&utm_
medium=campaign

LinkedIn

utm_source=linkedin&utm_
medium=campaign

Facebook
Twitter

utm_source=facebook&utm_
medium=campaign
utm_source=twitter&utm_
medium=campaign

---

# Candidate Search

## Job Requisition
*Chunk ID: OHR-USE-0101 | Chapter: Candidate Search | Guide: Using Recruiting*

Candidate Profile

The recruiter uses the Add to
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

utm_source=candidate
+profile&utm_medium=manual
+add

---

## Candidate Pool
*Chunk ID: OHR-USE-0102 | Chapter: Candidate Search | Guide: Using Recruiting*

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

## Job Requisition
*Chunk ID: OHR-USE-0103 | Chapter: Candidate Search | Guide: Using Recruiting*

Candidate Profile
Candidate Pool

The recruiter adds a candidate to a
job requisition from another pool,
from a candidate profile, from a
requisition, or after performing a
candidate search.

none

The application automatically adds
a candidate to a talent community

---

# Prospects and Candidates

## UTM Code
*Chunk ID: OHR-USE-0104 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Example:
• Source Medium: Candidate
added to pool
• Source: Candidate Profile
• Added By: John Smith
Candidate created manually

LinkedIn
Email
Phone
Resume handed in person
Facebook
Agency

---

## External Career Site
*Chunk ID: OHR-USE-0105 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Internal Career Site
Talent Community
Job Alert

The recruiter creates a candidate
manually using the Create
Candidate action. For example, a
recruiter was actively searching for
new candidates on LinkedIn, or a
candidate handed a resume in a
restaurant.

none

The task to add more source
names to the list is Manage
Candidate Dimension Source
Names.

The candidate applied from an
external career site or an internal
career site, or a candidate received
a job alert and applied using an
external career site. It doesn't
include referred candidates who
applied using an external or
internal career sites.

utm_source=job+alert&utm_
medium=career+site

Example:
• Source Medium: Career site
• Source: External Career Site
• Career Site: ABC Career Site 001
Intelligent matching

---

## Job requisition
*Chunk ID: OHR-USE-0106 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

The candidate is selected by the
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

## Name of job aggregator
*Chunk ID: OHR-USE-0107 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

The candidate found a link to a job
requisition on a job aggregator.

utm_source=indeed&utm_
medium=job+aggregator

Example:

or imported using Direct Apply

---

## Name of job board
*Chunk ID: OHR-USE-0108 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

The candidate applied on a job
from a job board.

utm_medium=jobboard&utm_
source=ziprecruiter

Referral

---

## External Referral
*Chunk ID: OHR-USE-0109 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

The user or agent is referring a
person outside of the company
(external candidate) or an
employee (internal candidate).

utm_source=external
+referral&utm_medium=referral

---

## Internal Referral
*Chunk ID: OHR-USE-0110 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Agency Referral

utm_source=agency
+referral&utm_medium=referral

Example:
• Source Medium: Referral
• Source: External Referral
• Referred by: John Smith
• Career Site: ABC Career Site 001
Referral website

The candidate originated from any
other referral website.
Example:
• Source Medium: Referral
Website
• Source: Referral website
domain
• Career Site: ABC Career Site 001

none
If you have an external career
site that has a link to the Oracle
Recruiting career site, by default
the Oracle Recruiting career
site is considered as an external
referral and it's logged as such
in the source tracking. To track
candidates as direct visitors, you
need to add the rel="noreferrer"
attribute to the link. For example:
<a href="www.mycareersite.com"
rel="noreferrer"> Find Jobs
Today</a>

---

## Search engine
*Chunk ID: OHR-USE-0111 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Google
Yahoo

The candidate searched for
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

The job shared using the copy link
on a career site.

utm_source=external+job
+share&utm_medium=jobshare

Example:

---

## UTM Code
*Chunk ID: OHR-USE-0112 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

• Source Medium: Share Job
Posting
• Source: Social Media ABC
• Career Site: ABC Career Site 001
Social media

Facebook
Twitter

The candidate found a link to a
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

## Third Party Name
*Chunk ID: OHR-USE-0113 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

The recruiter manually adds codes
to the job url link.

utm_source=ITJobs&utm_
medium=third+party

Example:
• Source Medium: Third Party
• Source: IT Jobs
• Career Site: ABC Career Site 001
HR

Initial
Import

---

## Close Out
*Chunk ID: OHR-USE-0114 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Candidates created as part of HR
close out activities.

Note: When the application tries to find the source of a candidate from a URL (using utm_source/utm_medium
attributes), a referrer website, or a source the candidate used to apply, if a match can't be found, the source will appear
as Unknown in the candidate profile and candidate application.

---

## URL Code to Capture a Source
*Chunk ID: OHR-USE-0115 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

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

## Candidate Duplicate Check
*Chunk ID: OHR-USE-0116 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

A duplicate check is done to determine if a candidate is already in your database. Every candidate can be compared
against all other candidates to see if they're a duplicate.
A duplicate check can be done automatically or manually.

---

## Automatically Check for Duplicate Candidates
*Chunk ID: OHR-USE-0117 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Your administrator can configure the candidate selection process to automatically initiate a candidate duplicate check.
The duplicate check can be configured at multiple points in the candidate selection process. When a job application
reaches a specific state in a phase, the candidate duplicate check is automatically triggered. The recruiter or designated
members of the Hiring Team are informed of duplicate check results. They receive a notification about the candidate
and the number of duplicates found. They can click a link to see the duplicates. Candidates can be automatically
progressed in the selection process based on duplicate check results.

---

## Manually Check for Duplicate Candidates
*Chunk ID: OHR-USE-0118 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can use the Check Duplicates action to verify if a candidate is a duplicate of any external candidate, external
contingent worker, ex-employee, or ex-contingent worker. Duplicate check isn't available for employees and contingent
workers.
You need these privileges:
• Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE)
• View External Candidate Sensitive Information (IRC_VIEW_EXTERNAL_CANDIDATE_SENSITIVE_INFORMATION)

• Use REST Service - Candidates List of Values (IRC_REST_SERVICE_ACCESS_CANDIDATES_LOV)
You can start a duplicate check from the Candidate Search page, from within a candidate profile, a candidate job
application, and a prospect record. The Check Duplicates action compares the candidates using these identifiers and
attributes:
• National Identifier: Type, Country, Value
• Name: First Name, Last Name
• Address: Country, Level 1, Level 2 according to the Geography Hierarchy Structure defined for your company.
For example: Country, State, City
• Employment: Employer Name
• Education: Degree, School Name
If potential duplicates are found, the top 10 potential duplicate candidates are listed in order of match score. When you
click the expand icon, you can view the following candidate info to help you better evaluate if there's a duplicate:
• Name
• Location
• Candidate type
• Phase and state of latest job application
• Hiring manager
• Recruiter
• Person number
• Number of days since candidate was last contacted
You can also see the match score. Scores are classified as highest, higher, high, medium, and low depending on which
candidate identifiers are identical.
In this table, you can see the match score when specific candidate identifiers are identical. As an example, if the national
identifiers are identical, the match score will display Highest.

---

## Name + Date of Birth + Address + Employment
*Chunk ID: OHR-USE-0119 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

History + Education

Name + 3 identifiers among Date of Birth,
Address, Employment History, Education

High

Name + 3 identifiers among Date of Birth,
Address, Employment History, Education

---

## Name + Date of Birth
*Chunk ID: OHR-USE-0120 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Or,

Or,

Name + 2 identifiers among Date of Birth,
Address, Employment History, Education

Name + 2 identifiers among Date of Birth,
Address, Employment History, Education

Or,

Or,

---

## Candidate Identifiers
*Chunk ID: OHR-USE-0121 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

Match Score

At least 3 identifiers among Date of Birth,
Address, Employment History, Education

Name + 1 identifier among Date of Birth,
Address, Employment History, Education

---

## Candidate Identifiers
*Chunk ID: OHR-USE-0122 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

At least 3 identifiers among Date of Birth,
Address, Employment History, Education

Low

Name + 1 identifier among Date of Birth,
Address, Employment History, Education

Another way to find duplicates is to search for candidates using specific criteria. When you're on the Check Duplicates
page, you can use the Search for a person tool to search for potential duplicates. A scan is done across candidates using
the selected criteria:
• Name
• Email
• Phone
• Person Number
The search engine identifies potential duplicate candidates across external candidates, external contingent workers, exemployees, and ex-contingent workers. A list of candidates matching the search criteria is displayed. You can also view
the detailed profile of candidates to better evaluate if there's a duplicate.

---

## Duplicate Check Indicator
*Chunk ID: OHR-USE-0123 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

When a duplicate check is run on a candidate, either automatically or manually, a Duplicate Check label appears in
the candidate file, in the Key Highlights section. The date when the duplicate check was run and the match score are
displayed.
The duplicate check indicator and match score are displayed for duplicate checks that match person records.
Note: The Duplicate Check label, date, and match score aren't displayed if the duplicate check isn't run for the
candidate in reference.
The table indicates the duplicate check match score and the number of color codes bars displayed on the indicator.

---

## Manually Check for Duplicate Candidates
*Chunk ID: OHR-USE-0124 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can use the Check Duplicates action to verify if a candidate is a duplicate of any external candidate, external
contingent worker, ex-employee, or ex-contingent worker. You can start a duplicate check from the Candidate Search
page, from within a candidate profile, a candidate job application, and a prospect record.
Before you start
You need these privileges:
• Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE)
• View External Candidate Sensitive Information (IRC_VIEW_EXTERNAL_CANDIDATE_SENSITIVE_INFORMATION)
• Use REST Service - Candidates List of Values (IRC_REST_SERVICE_ACCESS_CANDIDATES_LOV)
Here's what to do
1. Open a candidate profile.
2. In the Actions menu, select Check Duplicates.
3. Select one of the search options: Name, Person Number, Email, Phone.
4. In the Search box, enter the value corresponding to the search option that you selected.
For example, to search by a candidate's email address, select Email and enter the email address in the search box.
The matching candidate information appears in the drop-down list.
5. Select the candidate from the drop-down list. This takes you to the Pre-Merge Analysis page.
6. In the Pre-Merge Analysis page, review the candidate's details, and then click Continue to go to the Select Candidate
to Retain page.
7. On the Select Candidate to Retain page, you can decide which of the duplicate candidates you want to delete and
which ones to retain.
For example, when one of the candidates doesn't have a prior work relationship with your organization, such as an
ex-employee or an ex-contingent worker, you can delete that candidate.

---

## Candidate File Merge
*Chunk ID: OHR-USE-0125 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can merge candidate files identified as possible duplicates after you've run a duplicate check or used specific
identifiers.
The table displays the type of candidate that can be merged and the file kept after the merge.

Who

---

## Ex-contingent worker
*Chunk ID: OHR-USE-0126 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can merge candidate files when candidates have offers:
• When the candidate is in any phase before the Offer phase.
• When the candidate is in any phase after the Offer phase.
• When the candidate is in any state of the Offer phase.
You can't merge candidates when screening partners didn't enable notifications. For partners who didn't enable
notifications, here's the list of statuses preventing a merge:
• Assessment
◦ Initiated

◦ Started
◦ In Progress
◦ Completed by Candidate
• Background Check
◦ Initiated

◦ Candidate Input Required
◦ In Progress
• Tax Credit
◦ Initiated

◦ Started
◦ In Progress
◦ Completed by Candidate

---

## Merge Candidate Files
*Chunk ID: OHR-USE-0127 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You can merge candidate files identified as possible duplicates after you have run a duplicate check or used specific
identifiers.
Before you start
You need these privileges:
• Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE)

• View External Candidate Sensitive Information (IRC_VIEW_EXTERNAL_CANDIDATE_SENSITIVE_INFORMATION)
• Use REST Service - Candidates List of Values (IRC_REST_SERVICE_ACCESS_CANDIDATES_LOV)
Here's what to do
1. Open a candidate profile, a candidate job application, or a prospect record.
2. In the Actions menu, select Check Duplicates.
3. If you determine that a candidate is a duplicate, click Merge.
A pre-merge analysis of both duplicate candidates is displayed. Key attributes such name, address, email, phone, job
applications, screenings status are listed side by side.
4. Review the report. You can also click Download to view a PDF version of the pre-merge analysis.
5. Click Continue.
6. Decide which candidate you want to retain.
The candidate to retain is pre-determined when the candidate has a pre-existing work relationship. For instance, an
ex-employee, an ex-contingent worker, a current contingent worker.
7. Submit the merge request.
A prerequisite check is done. When prerequisites are met, the request proceeds. The merge process combines the
profile of both candidates and candidate activities such as job applications, talent community sign up.
8. View the post merge analysis.
The report lists the retained candidate profile and all activities of the candidate as a result of the merge.
Results:
What happens once the merge is done:
• The candidate that wasn't retained is deleted.
• Undeleted job applications of the deleted candidate are transferred to the candidate that was retained.
• A notification is sent to inform you of the merge request status.
• Merge reports are attached to retained candidate for further reference and traceability.

---

## Add a Candidate to a Job Requisition
*Chunk ID: OHR-USE-0128 | Chapter: Prospects and Candidates | Guide: Using Recruiting*

You add a candidate to a job requisition to create a prospect candidate profile associated with the job requisition.
You can add internal candidates to job requisitions posted on internal career sites, and external candidates to job
requisitions posted on external career sites.
You can add one candidate to one or many job requisitions. You can also add many candidates to one or more job
requisitions. If a few candidates don't get successfully added to the job requisition for any reason, you'll see a message
indicating that the candidates were added to the job requisition. There will be no indication why a specific candidate
wasn't added.
You can add candidates to a job requisition that isn't posted to a career site if you select the option Allow Candidates to
Apply When Not Posted in the job requisition.
You can add a candidate to a job requisition from the Candidate Search page, from within a candidate pool, or from a
prospect list or job application list on another job requisition. Let's say you're on the Candidate Search page:
1. On the Candidate Search page, select one or many candidates.

2. In the Actions menu, select Add to Requisition.
3. On the Add to Requisition page, select one or many job requisitions.
4. Select the option Create job application on behalf of candidate to skip the prospect process and not wait for the
candidates to submit their job applications.
5. Click Save and Close.
Results:
An invitation is sent to the candidates to invite them to apply to the job requisitions. If you selected the option Create
job application on behalf of candidate, no invitation is sent.
Related Topics
• Invite Candidates to Apply on Job Requisitions Not Posted
• Create a Job Application on Behalf of the Candidate

---

# Candidate Job Applications

## Create a Job Application on Behalf of the Candidate
*Chunk ID: OHR-USE-0129 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You can create a job application on behalf of a candidate when you want to skip the prospect process and not wait for
the candidate to submit their application for a job.
You can create a job application of behalf of a candidate from the Candidate Search page, from within a candidate pool,
or from a prospect list or job application list on another job requisition.
When you create a job application on behalf of an external candidate, the prescreening questionnaire is automatically
filled. When a question from a prescreening questionnaire has been answered before, the latest answer to the question
is retrieved and added to the job application. This applies to both external and internal candidates as long as all required
questions have been answered. It also applies to all types of questions: disqualification questions, prescreening
questions added automatically and manually.
When you create a job application on behalf of an external candidate, only the Talent Profile content sections included
in the application flow are copied from the candidate profile. Talent Profile content sections configured in request
information flows aren't copied from the candidate profile. It’s expected that external candidates would enter the
data in the request information flows themselves. Recruiting users who have the privilege Update Candidate Job
Application (IRC_UPDATE_CANDIDATE_JOB_APPLICATION_DATA) could also supply request information data on
behalf of candidates after the job application has been created. For internal candidates, all Talent Profile sections that
Recruiting is subscribed to are copied from their candidate profile.
Before you start
You need the privilege Create Candidate Job Application (IRC_CREATE_CANDIDATE_JOB_APPLICATION).
Here's what to do
1. Open a candidate file.
2. In the Actions menu, select Add to Requisition.
3. On the Add to Requisition page, select one or more job requisitions.
4. Select the option Create job application on behalf of candidate .
5. Click Save and Close.

8 Candidate Job Applications
Candidate Job Application
A candidate job application is a record containing information that the candidate provided when applying for a job. It
also contains information about the progression of the job application in the candidate selection process.
External candidate job applications display content sections as configured in the apply flow and request information
flow for the requisition. Whereas internal candidate job applications display content sections that Recruiting subscribes
to.
You can access candidate job applications from the Job Requisitions list and the job requisition Overview section. When
you view the list of job applications for a job requisition, you can:
• Navigate through candidate job applications.
• Sort and filter candidate job applications.
• Search for specific candidate job applications.
• Take actions such as moving candidate job applications in the candidate selection process, adding the
candidate to candidate pools, adding interactions, send messages, confirming unconfirmed job applications.
• See a blue dot next to a candidate job application when you open it for the first time. The dot disappears when
you open the job application.

---

## Advanced Job Application Filters
*Chunk ID: OHR-USE-0130 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You can perform more complex, targeted searches on the job applications list with advanced filtering capabilities when
Oracle Search is enabled.
Click Advanced filters to see advanced filtering criteria. You can select job application prescreening questions and
answers, skills, employers, positions, degrees, majors, schools, interview feedback questionnaires, and extra info fields
to find the right candidates faster.
With these filters, you can select multiple values.
When you select multiple job application questions and answers:
• An AND operator is used between questions.
• An OR operator is used between answers for the same question.
An OR operator is used when you select multiple values for these filters:
• Skills
• Candidate labels
• Employer
• Position
• Degree
• Major

• School and school name
• Interview questionnaires
• Extra Info
An AND operator is used when you select filter values across filter categories.
The Extra Info filter only supports independent flexfield segments. It’s not possible to filter segments which are
configured as dates. Flexfield segments types which aren’t supported:
• Dependent
• Subset
• View Object
• Table Based Dependent

---

## Print a Job Application
*Chunk ID: OHR-USE-0131 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You can use the Print action to create a PDF version of one or more job applications.
When you use the Print action from within a job application, the PDF file is generated in real time. A new browser tab
opens and displays the job application in a PDF format.
When you're on the list of job applications, you can use the Print action for one or more applications. The PDF file is
generated asynchronously as a batch. You receive a notification when the print is completed. Depending on how your
administrator configured the feature, you can receive a notification with a zipped file containing a separate PDF for each
job application. Or, the notification contains a link to download the zipped PDFs.
When you print a job application, you can also print its attachments. The types of attachment you can select are resume
and cover letter.
Note: If you want to add fields in the PDF output other than the fields defined by default, you need to create a custom
BI Publisher (BIP) report. The report provided by default is in the Shared Folders > Human Capital Management >
Recruiting > Job Application. If you create a custom report, it will be in the Shared Folders > Custom > Human Capital
Management > Recruiting > Job Application. Once a custom report is created, it will be picked up and used by the
Print action.
Before you start
You need the View Candidate Job Application OBI role to print job applications.
Here's what to do
1. Select one or more job applications.
2. In the Actions menu, select Print.
3. On the Print Job Application page, select which content and attachments you want to print.
4. Click Print.

---

## Add Info to Job Applications on Behalf of Candidates
*Chunk ID: OHR-USE-0132 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You can add info to job applications on behalf of candidates.
This includes:
• Info related to Talent Profile content such as Education, Experience, Languages, Licenses and Certifications,
Skills.
• Info in the Sensitive Info section.
• Info in the Personal Info section.
• Info in the Address section.
• Prescreening questionnaires.
• Request information questionnaires.
• Preferred locations in the Preferences section.
• Attachments in the Supporting Documents section.
• Flexfields.
Here are more details regarding this feature.
• There's no way to distinguish between info provided by the candidate versus info you provided.
• You can't add nor edit most of the info provided by the candidate through an apply flow or request
information flow, including info in the Talent Profile sections and prescreening responses provided by
candidates. This ensures that the info provided by the candidate is retained. You can edit the candidate's
contact info in the Personal Info and Address sections if you have the privilege Create or Update Candidate
(IRC_CREATE_OR_UPDATE_CANDIDATE). The info in the Personal Info and Address sections is updated across
all views of the candidate to ensure the most up to date contact info is available.
• You can't add veteran, disability, and diversity info.
• You need the privilege Update Candidate Job Application (IRC_UPDATE_CANDIDATE_JOB_APPLICATION) to
add apply flow and request information flow info to job applications on behalf of candidates.
• When you add info to a job application, the info is only saved for that job application. The candidate profile isn't
updated except for the info in the Address, Personal Info, and Sensitive Info sections (because that info is stored
in the profile).

◦ The Personal Info and Address sections are always kept in sync. Updates made on the job application are
◦

reflected on the candidate profile (and all other job applications for the candidate).
If the candidate later applies to another job or if the candidate is added to another requisition, their
profile data is used, not the data you added to the job application.

• If an external candidate went through the apply flow or request information flow with a block, you can't add
info to those block sections even if the candidate left the block empty. For example, the apply flow contains the
Languages block and the candidate left it blank. You won't be able to edit the Languages section.
• If an internal candidate went through the apply flow, you can't add info to their Talent Profile content or job
application questions. If the job application was created on behalf of the candidate, meaning the candidate
didn't go through the apply flow, you won't be able to add info to the Talent Profile content sections but you'll
be able to update answers to prescreening questions.

• You can see all questionnaires in the Questionnaire section, including the ones not yet initiated from future
request information flows. This allows users with the appropriate privilege to answer these questionnaires on
behalf of the candidate.
• In the case of request information flows, if you completed a questionnaire, the questionnaire won't be
presented to the candidate. If the candidate goes through a request information flow, they will see their profile
data prefilled. Any info the candidate provided will overwrite the info you provided on the job application.
• You can't edit most content on the job application once the application is in the HR phase or an inactive state.
You can only edit the Contact Info, Address.
• If the Country field is disabled in Profiles, when you enter education and experience info on behalf of a
candidate, the Country field value is defaulted to the country configured in Profiles. But when a candidate
applies to a job and provides education and experience info on the career site, the Country field is blank. The
Country field value defaults differently depending on how the job application is created.
• You can add sensitive info to external candidates and ex-employees, ex-contingent workers, and contingent
workers treated as external candidates if you have the Manage External Candidate Sensitive Information
(IRC_MANAGE_EXTERNAL_CANDIDATE_SENSITIVE_INFORMATION_DATA) duty role.
• Extensible flexfield (EFF) values provided by Recruiting users aren't copied over to the person record when the
candidate is hired or converted.

---

## Tag Candidates Using Predefined Labels
*Chunk ID: OHR-USE-0133 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You can tag candidates using labels to help you search and find candidates quickly based on your review. You can add
tags to candidate profiles, prospect records, pool members, and candidate job applications. For example, you might
want to tag a candidate as being a finance expert.
To tag candidates, select one or several candidates then use the Add Label action in the Actions menu, or from within
the Labels section in job applications. Labels are defined by your administrator.
When you assign labels, labels are displayed in the Labels section of the candidate file.
Note: Labels aren't shown in the job applications list and candidate pool members list.
When you're in a candidates list, you can filter candidates using Label filter criteria. For the job applications list, you
need to use the Candidate Labels filter, which is available in the advanced filters, in a section called Candidate Details.
Note: Oracle Search is required to view the Candidate Labels filter.
You can configure labels to appear in job application grid views. A maximum of three candidate labels appear in the
grid view, in alphabetical order. If there are more than three labels, a count is displayed and you can click it to get to the
Details tab to see the other labels.
When you assign labels to prospects, the labels appear within the prospect records and in the Prospects list, for each
prospect. Up to three labels are displayed in the Prospects list. If more than three labels were assigned to prospects, the
first three appear on the list based on alphabetical order. You can view the other ones on the prospect record's Details
tab. If you want to filter prospects using specific labels, you can use the Candidate Labels filter.
Related Topics
• What's a Grid View

---

## Take Action on Many Candidate Job Applications at Once
*Chunk ID: OHR-USE-0134 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You can take actions in a batch to save time while evaluating candidates for a job requisition.
When you're in the job applications list, use the check box at the top of the list to select dozens or hundreds of
candidates, even those not shown on the list. You can remove any unwanted applications by clearing the check box for
any rows. Then choose an action in the Actions menu. For example, you may want to send an email message to all of
them, or add them to another requisition or to a pool.
When you select fewer than 50 job applications, either by clicking the check box on each row or the check box at the top
of the job applications list, the action proceeds as usual. When you select more than 50 job applications, the action will
proceed as soon as possible, but you won't have to wait for it to complete. Here's what happens:
• For actions that don't require any further information, a process will start running on that batch of candidates.
• For actions that require further information, the usual page will gather the information necessary for you to
complete the action. At the top of this page, the number of candidates and the filters describing the list (but not
the candidate names) are shown. As soon as you complete this page, a process will start running on that batch
of candidates.
You're able to continue your work immediately and you receive an email when the process is completed. This email
informs you that the action was successful for the number of candidates. You can also view which job applications were
skipped or failed for any reason.

---

## How Candidate Job Applications Are Confirmed
*Chunk ID: OHR-USE-0135 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

Candidate job applications must be confirmed to be part of the candidate selection process.
There are different methods to confirm a candidate job application:
• In most cases, when external candidates complete a job application they're sent an email or SMS with a 6 digit
verification code asking them to confirm their job application. This is the default method.
• You can resend the confirmation email or SMS to the candidate using the Send Confirmation Request action.
• You can confirm the job application on behalf of the candidate using the Confirm Job Application action.
By default, unconfirmed job applications for a job requisition aren't displayed. Use the Unconfirmed filter to view
unconfirmed job applications.

When to Use Return to Prior Phase and Return to Prior
State on Candidate Job Applications
You can use the Return to Prior Phase and Return to Prior State actions on candidate job applications.

---

## Return to Prior Phase
*Chunk ID: OHR-USE-0136 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You use the Return to Prior Phase action to move a candidate job application back to a prior phase. This action is only
available for job applications that are active.
The Return to Prior Phase action is also available to revert candidate job applications to the prior phase after they
reach the Offer phase. The action is available for job applications that are in the Offer – Draft status and any terminal
states in the Offer phase. This is useful for situations where for example you have erroneously moved the candidate
application to the Offer phase, or there is a need to add one more round of interview or complete a compliance check
before starting the offer process. When you use the Return to Prior Phase action, the job application is taken back to
the same prior phase and state from where it moved into the Offer phase. The Job Offers tab in the job application is no
longer displayed. It becomes visible again when you click Create Job Offer and the job application is back in the Offer –
Draft status. Once you’re done with your changes, you use the Move action to move the job application to the Offer – To
be Created status. When you click the Create Job Offer action to work on the job offer which you had started earlier, the
job offer will be in the Draft state and you'll be directed to the Create Job Offer page. Data previously entered in the job
offer was retained and you can make changes if needed.
Note: For the below phases and states, you’ll need to use the Redraft Offer action to bring the job application to the
Offer – Draft status:
• Offer – Approved
• Offer – Extended
• Offer – Accepted
• Post-Offer custom phase
• HR phase

---

## Return to Prior State
*Chunk ID: OHR-USE-0137 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You use the Return to Prior State action to return a candidate job application to the last state it was in before a terminal
state (Rejected by Employee and Withdrawn by Candidate). The Return to Prior State action is only available for job
applications that are inactive.

---

## Attachments Displayed Under Supporting Documents
*Chunk ID: OHR-USE-0138 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

When a candidate applies to a job requisition and uploads documents such as resume and cover letter, both documents
are displayed in the candidate application's Attachments tab, in the Supporting Documents section.
When a candidate applies to a requisition, uploads a resume (and not a cover letter), then goes back to their profile and
uploads a cover letter, only the resume is listed in the Supporting Documents section.

Any changes to the candidate profile won't be updated on existing job applications, only on new job applications. This is
why updates to resume and cover letter on a candidate profile aren't reflected on any existing job application. They will
show when applying to a new requisition.
After a candidate has submitted their job application, the only way they can add attachments or information to that job
application is with a request information flow.

---

## Get a List of Candidates Recommended for Rehire
*Chunk ID: OHR-USE-0139 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

When you conduct a candidate search or review job applications, prospect candidates, and candidate pool members,
you can use the Rehire Recommendation filter to get a list of candidates that were recommended during the HR
termination process.
You can then open a candidate file and look in the Personal Information section to see the reason provided if the
candidate wasn't recommended for rehire.
The Rehire Recommendation filter is hidden by default. Click the Personalize Filters icon to add the filter.
Note: If your organization enabled Oracle Search using the profile option ORA_IRC_JA_ORACLE_SEARCH_ENABLED,
the Rehire Recommendation filter won't be available in the list of job applications. However, it's available for prospects,
pool members, and candidate search results.

---

## Delete a Candidate Job Application
*Chunk ID: OHR-USE-0140 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

You can use the Delete Job Application action to delete inactive or unconfirmed candidate job applications. You can also
delete active job applications as long as they don't have any active job offers. Deleted candidate job applications are no
longer visible in the application, but they're still available for reporting purposes.
1. Open a job application.
2. In the Actions menu, select Move.
3. Select an inactive state such as Withdrawn by Candidate or Rejected by Employer.
4. Click Save and Close.
5. In the Actions menu, select Delete Job Application.

---

## What Happens When a Candidate Deletes Their Profile
*Chunk ID: OHR-USE-0141 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

External candidates, including ex-employees and ex-contingent workers, can delete their profile using the candidate self
service.
When a candidate identified as an ex-worker deletes their profile in the candidate self service, the candidate is marked
as deleted, and there is no impact in Core HR. All job applications associated with that candidate are deleted. When the
same person later applies to a job using the same email, this person will be identified during the duplicate check as an

ex-worker. Going forward only new job applications will be visible in candidate self service, since the ones associated
with previously deleted candidate are no longer available.
Note that contingent workers, if they're processed as external candidates, can't delete their profile in the candidate self
service.

---

## Similar Candidates
*Chunk ID: OHR-USE-0142 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

When the Intelligent Matching features are enabled within your organization, you can find candidates that have similar
traits with an existing candidate.
The Similar Candidates feature increases your productivity, helps reduce the time in the overall candidate selection
process, and improves the quality of selected candidates. The Similar Candidates feature uses artificial intelligence (AI)
and machine-learning algorithms to suggest similar candidates. You can benefit most from the feature when you're
hiring for professional or skilled positions where the number of candidates is reasonably high. You spend less time
manually screening resumes, while still sourcing and recruiting the best talent.
This feature is available for candidates, prospects, and candidate pool members. You can view a maximum of 30 similar
candidates based on a specific candidate profile.
Your administrator may have defined a list of countries for which the Similar Candidates feature is hidden. If the posting
location of a job requisition is part of the list of countries defined by your administrator:
• The Similar Candidates tab in candidate profiles, prospect records, and candidate pool members isn’t displayed.

---

## Candidate Legislative and Diversity Information
*Chunk ID: OHR-USE-0143 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

Your organization can collect legislative and diversity information from both external and internal candidates when they
apply for jobs. This helps your organization to collect data as per regulatory guidelines and reporting in each country
where you hire candidates. It also helps you to monitor and improve your efforts to build a diverse workforce.
Your administrator configures which of the desired legislative, diversity, and disability fields are displayed to candidates
in each of the countries where hiring is done. Each of these fields can be displayed as optional or required when
candidates apply to jobs. Each country can have its own list of possible answers for these fields. Depending on which
blocks have been configured into each external job application flow, you can collect the following types of information
from candidate job applications:
• Diversity block can display the standard fields Date of Birth, Ethnicity, Gender, Marital Status, Religion.
Also it can include any flexfields delivered by Oracle for each country's legislative requirements
(PER_PERSON_LEGISLATIVE_DATA_LEG_DDF) and also any customer-defined legislative flexfields
(PER_PERSON_LEGISLATIVE_DFF).
• Disability block can show any standard disability-related fields configured for job requisitions in any country.
For requisitions in the United States, it shows the US disability form CC-305.
• Veteran block can show the US field Veteran Status for job requisitions located in the United States. For
requisitions that are posted only in other countries, this block won't be shown.
When the configuration is done, you can create a requisition that gathers legislative and diversity information by
selecting one of these job application flows. Depending on the primary posting location and any alternate posting

locations of the requisition, if these are in any countries that are configured to show these fields, then the candidates
will see these questions when they apply to the requisition.
External candidates can provide information in these fields, which is stored for compliance purposes for each job
application. Each time they apply to a job, these fields will be blank, not prefilled with their previous answers, to preserve
privacy and give them another opportunity to provide their current responses. This new information provided by
external candidates becomes available in the appropriate places in the HR file, as soon as the candidate is hired as a
worker.
Internal candidates aren't asked to provide this information when they apply for the same job requisitions. However
their current diversity data from their HR file now gets stored in their job applications to support reporting on both
internal and external candidates to the same requisition.
The legislative and diversity information provided by external and internal candidates isn't visible to the recruiting team.
This private data can influence hiring decisions so it's never displayed as part of the job application, not even on the tab
named Sensitive Info. It's available for reporting purposes.

---

## Details on Candidate Home Address
*Chunk ID: OHR-USE-0144 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

Here are some details regarding the home address of candidates.
When a candidate is converted as an employee or contingent worker, the candidate becomes an internal candidate by
default.
Note: Your organization may have decided to process contingent workers as external candidates to align with their
business practices and processes.
Depending on if the candidate is considered an internal candidate or an external candidate, the address displayed
will vary. For internal candidates, the work address is displayed whereas for external candidates, the home address is
displayed.
If the employee or contingent worker resigns or gets terminated, the candidate will be considered as an external
candidate and the candidate application will again display the home address.
If the candidate is still a pending worker or is in the HR processing state or any previous state in the HR phase, the
candidate application will display the home address.

---

## Info Shared Between Job Applications and Candidate
*Chunk ID: OHR-USE-0145 | Chapter: Candidate Job Applications | Guide: Using Recruiting*

Profiles
When a new candidate applies to a job requisition, the info they provide as part of the job application is also stored in
their candidate profile, so it's searchable when you search for candidates.
Basic candidate info, like their name, contact info, address is stored at the profile level and kept in sync across the profile
and any job application the candidate submits. If the candidate applies to another job requisition in the future, their
candidate profile will be updated with any new information provided but their already submitted job applications won't
be updated nor changed.

The responses a candidate provides for questions and screening services are stored only in the job application.
When a candidate is hired (the Moved to HR action is performed), their talent profile is created based on the job
application which they've been hired from. If their candidate profile was added to or edited after the job application was
submitted it will be out of sync with the content on their employee talent profile.
Once a candidate is hired and close out occurs, their candidate profile is converted to an internal candidate profile, their
talent profile is activated, and the two contain the same set of information. Their internal candidate profile can’t be
edited in Recruiting and reflects the information added or edited on their talent profile.
When a candidate gets terminated, their Talent profile gets end dated and the candidate profile is converted back to an
external candidate profile.
When a job application is moved from a pipeline to a standard requisition, the pipeline submission profile is copied into
a new standard requisition job application profile.

---

# Candidate Pools and Talent Community

## Validation for E-signatures on Job Applications and
*Chunk ID: OHR-USE-0146 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

Offers
Candidates can be asked to provide their full name as an e-signature, optionally when submitting a job application and
mandatory when accepting an offer.
They must provide their last name, and their first name is optional. This light validation allows signatures to be
successful from people who may apply using nicknames versus formal first names. The description that they see when
filling both of these e-signature fields is configurable in the Recruiting Content library. Also captured but not displayed
on the page are the date and time of the acceptance and the IP address that the candidate is using.

9 Candidate Pools and Talent Community
Candidate Pool
You use candidate pools to group candidates and manage sourcing activities for either a current job position or a future
job position that you will potentially fill.
With candidate pools, you can refine a list of candidates to remove unqualified candidates and at the same time, nurture
candidates that you want to pursue.
Candidate pools can be one of two kinds:
• Private: Only the owner of the candidate pool can access the pool.
• Shared: The owner of the candidate pool can grant other users access to the candidate pool contents and
actions available to the pool itself. When the pool is shared, all users who have access to the pool are listed as
pool owners and they can perform these actions:

◦ Add and remove candidates from the candidate pool
◦ Add candidates to a job requisition
◦ Add candidates to another candidate pool
When you view the list of candidate pools, you can use filters to narrow down the list of pools. There's a filter criteria
called Talent Community Sites. The values displayed represent active and inactive sites. Inactive sites are shown in case
you still want to see talent through that specific site.

---

## Candidate Pool Process Phases and States
*Chunk ID: OHR-USE-0147 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

The candidate pool management process provides the framework to progress pool members through the sourcing
lifecycle to ensure they're engaged with the organization even if they aren't actively involved in a hiring effort.
The candidate pool process consists of a series of phases and states. Recruiters move pool members from one phase to
another. The process isn't sequential, pool members can go back and forth between phases and states.
The table lists the phases and states provided as part of the default candidate pool process.

Phase

State

---

## Needs Attention
*Chunk ID: OHR-USE-0148 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

Contacted
Interested
Not Interested
Rejected by Employer
Withdrawn by Candidate

Nurture

---

## Needs Attention
*Chunk ID: OHR-USE-0149 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

Ready to Be Placed Now
Ready in 6 Months
Ready in 12 Months
Rejected by Employer
Withdrawn by Candidate

---

## Create a Candidate Pool
*Chunk ID: OHR-USE-0150 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

You create a candidate pool to group candidates being considered for a current or future job.
1. On the Candidate Pools page, click Add.
2. On the Create Candidate Pool page, enter a name and a description for the candidate pool.
3. Specify if the candidate pool is private or shared:
◦ Private: Only the owner of the candidate pool can access the pool.

◦ Shared: Other users can access the candidate pool contents and actions.
4. If the candidate pool is shared, click Add Owner and select a user from the list or search for a specific user.
You can select several users by highlighting a user and pressing the Control key.
5. Click Save and Close.
Results:
The candidate pool is created and appears on the Candidate Pools page.
What to do next

You can now add candidates to the pool. If you want to set the pool as one of your favorite pools, click the Star icon next
to the candidate pool name. You can then use the Favorite sort value to display your favorite pools at the top of the list.
Related Topics
• Create a Talent Community Pool

---

## Add a Candidate to a Candidate Pool
*Chunk ID: OHR-USE-0151 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

You can add candidates to a candidate pool to consider them for a position. You can add one or multiple candidates at a
time to a candidate pool.
1. On the Candidate Search page, select a candidate.
2. In the Actions menu, select Add to Candidate Pool.
3. On the Add the Candidate Pool page, select a pool.
4. Click Save and Close.
What to do next
When candidates are added to a candidate pool, you can:
• Sort, filter, and search candidate pool members.
Note: The Sort By drop-down list on the candidate pool member list will be disabled when there are over
10,000 pool members in the list. When you use the filters to lower the number of pool members to 10,000 or
fewer, the sort capabilities become usable.
• Move pool members through the sourcing process.
• Add pool members to job requisitions and other candidate pools.
• Add an interaction note.
• Send an email.
• Remove candidates from the pool.
• Delete candidates.

---

## Move a Candidate in a Candidate Pool
*Chunk ID: OHR-USE-0152 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

You move candidates in a candidate pool to progress candidates through the sourcing lifecycle to ensure they're
engaged with the organization even if they aren't actively involved in a hiring effort.
1. On the Candidate Pools tab, click a candidate pool.
2. On the Candidates page, select a candidate.
3. In the Actions menu, select Move Candidate.
4. On the Move Candidate page, select a phase and a state.
5. Click Save and Close.

---

## Print Candidate Pool Member Information
*Chunk ID: OHR-USE-0153 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

You can create PDF files of pool member information and share the PDF files with other users involved in the review and
selection process.
Before you start
You need the Perform Candidate Duplicate Check and Merge role
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE_PRIV_OBI).
Here's what to do
1. On the Candidate Pools page, open a candidate pool.
2. On the Candidates list, click a candidate.
3. In the Actions menu, click Print.
4. On the Print Candidate Pool Member page, select which content and attachments you want to print.
5. Click Print.
Results:
The PDF file is generated asynchronously as a batch. You'll receive a notification when the print is completed.
Depending on how your administrator configured the feature, you'll either receive a notification with a zipped file
containing a separate PDF for each pool member profile, or the notification contains a link to download the zipped
PDFs.

---

## Apply Bulk Actions to Pool Members
*Chunk ID: OHR-USE-0154 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

You can apply a bulk action to up to 50 pool members on the pool member candidates page. This means you can send a
message to up to 50 pool members at a time, or add up to 50 pool members at a time to a requisition.
Before you start
You need the role Manage Candidate Pool (IRC_MANAGE_CANDIDATE_POOL_PRIV_OBI).
Here's what to do
1. On a candidate pool member page, search for members, and filter if necessary until there are 50 or fewer members
in the results list.
2. Click the select all check box next to the Actions menu.
The select all check box only becomes available for use when the search results contain 50 or fewer results.
When you click the select all check box, all pool members in the search results are selected, even if they're not
immediately available on the page. You can click Load More to show more.
3. Select an action from the Actions menu.
4. Complete the fields of the action you selected, if any.

---

## Inactivate a Candidate Pool
*Chunk ID: OHR-USE-0155 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

You can inactivate a candidate pool when you no longer need it.
1. On the Candidate Pools page, select a candidate pool.
2. In the Actions menu, select Inactivate.
What to do next
To view inactive candidate pools, use the filter Include Inactive Pools. When a candidate pool is inactive, you can change
the status back to active using the Activate action.

---

## Create Follow-Up Tasks
*Chunk ID: OHR-USE-0156 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

You can manage candidate follow-ups by creating follow-up tasks with due dates. Follow-up tasks can be anything you
need to have a reminder to nurture candidates.
Examples might include things like remembering to call a candidate on a certain date to see if they're available for work,
or sending an email to a candidate to see how they liked a job fair.
1. Open a candidate pool.
2. On the Candidates page, select a candidate.
3. In the Actions menu, select Add Follow-Up Task.
4. Assign a future due date, and use the Note field to enter the pertinent follow-up information.
5. Click Save and Close.
What to do next
• You can edit, delete, or mark follow-up tasks as complete.
• You can filter the pool member list to identify follow-up tasks that are overdue, due today, due in the future, or
within a range of dates.
• You can view follow-up tasks related to a candidate using the View Follow-Up Tasks drop-down list on the Tasks
tab. When you select Related to Pool Member, you view follow-up tasks related to the current pool. When you
select All Other Follow-Up Tasks, you can view follow-up tasks for the candidate in the context of other pools
in which they're also members.
• You can add Follow-Up Tasks to Grid View using the Pool Member Follow-Up Task Info/Follow-Up Task Info
compound field. The follow-up task displays the first 120 characters. You can rest your cursor over the task to
show up to 500 characters. Only tasks in active status display in grid view.

Related Topics
• What's a Grid View

---

## Talent Community Pool
*Chunk ID: OHR-USE-0157 | Chapter: Candidate Pools and Talent Community | Guide: Using Recruiting*

When candidates don't find jobs matching their interests, they can join a talent community to show their interests in an
organization.
Internal candidates can be automatically added to talent community pools based on their job preferences matching
one or more pool attributes. External candidates can create their profile, indicate their preferred location and job family,
import their profile from a third party such as LinkedIn and Indeed, or upload a resume. Candidates also have the option
to receive news about new job opportunities and marketing communications.
When you view a list of candidate pools, talent community pools are identified as such. You can also filter the list
by talent community location, talent community job family, talent community site, and candidate types. The talent
community organization filtering is also available for internal candidates who can define the preferred organizations.
When you find the desired candidates, you can contact them if you have jobs matching their profile.
When external candidates join a talent community pool, the information is tracked in the candidate file Source
Information section. You can see:
• Source medium: Career Site
• Source: Talent Community
• Career Site: The career site where the candidate joined the pool
Note: You can't manually add candidates to a Talent Community. Candidates can only be manually added to
candidate pools that aren't defined as a Talent Community.

---

# Recruiting Campaigns

## Create a Talent Community Pool
*Chunk ID: OHR-USE-0158 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

You create a Talent Community pool to group candidates who signed up to a Talent Community pool and shared
their job preferences. If the parameters you select for the Talent Community pool align with the preferences set by
candidates, the candidates are automatically added to the Talent Community pool. You can’t manually add candidates to
a Talent Community pool.
1. On the Candidate Pools page, click Add.
2. On the Create Candidate Pool page, enter a name and a description for the candidate pool.
3. Specify if the candidate pool is private or shared:
◦ Private: Only the owner of the candidate pool can access the pool.

◦ Shared: Other users can access the candidate pool contents and actions.
4. If the candidate pool is shared, click Add Owner and select a user from the list or search for a specific user.
You can select several users by highlighting a user and pressing the Control key.
5. Select the Talent Community Pool option.
a. Select at least one location, job family, or candidate type parameter.
When you select the Employee candidate type, the Organization and Job fields appear.
6. Click Save and Close.

Results:
The candidate pool is created and appears on the Candidate Pools page.
Related Topics
• Create a Candidate Pool

10 Recruiting Campaigns and Social Media
Campaigns
Email Marketing Campaigns
You use email marketing campaigns to advertise jobs to candidates and generate and track job applications and
referrals.
You can also use email marketing campaigns to promote recruiting events and activities and capture candidate
responses like an RSVP for an upcoming recruiting event or learn more about the company's benefits and corporate
culture.
With email marketing campaigns, you can:
• Market jobs to targeted candidate audiences. Hard to fill positions can be advertised to relevant candidates,
improving the quality of job applications.
• Promote recruiting efforts with branded, easy to build emails.
• Track campaign metrics to measure campaign messaging effectiveness.
• Attribute job application and referral sources to campaigns and track the quality of hires.
When the campaign is active and the first campaign email is sent, you can view campaign details such as conversion
rate, response breakdown, and email metrics. These details are available on the Overview tab of the campaign.
• The conversion rate indicates the current response count obtained out of the campaign goal. The count takes
into account all the emails in the campaign (primary email and follow-up emails). For example, the conversion
rate circle graph indicates that the Apply to Job campaign obtained five responses to achieve the goal of
obtaining ten job applications.
• The response breakdown indicates the count obtained for each response defined for the Respond to Request
campaign. For Apply for Job and Refer Job campaigns, the response breakdown shows the count of job
applications and referrals. The response counts taken into account all of the emails in the campaign.
• The email metrics indicate the count obtained for the emails that were opened, clicked, bounced, and
unsubscribed. You can see metrics for the primary email and follow-up emails on the campaign details
page. The card view shows the primary email's metrics. The Refer Job campaign doesn't currently support
unsubscribes, even though this category is displayed in the email metrics graph.

---

## Create an Email Marketing Campaign
*Chunk ID: OHR-USE-0159 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

The first step when you create an email marketing campaign is to define basic details, associate job requisitions to the
campaign, and define the campaign audience.
1. On the Campaigns page, click Add.
2. On the Create Campaign page, enter basic information:
◦ Campaign Name

◦ Campaign Number
◦ Campaign Duration: You can select whether you want to create a campaign that runs one-time only, or runs
for a duration that you indicate.
Campaign Description

◦
◦ Campaign Purpose: Available options are: Collect Responses, Generate Job Applications, Generate
◦
◦

Referrals.
Campaign Goal: Number of responses you want to get. For example, you want to receive 20 job applications
or 5 referrals for a campaign.
Goal Label: Label for the goal such as "Sign Up for Campus Recruiting Event", "Download Technical Brief",
"Increase Referrals". The label is displayed in the campaign charts.

3. If you're creating a Collect Responses campaign, you can add one or multiple responses for the goal.
a. Enter a response label.
This is visible to recipients in the campaign email. For example, "Sign Me Up", "Download the Technical
Brief", "Learn More", "I'm Interested/I'm Not Interested".
b. Select the Counts Toward Goal option if you want the response clicks to be counted toward the target
campaign goal.
c. Select the Use Thank You Page page option if you want campaign recipients to be taken to the career site
Thank You page when they click the response button or link in the email.
A message displays "Your response has been recorded. Thank you."
d. In the Destination URL field, enter the URL where campaign recipients are taken upon clicking the response
link or button.
4. In the Associated Job Requisitions section, you can associate one or multiple job requisitions to the campaign. For
campaigns of type Generate Job Applications and Generate Referrals, you need to select at least one job requisition
or define one job requisition attribute. If you create a Collect Responses campaign, you're not required to associate
the campaign to a job requisition. However, if you intend on including the job list widget in an email, you need to
select at least one job requisition or one job requisition attribute.
◦ If you select Specify Requisitions, enter a job requisition title or number. They will all merge into the email
which is distributed to the audience.
◦ If you select Specify Requisition Query, enter a location or job family. The job requisitions that match the
query at the time of sending the email is in the job list widget in the email. The application will merge up to
5 requisitions of the ones that match the criteria into the Campaign email. A link is presented in the email to
visit the career site to view more positions.
5. In the Campaign Owners section, select one or several owners.
By default, you're the campaign owner. You can add additional owners. Owners can review campaign details and
track responses.
6. Click Save and Close.
Results:
The campaign is available on the Campaigns page and its status is Draft.
What to do next
Create Campaign Emails

---

## Create Campaign Emails
*Chunk ID: OHR-USE-0160 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

One of the step of creating an email marketing campaign is to create campaign emails. You can create your own email
or use a template as a starting point. The template is useful to enforce consistency in branding and messaging.
1. On the Campaigns page, open a campaign you created.
2. Click the Emails tab.
3. Click Add.
4. Enter a name for the email.
5. Select a template. The email template appropriate for your campaign type is available for selection. You can use the
email as is, or you can use the design editor to personalize the content.
You can create your own email using a blank form, or you can use a template as a starting point. The email templates
appropriate for your campaign type is available for selection.
6. Click Save.
Results:
The email editor opens in a new browser tab. The email editor displays the template you selected. You can keep the
content as is or, you can modify the template elements you want to use and add more as needed. When you position
your cursor in an area of the template, menus appear to help you modify the template. You can only edit unlocked areas
of the template. This helps ensure brand consistency in look and language.
You can also select a different template if you don’t like the look of the previously selected template. If you change the
template, the new template will overwrite the current design.
The first email you create is always sent to the entire audience by default. You can create follow-up emails. You can
send follow-up emails to the entire audience or any segments of the audience. For example, the recipients who haven't
opened the primary email can be sent a follow-up email. Or, the recipients who responded "I'm Interested" in an event
can be sent a follow-up email containing additional information about the event. The following audience segments are
available:
• Opened
• Unopened
• Applied to Job
• Referred to Job
You can select additional audience segments for follow-up emails if you configured responses for the campaign.
For example, if a campaign's responses are "Yes", "No" and "Maybe", there would be audience segments for those
responses. Recipients who clicked "Yes" or "Maybe" can be sent one follow-up email, and those who clicked "No" can be
sent a separate follow-up email.
When emails are sent, they are moved to the Sent Emails list and their status is changed to Sent. The following metrics
are provided for each email:
• Sent: The total count of recipients of the campaign. This count doesn't include bounced emails.
• Opened: The total count of recipients of the campaign that opened the email.
• Clicked: The total count of recipients of the campaign that clicked a response or tracked link or button in the
email.

• Bounced: The total count of recipients that didn't receive the campaign email. Bounces can be caused by
undelivered messages or invalid email addresses.
• Unsubscribed: The total count of recipients who unsubscribed from campaign emails. This count is captured
across the entire campaign, not per email like the other metrics.
What to do next
Define the Campaign Audience

---

## Define the Campaign Audience
*Chunk ID: OHR-USE-0161 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

You can target an email marketing campaign to a specific audience.
The campaign audience is based on the following factors:
• Candidate is active.
• Candidate is part of the pool.
• Candidate has opted in to receive marketing communications.
• Candidate was recommended to be rehired.
• Candidate didn’t receive campaign emails in the last 7 days.
• Candidate meets the audience criteria configured on the campaign by the campaign manager.
1. On the Campaigns page, open a campaign you created.
2. Click the Audience tab.
3. Click Add.
4. Select an audience. Available audience filters are:
◦ Candidate type: Internal, external, or all candidates.

◦ Location
◦ Education: School, degree, major.
◦ Work experience: Company, job title, years of experience.
◦ Candidate interactions: Only candidates who have opted in to receive recruitment marketing emails appear
in the audience search. To include candidates who haven't specified their opt-in status, use the Include
Unspecified Candidates filter.
Candidate pools: Select a candidate pool for the audience of the recruiting campaign.

◦
◦ Skills

For values to appear in filters, they need to appear in the candidate profile. For example, to view the Oracle
University school in the Education filter, at least one candidate must have that school in their profile.
5. Select the Exclude option to exclude a specific audience from the campaign.
6. Click Save.
Results:
As soon as you select one filter attribute, the estimated number of audience members is displayed. Charts showing the
breakdown of the top locations, top employers, and top degrees of the target audience are also displayed. The audience
count isn't final until the primary email has been sent. See the Emails tab for the actual audience count.

Note: If you select the Candidate interactions filter and the Candidate pools filter, the audience breakdown will
include the candidates who have opted in to receive marketing communications and candidates who have set
their preference to "Not specified" in their candidate profile. Also, candidates who declined to receive marketing
communications won't receive any emails.

---

## Campaign Duration
*Chunk ID: OHR-USE-0162 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

You can select whether you want to create a campaign that runs one-time only, or runs for a specific duration.
When you create a campaign, you can set the campaign duration:
• One-time campaign starts on a set date, and includes eligible candidates who were in your database on the day
the campaign began.
• An ongoing campaign starts on a set date, and includes eligible candidates who were in your database on the
day the campaign began, but also dynamically adds new candidates who either join or become eligible during
a set campaign period. They don't have to be in your database on the day the campaign begins, or they might
already be in your database, but not become eligible for the campaign until after it begins (for example, they
move to a new city, update their information, and your campaign targets that city).
When you schedule the emails for an ongoing campaign, a message displays to remind you that the audience for the
campaign is recalculated daily to identify newly eligible recipients up to the send date. What this means is on the first
day of the campaign, the primary email is sent to current candidates in the database who meet the criteria for the
campaign. The next day, the primary email is sent only to people who became eligible that day based on the campaign
criteria. For example, perhaps a campaign targets candidates who live in New York and is initially sent on November 1.
On November 2, three new people in New York sign up. The primary email only goes to those three people.
You delay sending follow-up emails by number of days (rather than by calendar date as is the case with one-time
campaigns). For example, you might want a follow-up email sent 7 days after a candidate receives the primary email.
This means no matter what date a candidate receives the primary email, they will receive the follow-up email 7 days
later. When the primary email has reached the send until date, and all follow-up emails are sent, the campaign is
automatically updated to the Completed status. Follow-up emails can still be created and when those emails are
scheduled the campaign automatically updates to the In Progress status again.

---

## Campaign Statuses
*Chunk ID: OHR-USE-0163 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

A campaign can have one of the following status.
• Draft: Upon initial save, the campaign is automatically in the Draft status. A draft campaign can be edited,
activated, and deleted.
• Scheduled: Once activated, the campaign is in the Scheduled status. Campaigns can be redrafted while in the
Scheduled status.
• In Progress: When the primary email's scheduled date is reached, the campaign is automatically updated to the
In Progress status. Additional emails can be added and scheduled. Emails that are still scheduled in the future
can also be modified.

• Completed: When the last email's scheduled date is reached and the emails were sent, the campaign is
automatically updated to the Completed status. Follow-up emails can still be created and when those emails are
scheduled the campaign automatically updates to the In Progress status again.
• Closed: When no additional follow-up emails need to be sent for a campaign, you can close the campaign using
the Close Campaign action. A closed campaign cannot be edited.
• Canceled: To stop an in progress campaign, use the Cancel Campaign action. Any draft or scheduled emails
are automatically updated to the Canceled status. If emails are in the process to be sent, the Cancel Campaign
action doesn't prevent those emails from being sent, but it prevents subsequent scheduled emails from being
sent. A canceled campaign can't be edited.

---

## Actions to Perform on Campaigns
*Chunk ID: OHR-USE-0164 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

You can perform several actions on campaigns from the Campaigns page.
The Actions menu lists actions that you can perform according to your privileges. Actions that don't apply to the
campaign status are disabled.
• Activate Campaign: Use the Activate Campaign action when you're done working on the campaign details,
defining the campaign audience, and designing and scheduling the primary email. A campaign must be
activated for scheduled emails to be sent. This action is only available when the campaign is in the Draft status
and the primary email has been scheduled. Once activated, the campaign is in the Scheduled status and
campaign details and audience can't be modified, unless the Redraft Campaign action is used before the first
email has been sent.
• Delete Campaign: Use the Delete Campaign action to delete any campaigns that were created in error and are
no longer needed. Deleting a campaign removes it from the list of campaigns. This action is only available when
the campaign is in the Draft status.
• Redraft Campaign: Use the Redraft Campaign action to make changes to an activated campaign. You can make
edits to the campaign details, campaign audience, and campaign emails. This action is only available when the
campaign is in the Scheduled status.
• Cancel Campaign: Use the Cancel Campaign action to stop a campaign in progress and prevent any unsent,
scheduled emails from being sent. If a scheduled job is in the process of sending emails, those emails can't be
stopped currently. Once canceled, campaign details can't be modified and no follow-up emails can be added to
the campaign. This action is only available when the campaign is in the In Progress status.
• Close Campaign: Use the Close Campaign action when the campaign is finished and no further follow-up
emails need to be sent. This action is only available when the campaign is in the Completed status. Once closed,
campaign details can't be modified and no follow-up emails can be created.

---

## Actions to Perform on Campaign Emails
*Chunk ID: OHR-USE-0165 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

You can perform several actions on campaign emails.
• Schedule Email: You can send the email now or schedule the delivery of the email by entering a date and time.
You can only schedule follow-up emails once the primary email is scheduled. To use the Send Now scheduling
option, you must first activate the campaign. You should only schedule an email when you're finished working
on the email design and contents. Follow-up emails can't be scheduled until the primary email has been
scheduled. Follow-up emails must be scheduled to be sent after the primary email.

• Delete Email: You can delete the primary email and follow-up emails when they are in the Draft status. You
can only delete the primary email once all follow-up emails are deleted. If you delete the primary email, you're
prompted to create a primary email again.
• Redraft Email: Use this action to make changes to an email in the Scheduled status. The email is returned to
the Draft status. If you're redrafting the primary email and there are scheduled follow-up emails, the follow-up
emails are also returned to the Draft status and you need to schedule them again. The previously selected send
dates are retained when rescheduling the redrafted emails.
• Edit Email Details: You can modify the name and audience of the email. For the primary email, you can only
modify the name.
• Design Email Content: You can work on the email design and content in the email editor. With the email editor,
you can move and delete elements in the email, modify the text, change background color, text color, text style,
text size, and align the content. You can also save the email as draft and send a test email so you can preview
how the email looks like before activating it.

---

## Create a Campaign from a Candidate Pool
*Chunk ID: OHR-USE-0166 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

You can create a campaign from a candidate pool and use that pool as the audience of the campaign.
1. On the Candidate Pools page, select a candidate pool.
2. In the Actions menu, select Create Campaign.
3. Complete the fields to specify the specific requirements of the campaign.

---

## Social Media Campaigns
*Chunk ID: OHR-USE-0167 | Chapter: Recruiting Campaigns | Guide: Using Recruiting*

You use social media campaigns to create a landing page or use an existing landing page to generate a unique link that
can be used on social media.
You can then paste the link to the post in the record and the post will be visible within the campaign area without the
need to go to the social media channel. All of the social media posts for a campaign are visible in one area.
Supported channels are:
• Facebook
• Twitter
• LinkedIn
• Other

---

# Recruiting Agencies

## Create a Social Media Campaign
*Chunk ID: OHR-USE-0168 | Chapter: Recruiting Agencies | Guide: Using Recruiting*

You can create and manage social media posts with personalized landing pages as part of an email marketing
campaign. This helps you to widen the target audience of engaged candidates.

1. Click on the Campaigns tab.
2. Open a campaign.
3. Click the Social Media tab.
4. Click Add.
5. On the Posts page, enter a name for the post.
6. Select a channel for the post. Possible options are:
◦ Facebook

◦ Twitter
◦ LinkedIn
◦ Other
7. Select a landing page or create a new one.
You can create a simple landing page based on the parent email. With this landing page, you can provide more
info than the social media channel allows, capture channel metrics, and capture contact info from social media
candidates.
8. Enter a URL to an image.
9. Enter an external description for the landing page.
10. Select a career site where the post will appear.
11. Click Save.
12. If you selected to create a landing page, you're taken to the landing page editor. This is where you can select the
email previously created for the campaign so that you keep the same branding and consistency. You can also add
elements to the page such as headline, paragraph, text, image, button, job list. If you add the Capture Candidate Info
element, you can capture basic information from candidates who visit the landing page so that they may join the
talent community.
13. On the Posts page, select Activate in the post's Actions menu.
This creates a URL for the post.
Results:
When candidates click the Join Talent Community button on the landing page, the application captures their visit. You
get basic metrics from the social media posts and can evaluate the effectiveness of each post and channel. To see those
metrics, go to the Overview tab of the campaign. Metrics are displayed in the Social Media Metrics section.

11 Recruiting Agencies
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
*Chunk ID: OHR-USE-0169 | Chapter: Recruiting Agencies | Guide: Using Recruiting*

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

# Candidate Selection Processes

## Invite Recruiting Agents to Submit Candidates for a Job
*Chunk ID: OHR-USE-0170 | Chapter: Candidate Selection Processes | Guide: Using Recruiting*

Requisition
You can invite recruiting agents to submit candidates for specific job requisitions. This is considered an agent referral.
1. On the Job Requisitions page, open a job requisition.
2. Click the Posting tab.
3. On the Posting page, go to the Staffing Agents section.
4. Click the Agent selector to see a list of agents matching the location and job family of the job requisition.
5. To expand your search and see a larger list of agents, click Advanced Search.
The Agents page displays a list of agents with details about each agent. You can see useful metrics such as the
number of job requisitions for which the agent was invited to submit candidates, the percentage of job applications
submitted by the agent where candidates were offered a job, the average time required by the agent to source
candidates through to the Offer phase. You can also filter the list of agents using the Location and Job Family filters.
6. Select one or more agents.
7. Click Save and Close.
You're back on the Posting page.
8. In the Staffing Agents section, click Actions.
9. Select Set Expiration Date to set an expiration date and time.
If you select No Expiration, the invitation will expire when the requisition expires.
10. Select Invite Agents to send agents an invitation to submit candidates for the job requisition.
Results:
When a candidate is referred by an agent, the information is tracked in the candidate file Source Information section.
You can see the source medium which is Agency Referral, and the source which is the name of the agency that
submitted the candidate.
Staffing agents don't receive an email every time they're added to a requisition. But they will see the requisitions that
they have been added to once they sign in.

12 Candidate Selection Processes
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

## Candidate Selection Process Phases and States
*Chunk ID: OHR-USE-0171 | Chapter: Candidate Selection Processes | Guide: Using Recruiting*

A candidate selection process is made of multiple phases, and each phase is made of multiple states. For details, see
What are the phases and states of a candidate selection process?

---

## How You Move Candidates in the Candidate Selection
*Chunk ID: OHR-USE-0172 | Chapter: Candidate Selection Processes | Guide: Using Recruiting*

Process
You move candidates in the candidate selection process by selecting the phase and state where you want to move the
job applications.
Here are a few things to keep in mind:
• You can only move candidate job applications that are active, confirmed, and have no job offer.
• You can move candidate job applications back and forth within the states of a phase.
• You can only move candidate job applications forward in a later phase of the candidate selection process. To
move a candidate to a prior phase, you need to use the Return to Prior Phase action.
• When you move one candidate job application, the phase defaults to the current phase. When you move more
than one candidate job application, the phase defaults to the first phase of the candidate selection process, not
the current phase.
• You can bypass phases if they're configured as not required. To do so, you
need the privilege Move Candidate Job Applications Ignoring Constraints
(IRC_MOVE_CANDIDATE_JOB_APPLICATION_SKIPPING_MANDATORY_PHASES), which is granted by default to
recruiters.

If your administrator defined move conditions on a given candidate selection process state, you can't move
job applications until the conditions are met. You can however manually move job applications regardless
of the move conditions if you have the privilege Move Candidate Job Applications Ignoring Constraints
(IRC_MOVE_CANDIDATE_JOB_APPLICATION_SKIPPING_MANDATORY_PHASES). Here's an example: Your administrator
defined a condition to prevent moving job applications when a background check was initiated but the results haven't
been returned yet. While the background check request is in progress, you can't move job applications to a different
phase or state. Once background check results are received, you can move job applications.
Note: A condition can prevent moving candidates forward. Even if the condition isn't met, you can still use the Return
to Prior Phase action.

---

## Move a Candidate in the Candidate Selection Process
*Chunk ID: OHR-USE-0173 | Chapter: Candidate Selection Processes | Guide: Using Recruiting*

You use the Move action to select the phase and state where you want to move one or several candidate job
applications.
Before you start
You can only move candidate job applications that are active, confirmed, and have no job offer.
Here's what to do
1. Go to the list of candidate job applications for a job requisition.
2. Select one or several candidate job applications.
3. In the Actions menu, select Move.
4. Select the phase and state where you want to move the job applications.
When you move one candidate job application, the phase defaults to the current phase. When you move more
than one candidate job application, the phase defaults to the first phase of the candidate selection process, not the
current phase.
5. You can enter a comment.
Comments you provide appear in the Progress tab of the job application.
6. Click Save and Close.

---

# Candidate Interviews

## Where You Can See the Phase and State of a Candidate
*Chunk ID: OHR-USE-0174 | Chapter: Candidate Interviews | Guide: Using Recruiting*

Job Application
You can see the phase and state of a candidate job application from the job applications list and from within the job
application.
When you view the list of job applications for a job requisition, the phase and state are displayed next to each job
application.

When you open a job application, click the Progress tab to obtain more details about the status of the job application.
Two views are available:
• Current Progress: This view displays all the phases the job application will go through, the amount of time spent
in each phase, and the state of the current phase.
• Progress History: This view displays every phase and state the job application has gone through.
Depending on where the job application is in the selection process and the configuration of the application flow, the
Progress tab can display e-signatures: the job application e-signature completed as part of the candidate's application
process, and the job offer e-signature completed as part of accepting a job offer. “Anonymous” is displayed when a
candidate file is created or changed by an external candidate on the career site. In such cases, the user name for the
created by / updated by field will display “Anonymous”.
Note: The Progress tab only appears when a job application is confirmed. It doesn't appear for unconfirmed
candidate job applications.

13 Candidate Interviews
You can schedule, manage, and track interviews with candidates to evaluate their qualifications and work experience
and move them through the candidate selection process.
All interview tracking and management tasks are done directly in the Oracle Fusion Cloud Recruiting, in one centralized
place. This helps reduce the amount of time spent on the phone and exchanging emails.
Let's look at the main steps of the interview creation process.
As a recruiter or hiring manager, you create interview schedules based on a template created by your administrator.
You can schedule interviews on behalf of candidates or you can invite candidates to schedule their own interviews
at the date and time that work best for them. Interviewers and candidates are sent notifications as interviews are
scheduled, rescheduled, and canceled, ensuring everyone is kept in the loop throughout the interview process. When
a candidate interview is completed, you can see the Completed status in the Interviews tab of a job application. An
interview is considered to be completed when the end date and time of the interview is now in the past. The Interactions
tab contains interview details.
Note: When an interview is scheduled in the future and the candidate is moved to a terminal state such as Rejected
by Employer or Withdrawn by Candidate, interview details are removed. If the interview already took place, interview
details are kept in the Interactions tab.
There are two types of interview schedules. The type of interview schedule determines when and who can create
interviews for candidates:
• Hiring team managed interview schedules: Members of the Hiring Team can start creating interviews for
specific candidates.
• Candidate managed interview schedules: Members of the Hiring Team create interview slots and candidates
can be sent invitations to schedule their interviews by selecting from the available time slots. Interviews can
also be created on behalf of candidates.

---

## Zoom Integration in Interview Scheduling
*Chunk ID: OHR-USE-0175 | Chapter: Candidate Interviews | Guide: Using Recruiting*

As a recruiter, you can use the Zoom integration to generate web conference links for interviews.
Zoom is available on:
• Interview schedules
• Interview schedule templates
• When creating interviews
• When creating interview slots on a candidate managed schedule

Before you can use Zoom for interviews, you need to provide your authorization to be added as a meeting host for
interviews scheduled with Zoom. The quick action Authorize Zoom Integration for Interviews is available under Me >
Hiring.
Note: For the quick action to be available, your administrator must enable and configure the
Zoom integration, and you need the privilege Access Zoom Authorization Page for Interviews
(IRC_ACCESS_ZOOM_AUTHORIZATION_PAGE_FOR_INTERVIEWS_PRIV).

---

## Microsoft Office 365 Integration in Interview Scheduling
*Chunk ID: OHR-USE-0176 | Chapter: Candidate Interviews | Guide: Using Recruiting*

If your organization has integrated Microsoft 365, here's how you can use interview scheduling:
• You can view the interviewer availability when scheduling interviews on behalf of candidates and when creating
interview slots for candidates to self-schedule.
• When editing scheduled interviews or interview slots, you can view interviewer availability to ensure you're
rescheduling when the interviewer is free.
• Interviewers and interview coordinators will receive interview events in Microsoft 365 that they can easily add
to their calendar. As those events are modified in Oracle Recruiting Cloud, the event in Microsoft 365 is updated
automatically.
• You can generate Microsoft Teams meeting links in candidate-managed interview slots. When you create
interview slots for a candidate-managed interview schedule or create an interview on a candidate-managed
interview schedule, you can select an option called Use Teams Integration. This option is available for interviews
with a Web Conference format.
• You can view interviewer responses to Office 365 interview invites when managing interviews. Interview
organizers no longer have to rely on the managing interviewer responses outside of Recruiting. When Office
365 events are sent to interviewers, and the interviewers respond to the invite, meeting organizers can view the
interviewer response (Accept, Tentative, Decline, Propose New Time) in the interview details.
Note: The signed in user or the person scheduling the interview need an active Azure account attached to their email
address. When the person creating the interview schedule selects the interviewer and refreshes their availability, the
application will try to get the Microsoft 365 user ID for that person. If the user ID isn't found, the application will verify
if the default user ID was added for Microsoft Graph Integration.

Related Topics
• Capture Interviewer Responses
• Create an Interview Schedule

---

## Google Workspace Integration in Interviews
*Chunk ID: OHR-USE-0177 | Chapter: Candidate Interviews | Guide: Using Recruiting*

The Google Workspace integration enables interview coordinators to view free / busy calendar information of
interviewers and to create, reschedule, and delete interviewers to sync with the interviewer's calendar.

When your enable the Google Workspace integration, here's how you can use it for interviews:
• When users create an interview schedule for a job requisition or when they schedule an interview for a
candidate, when they select the web conference format, the Enable Google Meet option is available.
• Users can view the availability of interviewers when scheduling interviews for a candidate and when creating
interview slots for the candidate to self-schedule.
• When users change scheduled interviews or interview slots, they can see the availability of interviewers to
ensure they're rescheduling when interviewers are free.
• Interviewers receive calendar events directly in Google. As those events are changed in Oracle Recruiting Cloud,
events in Google are updated automatically.
• Users can view interviewer responses to Google interview invites when managing interviews. When calendar
events are sent to interviewers, and the interviewers respond to the invite, meeting organizers can view the
interviewer response in the interview details.
• Interviewers and interview coordinators can define their preferred availability for candidate interviews in the My
Availability tab. Preferred availability is used when inviting candidates to self-schedule their interviews based on
the interviewers' availability (this is a Recruiting Booster feature). The system will propose to candidates time
slots which are part of the preferred availability and for which interviewers are available in their Google calendar.
Two options are available:
◦ Use the default working days and my Google Workspace calendar availability: This is the default option.
The default working days and working hours configured by the admin are used.
◦ Use my preferred availability and my Google Workspace calendar availability: With this option,
interviewers define their preferred availability for each day of the week. Interviewers can change their
availability at any time.
Related Topics
• Google Workspace Integration in Recruiting (ID 3073141.1)

---

## Create an Interview Schedule
*Chunk ID: OHR-USE-0178 | Chapter: Candidate Interviews | Guide: Using Recruiting*

To schedule interviews with candidates, you first need to create an interview schedule for the job requisition.
Before you start
• The job requisition must be in the Approval phase or later phases.
• You need the privilege Manage Job Requisition Interview Schedule
(IRC_MANAGE_JOB_REQUISITION_INTERVIEW_SCHEDULE).
Here's what to do
1. On the Job Requisitions page, open a job requisition in the Approval phase or later phases.
2. Click the Interviews tab.
3. In the Interview Schedules section, click Add then select Create Interview Schedule.

4. Complete the Basic Information section:
a. Select an interview schedule template. Content from the template is copied in the interview schedule. The
schedule type is defined by the schedule template you selected.
b. Define an interview title to indicate the purpose of the interview such as if this is a first interview, second
interview, or a technical interview. When you schedule an interview for a candidate, the interview title is
defaulted from the interview schedule but you can change it.
c. Select a schedule owner.
5. Complete the Location Details section:
The format of the interview is copied from the schedule template you selected. You can change the information.
Formats for the interview are in person, by phone, by web conference. The web conference format generates a link
for the interview. The Use Teams integration option or the Use Zoom integration option is available depending on
the integration enabled within your organization.
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
be offered to authorize the Zoom integration if it's not already authorized. If that's the case, you'll be able
to do it on the page without needing to access the Zoom authorization quick action. When you save an
interview schedule for the first time, the schedule owner (the current user creating the schedule) is asked to
authorize the Zoom integration if not already done. That's because in some situations it's possible to have a
meeting host who hasn't provided the Zoom authorization. When that happens, the schedule owner is used
as the meeting host instead.
Note: The other fields related to web conference are disabled: Phone, Web Conference Link, Access Code.
6. Complete the Settings section:
a. Select which actions candidates can perform on their interviews. See Interview Schedule Settings.
7. Complete the Candidate Info section:
a. Details are copied from the schedule template you selected. You can change the information.
- Preschedule details are instructions for candidates before scheduling their interview.
- Postschedule details are instructions for the interview such as directions to the interview location,
instructions on how to join a web conference.
8. Complete the Interviewer Documents section:
a. Include documents attached to the notification sent to interviewers.
- You can include a link to the job posting so that the interviewers can refer to the job description,
qualifications, or other details.
- You can include a link to the resume.
- You can include a .ics attachment so that candidates and interviewers can add the interview to their
calendar. The .ics setting is used for both the interviewer and the candidate, and contains complete
interview location information. The subject text includes the candidate's name.

9. Complete the Reminder section:
a. Complete this section for candidate managed interview schedules. You can indicate if you want to send a
reminder notification to the interview schedule creator when the schedule has a low number of available
interview openings. You can also send a reminder notification when the schedule is full. The number of
available interview openings can decrease when candidates are scheduling interviews, but also due to time
passing (interview openings now being in the past).
10. Click Save and Close.
Results:
The interview schedule appears on the Interview Schedules page and its status is Published.

---

## Create an Interview Schedule Before Submitting the Job
*Chunk ID: OHR-USE-0179 | Chapter: Candidate Interviews | Guide: Using Recruiting*

Requisition for Approval
You can create interview schedules for a job requisition before submitting the requisition for approval. This way
interview schedules are created earlier and the requisition is fully ready when approved.
Before you start
• The job requisition must be in the Draft phase.
• You need the privilege Manage Job Requisition Interview Schedule
(IRC_MANAGE_JOB_REQUISITION_INTERVIEW_SCHEDULE) and the privilege
Manage Job Requisition Interview Schedule Before Job Formatting Phase
(IRC_MANAGE_JOB_REQUISITION_INTERVIEW_SCHEDULE_BEFORE_JOB FORMATTING_PHASE).
Here's what to do
1. On the Job Requisitions page, find a draft job requisition.
2. In the Actions menu, select Define Interview Schedules.
Note: Content such as headers, tabs, navigation isn't displayed.
3. On the Interview Schedules page, click Add then select Create Interview Schedule.
4. Complete the fields and provide all the details required for the interview schedule. For details, see Create an
Interview Schedule .
5. Click Save and Close.
Results:
The interview schedule appears on the Interview Schedules page.
What to do next
Publish the schedule so that you can schedule interviews. In the Actions menu, select Publish Schedule.

---

## Candidates can reschedule
*Chunk ID: OHR-USE-0180 | Chapter: Candidate Interviews | Guide: Using Recruiting*

• Candidates can cancel their
interviews on external and internal
career sites. When candidates view a
scheduled interview, they can use the
Cancel Interview action.
Candidates can't make last-minute
changes - Hours Before Interview
• Select the number of hours before
an interview when candidates can no
longer make changes.

• Candidates can reschedule their interviews on external and internal career sites when the
schedule permits it. When candidates view a scheduled interview, they can use the Reschedule
Interview action.

---

## Candidates can cancel
*Chunk ID: OHR-USE-0181 | Chapter: Candidate Interviews | Guide: Using Recruiting*

• Candidates can cancel their interviews on external and internal career sites. When candidates
view a scheduled interview, they can use the Cancel Interview action.

---

## Candidates can schedule on same day
*Chunk ID: OHR-USE-0182 | Chapter: Candidate Interviews | Guide: Using Recruiting*

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

## Create Interview Slots
*Chunk ID: OHR-USE-0183 | Chapter: Candidate Interviews | Guide: Using Recruiting*

If you created an interview schedule of type Candidate Managed, you need to create interview slots. You use interview
slots to define the date, time, duration, and interviewers of the interview.
1. On the Job Requisitions page, open a job requisition.
2. Click the Interviews tab.
3. On the Interview Schedules page, click the schedule you just created.
4. Click Add.
5. Complete the fields in the Interview Details section.
a. Click the Calendar icon and select the days when the interview will take place.
b. Enter the start time and end time of the interview.
The Start Time and End Time fields show your time zone, based on your regional preference setting. You
can select a different time zone. Upon saving the interview time slots, you'll see the slots in the interview

schedule based on your time zone. Candidates will see the slots converted to their time zone when
scheduling their interviews and when interviews are scheduled on their behalf.
c. Enter the interview meeting duration.
d. Enter the number of candidates. For details see, Define Number of Seats Available per Interview Slots.
e. Complete the fields in each section. For details, see Create an Interview Schedule .
6. Click Save and Close.
Note: There are situations where the user who creates the interview slot or interview is considered as the interview
organizer and therefore considered as not available for other interviews at this same time. However, there are
situations where this isn't the case:
◦ Recruiting is set up to allow double booking of interviewers. In this situation, the user is still the
organizer, but the application won’t check the user’s availability. For details, see Configure Double
Booking of Interviewers.
◦ The Microsoft 365 Calendar integration is enabled and the access type is set to Single User. When
Single User is selected, users can create interviews without receiving a Microsoft 365 calendar event
for this interview. The interview creator receives a calendar event only if the interview creator is also
an interviewer. This means the user creating the slot or interview isn't considered as being part of the
interview, unless the user is also added as an interviewer. For details, see Enable Microsoft 365 Calendar
Integration in Interviews.
◦ The Microsoft 365 Calendar integration is enabled and the access type is set to All Users, the slot or
interview is set to use Teams or Zoom integration, and a user is selected as being the meeting host. In
this situation, the meeting host can be selected when creating the slot or interview. The user selected as
the meeting host is also the organizer. So, unless the user creating the slot or interview is selected as the
meeting host, this user isn't considered as being part of the interview.

---

## Additional Interview Slots Request from Candidates
*Chunk ID: OHR-USE-0184 | Chapter: Candidate Interviews | Guide: Using Recruiting*

When candidates are on a career site and access the page allowing to schedule an interview, they can click a link to
request additional interview slots. The link is always available regardless if interview slots are proposed to candidates.
Before candidates submit their request, they need to provide some text explaining their request. When the request
is submitted, a notification is sent to the interview schedule owner. The notification is available in Alerts Composer:
Additional Interview Slots Request from Candidate (IRC_Intrv_Candidate_Request_More_Slots).
By default, the schedule owner is the recipient of the notification. However, you can change the recipient by adding the
recruiter and the hiring manager of the requisition. You can also change the content and formatting of the notification.
The schedule owner who receives the notification can review the comments provided by the candidate and act as
needed. For instance, add more interview slots, schedule an interview manually, ask interviewers to free up their
calendar.

The notification might contain the following tokens. These tokens are replaced by a value only if the interview invitation
is sent for an interview schedule where the setting "Candidates schedule based on interviewers' availability" is selected.
In other situations, it's not possible to determine a value for these tokens.
• InterviewSchedulingInterviewerName
• InterviewSchedulingInterviewMeetingDuration
When the tokens are used, the value can be different for all slots on the schedule, making it impossible to determine
the value. This is why a condition is included in the notification to display these values and their labels only when the
"Candidates schedule based on interviewers' availability" setting is selected on the interview schedule. This is done
using the following condition:
<% if (InterviewSchedulingUseInterviewerAvailability== "Y") print("Interviewers: " +
InterviewSchedulingInterviewerName); %><% if (InterviewSchedulingUseInterviewerAvailability==
"Y")print("Meeting duration: " + InterviewSchedulingInterviewMeetingDuration); %>

---

## Define Number of Seats Available per Interview Slots
*Chunk ID: OHR-USE-0185 | Chapter: Candidate Interviews | Guide: Using Recruiting*

When you create interview slots on candidate managed interview schedules, you can define the number of seats
available per slot using the Number of Candidates field.
Let's say for example that you create an interview slot between 9 am and 10 am and that 5 interviewers are available
during that interview slot. This means that up to 5 candidates can select that time slot when scheduling their interview.
When candidates are scheduling their interview, they only see one interview slot. There's no indication that there are
multiple seats. As candidates select that time slot, the number of available seats decreases until the interview slot is fully
booked, at which time the interview slot is no longer available for selection by candidates. Also note that:
• If the number of seats is filled before the candidate accesses the scheduling page, that time slot isn't displayed
• If the number of seats is filled while the candidate is attempting to schedule that slot, the candidate will see an
error message that directs them to select another available slot.
• If candidates reschedule or cancel their interview, the number of available seats is updated.
When you create an interview slot with one seat, you can see the name of the candidate who selected that time slot in
the Interviews calendar. If you create an interview slot with multiple seats, you can see the number of available seats
versus booked seats for the interview slot.
If you go to the requisition's Interviews tab, in each interview slot there is now a Scheduled Candidates section, you
can see the name of the candidates who will attend the interview. You can also perform actions on candidates such as
canceling the interview or sending an invitation to reschedule the interview. If you click the name of the candidate, you
are navigated to the candidate's job application where you can see and manage all of their interviews.

---

## Defining an Interview Schedule Owner
*Chunk ID: OHR-USE-0186 | Chapter: Candidate Interviews | Guide: Using Recruiting*

You can define an interview schedule owner on interview schedules, who's different than the schedule creator
As an interview coordinator, you can change the owner of an existing interview schedule. The schedule owner is
required. When you create an interview schedule using a schedule template, the schedule owner is defaulted from the
schedule template. If the template doesn’t have a named user, you’ll be the schedule owner.

Here's more info on how the schedule owner is set.
When you create an interview schedule:
• If your administrator created an autocomplete rule to default the schedule owner, the schedule owner is set
according to the rule.
• If no autocomplete rule was created, the schedule owner is set to the current user (you).
If you later select an interview schedule template for the interview schedule:
• If a schedule owner is defined in the template, the schedule owner is set according to the template.
• If no schedule owner is defined in the template, the schedule owner defined while creating the schedule (with
or without an autocomplete rule) is kept.
When Zoom integration is selected on the interview schedule, the selected schedule owner must have provided a Zoom
authorization.
• If you’re the schedule owner, you’ll be asked to provide a Zoom authorization, if you haven’t provided one.
• If another user is the schedule owner and that user didn’t provide a Zoom authorization, you’ll have to select a
new user.
Note: There are no impacts to Teams integration as the authorization mechanism is different.

---

## Schedule Interviews for Candidates
*Chunk ID: OHR-USE-0187 | Chapter: Candidate Interviews | Guide: Using Recruiting*

You can schedule interviews for candidates for a job requisition. You can schedule interviews for hiring-team managed
schedules and candidate-managed schedules.
1. On the Job Requisitions page, open a job requisition that has an interview schedule.
2. Access the list of job applications.
3. Click a job application.
4. In the job application, click the Interviews tab.
5. Click Add.
6. Complete the fields in the Interview Details section.
a. Select the format of the interview. Available formats are In Person, Phone, Web Conference.
b. Select an interview schedule.
c. The interview title is defaulted from the interview schedule but you can change it.
d. Enter the start date and time, and the end date and time of the interview.
The start and end times will show the candidate's time zone if it was captured when the candidate applied
for the job or when the candidate was created by a Recruiting user.
7. Complete the fields in the Interviewers section.
When an interviewer is scheduled for an interview, any existing unscheduled time slots during that period for that
interviewer are removed from interview schedules automatically. Also, when you schedule interviews on behalf of
candidates, you're notified if an interview is already scheduled for the interviewer during that time and prompted to
select a new time or new interviewer.
8. Click Save and Close.

Related Topics
• Create an Interview Schedule

---

## Invite Candidates to Schedule Their Interviews
*Chunk ID: OHR-USE-0188 | Chapter: Candidate Interviews | Guide: Using Recruiting*

You can manually send an interview invitation to candidates so they schedule their own interviews. This can be done
with interview schedules of type candidate managed.
1. On the Job Requisitions page, open a job requisition.
2. Access the list of job applications.
3. Select one or multiple candidate job applications.
4. Use the Send Interview Invite action.
Results:
Candidates receive a notification containing a link to the career site where they can schedule the interview. They select
a time among the available time slots that have been defined on the interview schedule added to the job requisition. As
soon as a candidate selects a time slot, that time slot is no longer available to other candidates invited to the interview.
As a recruiter, you can see which time slots were selected by candidates. This information is available in the candidate
job application and in the interview schedule of the job requisition.
Candidates can access interview details as long as their job application is still active.
What to do next
You can invite a candidate to reschedule an interview. You can use the Send Invitation to Reschedule action when you're
on the Interviews list or viewing the details of an interview. The candidate receives a notification containing a link to
access their career site where they can reschedule their interview.

---

## Capture Interviewer Responses
*Chunk ID: OHR-USE-0189 | Chapter: Candidate Interviews | Guide: Using Recruiting*

You can view interviewer responses to Microsoft 365 interview invites when managing interviews.
Interview organizers no longer have to rely on the managing interviewer responses outside of Recruiting. When
Office 365 events are sent to interviewers, and the interviewers respond to the invite, meeting organizers can view the
interviewer response (Accept, Tentative, Decline, Propose New Time) in the interview details.
The system sends a notification to the "interview slot owner" or "interview creator" when an interviewer responds to the
invite. This is true for all possible responses (Accept, Decline, Tentative, and Propose New Time).
To draw attention to when interviewers have declined or proposed a new time, different colors are used for interviews in
the interview schedule's calendar. This helps interview organizers to take appropriate actions.
• Red: At least one interviewer has declined.
• Purple: No interviewer has declined, and at least one has tentatively accepted.
• Green: No interviewer has declined or tentatively accepted, and at least one interviewer accepted.
• Blue: No interviewer has responded, but the interview or interview slot has been scheduled.
• Orange: No interview is scheduled for the interview slot.

When a candidate declines or proposes a new time for the interview, a notification is sent to the interview schedule
owner and the interview slot creator. The notification includes a link to the job application's Interviews tab, and the user
can make the required changes (either cancel the interview, change the interviewer, or reschedule the interview).
When candidates select a date and time for an interview, the interviewer receives an invite in Microsoft 365. When the
interviewer accepts the interview date and time selected by the candidate, the info is updated in Recruiting.

---

## Automatically Send Interview Invitations
*Chunk ID: OHR-USE-0190 | Chapter: Candidate Interviews | Guide: Using Recruiting*

Interview invitations can be sent automatically to candidates when their job applications reach a given point in the
candidate selection process.
If your administrator enabled the feature, a section called Automated Interview Invitation is available in the Interviews
tab of a requisition.
1. You first need to create and publish one or multiple candidate-managed interview schedules for the job requisition.
2. You can then assign a candidate-managed interview schedule to the phases, states, and events of the candidate
selection process for which the automated interview invitation was added.
Results:
When the job application reaches the defined phase or state, or when the event occurs, an invitation is automatically
sent to candidates if there are available slots in the schedule.
Note: The manual action Send Interview Invite is still available even if automated interview invitations have been
configured.
What to do next
Note that some of the automated interview notifications configurations might show as being deactivated if the action is
deactivated in the candidate selection process:
• When your administrator modifies actions of a candidate selection process that generates additional
configuration on job requisitions, the configuration of the job requisition or requisition template using this
process is updated accordingly.
• When a job requisition uses a candidate selection process with deactivated actions, these actions are still visible
on the job requisition configuration, but there is an indication that they're deactivated.
• For actions that are waiting to receive information by a candidate (interview invite), the information will be
accepted even if the corresponding action has been deactivated. The fact that the action is deactivated only
impacts its triggering, not the reception of information after.

---

## Candidate Interview Notifications
*Chunk ID: OHR-USE-0191 | Chapter: Candidate Interviews | Guide: Using Recruiting*

Several notifications related to interviews are sent to candidates and interviewers. Notifications sent to candidates are
logged in the candidate's job application Interactions tab.
This table lists the notifications that are sent for actions related to candidate interviews.

Action

---

## Candidate Interview Time Zones
*Chunk ID: OHR-USE-0192 | Chapter: Candidate Interviews | Guide: Using Recruiting*

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

## Ask For Feedback About a Candidate Interview
*Chunk ID: OHR-USE-0193 | Chapter: Candidate Interviews | Guide: Using Recruiting*

You can ask the Hiring Team to provide feedback regarding the interview of a candidate.
You can request feedback for one candidate or several candidates. When you select five or less job applications, the
Collect Feedback action is performed in real time. When you select more than five job applications, the action is
performed asynchronously and is processed as soon as possible. You're still able to continue to work. When the process
is completed, you receive an email informing you that the action was successful for the number of job applications. You
can also view which job applications were skipped or failed for any reason.
1. On the Job Applications list, select one or several candidate applications.
2. In the Actions menu, select Collect Feedback.
3. On the Collect Feedback page, in the Candidates section, you can keep the candidates you selected or remove some
of them.
4. In the Select Respondents section, select respondents.
By default, the Hiring Team defined on the job requisition is available for selection as respondents. You can add other
respondents (any HCM user). They'll also be added to the job requisition's Hiring Team as collaborators unless the
profile option has been set to not add respondents to the Hiring Team.
5. In the Select Interview Questionnaire section, select interview feedback questionnaires. These questionnaires
contain questions to collect interview feedback.
If you select a questionnaire that contains questions that are scored, you can take advantage of the questionnaire
scoring capabilities to capture and display interview feedback scores on job applications. This is done using the
Request Rating from Respondent.
6. In the Include Documents section, select job application's attachments to include in the feedback request. You can
include a resume, cover letter, or miscellaneous attachments.
7. In the Request Details, enter the expiration date for the request. You can also add a note for respondents.
8. If you select the Request Rating from Respondent option, a Rating section becomes available in the questionnaire,
and respondents provide a rating while completing the interview feedback questionnaire. When feedback
respondents have submitted feedback questionnaires (the request status is Completed), the Feedback Requests
section displays individual score and rating provided by each respondent for each questionnaire. For details,
seeInterview Feedback Scoring and Ratings
9. Click Submit.
Results:
The respondents get a worklist notification (Bell icon) or an email that contains a link to open the interview
questionnaire. The questionnaire includes basic information such as the requisition title, candidate name, job
application-specific attachments, questionnaire instructions, any notes you added for the respondents. A Rating section
is available if you enabled the option Request Rating from Respondent.
Note: The feedback form is secured. Respondents can access the link if they have one of these privileges:
Access to Hiring as Manager (IRC_ACCESS_TO_HIRING_AS_MANAGER_PRIV), Access to Hiring as Recruiter
(IRC_ACCESS_TO_HIRING_AS_RECRUITER_PRIV).
The respondents can complete the questionnaire or save their responses to complete the questionnaire later. When
respondents submit the questionnaire, the completed questionnaire is available to review in the job requisition and
candidate job application, on the Feedback tab. If you enabled the option Request Rating from Respondent, a Score and
Ratings section shows the average score and rating provided so far by respondents for each questionnaire attached to

the interview feedback request. Also, the Key Highlights section in the job application Details tab displays the overall
rating for all feedback questionnaires and respondents. You can use the advanced filter called Feedback Questionnaires
to filter the average score for a questionnaire. When you select a questionnaire, you define the minimum and maximum
scores. When you apply the filter, job applications whose average score is between the minimum and maximum scores
are displayed.
If respondents try to access a questionnaire they already submitted, they don't see the questionnaire; instead they just
see a generic message that the questionnaire was completed and submitted.
You can manage requests for interview feedback for a single candidate at the job application level or across all job
applications at the job requisition level, on the Feedback tab. Requests are grouped by questionnaire and display the
candidate, respondent, request status, and request date.
To send a message to respondents to remind them that they need to provide feedback, use the Send Reminder action.
You can cancel feedback requests using the Cancel Request action. You can also renew expired requests so that
respondents can complete the questionnaire. The Renew action resends the request to the respondent with the original
attachments and notes. The renewed request automatically expires 14 days from the renewed request date.
Related Topics
• Interview Feedback Scoring and Ratings

---

## Interview Feedback Scoring and Ratings
*Chunk ID: OHR-USE-0194 | Chapter: Candidate Interviews | Guide: Using Recruiting*

You can take advantage of the questionnaire scoring capabilities to capture and display interview feedback scores on
job applications.
When you want to collect feedback regarding the interview of a candidate, you can select feedback questionnaires
that contain questions that are scored. While you define the details for collecting feedback, an option called Request
Rating from Respondent is available. When you select this option, a Rating section is available in the questionnaire,
and respondents provide a rating while completing the interview feedback questionnaire. When feedback respondents
have submitted feedback questionnaires (the request status is Completed), the Feedback Requests section in the job
application Details tab displays individual score and rating provided by each respondent for each questionnaire.
The Scores and Ratings section shows the average score and rating provided so far by respondents for each
questionnaire attached to the interview feedback request. The Key Highlights section displays the overall rating for all
feedback questionnaires and respondents.
Note: Depending on how the questionnaire is configured, scores are displayed as sum, average, or percentage. For
scores displayed as average, up to two decimals are used. Note that the questionnaire table stores the individual
questionnaire scores as whole numbers.

---

## Configure Grid View with Interview Feedback Fields
*Chunk ID: OHR-USE-0195 | Chapter: Candidate Interviews | Guide: Using Recruiting*

If you have the privilege Personalize Candidates Lists (IRC_PERSONALIZE_CANDIDATE_JOB_APPLICATION_LISTS),
you can access the Manage Views page available in the View menu of the Job Applications list. From there, you can
configure interview feedback fields to appear in the job application grid view.
You can use the Feedback Questionnaire category. These fields are available for this category:
• Recent Feedback Average

• Recent Feedback
• Overall Feedback Rating
If you have the privilege Manage Candidate Lists (IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS), you can
select the Manage Compound Fields action in the Manage Views page to create compounds fields for feedback
questionnaire and to display these compounds fields in the grid view.
You can use the Feedback Questionnaire category. These fields are available to create compound fields:
• Interview Feedback Questionnaire Average Score
• Interview Feedback Questionnaire Maximum Score
• Interview Feedback Questionnaire Name
• Interview Feedback Questionnaire Respondents Count
• Interview Feedback Questionnaire Respondent Name
• Interview Feedback Questionnaire Score

---

# Job Offers

## Feedback Questionnaires Filter
*Chunk ID: OHR-USE-0196 | Chapter: Job Offers | Guide: Using Recruiting*

An advanced filter called Feedback Questionnaires is available to filter the average score for a questionnaire. When you
select a questionnaire, you define the minimum and maximum scores. When you apply the filter, job applications whose
average score is between the minimum and maximum scores are displayed.
Related Topics
• What's a Grid View

14 Job Offers
Where You Can See Job Offers
There are several places where you can see job offers.

---

## Job Offers Page, in Hiring Work Area
*Chunk ID: OHR-USE-0197 | Chapter: Job Offers | Guide: Using Recruiting*

Recruiters can see job offers in My Client Groups > Hiring > Job Offers. Hiring managers can see job offers in My
Team > Hiring > Job Offers.
The Job Offers page lists job applications in the Offer phase. As soon as a job application leaves the Offer phase, it's no
longer displayed on the page.
To see job offers, recruiters and hiring managers need the privilege View Job Offer (ORC_IRC_VIEW_JOB_OFFER). They
can only see offers based on specific data security.
The Actions menu for each offer lists the most-frequently used actions that you can take for that candidate's offer. Note
that the Move action is available only to change the job application's state to Withdrawn by Candidate and Rejected by
Employer. When users click a job application, they're brought to the Offer tab of the application.

---

## Job Application's Offer Tab, in Hiring Work Area
*Chunk ID: OHR-USE-0198 | Chapter: Job Offers | Guide: Using Recruiting*

Recruiters and hiring managers can see a job offer for a specific candidate application in My Client Groups > Hiring >
Job Requisitions > Job Application.
The Offer tab becomes available as soon as the job application is moved to the Offer - Draft status.
To see the Offer tab and its content, recruiters and hiring managers need specific privileges and data security.
The Actions menu lists actions relevant to the phase and state of the job application. Only actions to which users have
access according to their privileges are displayed.

---

## Job Offers Page, from Quick Action
*Chunk ID: OHR-USE-0199 | Chapter: Job Offers | Guide: Using Recruiting*

HR specialists can see job offers in My Client Groups > Quick Actions > Manage Job Offers
The Job Offers page, reached from the Manage Job Offers quick action, lists job applications in the HR phase. If a job
application ever leaves the HR phase (by redrafting the job offer), it's no longer displayed on the page.
To view the quick action and access the Job Offers page, HR specialists need the duty role Address Job Offer
(ORA_PER_ADDRESS_JOB_OFFER_DUTY). They can only see offers based on specific data security.
The Actions menu lists actions that are appropriate for the HR specialists to perform on this offer, at this point in the
lifecycle.
When the HR specialists click a job offer, they're brought to the offer's details page.

---

## Job Offers Details Page, from Quick Action
*Chunk ID: OHR-USE-0200 | Chapter: Job Offers | Guide: Using Recruiting*

HR specialists can see a job offer for a specific candidate application in My Client Groups > Quick Actions > Manage
Job Offers > Job Offer .
When the HR specialists click a specific offer from the Job Offers page, they land on a page that contains all the details
of the offer. They don't see the candidate's full job application.
The Actions menu lists actions relevant to the state of the offer.

---

## Job Offer Life Cycle
*Chunk ID: OHR-USE-0201 | Chapter: Job Offers | Guide: Using Recruiting*

The job offer life cycle includes these main activities:
• A recruiting user decides to create a job offer for a candidate who has applied for a job. They draft the
various details of that offer, including the proposed start date, job assignment, position if any, salary, or other
compensation. This job offer can be submitted for approval, then extended to the candidate.
• The candidate gets notified that they have a job offer. They can read the offer online and consider it. The
candidate can accept the offer or decline it, either electronically with an e-signature, or by providing their
response to a user who enters the information on their behalf.
• After accepting the job offer, the candidate is moved into any configured custom phases of the selection
process, such as a background check or providing additional information like their national identifier.
• Finally, the candidate's job application is handed off to the HR specialist who finishes the work to transform
the job offer into a pending worker or a worker with a new assignment, as appropriate. The HR team performs
different tasks depending on whether the candidate is a brand new hire, a rehire coming back to the company,
or a current worker moving to a new or additional job within the company.
• After all the processing is completed, the requisition has one fewer opening, and the worker is now considered
as an internal candidate for purposes of any future recruiting.

---

## Job Application States Within the Job Offer Phase
*Chunk ID: OHR-USE-0202 | Chapter: Job Offers | Guide: Using Recruiting*

A job application goes through different states within the Job Offer phase.
The table presents the states within the Job Offer phase.

---

## State in the Job Offer Phase
*Chunk ID: OHR-USE-0203 | Chapter: Job Offers | Guide: Using Recruiting*

Description

To Be Created

No job offer exists yet.

Draft

These are states within the normal job offer path.

---

## Withdrawn by Candidate
*Chunk ID: OHR-USE-0204 | Chapter: Job Offers | Guide: Using Recruiting*

Rejected

This diagram shows the different states of a candidate job application when it goes through the job offer lifecycle.
The states that a successful candidate's job offer goes through are presented in the center of the diagram. There
are also a few states for when the job offer gets stopped in the process for some reason. The arrows going back and
forth between states show that the job offer can get redrafted if necessary at various points. The goal is to reach the
final state Accepted so that the candidate can finally get passed forward to the HR processing in the last phase of the
recruiting lifecycle. Note that it's not possible to add or remove any states from the Job Offer phase.

---

## Job Offer Actions and Privileges
*Chunk ID: OHR-USE-0205 | Chapter: Job Offers | Guide: Using Recruiting*

Users with specific privileges can perform several actions depending on the job offer state.

Action

---

## Create Offer
*Chunk ID: OHR-USE-0206 | Chapter: Job Offers | Guide: Using Recruiting*

You create a job offer to detail the proposed assignment, salary, and other details to be used if and
when the candidate accepts the offer and starts working in their new assignment.
If your tasks consist of selecting the right candidate for the requisition, drafting the job offer
completely, and sending it for approval, you need these privileges or duty roles:
• Initiate Job Offer (IRC_INITIATE_ JOB_OFFER_PRIV)

Action

Description and Privilege or Duty Role
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

## Edit Offer
*Chunk ID: OHR-USE-0207 | Chapter: Job Offers | Guide: Using Recruiting*

You edit a job offer to modify its content. The Edit Offer action is available for job offers in the Draft
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

---

## Submit Offer
*Chunk ID: OHR-USE-0208 | Chapter: Job Offers | Guide: Using Recruiting*

You submit a job offer to have it approved by approvers. The Submit Offer action is available for job
offers in the Draft state. The action is available while editing the offer.
Privileges or duty roles required for this action:
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• Update Job Offer (duty role) (ORA_IRC_UPDATE_JOB_OFFER)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)

---

## Extend Offer
*Chunk ID: OHR-USE-0209 | Chapter: Job Offers | Guide: Using Recruiting*

You use the Extend Offer action to communicate a job offer to a candidate. The Extend Offer action is
available for job offers in the Approved state.
Privileges required for this action:
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)

Action

---

## Resend Offer
*Chunk ID: OHR-USE-0210 | Chapter: Job Offers | Guide: Using Recruiting*

You use the Resend Offer action if the candidate deleted or misplaced the email that contains the
link to reach a job offer on the career site. The Resend Offer action is available for job offers in the
Extended state.
Privileges or duty roles required for this action:
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)

---

## Accept Offer
*Chunk ID: OHR-USE-0211 | Chapter: Job Offers | Guide: Using Recruiting*

You use the Accept Offer action to accept the offer on behalf of the candidate. The Accept Offer
action is available for job offers in the Extended state, or in the Approved state if the Extend state is
configured to be skipped.
Privileges required for this action:
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
To capture a negative response to an offer on behalf of a candidate, you use the Move Candidate
action.

---

## Redraft Offer
*Chunk ID: OHR-USE-0212 | Chapter: Job Offers | Guide: Using Recruiting*

You use the Redraft Offer action to revise the job offer and start the Offer phase lifecycle again. When
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

---

## Cancel Offer
*Chunk ID: OHR-USE-0213 | Chapter: Job Offers | Guide: Using Recruiting*

You can cancel a job offer for a candidate when the offer is rejected by the employer or the candidate
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
*Chunk ID: OHR-USE-0214 | Chapter: Job Offers | Guide: Using Recruiting*

You use the Preview Offer action to see how the job offer letter appears to the candidate.

Action

Description and Privilege or Duty Role
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
*Chunk ID: OHR-USE-0215 | Chapter: Job Offers | Guide: Using Recruiting*

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

## Move to HR
*Chunk ID: OHR-USE-0216 | Chapter: Job Offers | Guide: Using Recruiting*

The Move to HR action is available for job offers in the Accepted state and in any subsequent
custom phase that may be configured after the Offer phase. The action is always shown for external
candidates. If a custom phase is configured after the Offer phase and before the HR phase:
• The Move action will move the candidate forward into a state in that custom phase.
• The Move to HR action will skip the custom phase and go directly to the HR phase.
To perform the Move to HR action, you need this privilege:
• Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV)

---

## Delete Job Application
*Chunk ID: OHR-USE-0217 | Chapter: Job Offers | Guide: Using Recruiting*

The Delete Job Application action is available for job offers in the Withdrawn by Candidate or Rejected
states.
Privilege required for this action:
• Delete Candidate Job Application (IRC_DELETE_JOB_APPLICATION_PRIV)
• View Candidate Job Application (ORA_IRC_VIEW_CANDIDATE_JOB_APPLICATION or ORA_IRC_
VIEW_NON_RESTRICTED_CANDIDATE_JOB_APPLICATION)

---

## View Duplicates
*Chunk ID: OHR-USE-0218 | Chapter: Job Offers | Guide: Using Recruiting*

When the duplicate check is configured during the Move to HR and when one or more duplicates have
been identified, the View Duplicates action brings you to the list of possible duplicates. You don't need
any additional privilege to see this action.

---

## Job Offer Creation Process
*Chunk ID: OHR-USE-0219 | Chapter: Job Offers | Guide: Using Recruiting*

There are two scenarios that you can use to create job offers. You'll have access to these scenarios depending on your
privileges and roles.
There are two scenarios that you can use to create job offers, depending on your privileges and roles.
• Shared process: The creation of the job offer is shared between two roles, usually configured to be the
hiring manager and the recruiter. In this scenario, the hiring manager has the privilege Initiate Job Offer
(IRC_INITIATE_JOB_OFFER_PRIV). The hiring manager uses the Create Offer action to move a candidate's job
application into the Offer - Draft status. The hiring manager can communicate any intentions or notes to the
recruiter and Offer Team using the Comment field. The hiring manager doesn't provide any other information
for this offer. Then the recruiter receives a notification to enter details about this candidate's job offer using the
Edit Offer action. All appropriate offer sections are displayed and the recruiter can provide necessary values
and also can see any comment provided by the hiring manager. The recruiter submits the offer for approval, or
can save the offer to edit it later, then submit it.
• Recruiter process: The creation of the job offer is handled by a single user, usually configured to be the
recruiter. In this scenario, the recruiter has the Initiate Job Offer (IRC_INITIATE_JOB_OFFER_PRIV) and Update
Job Offer (ORA_IRC_UPDATE_JOB_OFFER) privileges. The recruiter uses the Create Offer action to move a
candidate's job application into the Offer - Draft status. All appropriate sections and fields of the offer are
available to be filled. When the recruiter has filled all necessary values, the recruiter submits the offer for any
approval, or can save the offer to edit it later (or another user can return later) using the Edit Offer action. In this
scenario, there's no need for a Comment field because the process is done by a single user.

---

## Create a Job Offer
*Chunk ID: OHR-USE-0220 | Chapter: Job Offers | Guide: Using Recruiting*

You create a job offer to detail the proposed assignment, salary, and other details to be used when the candidate
accepts the offer and starts working in their new assignment.
1. Open a job application.
2. In the Actions menu, select Create Job Offer.
3. On the Create Job Offer page, select the sections of the job offer you want to work on and click Continue.
Note: Required sections don't appear as sections you can select.
4. Enter details about the job offer by navigating to each section of the job offer.
If you have the privilege Update Candidate Job Offer Letter (IRC_UPDATE_CANDIDATE_JOB_OFFER_LETTER), you
have the choice of using an offer letter template or uploading an offer letter that you can personalize.
5. When you're done entering all the details of the job offer, click Submit to submit the job offer for approval.
You can create a job offer and save it as Draft without selecting an offer letter. But an offer letter must be selected
before you can submit the job offer for approval, unless the offer lifecycle is configured in the requisition's candidate
selection process to bypass the Offer Extended state.
Results:
The candidate's job application is moved to the Offer - Draft status. The job offer has the same name as the job
requisition title. If the job requisition title is changed after the job offer is created, the job offer name won't automatically

be updated with this change, it will remain with the name it had at the time of creation. The job offer will need to be
recreated to adopt any change to the job requisition title.
Related Topics
• Sections and Fields in the Job Offer

---

## Sections and Fields in the Job Offer
*Chunk ID: OHR-USE-0221 | Chapter: Job Offers | Guide: Using Recruiting*

Below are the sections and fields that can appear in a job offer. These are configurable by your administrator and can be
displayed or hidden.
On the Create Job Offer page, you can select the sections of the job offer you want to work on right now. Required
sections don't appear as an option.
Note: When you create a job offer, the job offer will adopt the same name as the job requisition title. If the job
requisition title is changed after the job offer is created, the job offer name won't automatically be updated with this
change, it will remain with the name it had at the time of creation. The job offer will need to be recreated to adopt any
change to the job requisition title.

When and Why
The When and Why section and all its fields are required. Here's some important information about fields in the When
and Why section.

Field

---

## Information to Consider
*Chunk ID: OHR-USE-0222 | Chapter: Job Offers | Guide: Using Recruiting*

When is the employee start date?

This is the projected day that the candidate would begin work in the new assignment. By default, this
required field displays the current date. You can select a date in the future or in the past, although not
earlier than the date when the candidate was first entered in the database.
The value you select for the start date has an impact on the values available in the Action field
depending on whether the candidate has any other active work relationships with the company which
are starting or ending in the future. For instance, consider a worker whose current assignment ends
next month. If the current job offer's start date is after that termination date, the job offer represents a
rehire. If the current job offer's start date is before that termination date, it likely represents a transfer
or perhaps a second concurrent assignment.

---

## Legal Employer
*Chunk ID: OHR-USE-0223 | Chapter: Job Offers | Guide: Using Recruiting*

This is the legal employer for the candidate's new assignment. By default, this required field displays
the value of the requisition's Legal Employer field if any, which is shown on the Details tab, in the Offer
Info section.
The value you select in the Legal Employer field has an impact on the fields and sections shown in the
rest of the offer page. For instance, certain legal employers are configured to use Contracts. In that
case, a Contracts section is displayed when one of these legal employers is selected.
When you come back to edit an offer that was previously drafted, if a new legal employer is selected,
already-saved values in the Assignment section get removed. This is done to ensure that all values can
coexist correctly, and that all necessary fields are displayed for the new legal employer.

Field

---

## Worker Type
*Chunk ID: OHR-USE-0224 | Chapter: Job Offers | Guide: Using Recruiting*

This is the type of worker which the candidate's new assignment will be. By default, this required field
displays the value of the requisition's Worker Type, which is shown on the Details tab, in the Offer Info
section.
Two worker types are available: Employee and Contingent. The value you select in the Worker Type
field has an impact on the values available on the page if the candidate has any other active work
relationships with the company. For instance, if the candidate is already a contingent worker in a given
legal employer, a job offer for another job as a contingent worker in the same legal employer would be
an additional assignment. On the other hand, if the new job offer was as an employee in the same legal
employer, the offer would ultimately have to create a new work relationship for this person.

Action

This is the action used after the candidate accepts this offer, when the HR team processes the offer
to become the worker's new assignment. The value of this required field can be selected from the list,
which will display relevant choices after the fields Start Date, Legal Employer, and Worker Type are
completed. The values selected in those fields have an impact on this list of available actions.
Available values in this field include options that are appropriate for external candidates such as
Add Pending Worker, or options appropriate for internal mobility candidates such as Global Transfer,
Temporary Assignment, Promotion.
For details, see Actions Available Based on Employment Scenarios.

---

## Assignment Info
*Chunk ID: OHR-USE-0225 | Chapter: Job Offers | Guide: Using Recruiting*

The Assignment Info section is required. It provides information about a person's role such as business unit, job,
grade, location, any position, and any flexfields on the assignment. If the candidate successfully reaches the end of the
recruiting lifecycle, this will become their assignment for their new job.
If you select a position, many of the fields in the Assignment Info section get their initial values from the selected
position. If you don't select a position, many of the fields in the Assignment Info section get their initial values from the
job requisition. If the requisition has a position, the offer's Position field will have the same value as the requisition. You
can change the position if needed. For details, see Create a Job Offer Based on a Position.
If you select a grade or grade ladder with or without a step, then the associated salary will get prefilled by default in the
Salary section of the job offer.
If any flexfields have been defined for Assignments and configured to appear when creating and editing job offers,
these will be displayed in this section. If and when this candidate successfully reaches the HR phase and starts their new
job, the values in these offer assignment flexfields will be transferred into the worker's new assignment.
To modify assignment info, you need this duty role:
• Update Job Offer (ORA_IRC_UPDATE_JOB_OFFER)
Note: When searching for items to put into the offer fields, you can choose among items that are available as of the
beginning of the offer. Locations, departments, or other things that are associated with offers can have effective dates
that govern when they became active and when they will become inactive. For most offers, in which the candidate's
proposed start date is the same date as when the offer is first drafted or later, the lists of these associated items will
include only those which were active as of that drafting date. Items that only became available later, for example by
the offer's proposed start date, will not be shown; instead the visible items that you can choose are those which are
active as of the offer assignment's initial creation in Draft. For the unusual situation of offers whose proposed start
date is earlier than when the offer is first drafted, the list of these associated items will include those which were
already active as of that proposed start date.

---

## Offer Team
*Chunk ID: OHR-USE-0226 | Chapter: Job Offers | Guide: Using Recruiting*

The Offer Team section is required. It displays the list of users who can access the job offer if they have the necessary
privileges. If the offer proceeds all the way through a successful hiring cycle, the hiring manager listed in the Offer Team
will become the direct manager or line manager of the candidate.
The Offer Team is composed of the hiring manager, the recruiter, and collaborators of any type. When you create a
job offer, the hiring manager, recruiter, and collaborators of the job requisition's Hiring Team are copied into the Offer
Team. The hiring manager and the recruiter are the required members of the Offer Team. You can replace them. You can
also replace, remove, or add any collaborators. When selecting users for this section, you can see all the assignments for
that person.
Note: Changes made to the requisition's Hiring Team after the creation of the offer aren't reflected in the Offer Team.
To view job offer details within the Hiring pages, you need to:
• Be named on the Offer Team or be in the hierarchy above someone on that team, or have the duty role Manage
Job Offer by Recruiting Manager (ORA_IRC_MANAGE_JOB_OFFER_BY_RECRUITING_MANAGER).
• Have the View Job Offer (ORA_IRC_VIEW_JOB_OFFER) duty role.
• Optional: Have the View Job Offer Salary (ORA_IRC_VIEW_JOB_OFFER_SALARY) and View Job Offer Other
Compensation (ORA_IRC_VIEW_JOB_OFFER_OTHER_COMPENSATION) duty roles.
• Have the proper data security to view persons and assignments in the given area of your organizations.
To replace, add, and remove people listed on the Offer Team, you need this duty role:
• Update Job Offer (ORA_IRC_UPDATE_JOB_OFFER)

Payroll
The Payroll section is displayed by default for offers to internal candidates (employees). For external candidate offers,
your administrator might have displayed it as well. The Payroll section is supported in these flows:
• Create Work Relationship
• Local and Global Transfer
• Add Assignment
• Change Assignment
When an offer is made to an internal candidate, the offer details are transferred to the employee new work relationship
once the record is moved to HR. After the offer info is copied to an internal candidate, the HR specialist can review the
details on the Manage Job Offers page.

Salary
The Salary section provides information about salary such as salary basis, salary amount, annual salary. An offer can be
created and saved in the state Draft without a salary, but for external candidates it can't be submitted to approvers nor
extended to candidates if the salary has not been determined.
To view and update salary details, you need these duty roles:
• View Job Offer (ORA_IRC_VIEW_JOB_OFFER)

• Update Job Offer (ORA_IRC_UPDATE_JOB_OFFER)
• View Job Offer Salary (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• Update Job Offer Salary (ORA_IRC_UPDATE_JOB_OFFER_SALARY)
Here's some important information about fields in the Salary section.

Field

---

## Salary Basis
*Chunk ID: OHR-USE-0227 | Chapter: Job Offers | Guide: Using Recruiting*

The salary basis determines the period in which salary is expressed and the currency of the salary for
this job offer. You're only shown salary bases available within the legal employer (LDG) that's selected
in the Assignment Info section. Regardless of the offer's proposed start date, you're shown all salary
bases that are active as of the current date.
The element associated with the salary basis must be configured to have open eligibility. Any eligibility
limitations on the salary basis's elements may prevent smooth hiring of the candidate after they accept
the job offer.
If the salary basis frequency is specified as "Payroll Period" then you'll need to select a payroll for this
offer. By default the Payroll Info section is hidden, but it must be displayed and filled to finish drafting
the job offer. Offers for external hires and rehires can specify payroll information, but offers for internal
candidates should not include this section.
For more information, see Configuring Payroll Elements for Use in Oracle Compensation Cloud on My
Oracle Support (Doc ID 1589502.1).

---

## Salary Amount
*Chunk ID: OHR-USE-0228 | Chapter: Job Offers | Guide: Using Recruiting*

When you have selected a salary basis, you can enter the amount of salary the candidate will get.
The currency (a three-letter code) and frequency selected as part of the salary basis are displayed.
Example: USD monthly.
Job offers include any compensation zone based salary range differentials that are configured. Based
on the work location selected above in the candidate's Assignment Info section and the salary basis
selected here, their appropriate compensation zone is identified and appropriate differential gets
applied. The salary range and analytical values such as compa-ratio are recalculated considering the
compensation zone differential. This information can be the basis of offer approval rules, and is also
included in notifications sent to offer approvers.
The salary ranges will be shown as of the offer’s proposed start date. When the default salary amount
is integrated with GSP ladder, the amount will be defaulted as of the offer’s proposed start date. If
you're using salary rate components based on payroll rates, these will be based on the date when the
offer assignment was initially created.
For more information, see Salary Range Differentials and Compensation Zones on My Oracle Support
(Doc ID 2605772.1).

---

## New Salary
*Chunk ID: OHR-USE-0229 | Chapter: Job Offers | Guide: Using Recruiting*

This area appears once you have entered the salary amount. The salary amount is displayed in a
graphical way. If there is a configured Minimum and Maximum, this information may also be displayed
graphically here.

---

## Other Compensation
*Chunk ID: OHR-USE-0230 | Chapter: Job Offers | Guide: Using Recruiting*

Eligible individual compensation plans are displayed based on the values that have already been selected in this offer.
After you select the Plan and Option values, many other relevant fields are displayed to complete the compensation for
this offer.

To view and modify the Other Compensation section, you need these duty roles:
• View Job Offer (ORA_IRC_VIEW_JOB_OFFER)
• Update Job Offer (ORA_IRC_UPDATE_JOB_OFFER)
• View Job Offer Other Compensation (ORA_IRC_VIEW_JOB_OFFER_OTHER_COMPENSATION)
• Update Job Offer Other Compensation (ORA_IRC_UPDATE_JOB_OFFER_OTHER_COMPENSATION)
Regardless of the offer's proposed start date, you're shown all the individual compensation plans (that are active as
of the current date) for which this candidate's assignment is eligible, and all their eligible options. When you select
any individual compensation plans for this candidate's assignment, the plan start dates can be defaulted to the offer's
proposed start date, or defaulted to some preconfigured number of days after the candidate will start their new
assignment. If you later need to revise the offer’s start date, these defaulted individual compensation plan dates will
automatically get revised in tandem with the new proposed start date.
Depending on the configuration, you may be able to change the individual compensation plans’ default dates. If
you do, be aware that any future changes to the offer’s start date will no longer cause automatic adjustments to the
compensation plans’ dates. If you want, you can manually change the dates as needed, or you can delete the incorrect
individual compensation plan and add it again with the correct date.

---

## Comments and Attachments
*Chunk ID: OHR-USE-0231 | Chapter: Job Offers | Guide: Using Recruiting*

You can provide free-text comments and add attachments while drafting or editing job offers. These are visible to
internal users and approvers, but not to candidates. You can select files and links to associate them with the offer.
Internal documents are those attachments intended for internal viewers. These files and links are visible to all users
including the hiring manager, the offer team, and any approvers who will review the offer. These attachments aren't
shared with candidates.

---

## Additional Info
*Chunk ID: OHR-USE-0232 | Chapter: Job Offers | Guide: Using Recruiting*

These are flexfields that can be configured on the offer, in addition to those which can be configured for the assignment
to show in the Assignment Info section above.
Offer Assignment flexfields are transferred over into the worker's new assignment when the hiring process is successful.
Offer flexfields are intended for recruiting purposes and aren't available in the worker's new assignment.

---

## Offer Letter
*Chunk ID: OHR-USE-0233 | Chapter: Job Offers | Guide: Using Recruiting*

The offer letter is a formal written document given by an employer to a candidate. The letter confirms details of the job
offer such as the job title, proposed start date, work location, salary, or other compensation.
Here's some important information about fields in the Offer Letter section.

Field

---

## Offer Letter
*Chunk ID: OHR-USE-0234 | Chapter: Job Offers | Guide: Using Recruiting*

This is where you select the offer letter template, which merges the candidate's specific information
with the standard formatting and text to create a formal document that will display to the candidate
when the offer gets extended. Offer letter templates help to meet business requirements and legal
compliance requirements while maintaining consistent offer letter and business image.
There might be a choice of templates for selection depending on how many your company has
configured to meet its needs. You may see certain letters while drafting offers for external candidates,
and other letters only while drafting offers for internal candidates. For contingent workers' offers,

Field

Information to Consider
the choice of letters will vary depending on whether these people are configured to be considered as
external or internal candidates.
If you have the privilege Update Candidate Job Offer Letter (IRC_UPDATE_CANDIDATE_JOB_OFFER_
LETTER), you have the choice of using an offer letter template or uploading an offer letter that you can
personalize.

---

## Candidate Job Application Language
*Chunk ID: OHR-USE-0235 | Chapter: Job Offers | Guide: Using Recruiting*

This is a read-only field indicating the language used by the candidate when applying for the job. This
information helps you use the appropriate language for the Additional Text fields and for adjusting the
offer letter, so that the candidate can read and understand the text.

---

## Expiration Date
*Chunk ID: OHR-USE-0236 | Chapter: Job Offers | Guide: Using Recruiting*

This optional field is the date when a response from the candidate is expected. If the job offer is still
in the Offer - Extended status when the expiration date is reached, both you and the candidate can
receive a notification. The candidate has the opportunity to respond to the job offer. If the candidate
doesn't respond, you can for example reject the candidate. No other actions happen automatically
when the expiration date arrives.

---

## Additional Text 1 and Additional Text 2
*Chunk ID: OHR-USE-0237 | Chapter: Job Offers | Guide: Using Recruiting*

You can use these fields to add any personal touches into the standard offer letter. The content
appears within the job offer letter, as long as the selected job offer letter template was configured to
display these two fields.
The text you enter in these two fields appears in their own paragraphs when the offer letter template is
displayed to the candidate. A short amount of text can be displayed inline within an existing paragraph
of the template, as long as the text you enter into each of these fields is a single line and doesn't use
the Enter key.

---

## Candidate-facing Documents
*Chunk ID: OHR-USE-0238 | Chapter: Job Offers | Guide: Using Recruiting*

Candidate-facing documents are files and links displayed to the candidate at the bottom of their online
job offer. Candidates can read, save, and print them. When each successful job application is moved to
the HR phase, these attachments are copied into the person's Document Records. They can be found
in the document type Recruiting, alongside any attachments that candidates provided as they applied
to the job except their resume. Note that the resume goes into the candidate's Talent Profile and not in
the Document Records.

---

## Actions Available Based on Employment Scenarios
*Chunk ID: OHR-USE-0239 | Chapter: Job Offers | Guide: Using Recruiting*

When you create a job offer, you select the appropriate human resource (HR) action. The list of actions is narrowed
down, showing only the limited set of actions that are appropriate for the candidate based on the info available in the
job offer and the candidate's existing work relationship.
Then, when the candidate moves into the final HR phase, the candidate is put into the hands of the HR specialists. As
soon as the candidate job application enters the HR phase, it becomes visible on the HR specialist's list on their Job
Offers page, from the Manage Job Offers quick action. It's the HR specialist responsibility to perform that preselected
HR action to create the appropriate records for the candidate to become a worker in the promised job.
This table describes six employment scenarios and the available actions that the HR specialists can perform for each
scenario.

Scenario

---

## Global Change: The person has only one
*Chunk ID: OHR-USE-0240 | Chapter: Job Offers | Guide: Using Recruiting*

active work relationship with the same
worker type as the job offer. However, the
legal employer of the work relationship
and the job offer are different.

---

## Local Change: The person has one active
*Chunk ID: OHR-USE-0241 | Chapter: Job Offers | Guide: Using Recruiting*

work relationship with the same worker
type and legal employer as the job offer.

---

## Add Assignment
*Chunk ID: OHR-USE-0242 | Chapter: Job Offers | Guide: Using Recruiting*

Assignment Change
Job Change
Position Change
Promotion
Temporary Assignment
Transfer

---

## Change Worker Type: The person has one
*Chunk ID: OHR-USE-0243 | Chapter: Job Offers | Guide: Using Recruiting*

or more active assignments in the same
work relationship. However, the worker
type of the work relationship and the job
offer are different.

---

## Other: The person may already have more Add Assignment
*Chunk ID: OHR-USE-0244 | Chapter: Job Offers | Guide: Using Recruiting*

than one active assignment besides this
job offer, or is in another complex situation Add Contingent Work Relationship
that isn't covered by any above scenario.
Add Employee Work Relationship
Assignment Change
Global Temporary Assignment
Global Transfer
Job Change
Position Change
Promotion
Transfer
When it's time for the HR specialists to perform this preselected action for the candidate whose offer is
in this scenario, more complex processing steps will be required. See Complex Job Offers: How They're
Processed.

Scenario

Actions to Process the Job Offer

---

## Create a Job Offer Based on a Position
*Chunk ID: OHR-USE-0245 | Chapter: Job Offers | Guide: Using Recruiting*

When you create a job offer for a candidate, you can select a position in the Assignment Info section to tie the offer to a
specific position. The offer's Assignment Info section gets field values from the selected position.
When you create a job offer based on a position, it ensures that the organization has planned to have a place for the
worker in the workforce.
The position can either come from the offer's job requisition or directly on the offer.
• If the job offer is created from a job requisition that has a position, the job offer's Position field is required. The
job requisition's position is defaulted into the job offer's Position field. But you can change the value for this
specific job offer.
• If the job requisition doesn't have a position, the Position field in the job offer is optional.
When you search for a position for an offer, you can choose among positions that are available as of the beginning of
the offer. Positions have effective dates that govern when they became active and when they will become inactive. For
most offers, where the candidate's proposed start date is the same date as when the offer is first drafted or later, the list
of available positions will be those which were active as of that drafting date. Positions that only become active later,
for example as of the offer's proposed start date, won't be shown; instead the visible positions that you can choose are
those which are active as of the offer assignment's initial creation in Draft. For the unusual situation of offers where
the proposed start date is earlier than when the offer is first drafted, the positions displayed will be those which were
already active as of that proposed start date.
Here's the list of field values that appear in the offer from the associated position. If the selected position has a value
in these fields, that value gets copied to the offer. If the position's value is null for any of these fields, the offer gets the
value in the requisition.
• Manager
• Department
• Job
• Location
• Grade Ladder
• Grade
• Probation Period
• Full Time vs. Part Time
• Regular vs. Temporary
• Assignment Category
• Working Hours (needed to calculate offer's FTE)
• Start Time and End Time
• Union, Bargaining Unit, and Collective Agreement

• Mapped flexfields. Each flexfield on a position can be configured to associate with a flexfield on assignment.
These values will be copied here.
If your company has configured the system-wide setting to respect the hiring status of positions, then you can only
select a position that you can access and that has the Approved hiring status as of the offer's start date. There's no way
to expand the list of available positions to those with other hiring status values such as Draft or Frozen.
Even after an approved position has been selected, its hiring status value is checked at the same three points in the
lifecycle where position's headcount is already checked. When you try to take any of these three actions, if the selected
position's hiring status value is no longer Approved as of the offer's start date, the action won't succeed:
• When submitting a job offer for approval, the offer will remain in Draft state.
• When extending a job offer to the candidate, the offer will remain in Approved state.
• When using the Move to HR action, the offer will move to the HR phase but in the state Error During Processing.

---

## Position Synchronization
*Chunk ID: OHR-USE-0246 | Chapter: Job Offers | Guide: Using Recruiting*

You can change the offer values that came from the position, depending on how position synchronization is configured
by your administrator.
• If position synchronization isn't enabled, the position's values are prefilled into some offer's fields in the
Assignment Info section by default. You can change the values.
• If position synchronization is enabled and various fields on the position are configured to be sync, then these
fields appear as read-only in the job offer's Assignment Info section. You can't change their values on the job
offer. This ensures that the values stay in sync with the values of the position. However, if your administrator
has configured to allow individual assignments to override their positions, this job offer will display an option
to make these fields editable and you'll be able to change the values. If the remaining fields aren't configured to
be sync, then these fields appear as default values in the job offer. You can change these default values in the
offer's Assignment section to diverge from the position's starting point.

---

## Changes to Sync Position Values
*Chunk ID: OHR-USE-0247 | Chapter: Job Offers | Guide: Using Recruiting*

When changes are made to a position's field values that are sync with a job offer's assignment, the offer assignment's
values can be updated at many points in the candidate's lifecycle.
• If the position's values are updated in fields for which position synchronization isn't enabled, this will never
cause an update of the candidate's offer assignment fields.
• If the position's values are updated in fields for which position synchronization is enabled, the candidate's offer
will be automatically updated as long as the offer isn't yet communicated to the candidate. This means that
the relevant fields in the offer assignment will be changed while in the states Draft, Pending Approval, and
Approved within the Offer phase. Note that the position's changed values must be date-effective starting when
the offer was created.
• If the position is updated after the candidate might have seen their job offer, no changes to the offer fields can
occur. This means the offer assignment's values remain unchanged regardless of position updates while the
job application is in the state Offer - Extended or any subsequent active state. This includes the Offer phase's
states Extended and Accepted, and any active states in the HR phase or other custom phase that might be
configured. Because the position now has slightly different values than the job offer, the HR specialist might
have to reconcile any differences later after the candidate is moved to the HR phase.
• If the position's values are updated after the job application is no longer active, no changes to the offer fields
occur. This means the values in the offer's Assignment Info section remain unchanged while in the states
Approval Rejected, Withdrawn by Candidate, or Rejected within the Offer phase, or any state in any phase
beyond that. However, if the job offer is redrafted, any synced fields will automatically be updated to match the

position's changed values when the offer is once again in the state Draft, as long as the position's changes are
date-effective starting when the offer was created.

---

## Behavior of the Hiring Manager Field on the Job Offer View and Edit
*Chunk ID: OHR-USE-0248 | Chapter: Job Offers | Guide: Using Recruiting*

Modes
Here are explanations on the behavior of the Hiring Manager field on the job offer in view and edit modes when the
incumbent on the Parent Position becomes inactive after initiating the job offer and Position Sync is on.
• The Hiring Manager field value on the job offer is pulled from the incumbent on the Parent Position of the
position used in the job offer as of the offer creation date or proposed start date (whichever date comes first).
Let's say a user creates a job offer on 1/1/2024. The Hiring Manager field of the job offer will be populated with
whoever is the incumbent on the Parent Position of the position on 1/1/2024. For example, the incumbent value
is John Palmer. Later, if John Palmer is terminated on 1/5/2024, the Hiring Manager field value on the job offer
will be John Palmer even if the proposed start date of the job offer is in the future.
• When a user edits the job offer, the Hiring Manager field value will still be John Palmer. However, the user will
see the assignment ID of John Palmer’s assignment record in edit mode as the assignment is terminated. The
user won't be able to submit the job offer when the Hiring Manager field value has an inactive record. In this
case, users with appropriate admin privileges will be able to change the Hiring Manager value using HDL only.
Let's say they change the value to Carla Johnson.
• Now, when a user looks at the Hiring Manager value in the job offer view mode, they'll see the updated value
of Carla Johnson. However, if this user tries to edit the offer again (2nd time), they'll see John Palmer in the
Hiring Manager field, because Position sync will trigger every time the user tries to edit the job offer and it will
pull the value of incumbent of the incumbent on the Parent Position of the position as of the offer creation date
(1/1/2024).

---

## Create Job Offers by Copying Another Candidate's Offer
*Chunk ID: OHR-USE-0249 | Chapter: Job Offers | Guide: Using Recruiting*

You can quickly create job offers for one or more external candidates by copying another candidate's offer within that
same requisition.
If you have the privilege Copy Job Offer (IRC_COPY_JOB_OFFER), you can go into any job requisition, select one or
multiple external candidates who don’t yet have a job offer, and select the Copy Offer action.
Note: The only person types you can select are external candidates, including new hires and rehires. Current
employees and current contingent workers usually need more tailored job offers, so these internal workers can’t be
selected to receive a copied offer from a prior external candidate’s offer. If you do select these current employees or
contingent workers, they will be omitted from the list of people intended to receive a copy of the selected offer.
On the Copy Offer page, you select an external candidate on this requisition who has a job offer in any state. When you
select the person’s offer to copy, you can see its current state, so you can be sure to select an offer that’s in a state that
you want, for instance one that’s in the state Approved, Accepted, or HR - Processed. You can select an offer to copy
even if it’s in the state of Draft, Approval Rejected, or Rejected by Candidate. An offer that was approved but rejected
by one candidate might be perfectly acceptable to other candidates. All of the content and attachments on their offer
will be copied to create new job offers for the other selected candidates. It’s preferable to select a recent offer because
it contains active values. Older offers on this requisition may no longer be selectable, or if they have values that aren’t
current anymore then the copying will be unsuccessful.

Before you submit the Copy Offer action, you can decide what should happen next for all of the new offers that get
successfully drafted.
• You can submit new offers for approval. If you select this default option, all the newly-created offers will be
immediately submitted directly into the approval cycle. They will move from the phase and state in which they
started, into the status Offer - Pending Approval. This option is helpful to reduce clicks, if you won't need to edit
each newly-created offer before sending it to any approvers.
• You can leave the new offers in the Draft state to edit them. If you select this option, all the newly-created offers
will remain editable in case any changes need to be made to each one. They will move from the phase and state
in which they started, into the status Offer - Draft. This is helpful for using the original offer as a starting point,
if you know that each individual candidate will need to be adjusted.

---

## What Happens After Submitting the Batch Copy Offer Process
*Chunk ID: OHR-USE-0250 | Chapter: Job Offers | Guide: Using Recruiting*

When you submit the Copy Offer action, here's what can happen:
• If the batch copy offer process is successful, all of the offer content and attachments on the offer are copied to
create job offers for the selected candidates.
• If there are warnings, the new offers still get copied.
• If there are errors, the batch copy offer process stops.
The table presents possible warnings and errors that can occur during the batch copy offer process.

---

## Warning or Error
*Chunk ID: OHR-USE-0251 | Chapter: Job Offers | Guide: Using Recruiting*

Scenario

Warning

The original offer letter was adjusted to include specific info about the candidate. You'll see a warning
message asking you to update each new candidate's offer letter after it gets copied. Copies will then be
created.

Error

The recruiter or hiring manager on the original offer is no longer working for the company. The
batch copy offer process can't proceed. You'll see an error message asking you to select a different
candidate's offer to be copied.

Error

The original offer has no salary amount or no offer letter, or the job requisition doesn't have enough
openings left to accommodate all of the candidates selected and you don't have the privilege
Communicate Job Offer Ignoring Number of Openings (IRC_COMMUNICATE_JOB_OFFER_IGNORING_
NUMBER_OF_OPENINGS).

In case of any failure, the selected candidates will likely have a partially-created offer but you'll have to check the Errors
section for each candidate's offer to see which regions' fields were unable to be copied. For example:
• The Assignment section may not be filled out for all the new candidates if the original offer's assignment had a
location or grade that's currently inactive.
• The Other Compensation section may be empty for all the new candidates if they don't satisfy the eligibility
profile or element eligibility for the original offer's Individual Compensation Plan.
These incomplete new offers will remain in the status Offer - Draft so that the missing values can be manually provided
as needed, even if the option selected when copying the offer was Submit new offers for approval. When each offer is
edited to be complete, you can submit them individually for approval.

As soon as the batch copy offer process is finished, you may receive a notification if this was configured by your
administrator. The notification indicates the number of offers that were successfully copied as well as the number of
offers that failed, were skipped, or canceled.

---

## Copied Offers Move Forward in the Lifecycle
*Chunk ID: OHR-USE-0252 | Chapter: Job Offers | Guide: Using Recruiting*

Depending on your administrator's configuration, all the job applications with copied offers can be automatically moved
forward quickly through various points in the candidate selection process. Offer approval can be bypassed and other
moves through the lifecycle can be automated, if desired. Or if these quick configurations aren't implemented, these
copied job offers will act like all other job applications which your users individually approve, extend, and move into the
HR phase when each candidate is ready.

---

## Copy a Job Offer
*Chunk ID: OHR-USE-0253 | Chapter: Job Offers | Guide: Using Recruiting*

You can quickly create job offers for one or more external candidates by copying another candidate's offer within that
same requisition.
Before you start
• You need the privilege Copy Job Offer (IRC_COPY_JOB_OFFER).
• You also need the duty role Use REST Service - Job Offers List of Values
(IRC_REST_SERVICE_ACCESS_JOB_OFFERS_LOV)to see the list of offers in the Offer to Copy from Candidate
field.
Here's what to do
1. Open a job requisition and go to the list of job applications.
2. Select one or multiple external candidates who don’t yet have a job offer.
3. Select the Copy Offer action.
4. On the Copy Offer page, select an external candidate on this requisition who has a job offer in any state.
5. In the Offer to Copy from Candidate field, select an offer.
6. In the Start Date of New Offers field, you can choose a projected start date for all the new offers that's different than
the original offer's start date.
Except for this, the fields in the new offers will have all the same values as the original offer.
7. In the Name of Batch Offer Process field, you can use the default name for the batch offer process which includes the
requisition number and the current date and time. Or you can set a new one.
This name is useful for tracking all of these newly-copied offers on the Job Offers list.
8. You can decide what should happen next for all of the new offers that get successfully drafted.
◦ Submit new offers for approval: This option is helpful if you won't need to edit each newly-created offer
before sending it to approvers.
◦ Stay in draft state to edit new offers: This option is helpful for using the original offer as a starting point, if
you know that each individual candidate will need to be adjusted.
9. Click Submit.

---

## Adjust a Job Offer Letter
*Chunk ID: OHR-USE-0254 | Chapter: Job Offers | Guide: Using Recruiting*

You can create consistent offer letters based on templates, and then you can personalize them for individual situations
as needed. For instance, certain kinds of hiring require unique wording or agreements, such as offers for an executive
position or a hard-to-recruit job.
Before you start
• The offer's state must be Draft.
• You need the privilege Update Candidate Job Offer Letter (IRC_UPDATE_CANDIDATE_JOB_OFFER_LETTER).
Here's what to do
1.
2.
3.
4.

---

## Select an Offer Letter Template
*Chunk ID: OHR-USE-0255 | Chapter: Job Offers | Guide: Using Recruiting*

Download the Offer Letter
Make Adjustments to the Offer Letter
Upload and Use the Adjusted Offer Letter

---

## Select an Offer Letter Template
*Chunk ID: OHR-USE-0256 | Chapter: Job Offers | Guide: Using Recruiting*

When you're creating or editing a job offer, in the Offer Letter section, you select a template in the Offer Letter field.
There might be a choice of templates for selection depending on how many your organization has configured to meet
their needs.

---

## Download the Offer Letter
*Chunk ID: OHR-USE-0257 | Chapter: Job Offers | Guide: Using Recruiting*

If you have the privilege Update Candidate Job Offer Letter (IRC_UPDATE_CANDIDATE_JOB_OFFER_LETTER), you can
download the selected offer letter template and use it as a starting point to adjust and create this candidate's offer letter.
The template is an .rtf file. You can use Microsoft Word or any text editor to open it.

---

## Make Adjustments to the Offer Letter
*Chunk ID: OHR-USE-0258 | Chapter: Job Offers | Guide: Using Recruiting*

Your organization can choose one of two methods to adjust offer letters:
• Offer letter with all tokens (original method)
• Offer letter with resolved tokens
Offer letter with all tokens (original method): If your administrator didn't enable the option Download Offer Letter
with Resolved Token, then you're using the original method. When you open the downloaded offer letter, you'll see
tokens that represent the various field values for that candidate, and all the conditional sections that may or may not
end up being relevant to this candidate's situation.
You make changes starting from the letter with all its tokens. These tokens will be replaced with the current values in the
offer fields about this candidate, whenever a user or approver or the candidate views the offer letter after it's drafted.
Some sections of the letter won't be shown to other users or approvers or the candidate because they're conditional,
that is, they're dependent on specific values that might not end up being relevant to the given candidate. Also, because
there isn't anything yet entered into the Acceptance and E-signature fields, that e-signature conditional section at
the bottom of the template is full of tokens that will be resolved later. They will be resolved if and when this offer gets
accepted by the candidate.

You may see token codes like the letter "C" at the beginning of sentences or sections, and the letters "EC" at the
end. These represent conditions, indicating that the enclosed text may or may not display to this specific candidate,
depending on the values in their offer.
If you remove any tokens while you're adjusting this offer letter, the letter will no longer include the corresponding value
from that candidate's offer. For instance, if the offer letter template includes the token "START_DATE", you may want to
remove it and replace it by typing in the specific date when you expect the candidate to arrive for their first day of work.
However, later you may need to select a new start date in the Assignment section of the Edit Offer flow. In this case, this
new value won't be represented in the offer letter anymore; only the date which you typed into the text will continue to
be shown. You can revise the .rtf version of that offer letter again to type in the new start date.
Any changes made to this offer letter in this candidate's offer won't affect any other candidates or any other job
applications.
Offer letter with resolved tokens: Your administrator needs to enable the option Download Offer Letter with Resolved
Tokens. With this method, when you open the downloaded offer letter, you won't see any tokens; they will have all been
replaced with the values that were entered while creating or editing the offer. You won't see any conditional sections,
because everything that isn't relevant to this candidate as of right now has been removed. Only the content that's
currently appropriate for the candidate remains in the letter. You can make any changes to the candidate's offer letter
from that starting point, and you can remove anything not relevant.
Using this method, the downloaded offer letter is a lot closer to what the candidate will see, so it's easier for you to make
any necessary additions or subtractions. While you're adjusting an offer letter you won't see the e-signature section
because this draft offer is currently not accepted. The default e-signature section will be added back to the bottom of
the letter later, when the candidate accepts the offer.
Note: Regardless of which method you're using to adjust the offer letter, you must save the final version in .rtf format
to upload it in the next step. Also, you don't need a BI Publisher plug-in for Microsoft Word to adjust offer letters using
either method.

---

## Upload and Use the Adjusted Offer Letter
*Chunk ID: OHR-USE-0259 | Chapter: Job Offers | Guide: Using Recruiting*

You can now upload the new adjusted offer letter in the Create Offer or Edit Offer flow by dragging the file into the Offer
Letter section or by clicking to add it as an attachment. In case more than one .rtf offer letter was mistakenly attached,
the most recently-uploaded file will be used.
The adjusted .rtf file that you just uploaded will now be used only for this candidate, and won't be available for other
candidates on other offers. Even though the name of the standard offer letter that was originally selected will continue
to show in this section, still the adjusted file will be used in the future for generating this candidate's offer letter.
After saving the draft offer, you can preview the adjusted offer letter for this candidate, and it will include all the correct
current values and all the appropriate paragraphs and sections. Use the action Preview Offer for this candidate's job
application to see the offer as the candidate would see it (although your own privileges may affect whether or not you
can see the values of certain fields such as salary or other compensation).

---

## Submit a Job Offer for Approval
*Chunk ID: OHR-USE-0260 | Chapter: Job Offers | Guide: Using Recruiting*

When you're done drafting a job offer and are satisfied with its content, you can use the Submit action to submit the job
offer for approval.

The job application is moved into the approval cycle and its status becomes Offer - Pending Approval. A banner is
displayed in the job application's Details and Offer tabs so you can track how the job offer is moving through the
approval process.
To ensure that the time of the approvers and the candidate isn't wasted on over-hiring, the Submit button only appears
in the Edit Offer flow if:
• There are still openings in the job requisition, compared to the number of hired candidates as of today.
• There are still open headcounts and vacant FTE in any position that's associated with the job offer, if position
incumbent validation is enabled. This includes the number of incumbents as of the offer's start date, plus any
other candidates who have an extended or accepted job offer to become incumbents by that date.
To submit a job offer for approval, you need these privileges or duty roles:
• View Job Offer (duty role) (ORA_IRC_VIEW_JOB_OFFER)
• Update Job Offer (duty role) (ORA_IRC_UPDATE_JOB_OFFER)
• Move Candidate Job Applications (IRC_MOVE_CANDIDATE_JOB_APPLICATIONS_PRIV)
If the approval is configured to be bypassed, the status will change to Offer - Approved immediately after the user has
submitted the draft offer.

---

## Copied Job Offers and Approval
*Chunk ID: OHR-USE-0261 | Chapter: Job Offers | Guide: Using Recruiting*

New offers that are created in the Copy Job Offer action can be automatically submitted into the approval cycle after
they're successfully copied, so they don't need to be individually submitted. These offers can remain in the Offer - Draft
status and a user must submit each one from within the Edit Offer flow.
Regardless of how these copied offers reach the Offer - Pending Approval status, the approval cycle can run on each
of them. Or if your administrator has configured it this way, these copied offers could bypass the need for approval
entirely, or could follow a different approval path. Either way, these offers will reach the Offer - Approved status
afterwards, just like other standard offers.

---

## Approve a Job Offer
*Chunk ID: OHR-USE-0262 | Chapter: Job Offers | Guide: Using Recruiting*

When a job offer is ready to be approved, approvers receive an email notification and a worklist notification (bell icon).
The notification can contain any of the offer's fields and their values for the approver to consider.
Approvers can click a link in the notification to view the exact offer letter that the candidate will see. Note that
the privileges of the approvers might determine if they can see the values of certain fields such as salary or other
compensation. If the offer has attachments, approvers can view the titles of all candidate-facing documents and all
internal documents in the approval notification. At the bottom of this notification are the attachments themselves,
displayed next to the name of the user who initiated the approval. Approvers can open and view any of these
documents here.
Approvers don't need to be named on the offer team, but they do need the right to see the candidate based on their
data security. Also, to see all the relevant fields within the approval notification and within the candidate's offer letter
linked from that notification, they need the following duty roles.
• View Job Offer (ORA_IRC_VIEW_JOB_OFFER)
• View Job Offer Salary (ORA_IRC_VIEW_JOB_OFFER_SALARY)
• View Job Offer Other Compensation (ORA_IRC_VIEW_JOB_OFFER_OTHER_COMPENSATION)

• View Job Requisition (ORA_IRC_VIEW_JOB_REQUISITION)
When all approvers give their approval, the approval is completed successfully. The job application changes to the Offer
- Approved status. When the approval is rejected, the job application changes to the Offer - Approval Rejected status.
If the approval is configured to be bypassed, the status will change to Offer - Approved immediately after the user has
submitted the draft offer.
In case the approval cycle needs to be stopped for a candidate before it reaches the last approver, the person who
submitted the offer into approval can do the following. They can use the Move action to change the job application's
status to either Offer - Rejected by Employer or Offer - Withdrawn by Candidate. Alternatively, they can go to the
Worklist area, find the tasks that they have initiated, and take the action Withdraw on this candidate. This will bring
the job application back into the status Offer- Draft. Also, administrators can go to the Transaction Console tool and
withdraw any pending offer from the approval cycle, as usual.

---

## Preview a Job Offer Letter
*Chunk ID: OHR-USE-0263 | Chapter: Job Offers | Guide: Using Recruiting*

You can use the Preview Offer action to see the job offer letter online just like the candidate will see it. You can also
download a PDF version of the candidate's offer letter.
You can use the Preview Offer action at any point in the offer's lifecycle to view the offer letter with its current values.
This can be after you created a draft of the offer letter, or after the candidate declined the offer, or after the candidate
was hired.
There are security restrictions to preview an offer letter. Depending on your privileges, you might not see the values
of the job offer salary or the other compensation values, even if these fields are configured in the selected offer letter
template.
When you preview the offer letter, you see:
• Text and buttons in the language used by the candidate when applying for the job.
• Tokens replaced with current values for each field in the offer letter template, using your security privileges.
• Name of offer attachments that the candidate needs to review. Note that you can't click these links when you
preview the offer letter.
• Media files configured in the requisition to display in the offer.
• A simplified version of the branding matching the career site where the candidate applied for the job.
• Link to download a PDF version of the candidate's offer letter with its current values, using your security
privileges. This can be useful if you want for instance to send a paper copy to the candidate.
• The newest version of the offer letter template, regardless of the current status of the job offer itself.
The Preview Offer page displays the job offer letter in HTML format. There might be some differences when you view
the job offer letter in the Preview Offer page (the letter is displayed in HTML format) versus when you view it as a
PDF or Word format. For example, the HTML format supports only bulleted and numbered lists, whereas in Word,
bulleted, numbered, and multilevel lists are supported. If you want more information on these differences, refer to the
documented Differences Between Preview Offer and RTF or PDF File available on My Oracle Support (Doc ID 2747108.1).
If you realize that the offer letter isn't appropriate for the candidate, you can use the Edit Offer action (if the offer is in
the Draft state) and select another offer letter if your organization created more than one offer letter template to meet
their business needs. If the offer is still draft and you have the appropriate privileges, you could also change some of the
text in the offer letter to adjust the content to that specific candidate.

Related Topics
• Job Offer Letter Template
• Create a Job Offer Letter Template
• Differences Between Preview Offer and RTF or PDF File

---

## Extend a Job Offer
*Chunk ID: OHR-USE-0264 | Chapter: Job Offers | Guide: Using Recruiting*

You extend a job offer when you want to communicate the offer to the candidate.
As soon as the job offer is approved, it might get communicated to the candidate automatically if the requisition is
configured to automatically extend offers. This can occur immediately or after a specific number of hours after the offer
reached the Offer - Approved status. If this doesn't happen automatically or if you want to extend the offer sooner, use
the Extend Offer action. You can use the Extend Offer action for any job application in the Offer - Approved status. You
need the privilege Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV).
When you extend a job offer using the Extend Offer action, two areas are verified before moving the candidate forward
into the Offer - Extended status:
• If there are still openings in the requisition. This check prevents extending more job offers than the number
of available openings. A requisition is considered to have available openings if the number of current
openings is greater than the number of hired candidates combined with the number of candidates with an
extended or accepted job offer. Extending the offer can still be successful even for a requisition that's filled
or overfilled, if you have the privilege Communicate Job Offer Ignoring the Requisition Number of Openings
(IRC_COMMUNICATE_JOB_OFFER_IGNORING_NUMBER_OF_OPENINGS).
• If the offer is based on a position, whether there are still open headcounts and vacant FTE in the position as
of the offer's intended start date. This check might show you a warning or you might be unable to extend the
offer, depending on how strictly this area is configured. For details, see Job Offers Respect Headcount of Job
Requisitions and Positions.
After the Extend Offer action is underway, a banner shown on the job application's Details and Offer tabs says that the
offer is being extended. After the extend action is successful and any candidate notification has been sent, the banner is
no longer there and the job application status is Offer - Extended.
In rare cases when the banner no longer appears but the status remains Offer - Approved, you can check the Errors
section on the job application's Offer tab to find out if anything is preventing the offer from being extended. For
example, it's possible that the offer letter couldn't be generated from the Content Library's template, and this error
would be explained in the Errors section. After you resolved any error, you can use the menu action Extend offer once
again.
When a job offer is successfully extended, the candidate receives the following email or SMS informing them of the new
offer and inviting them to view their offer letter and give their response.
• Job Offer Extended External Notification: External candidates click the link in the invitation, which sends them
a new message containing a 6-digit verification code. This allows external candidates to access the web page
displaying their job offer.
• Job Offer Extended Internal Notification: Internal candidates click the link in the invitation, or click the link in the
worklist notification (Bell icon) which also notifies them of their offer. They can also visit the Current Jobs work
area to see their offers (Navigator > Me > Current Jobs > Job Offers).

From the extended offer page, both external and internal candidates can print the job offer, open any attachments, view
any media, and respond to the offer.
If the external or internal candidate needs another copy of the invitation to reach the job offer, perhaps because they
deleted or misplaced it, use the Resend Offer action. The Job Offer Reextended External Notification and Job Offer
Reextended Internal Notification are used. The message is exactly the same as the email or SMS sent to the candidate
the first time the job offer was extended. You can use this action as many times as needed when the job offer is in the
Extended state.
Note: The requisition's candidate selection process can be configured to bypass extending any offers to candidates.
In this case, you won't see any Extend Offer action on any job applications in the Offer - Approved status, even if you
have the privilege Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER_PRIV).

---

## Bypass Extending a Job Offer
*Chunk ID: OHR-USE-0265 | Chapter: Job Offers | Guide: Using Recruiting*

Your administrator can configure the candidate selection process to bypass extending offers to candidates. When this
candidate selection process is used in a job requisition, the Offer Team will indicate if the offer is accepted or declined
without the need for any online communication to or from the candidate.
There are different reasons why your organization might decide to enable this feature. One could be that there are many
different languages used by candidates and they prefer to communicate directly with candidates instead of having to
translate all the notifications used in the regular offer process. Or, your organization wants to avoid having back and
forth written communications with candidates during the offer process.
As soon as an offer reaches the Approved state, you can tell the candidate about the offer. If the candidate tells you that
they accept the offer, use the Accept Offer action as long as there are still available openings on the job requisition and
if any related position has sufficient open headcount. The offer goes from Offer - Approved directly to Offer - Accepted.
If the candidate tells you that they decline the offer, use the Move action to change their status to Offer - Withdrawn by
Candidate.
Because the offer is never extended to the candidate, no automated notification is sent to the candidate, inviting
them to view and accept their offer. And no offer letter is displayed to the candidate. It’s the responsibility of the hiring
manager, recruiter, or anyone in the offer team to discuss the details directly with the candidate and to record whether
or not they accept the offer.
When this feature is enabled, here's what it means for candidates:
• The candidates don't receive any automated notification informing them that an offer was extended to them.
• The candidates can't see their offer before responding to it.
• The candidates tell someone on the Offer Team whether they accept or decline the offer.
• The candidates don't receive a notification confirming that their response was received, unless this is
configured.
For hiring processes configured to bypass extending offers, there's no need to select an offer letter while drafting the
offer. If an offer letter is specified, you'll still be able to preview the candidate's offer letter, and it will get stored in the
worker's Document Records when the candidate accepts the offer. If the selected offer letter is configured to track esignature, it won't show that the candidate e-signed it; but it can show the name of the user who accepted the offer on
behalf of the candidate, the date, and time.
The Resend Offer action isn't available because no offer invitation was sent in the first place.

There are a few places where the candidate can see their offer letter, if any was selected, after the user has accepted it
on their behalf. If an alert was configured to acknowledge that they accepted the offer, this may contain a link to view
that offer letter. Internal candidates can view their letter in the My Jobs > Accepted Offers work area. And all candidates
may be able to see it in their Document Records after they join the organization.

---

## Cancel a Job Offer
*Chunk ID: OHR-USE-0266 | Chapter: Job Offers | Guide: Using Recruiting*

You can cancel a job offer for a candidate when the offer is rejected by the employer or the candidate has withdrawn.
You can use the Cancel Offer action when the job applications are in the following phases and states:
• Job Offer phase, with the Approved, Extended, or Accepted state.
• Custom phases after the Job Offer phase.
• HR phase, all states except Processed.
Before you start
You need the privilege Cancel Job Offer (IRC_CANCEL_JOB_OFFER_PRIV).
Here's what to do
1. Open a job requisition and go to the list of job applications.
2. Select a job application.
3. Select the Cancel Offer action.
4. On the Cancel Offer page, complete these fields:
◦ Phase: The phase is displayed in read-only mode.

◦ State: The state is defaulted to Rejected by Employer, but you can change it to Withdrawn by Candidate if
◦

needed.
Comment: You can enter the reason for rejecting the candidate application.

5. Click Submit.
Results:
An alert is sent to the offer team (hiring manager and collaborators) to inform them that the offer was canceled.

---

## Respond to a Job Offer
*Chunk ID: OHR-USE-0267 | Chapter: Job Offers | Guide: Using Recruiting*

When you extend a job offer to a candidate, the candidate responds to the offer.

---

## Response by the Candidate
*Chunk ID: OHR-USE-0268 | Chapter: Job Offers | Guide: Using Recruiting*

The candidate views the job offer letter online and responds themselves.
To accept a job offer, the candidate selects the Accept option. They must provide light e-signature information to
confirm their acceptance. By providing their name, the job offer state changes to Accepted. The time, date, time zone,
and IP address of when this light e-signature was captured gets recorded. The candidate lands on a page that may have
a short message at the top providing any acknowledgment or instructions from the organization, and then their offer
letter is displayed on the rest of the page. A notification message can also be sent, which contains a link to revisit their

accepted offer letter in the future. For external candidates, they will again receive a 6-digit verification code to reach
that offer page.
To decline a job offer, the candidate selects the Decline option. They may have the opportunity to provide text
comments or even to select a reason why they are choosing to decline the offer, if this was configured. As soon as they
confirm this action, the job offer state changes to Withdrawn by Candidate. The candidate can no longer view this offer
letter. It's possible the candidate declined because they want to negotiate possible changes to the offer with the recruiter
or manager. If the user decides to revise the candidate's job offer and start the Offer phase lifecycle again, they can use
the Redraft Job Offer action from this state.

---

## Offer Team Records Candidate's Response
*Chunk ID: OHR-USE-0269 | Chapter: Job Offers | Guide: Using Recruiting*

A recruiting user can record the candidate's response to their offer, if the candidate won't be providing it directly.
To accept the job offer, use the Accept Offer action. The response, date, time, and user name of the person capturing
the response on behalf of the candidate are recorded. The e-signature and IP address aren't recorded. This action is
available to users with the privilege Communicate Job Offer (IRC_COMMUNICATE_JOB_OFFER).
To decline the job offer, use the Move action and select the Withdrawn by Candidate state. The response, date, time,
and user name of the person capturing the response on behalf of the candidate are recorded. The e-signature and IP
address aren't recorded. As usual, you can enter a text comment and possibly choose from a list of reasons why the
candidate is withdrawing themselves from consideration in the job application by declining this offer.

---

## Redraft a Job Offer
*Chunk ID: OHR-USE-0270 | Chapter: Job Offers | Guide: Using Recruiting*

You can adjust a job offer after the offer is approved by the approver or accepted by the candidate. When you redraft a
job offer, the state changes to Draft so you can change the content.
You can redraft a job offer before it's extended to the candidate and also after the candidate has seen it.

---

## Redraft Before the Job Offer is Extended
*Chunk ID: OHR-USE-0271 | Chapter: Job Offers | Guide: Using Recruiting*

Redrafting a job offer can be useful if a job offer gets stopped or must be revised after it leaves the Draft state. For
example, you need to make a change in the offer or the candidate wants to negotiate elements in the offer. When you
redraft a job offer, it must go through the approval process again.
You can use the Redraft Offer action when the job offer status is:
• Offer - Approval Rejected, and you judge that it's worthwhile to review the job offer.
• Offer - Approved, and you discovered that changes are necessary after the job offer was approved.
When the job offer status is Offer - Pending Approval, the person who submitted the offer into approval can withdraw
it from the approval cycle if needed, using the Worklist area. This moves the offer back to Offer - Draft, and no redraft
action is required.

---

## Redraft After the Job Offer is Extended
*Chunk ID: OHR-USE-0272 | Chapter: Job Offers | Guide: Using Recruiting*

You can redraft a job offer after the candidate has seen it, if changes are needed. You can revise the offer letter for the
candidate to consider it again.

There are situations where a candidate saw or accepted a job offer but something changed and you need to re-issue
a new job offer letter. In these situations, you can use the Redraft Offer action. The job offer gets reset to Draft. You
can change the job offer, get it approved again, and re-extend it to the candidate. The candidate then responds to the
revised offer.
You can redraft a job offer when the job application is in the following phases and states without rejecting or
withdrawing the candidate job application:
• Offer – Extended
• Offer – Accepted
• Any custom phases configured after the Offer phase
• HR – Pending Automated Processing
• HR – Pending Manual Processing
• HR – Error During Processing
• HR - Processing in Progress (for external candidates only)
To redraft job offers after a job application has reached the HR phase, you need the privilege Redraft Job Offer After HR
Phase (IRC_REDRAFT_JOB_OFFER_AFTER_HR_PHASE_PRIV).
Note: When the job requisition is closed or canceled, the Redraft Offer action is no longer available.
For internal candidates:
If the job application is in HR phase and Processing in Progress state, you need to follow these steps:
1.
2.
3.
4.

Delete the future dated new assignment record for the employee.
Run the Complete the Recruiting Process scheduled process.
The job application will move to the Withdrawn by Candidate state and the Redraft Offer link will be enabled.
Click the Redraft Offer link to bring the job application in the Offer - Draft status.

All versions of accepted job offer letters are retained on the worker's Document Records page, in the document type
Recruiting Job Offer Letters. This means that each version of the same job application's offer letter can be seen at once,
if the candidate accepted an offer which was then redrafted and re-accepted. This is important because the changed
values might be reflected in the new offer letter compared to the old offer letter, such as a new work location, start date,
and e-signature date, if these fields are configured to be included.
If a job offer gets redrafted before being accepted by the candidate, the prior version of the offer isn't retained in the
worker’s Document Records.
Note: The Redraft Count column is made available to capture the number of times a job offer is being redrafted. This
attribute is exposed in Approval Rules which will help you to configure the leaner approval rule or bypass approval for
redraft scenarios.

---

## Use Cases
*Chunk ID: OHR-USE-0273 | Chapter: Job Offers | Guide: Using Recruiting*

Use Case 1: The job requisition is in the Filled state and is no longer posted. To redraft the job offer, the requisition must
be reopened and posted so that it's in an Open state. The Redraft Offer action is no longer available when a requisition
is closed or canceled.

Use Case 2: Your administrator enabled the Prevent Redrafting Offers feature and the offer was processed or rejected
over 90 days ago. To redraft the job offer, your administrator must disabled the Prevent Redrafting Offers in the Setup
and Maintenance work area.
Use Case 3: The Redraft Offer action is grayed out and you're unable to redraft a job offer for a candidate in the
Withdrawn by Candidate state. That's because your administrator enabled a setting to prevent job offers from being
redrafted.
Related Topics
• End Dating Offer Assignments

---

## Change the Start Date of Candidates
*Chunk ID: OHR-USE-0274 | Chapter: Job Offers | Guide: Using Recruiting*

You can change the start date of internal and external candidates in a simple one-step process using the Change Start
Date action.
The Change Start Date action is available in the Job Applications and Offers lists when job applications are in the Offer
or Post Offer (custom) phase, and on the Job Offers page (Manage Job Offers quick action) when job applications are in
the HR phase.
You can change the start date many times. The Offer team and candidate are informed of this change. You can track
these start date changes in the notification date time stamps in the Messages tab of the job application.
No approval is required for changing the start date, for any business reasons.
You can't change the start date of an external candidate from the job application or Manage Job Offers area when the
job application is in the HR phase and the employee record becomes active (start date has been reached).
You can't change the start date of an internal candidate from the job application or Manage Job Offers area when their
record in Oracle Recruiting is converted (manually submitted from Manage Job Offers page, or submitted automatically
using the profile option setting). The Change Start Date action can be used only during the window period where the
redraft of an offer is allowed. This window period is specified in the Redraft and Cancel Offers section of the Enterprise
Recruiting and Candidate Experience Information task.
Note: When you change the start date, the new date appears in the job offer and offer letter. The date isn't changed
in the Document of Records.
This table explains the behavior where exactly the start date change will occur for various scenarios.

When

---

## Start date will be updated in the Pending worker
*Chunk ID: OHR-USE-0275 | Chapter: Job Offers | Guide: Using Recruiting*

record but a banner will be displayed with the
new start date for recruiting users on the Job
Offers page.

---

## Start date will be updated in the Employee
*Chunk ID: OHR-USE-0276 | Chapter: Job Offers | Guide: Using Recruiting*

record only.

To see the Change Start Date action, you need to have the Change Job Offer Start Date duty role and function
privileges.
• Change Job Offer Start Date (ORA_IRC_CHANGE_JOB_OFFER_START_DATE_DUTY)
• Change Job Offer Start Date by Recruiting Manager
(ORA_IRC_CHANGE_JOB_OFFER_START_DATE_BY_RECRUITING_MANAGER_DUTY)

---

## What Happens if the Candidate's Start Date isn't Known
*Chunk ID: OHR-USE-0277 | Chapter: Job Offers | Guide: Using Recruiting*

or Needs to Change
A job offer must have a start date when it's first created and throughout its lifecycle. This date is important for ensuring
that other values in the draft offer will be valid and available as of the point in time when this candidate would start
working.
The proposed start date field can never be blank. However, you can enter a date which is considered tentative or a
placeholder, with the intention of changing it later. The proposed start date can be in the past, but not on a date earlier
than when the candidate was first known to the company.
Offer values, including the start date field, can only be changed when the offer is in the Draft state. The procedure to
update the offer's projected start date is different depending on what state the candidate has reached in the recruiting
process. After the candidate has accepted the job offer, you can follow different processes to change the expected
start date depending on whether or not they will require the candidate to review and re-accept an updated offer letter.
You may find it acceptable to retain the offer letter with the light e-signature and the obsolete start date, and not to
change the offer at all, but rather to provide the new correct start date directly while creating the worker record or the
pending worker record. You may need to cancel the worker or pending worker transaction to regenerate a new offer
letter containing the new start date, to get the candidate's light e-signature on a corrected version of the letter.

Status

---

## Use the Edit Offer action and update the start date and any other fields. There is no impact for the
*Chunk ID: OHR-USE-0278 | Chapter: Job Offers | Guide: Using Recruiting*

candidate, approvers, or other users because they haven't seen the offer yet.
Changing the start date in a draft offer may cause other fields to require recalculation or changes too.
For instance, if the candidate's start date is changed to be later or earlier, this offer might now interact
differently with another job the candidate will have or will be terminated from at that time. So the
appropriate action might change from Hire to Transfer, or from Transfer to Rehire. Another example is
if the candidate's revised start date means they're no longer eligible for a given salary or compensation
plan, these too will have to be recalculated by visiting the relevant section in the revised draft offer.

---

## Offer - Pending Approval
*Chunk ID: OHR-USE-0279 | Chapter: Job Offers | Guide: Using Recruiting*

The initiator of the approval cycle must remove the offer from the approval cycle, which puts the offer
into the Offer - Draft status. There is no impact for the candidate because they haven't seen the offer
yet.
Follow the recommendations provided for Offer - Draft for updating the start date or any other fields.
Approvers who have not yet seen the offer will not see it this time. All approvers will have to give their
approval again after the new draft offer is submitted with the changes.

---

## Offer - Approved or Offer - Approval
*Chunk ID: OHR-USE-0280 | Chapter: Job Offers | Guide: Using Recruiting*

Rejected

Use the Redraft action to bring the offer back into the Offer - Draft status. There is no impact for the
candidate because they haven't seen the offer yet.

Status

What to do
Follow the recommendations provided for Offer - Draft for updating the start date or any other fields.
Approvers if any will have to give their approval again after the new draft offer is submitted with the
changes.

---

## Offer - Extended
*Chunk ID: OHR-USE-0281 | Chapter: Job Offers | Guide: Using Recruiting*

Use the Move action to bring the offer into the Offer - Rejected by Employer status (or alternately Offer
- Withdrawn by Candidate). This will notify the candidate that their offer was rescinded, if notifications
are configured in the Recruiting Content Library using the Job Offer Extended Rejected Notification
category.
Then use the Redraft action to bring the offer back into the Offer - Draft status. Follow the
recommendations provided for Offer - Draft for updating the start date or any other fields. Approvers
if any will have to give their approval again after the new draft offer is submitted. After the revised
offer reaches the Offer - Extended status again, the candidate will be notified that their offer was
extended, if notifications are configured in the Recruiting Content Library using the Job Offer Extended
Notification category.

---

## Offer - Accepted
*Chunk ID: OHR-USE-0282 | Chapter: Job Offers | Guide: Using Recruiting*

Is it necessary to get the candidate's acceptance on a new offer letter with the revised date? If not, then
the offer can remain unchanged. The new desired start date can be entered instead of the offer's start
date when the candidate becomes a worker or a pending worker, during the final HR phase.
If the candidate must review and accept a new offer letter with the revised date, then use the Move
action to bring the offer into the Offer - Rejected by Employer status (or alternately Offer - Withdrawn
by Candidate). This will notify the candidate that their offer was rescinded, if notifications are
configured in the Recruiting Content Library using the Job Offer Extended Rejected Notification
category. A copy of the accepted job offer letter will be stored in the Document Records for this
candidate, which is available for each worker and their manager to view after the candidate becomes a
worker.
Then use the Redraft action to bring the offer back into the Offer - Draft status. Follow the
recommendations provided for Offer - Draft for updating the start date or any other fields. Approvers
if any will have to give their approval again after the new draft offer is submitted. After the revised
offer reaches the Offer - Extended status, the candidate will be notified that their offer was extended, if
notifications are configured in the Recruiting Content Library using the Job Offer Extended Notification
category. If the candidate accepts the new revised offer letter, another copy of the newly accepted job
offer letter will be stored in the Document Records for this candidate, alongside the prior accepted
offer letter.

---

## Offer - Rejected by Employer or Offer Withdrawn by Candidate
*Chunk ID: OHR-USE-0283 | Chapter: Job Offers | Guide: Using Recruiting*

Use the Redraft action to bring the offer back into the Offer - Draft status. Update the start date and
any other fields.

---

## Follow the steps for the Offer - Accepted status. If a new offer letter isn't needed, the offer can
*Chunk ID: OHR-USE-0284 | Chapter: Job Offers | Guide: Using Recruiting*

remain unchanged, and the new date can be entered while creating the pending worker or the new
assignment. If a new offer letter acceptance is needed, move the candidate into the Rejected or
Withdrawn state in that custom phase, and then use the Redraft action.

---

## HR - Pending Automated Processing
*Chunk ID: OHR-USE-0285 | Chapter: Job Offers | Guide: Using Recruiting*

Wait until the automated processing changes the state, then follow the steps for that new state.

---

## HR - Pending Manual Processing
*Chunk ID: OHR-USE-0286 | Chapter: Job Offers | Guide: Using Recruiting*

Is it necessary to get the candidate's acceptance on a new offer letter with the revised date? If not, then
the offer can remain unchanged.
If the feature was enabled by your administrator, the HR specialist can change the proposed start
date for internal candidates after they’ve accepted their job offer, in case the intended date in their
offer now needs to be adjusted before their new assignment is processed. For details, see Internal Job
Offers: How They're Processed
If the feature wasn't enabled, the new desired start date can be entered when the candidate becomes a
worker or a pending worker, replacing the original start date in the final HR phase.

Status

What to do

An HR specialist is expected to perform the pre-selected HR action for this candidate in the Manage
Job Offers area, such as Transfer, Promote, Add Assignment, Global Transfer, Add Pending Worker, or
even Process Now. They will arrive on a guided process page where the agreed-upon start date from
the offer is filled in by default. In this flow, the date can be changed to the preferred new start date, and
then submitted.
No notification is sent to the candidate. There will also be no impact on the original offer which
remains intact in Oracle Fusion Cloud Recruiting. There will be no impact on the original accepted offer
letter which remains intact in the candidate's Document Records.
If instead the candidate must review and accept a new offer letter with the revised date, the HR
specialist can use the Reject Candidate or Withdraw Candidate action. The candidate's job application
now displays the Rejected by Employer state or the Withdrawn by Candidate state, both in the HR
specialist's area Manage Offers and in the recruiters' area within Hiring. Either of these users can now
perform the Redraft action. No notification is sent to the candidate. When the offer is in the Draft state,
the start date or any other fields can be updated in the offer by recruiters, while the original accepted
offer letter remains intact in the candidate's Document Records.

---

## HR - Processing in Progress
*Chunk ID: OHR-USE-0287 | Chapter: Job Offers | Guide: Using Recruiting*

Is it necessary to get the candidate's acceptance on a new offer letter with the revised date? If not, then
the offer can remain unchanged. The new desired start date can be entered in the candidate's new
assignment as it gets created, replacing the original start date. The HR specialist needs to find and fix
the new assignment that's associated with this candidate, because it's currently in progress.
For an external candidate, a new hire, or a rehire, the state Processing in Progress usually means that
a Pending Worker has been created for this person, but has not yet been converted to a worker. In
this case, the HR specialist can go to the Pending Worker area and use the Edit action to change this
person's start date in the When and Why section.
For an internal candidate, a transfer or other type of internal mobility, the state Processing in Progress
usually means that an HR specialist has already submitted a new assignment for this person, but this
assignment has not yet been approved or recorded on the Oracle Recruiting side. In this case, the HR
specialist can go to that new assignment and update the start date when appropriate.
No notification is sent to the candidate. There will be no impact on the original offer which remains
intact in Oracle Recruiting. There will be no impact on the original accepted offer letter which remains
intact in the candidate's Document Records.
If instead the candidate must review and accept a new offer letter with the revised date, the HR
specialist needs to find the new assignment that's associated with this candidate, which is currently in
progress, and stop its progress. For an external candidate, the HR specialist should cancel the Pending
Worker. For an internal candidate, the associated assignment may not yet be approved or recorded on
the Oracle Recruiting side, so it can be canceled after it gets completed.
These cancellations will update the candidate's status in the Manage Job Offers area to Rejected or
Withdrawn (based on the frequency of the scheduled process Complete the Recruiting Process. From
this state, either the HR specialist or the recruiter can perform the Redraft action. No notification is sent
to the candidate. When the offer is in the Draft state, the start date or any other fields can be updated
in the offer by recruiters, while the original accepted offer letter remains intact in the candidate's
Document Records.
Note about candidates with complex job offers (see Complex Job Offers: How They're Processed):
The HR specialist should cancel any associated new assignment that was based on this offer, before
redrafting the new offer with the new start date. However this cancellation alone doesn't automatically
trigger a change of status to become HR - Withdrawn by Candidate. For these complex offers in the
status HR - Processing in Progress, the HR specialist must also use the Return to Manual Processing
action, and from there use the Withdraw Candidate or Reject Candidate action. Then the Redraft action
becomes available both to the HR specialist and to the recruiters.

---

## HR - Processed
*Chunk ID: OHR-USE-0288 | Chapter: Job Offers | Guide: Using Recruiting*

Is it necessary to get the candidate's acceptance on a new offer letter with the revised date? If not,
then the offer can remain unchanged. The new desired start date can be entered in the candidate's

Status

What to do
new assignment, replacing the original start date. The HR specialist needs to find and fix the new
assignment that's associated with this candidate, which is already complete, by making a correction or
an update.
No notification is sent to the candidate. There is no impact on the original offer which remains intact in
Oracle Recruiting. There is no impact on the original accepted offer letter which remains intact in the
candidate's Document Records.
If instead the candidate must review and accept a new offer letter with the revised date, the HR
specialist needs to find the newly-created assignment that's associated with this candidate, and cancel
it. This cancellation will shortly affect the HR specialist's Manage Job Offers area, by showing the new
status of HR - Withdrawn by Candidate for this candidate. From this status, either the HR specialist or
the recruiter can execute the Redraft action. No notification is sent to the candidate. When the offer is
in the Draft state, the start date or any other fields can be updated in the offer by recruiters, while the
original accepted offer letter remains intact in the candidate's Document Records.
Note about candidates with complex job offers (see Complex Job Offers: How They're Processed):
The HR specialist should cancel any associated new assignment that was based on this offer, before
redrafting the new offer with the new start date. However this cancellation alone doesn't automatically
trigger a change of status to become HR - Withdrawn by Candidate. For these complex offers in the
status HR - Processed, the HR specialist must also use the Withdraw Candidate or Reject Candidate
action. Then the Redraft action becomes available both to the HR specialist and to the recruiters.

---

## HR - Rejected by Employer or HR Withdrawn by Candidate
*Chunk ID: OHR-USE-0289 | Chapter: Job Offers | Guide: Using Recruiting*

The HR specialists or recruiters can use the Redraft action to return the offer to the Draft state. No
notification is sent to the candidate. When the offer is in the Draft state, the start date or any other
fields can be updated in the offer by recruiters, while the original accepted offer letter remains intact in
the candidate's Document Records.

---

## What Happens When a Candidate Accepts a Job Offer
*Chunk ID: OHR-USE-0290 | Chapter: Job Offers | Guide: Using Recruiting*

When a candidate accepts a job offer, the state of the job application becomes Accepted. This is the final state in the
Offer phase of the lifecycle. From there, various things can occur.
• When the candidate clicks Respond to Job Offer in the notification email, the career site where the candidate
applied will open. However if the candidate was added to a requisition manually, there's no career site context,
and the offer will be displayed on the first active career site.
• Immediately after accepting their job offer, the candidate will initially see their offer letter with any
acknowledgment text shown above it, and without its light e-signature section if any.
• The candidate can choose to return later to view or download their offer letter. On that page the offer letter will
no longer include the initial acknowledgment text; instead, it will show any light e-signature information that
was configured to display. This can include their full name, the date and time of their acceptance, and the IP
address from which they accepted the offer. Alternately, if a user recorded the candidate's acceptance on their
behalf, that person's name can be shown in this section of the offer letter.
• Any other users will also see this offer letter with any light e-signature information from the candidate's
acceptance, or the user's name who accepted on the candidate's behalf. This includes users who preview the
offer letter from the candidate's job application and those who view it in the worker's Document Records where
it has been automatically copied.
• The latest generated version of the offer letter is copied to the Documents of Record.

◦ If there's no offer letter configured for this offer, there's nothing to store in Document Records.
◦ If the candidate's accepted offer letter hasn't yet been generated due to some BI Publisher issue, the offer
letter is copied in the Documents of Record without its light electronic signature information if any. When
the accepted letter does get automatically regenerated, that will be copied to Documents of Record as
well.

• The Progress tab of the job application shows that this offer has been accepted, either by the candidate or by
the user.
• If auto-progression was configured to move candidates forward from the status Offer - Accepted, it occurs
immediately. This can be configured to automatically move all candidates, only internal or only external
ones, or any subset of candidates as specified by your administrator. Immediately upon accepting the offer,
candidates can move forward into any remaining custom phase, or into the final HR phase.
• If any custom phases are configured between the offer phase and the final HR phase, then candidates can
be moved into these states. They can be progressed manually using the Move action, or an auto-progression
might be configured to move them here instead.
• If no auto-progression and no custom phases are configured for this selection process, then:

◦ External candidates remain in Offer - Accepted, and you can move them forward as needed.
◦ Internal candidates automatically move forward into the HR phase. Which state they land in depends on
the situation, the available headcount, and other factors.

When a candidate moves into the final HR phase, due to a manual action or an auto-progression, the candidate is put
into the hands of the HR specialists. The following events occur automatically:
• As soon as the candidate job application leaves the Offer phase, it's no longer listed on the Job Offers page in
the Hiring work area, although the job application and its Offer tab remain visible within the requisition's list of
candidates.
• The states of the candidate's other active job applications, if any, change to Withdrawn by Candidate.
Exceptions: The approval process continues for job applications in Offer Pending Approval. Also, job
applications in Offer - Extended or later state (including the HR phase) remain untouched. You might want to
manually withdraw the job application to avoid offering another job to the same candidate.
• The number of hires on the offer's related requisition gets increased by one. If the number of hires now
matches the number of openings and the requisition is configured to be automatically filled, it will be filled at
this point.
• Recruiters have no further influence on the job offer or on the candidate's job application. They can't reject it
nor change its state by moving it forward. But they can still see its state change as the HR specialists process it
through the HR phase.
• The job offer becomes visible to HR specialists on their Job Offers page, from the Manage Job Offers quick
action. HR specialists, not recruiters, are now responsible for finishing the new assignment for the accepted
candidate and their job offer. The state in which the candidate arrives in the HR phase will depend on whether
they're a brand new hire or rehire, or a current worker moving within the company, or whether any duplicate or
other error occurred.

---

## What Happens if a Candidate is Hired for a Job and
*Chunk ID: OHR-USE-0291 | Chapter: Job Offers | Guide: Using Recruiting*

Wants to Accept Another Job
It's possible that a candidate will be joining your organization in two different roles, and one job may start earlier than
the other.
Depending on the timing of each assignment's intended start date, this may be easy to process or it may require several
steps. The most complex case may be when you hired the candidate for a job that will start in a far-future date and the
candidate is now seeking a nearer-term job as well.
Let's say a new person is planning to join your company full-time in June, after they graduate from school. They have
applied to a requisition and they received and accepted a job offer for a start date of June 1. This candidate record has
been handed off to the HR specialist and has been transformed into a pending worker, with the status HR - Processing.
Alternately, the pending worker may have already been converted to a worker with a future start date of June 1, with the
status HR - Processed.
Now the same person also applies for a different requisition, because they also want to work for your company part
time from January 1 up to their graduation in June. They identify themselves in the same way and Oracle Fusion Cloud
Recruiting recognizes them as being the same candidate. They get a job offer on this January job application, but after
it's accepted, the HR specialist faces a problem when trying to process it. This is because a pending worker or a futuredated worker can't have a second assignment if the new assignment would start earlier (January) than they're already
planning to start (June).
The same situation would have been fine if the candidate had first applied to and been hired for the near-term job
(January), and then for the later-dated job (June). That's because an existing worker can always get an additional or
replacement job that starts later than their first job.
To reverse the sequence of when these assignments get created for the candidate, follow these steps:
1. Cancel the Later-Starting Job
2. Process the Earlier-Starting Job
3. Reprocess the Original Later-Starting Job

---

## Cancel the Later-Starting Job
*Chunk ID: OHR-USE-0292 | Chapter: Job Offers | Guide: Using Recruiting*

You first need to cancel the later-starting job and set it aside temporarily. This may be a pending worker with an
intended start date of June, or perhaps it's already been converted to a future-dated worker with an assignment start
date of June. Either way, you need to cancel this record, don't terminate it.
The pending worker had been created from a recruiting record which was in the status HR - Processing in Progress (or
HR - Processed in the case of a worker). This cancellation will soon cause the job application for June to change status
based on the scheduled process Complete the Recruiting Process. In both cases, the status will become HR - Withdrawn
by Candidate. This status is temporary and expected. This leaves the candidate with no assignment beyond their job
offers, so they're ready to be a brand new hire as of January.

---

## Process the Earlier-Starting Job
*Chunk ID: OHR-USE-0293 | Chapter: Job Offers | Guide: Using Recruiting*

Now you can process the job offer that has the earlier start date, to transform the candidate into a new hire as of
January. However this offer was originally created with some awareness of the other job, so it was drafted with an action

such as Add Assignment. This action is no longer appropriate, so the job offer needs to be redrafted to select the correct
action Add Pending Worker.
If the candidate's January job offer is waiting in status HR - Pending Manual Processing, the HR specialist must move
the candidate to HR - Withdrawn by Candidate to make the Redraft action available. If the candidate's situation was
discovered after this January job had already been moved to HR - Processing in Progress then you must use the Return
to Manual Processing action, move them to HR - Withdrawn by Candidate, and finally use the Redraft action. These
withdrawals won't send any notification to the candidate. The job requisition will immediately reflect that this candidate
is no longer filling an opening, but the recruiter knows that they will be taking that opening again shortly.
The recruiter can now find this candidate's job application back in the status Offer - Draft. They must click Edit Offer
to enter the guided flow and select the appropriate action Add Pending Worker. The original January start date
and all other fields remain the same, and the offer can be moved forward again through the lifecycle. Note that the
candidate may be a bit surprised to receive another notification requesting them to accept the same job offer for the
January start date. The recruiter may want to explain to them why this is needed. They may even choose to capture
the candidate's acceptance on this redrafted offer on their behalf, because the offer letter that was originally accepted
remains accessible in the candidate's Document Records with any light e-signature that the candidate provided in the
first place.
As soon as this January job offer is accepted and the candidate moves into the HR phase, the candidate should
smoothly become a pending worker. The candidate's name will appear on the Pending Worker list, and the status will
automatically become HR - Processing in Progress. As soon as this pending worker gets converted, the status will
automatically become HR - Processed, based on the scheduled process Complete the Recruiting Process. This will also
reclaim the candidate's spot in the requisition which had been temporarily freed at the start of this step.

---

## Reprocess the Original Later-Starting Job
*Chunk ID: OHR-USE-0294 | Chapter: Job Offers | Guide: Using Recruiting*

Finally the HR specialist can recreate the candidate's post-graduation assignment for June. You do this by reprocessing
the job offer that corresponds to the pending worker's or worker's assignment that you canceled in step 1.
From the quick action Manage Job Offers, the HR specialist finds the candidate's June offer in the status HR Withdrawn by Candidate, which it reached as soon as the scheduled process Complete the Recruiting Process noted
that you had canceled it. Now you must take the action Return to Manual Processing to start processing this offer again.
Because this candidate's situation has changed since this June job offer was drafted, their job offer is now categorized
as a complex situation for you to handle manually. However the job offer still shows the action Add Pending Worker so
you must click this to start processing the candidate once again. You will be asked to confirm that you're processing this
candidate, and your agreement will bring you to the candidate's Employment Info page while changing the status to HR
- Processing in Progress.
From the candidate's Employment Info page you can review this candidate's January assignment then you must select
the appropriate HR action to create their June assignment. For instance Transfer, Add Assignment, or even Create Work
Relationship. Within the guided flow for that action, you must manually enter all relevant information from the job offer
into the fields of the HR action page you selected. Unlike other types of job offer processing, the field values aren't
populated with the agreed-upon values from the offer's assignment, salary, compensation, or other sections. So you
should be careful about information that was already viewed and understood in the job offer while you copy each field's
value into the HR flow sections. Then you must submit the HR action.
After you submit that new June assignment, the candidate remains on the Manage Job Offers list in the status HR
- Processing in Progress. Like all complex offers, their job application won't automatically change to status HR Processed even after that June assignment gets any required approval and is committed in the HR application. You
must use the action Move to Processed to change their Recruiting status to HR - Processed. This is the final successful
state in the recruiting process, and the candidate now has the proper records for both January and June.

Related Topics
• Complex Job Offers: How They're Processed

---

## Merge Candidates With Job Offers
*Chunk ID: OHR-USE-0295 | Chapter: Job Offers | Guide: Using Recruiting*

You can merge candidate files when candidates have more than one active or inactive job offer.
You can merge candidate files:
• When the candidate is in any phase before the Offer phase.
• When the candidate is in any state of the Offer phase.
• When the candidate is in any phase after the Offer phase.
Below are some scenarios.
Scenario 1: When the beta (external) candidate is in any phase before the Offer phase (No offer created on Job
Application 1)
In this scenario, you can click the Check Duplicates action from the job application or candidate search screens to find
potential duplicates and merge the records. If there's an active offer (Job Application 2) for the same beta candidate,
then a warning message will appear at the time of merge. When you click Continue, the Job Application 2 will be
automatically moved to the Rejected by Employer state and the beta (external) candidate will be successfully merged
with the alpha record (ex-employee or employee).
Scenario 2: When the beta (external) candidate is in the Offer phase or any phase after the Offer phase (Existing
job offer on Job Application 1)
You can use the below 2 options to merge the records:
• Click Check Duplicates action from job application screen to find potential duplicates
In this option, if there's no other active offer for this beta candidate, a warning message will appear at the time
of merge. When you click Continue, then the Job Application 1 will be moved to Rejected by Employer and the
beta (external) candidate will be successfully merged with alpha record (ex-employee or employee). You'll need
to select the Inactive filter to find the job application and then you can redraft the job offer.
If there's an additional active offer (Job Application 2) for the same beta candidate, a warning message will
appear at the time of merge. When you click Continue, then both job applications (1 and 2) will be moved to
Rejected by Employer and the beta (external) candidate will be successfully merged with alpha record (exemployee or employee). You'll need to navigate to the specific job requisition and select the Inactive filter to
find the job application of the beta candidate which you want to proceed with, and then you can redraft the job
offer.
• Move the beta record to HR phase which automatically triggers post offer duplicate merge process and bring
the record to Error in processing state
• In this option, if there's an active additional offer (Job Application 2) for the same beta candidate, a warning
message will appear at the time of merge. When you click Continue, then only Job Application 2 will be moved
to Rejected by Employer and the beta (external) candidate will be successfully merged with alpha record (exemployee or employee). Once the merge process is complete, you'll be directed to the Recreate Job offer screen
and you'll see all the details from beta Job Application 1 offer only if you click continue to revisit all the sections
on the job offer page.

---

## Check and Merge Duplicates After Job Offer
*Chunk ID: OHR-USE-0296 | Chapter: Job Offers | Guide: Using Recruiting*

After an external candidate accepts a job offer and moves to the HR phase, a check can be automatically done to verify
if the candidate is a duplicate of a person in the database. If that's the case, the two candidate records can be merged,
the offer can be recreated for the preexisting person, and the recruiting process can be completed.

---

## Checking for Duplicates During the Move to HR
*Chunk ID: OHR-USE-0297 | Chapter: Job Offers | Guide: Using Recruiting*

When external candidates are moved into the HR phase, each candidate can be checked for possible duplicates against
all workers, ex-workers, contingent workers, ex-contingent workers, and even against contacts and beneficiaries who
have information in the database. This check is automated and can be configured to occur only as part of the Move
to HR action, regardless of whether this move is done manually or automatically. This final check complements any
previous checks in this candidate's lifecycle that searched for duplicates among all other candidates, which can be done
manually or automatically before the Offer phase.
If any potential duplicate records are found while the external candidate gets moved to the HR phase, their job
application will go into the HR - Error During Processing status. They won't go into the usual HR - Processing in
Progress status with a pending worker record created for them. A message banner notifies you of the candidate's
duplicate-related situation, and an email notification can also be sent.
For candidates in the HR - Error During Processing status due to a possible duplicate, the menu can display the View
Duplicates action (replacing the Check Duplicates action that usually compares a candidate against other candidates).
A View Duplicates button can also appear in the message banner. It's visible by default to the recruiting team looking
at the job application on the requisition, and possibly to the HR specialist looking at the candidate's page in the Job
Offers area. This View Duplicates action is available to any user with the privilege Perform Candidate Duplicate Check
and Merge (IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE) and duty role Perform Candidate Duplicate
Check and Merge (IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE_PRIV_OBI).
When you click the View Duplicates action, a list displays all people who are potential duplicates of this candidate, with
identifying information such as person name, person type (even if there's no work relationship), business title, business
unit. You can also see if the potential duplicates have the same date of birth and national ID as the candidate. If that info
isn't available, it means that the candidate, or the potential duplicate, or both have null values for the national identifier
or date of birth respectively. Also, if the candidate or potential duplicate has a national identifier of a different type,
the National ID Match field displays Not Available. For example, the candidate has a Social Security Number issued in
the United States, and the potential duplicate has a Matrícula Consular de Alta Seguridad issued in Mexico. When you
view the list, you have to decide whether any of these people is truly a duplicate of the current candidate, or only shares
some similar information. The definition of a duplicate is configured by your administrator, based on matching or null
values in some or all the following fields: last name, first name or first initial, date of birth, gender, and national identifier
and its type and country.

Note: To view sensitive information match indicators, you need these privileges:
• Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE)
• Manage Person National Identifier Data (PER_MANAGE_PERSON_NATIONAL_IDENTIFIER_DATA)
• Display Recruiting Duplicate Check with Sensitive Info Match
(IRC_DISPLAY_RECRUITING_DUPLICATE_CHECK_WITH_SENSITIVE_INFO_MATCH)

---

## Merging the Candidate with the Correct Person
*Chunk ID: OHR-USE-0298 | Chapter: Job Offers | Guide: Using Recruiting*

You might decide that none of the potential duplicates of the candidate are truly the same person. In this case, the
HR specialist should process the candidate's job application by performing the action that was originally selected
when their offer was drafted, such as Add Pending Worker. However, if this candidate turns out to have the same
national identifier as an existing person, it might not be possible to complete their pending worker record successfully,
depending on whether the application has been configured to require these IDs to be unique.
If you decide that one of the duplicates really is the same person as the candidate, you can merge the two records
together. The candidate's new up-to-date information gets added to the existing person's profile as follows:
• Person-related info is merged: The candidate's email addresses, phone numbers, and attachments are all
added to the person's record, if these weren't already known. The person's name and address are only updated
if the candidate's info is more recent, and only if the person is an ex-worker, not a current worker.
Note: When merging candidate records, the ex-employee home address is updated only if the external
candidate is more recent than the one on file. That's because external candidate's records shouldn't have any
other address type. Any other address type or with previous date will remain the same. Same type of address
will be updated in the ex-employee record if a later date exists in the external candidate record.
• Recruiting-related info is merged: The candidate's interviews, assessments, and any talent communities, pools,
and campaign memberships are moved to the person's record. All the candidate's past job applications are also
moved to the person's record, including the current one which moves to the person in the Offer - Draft status.
After the merge is complete, this candidate is no longer visible in searches or other areas of Oracle Fusion Cloud
Recruiting. The duplication has been removed and the person is retained. Merge reports are attached to the person's
record for further reference and traceability.
Note: The candidate can have potential duplicates of many different person types, but not all types can be merged.
Candidate records can be merged with workers or ex-workers, but not with contacts, nonworkers, or pending workers.
For a potential duplicate who's a pending worker, the record can be converted to a worker and then the merge with the
candidate will succeed.

---

## Recreating the Offer for the Correct Person
*Chunk ID: OHR-USE-0299 | Chapter: Job Offers | Guide: Using Recruiting*

It's possible that everything in the candidate's job offer will remain appropriate for the retained person after the merge is
done, but you need to verify the info. A message banner and an alert can inform you that the merge happened, and that
the new person's job application is now in the Offer - Draft status. Recruiting users such as hiring managers with only

the privilege Initiate Job Offer (IRC_INITIATE_JOB_OFFER_PRIV) will be unable to review the draft offer after it has been
recreated for the retained person. But recruiters with the privilege Update Job Offer (ORA_IRC_UPDATE_JOB_OFFER)
can do so.
After the merge is complete, you immediately arrive at the recreated offer page. Here you'll revisit every section of
the offer that's now being drafted for the retained person. All the previous values from the candidate's original offer
are prefilled in every section of this page. You must continue through every section before saving or submitting this
offer for the first time, to ensure that the original values get recopied into the assignment, payroll, salary, and other
compensation sections. You can make any changes to the offer values while in the Draft state, as usual.
Note: When you access the job offer the first time, the start date and legal employer aren't editable. However, if you
save and close the offer and go back in, you'll be able to edit these two fields.
If this offer was originally based on a position, any fields that are configured to be sync will be updated into the new
offer from the position and will be read-only, as usual. Fields that aren't sync retain the values of the original offer and
can be edited.
Occasionally some candidate's original values aren't valid for the retained person. For instance, new hires are eligible
for certain bonuses whereas current employees or rehires aren't eligible based on your configurations. Any information
that's no longer allowed in the person's offer will be identified or removed, to ensure that the recreated offer follows all
your organization's business rules. In case the original or adjusted offer letter had been based on a template that's only
available to external candidates, this too will need to be revisited.

---

## Completing the Offer Phase for the Correct Person
*Chunk ID: OHR-USE-0300 | Chapter: Job Offers | Guide: Using Recruiting*

When you're done drafting the recreated offer for the retained person, you have a choice to proceed through the rest
of the recruiting states, or to bypass the process and go directly to the HR phase. Upon clicking Submit, you can choose
one of these paths:
• Bypass the Process: Because the original candidate's offer had already been approved, accepted, and reached
the point of moving to the HR phase, you can decide to bypass all these states for the retained person's
job application and return it immediately to the HR phase. The new offer will bypass any approval, it will be
accepted on behalf of the person by the user who made this decision, and it will skip any custom phases that
have been configured between the Offer and HR phases.
• Follow the Process: If you decide that a new approval or new offer letter is desirable, you can decide to move
this job application through each state in the recruiting lifecycle as usual. It's possible that offer approval
rules have been configured to treat merged person offers differently than original offers. If this original offer
had been extended to the candidate, this new offer will also need to be extended again, for another light esignature from the retained person or for a user to accept it on their behalf. It's possible that additional rules
were configured to move merged person offers into the HR phase automatically after acceptance, or after any
intervening custom phases that have been configured between the Offer and HR phases.
Finally the recreated offer in the retained person's new job application arrives in the HR phase, ready to be processed
into a new assignment. As usual, the job application will land in the HR - Pending Manual Processing status for an
internal candidate, or in the HR - Processing in Progress status for a rehire who will be getting a new pending work
relationship, or possibly in HR - Error During Processing if there's another problem.

---

## HR Specialist vs Recruiter Privileges
*Chunk ID: OHR-USE-0301 | Chapter: Job Offers | Guide: Using Recruiting*

Users who have the equivalent of the HR Specialist role can see candidate job applications in the HR - Error During
Processing status, can read the message banner explaining that they might be a duplicate, and can reach the list of

possible duplicates. To perform the merge with a selected existing person record, these users need to be granted the
following:
• Functional privilege Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE)
• Role for tracking purposes Perform Candidate Duplicate Check and Merge
(IRC_PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE_PRIV_OBI)
After performing a merge, these HR specialists will rely on Recruiting users to recreate the job offer for the merged
person, because by default HR specialists don't have the necessary additional privileges such as Update Job Offer. HR
users will return to the main list of job offers in the Manage Job Offers work area after they perform a candidate merge.
An alert can be sent automatically to inform the recruiter that a draft offer is waiting to be reviewed.

---

## Profile Option to Restrict Candidate Merge With Offers
*Chunk ID: OHR-USE-0302 | Chapter: Job Offers | Guide: Using Recruiting*

The following table explains the behavior when the profile option Restrict Candidate Merge With Offer
(ORA_IRC_RESTRICT_MERGE_WITH_OFFERS) is enabled.

---

## HR phase (move to HR) No
*Chunk ID: OHR-USE-0303 | Chapter: Job Offers | Guide: Using Recruiting*

pre-move to HR)

change in behavior with

Offer"
N (default setting) - Merge

profile option
Yes

is allowed

---

## Merge is allowed and
*Chunk ID: OHR-USE-0304 | Chapter: Job Offers | Guide: Using Recruiting*

applications are moved to

applications are moved to

all applications are

the Rejected by Employer

the Rejected by Employer

moved to the Rejected by

state.

state.

---

## Merge is allowed and all
*Chunk ID: OHR-USE-0305 | Chapter: Job Offers | Guide: Using Recruiting*

applications are moved to

applications are moved to

the Rejected by Employer

the Rejected by Employer

state.

state.

Merge isn't allowed.

Merge isn't allowed.

Merge is allowed.

Merge isn't allowed.
Merge is allowed after
manually deleting other
applicationswith offers.

---

## Y (default setting) - Merge
*Chunk ID: OHR-USE-0306 | Chapter: Job Offers | Guide: Using Recruiting*

No

Merge isn't allowed.

Merge isn't allowed.

Merge is allowed.

is not allowed

---

## Job Offers Respect Headcount of Job Requisitions and
*Chunk ID: OHR-USE-0307 | Chapter: Job Offers | Guide: Using Recruiting*

Positions
As candidates move through the lifecycle, validations are done to check if the business still needs an additional worker
or whether the opportunity is no longer available. This includes checking whether the requisition still has openings

and, for position-based offers, whether the position still has enough open headcounts and vacant FTE as of the offer's
intended start date.
Your administrator can configure the application to fully control how to manage requisitions and positions to ensure
offers don't exceed various limits.
• Communicate Job Offers Ignoring Requisition Limits: This requisition-related privilege allows Recruiting users
to hire more candidates than the number of openings on the requisition.
• Number of Incumbents Validation: This position-related setting controls whether all positions' headcount is
enforced across your organization. When the setting is disabled, no verification is done to check if there are still
open headcounts and vacant FTE in any position.
• Allow Overlap: This option is available for each position to control whether extra people can be hired when that
position's headcount and FTE limit have been reached.
When are these limits considered to be reached?
• A position considers a candidate to be an incumbent as of their proposed start date, as soon as their job
application has reached the status Offer - Extended in the recruiting lifecycle (and all later states, except the
states Withdrawn by Candidate or Rejected by Employer in any phase).
• A requisition increases its count of hired people as soon as a candidate reaches the HR phase, which is the final
phase of the recruiting lifecycle (unless they're in the states Withdrawn by Candidate or Rejected by Employer,
or Pending Automated Processing in that phase).

When Are Verifications Done
Here's when validations are performed in the job application's lifecycle:
• When using the Submit button: A job offer can be drafted for a candidate's job application regardless of any
limits, but when the user is ready to submit it into the approval cycle, these validations occur. When clicking
the Submit button in the flow Create Offer or Edit Offer, the user might receive a warning or error message.
This saves time for the approvers because the job offer can't be submitted if the requisition doesn't have
any remaining openings - unless the user has the privilege to ignore this limit. The draft offer also can't be
submitted if it has a position which doesn't have enough open headcount or enough vacant FTE (unless the
Number of Incumbents Validation is disabled). However, if the position is configured to allow overlap, the user is
warned that this candidate will be overfilling the position as of their offer start date, but they're given the choice
of continuing anyway and submitting the draft offer for approval.
• When using the Extend Offer action: By the time the user is ready to extend the draft job offer to the candidate,
it's possible that the requisition or position was updated or became filled, so that no room now remains for this
candidate. The same validations are performed before the status can be moved to Offer - Extended, displaying
the appropriate error or warning based on the requisition and any position according to the relevant privilege,
setting, and option above.
• When the automatic action Extend Offer is triggered in the candidate selection process: If the requisition's
candidate selection process is configured to extend job offers, either immediately or after a delay, these
validations occur. However, as there's no Recruiting user to consider any warnings, only errors can prevent the
action and leave the job application in the status Offer - Approved. The requisition's count of hired candidates
isn't checked by default, but the automatic progression can be configured to prevent the extend of the offer
if the requisition is full. For position-based offers, the position's number of incumbents is checked, and the
automatic action is successful if the position has room or if it allows overlap. If there's no room, and the position
doesn't allow overlap, the candidate's job application remains in the status Offer - Approved.
• Never During Accept: As long as the job offer is in the state Extended, the candidate isn't prevented from
accepting the offer. This is also true for the Recruiting user who might accept the offer on behalf of the
candidate. Even if the requisition or any position was updated or became filled in the meantime, the candidate

and users aren't informed of these limits. It will be the responsibility of the HR specialists to reconcile any
problems after this point.
• During Move to HR, using the menu action or the automatic candidate selection process action: When the
candidate moves into the HR phase, no further validation is done for the requisition's limits. It's still important
to not overfill a position's headcount and FTE, so these validations do occur if the offer has a position.
The move into the HR phase is always successful. However, the Recruiting user needs the HR specialist to
reconcile any issues that arose from position changes in the meantime. If the position will already have enough
headcount or FTE as of the offer's start date, the candidate will be moved into the HR phase but in the state
Error During Processing. If the position does allow overlap, the candidate will be moved into the HR phase
without a problem, although the warning will be visible in the Errors section of the Offer page. If the move to
HR is done automatically using a process (not manually), the warning message alert will be sent to the hiring
manager.

---

## Job Offer Multilingual Content
*Chunk ID: OHR-USE-0308 | Chapter: Job Offers | Guide: Using Recruiting*

Oracle Fusion Cloud Recruiting is available in multiple optional languages to deliver a multilingual recruiting experience.
When you sign in Oracle applications, you can select your session language in your user preferences. American English
is the default session language for the first visit (the application remembers the last session language). The session
language you select defines the language of every label in a product. The session language is used as the creation
language. For example, Spanish is installed in the environment. If you sign in Spanish, you create job requisition
templates in Spanish.
When you view job offers on the Job Offers list, requisition titles are displayed in your session language (not in the
candidate job application language). This way, you can see the same job requisition title for all candidates who applied
on the requisition no matter which language they used to apply.
When you view the details of a job offer for a candidate, a field indicates the language used by the candidate to apply for
the job. The Additional Text 1 and 2 appear in the language in which they were created by the Offer Team, and so does
the uploaded adjusted offer if any.
When you do a keyword search on the Job Offers list, the search retrieves all job offers where the word is found, that is
the job requisition title in your session language and in each recipient's language.
When you preview a job offer, the content of the job offer appears in the candidate job application language.
When candidates receive a job offer, they view job offers in their job application language, this includes the language of
the actions Accept and Decline.

---

## Number of Job Offers for a Candidate
*Chunk ID: OHR-USE-0309 | Chapter: Job Offers | Guide: Using Recruiting*

A candidate can apply to multiple job requisitions and therefore have multiple job applications.
When a candidate accepts a job offer and it's handed off to HR, all of the candidate's other active job applications get
withdrawn. However, if you know that the candidate wants to be considered for additional jobs, you can manually revert
back any of those automatically withdrawn job applications into the previous active state.

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0310 | Chapter: Job Offers | Guide: Using Recruiting*

15 HR Specialists and Job Offers
Job Offers: How They're Processed in HR
As an HR specialist, you process the job offers of candidates after they accept the offers. The HR phase is the last phase
in the recruiting lifecycle. This is when HR assignments are created for new or existing workers.
The Job Offers page that you access from the Manage Job Offers quick action displays all candidates who accepted
their job offers (and possibly completed any intervening phases).
Note: Make sure you have the required data security to view people and assignments you want to see.
If you want to process the job offers, each candidate needs to get an appropriate HR assignment and possibly a new
work relationship too, based on the approved and accepted job offer. All offer values are automatically copied into the
pending worker record for external candidates. They are copied into the fields in the relevant HR pages when you start
processing offers for most internal candidates.
These job offer details contain almost all the information required for the new assignment, including the salary. If the
recruiting team or offer team didn't specify some fields in the job offer, you can enter these values here, or update any
values as necessary. After you submit the new HR assignment or convert the pending worker, recruiters in the Hiring
work area will soon see the final completed state of the candidate's job application.

---

## Job Application States Within the HR Phase
*Chunk ID: OHR-USE-0311 | Chapter: Job Offers | Guide: Using Recruiting*

Job applications move to the HR phase after completing all other phases of the candidate selection workflow.
As an HR specialist, you can view the states of these job applications on the Job Offers page, which you can access
using the Manage Job Offers quick action, in the My Client Groups. As you change these states to finish processing
candidates, users in the Hiring work area will also be able to see the new states and watch as the candidate job
applications get successfully processed.
The table presents the states within the HR phase.

State

Description

---

## Job offers in this state are awaiting an HR specialist to process them to finalize their worker
*Chunk ID: OHR-USE-0312 | Chapter: Job Offers | Guide: Using Recruiting*

assignments. This usually includes internal candidates who have been moved to the HR phase,
and possibly any external candidates who need manual reprocessing. If any errors arise during the
subsequent flow, error messages are displayed and the HR specialist needs to resolve the errors. These
errors aren't tracked further, so the state doesn't change to Error During Processing after this state.

---

## Pending Automated Processing
*Chunk ID: OHR-USE-0313 | Chapter: Job Offers | Guide: Using Recruiting*

If an auto-progression into the HR phase is configured, this is the state into which most candidates all
get moved initially.
• External candidates are moved in the state Processing in Progress as soon as a Pending Worker
record has automatically been created based on that offer.

State

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0314 | Chapter: Job Offers | Guide: Using Recruiting*

Description
• If the automated process is enabled, internal candidates go into the state Pending Automated
Processing. As soon as the proposed start date approaches, the new assignment gets created and
then the state becomes Processing in Progress, then Processed.
• For internal candidates in complex job offer situations, if the automated process is enabled,
internal candidates go into the state Pending Automated Processing. As soon as the proposed
start date approaches, the new assignment gets created and then the state becomes Processing
in Progress, then Processed.
If some problem arises during these automatic state changes, the candidate job applications go into
the state Error During Processing instead. The HR specialist will view the errors and resolve them.
If the HR specialist needs to move a given candidate out of the state Pending Automated Processing
more quickly than the configured frequency, they can use the Quick Process Offer action.

---

## Error During Processing
*Chunk ID: OHR-USE-0315 | Chapter: Job Offers | Guide: Using Recruiting*

When a job offer encounters a mismatch or problem in its automated processing, the offer goes into
the state Error During Processing. Errors can also occur for external candidates if a potential duplicate
person record is found (when this check is enabled). If the recruiting user performed the Move to HR
action, they're informed of the error and the HR specialist will need to resolve it.
These errors are also shown in a banner and a section named Errors on the candidate's Job Offer page,
visible to both the recruiter in the Hiring work area and the HR specialist from their Job Offer list. If the
Move to HR was performed using auto-progression, the team can still get informed about any error by
a notification.
After the HR specialist has resolved the situation causing the error, they can try again to progress the
candidate forward through the lifecycle. If there are additional errors, an error message will appear
and the state will remain Error During Processing. If the action is successful for an external candidate,
then a pending worker will be created and the state will become Processing in Progress until the new
pending worker is converted. If the action is successful for an internal worker, the state will become
Processing in Progress until the new flow is submitted and approved.
Users who have the equivalent of the seeded HR Specialist role can see candidate job applications in
the status HR - Error During Processing, can read the banner explaining that they may be a duplicate,
and can reach the list of possible duplicates. To perform the merge with a selected existing person
record, these users need to be granted the following:
• functional privilege Perform Candidate Duplicate Check and Merge (IRC_PERFORM_CANDIDATE_
DUPLICATE_CHECK_AND_MERGE_PRIV )
• role needed for tracking purposes Perform Candidate Duplicate Check and Merge (IRC_
PERFORM_CANDIDATE_DUPLICATE_CHECK_AND_MERGE_PRIV_OBI) After performing a merge,
these HR specialists will rely on Recruiting users to recreate the job offer for the merged person,
because by default HR specialists don't have the necessary additional privileges such as Update
Job Offer. HR users will return to the main list of job offers in the Manage Job Offers work area
after they perform a candidate merge, and an alert can be sent automatically to inform the
recruiter that a draft offer is waiting to be reviewed.

---

## Processing in Progress
*Chunk ID: OHR-USE-0316 | Chapter: Job Offers | Guide: Using Recruiting*

This is the state where all candidates go as they move successfully forward through the lifecycle.
• For external candidates, it means that a pending worker has been created based on that offer.
• For internal candidates, it means that the appropriate action is underway to create the new
assignment.

Processed

This is the final state where all successful candidates end up after their new assignment is committed
to HR. This means when the pending worker has been converted to a worker with an assignment, or
when the internal candidate's assignment has been created. The Processed state is the final successful
state in the final HR phase of the job application lifecycle.

---

## Rejected by Employer
*Chunk ID: OHR-USE-0317 | Chapter: Job Offers | Guide: Using Recruiting*

This state indicates that the employer's decision ended the hiring process. The HR specialist has for
some reason rejected the candidate after the candidate accepted the job offer. Consequently, no new
worker assignment exists for the candidate.

---

## Withdrawn by Candidate
*Chunk ID: OHR-USE-0318 | Chapter: Job Offers | Guide: Using Recruiting*

This state indicates that the candidate's decision ended the hiring process. The HR specialist has
withdrawn the candidate because they requested it after they accepted the job offer. Consequently, no
new worker assignment exists for the candidate.

---

## External Job Offers: How They're Processed
*Chunk ID: OHR-USE-0319 | Chapter: Job Offers | Guide: Using Recruiting*

An external job offer refers to the offer extended to a candidate who has no current work relationship with the
organization. The candidate may have no previous work relationship (new hire) or a previous work relationship (rehire).
After the new hire or rehire gets moved to the HR phase, a pending worker or pending work relationship is automatically
created based on the offer details. The values in the pending work relationship are copied directly from the candidate's
approved and accepted job offer. This pending worker or pending work relationship is displayed in the Pending Workers
quick action, in My Client Groups. After the external candidate becomes a pending worker, their job application isn't yet
complete, it's in the status HR - Processing in Progress. After that pending worker gets converted to a worker, then the
candidate's recruiting lifecycle is successfully completed. The new status of the job application becomes HR - Processed
and is displayed to recruiters in the job application, and to HR specialists on the list that they access using the quick
action called Manager Job Offers.

---

## Job Offer Processing
*Chunk ID: OHR-USE-0320 | Chapter: Job Offers | Guide: Using Recruiting*

The following points describe how you as an HR specialist process external job offers as soon as they have been moved
to HR.
• External job offers usually appear on your Job Offers list initially in status HR - Pending Automated Processing.
Then, without any action needed from users, they go into HR - Processing in Progress. This is because usually
a pending worker or pending work relationship has automatically been created, which is the appropriate next
step for a new hire or a rehire. No action is required on the Job Offers list. This status change is based on the
scheduled process Complete Recruiting Process.
• When you convert the pending worker or work relationship into a worker, and this transaction is submitted and
approved, the offer status automatically changes to HR - Processed. This status change is also based on the
scheduled process Complete Recruiting Process.
• The new status HR - Processed is also reflected in the job application in the Hiring work area, indicating to
Recruiting users that the overall candidate lifecycle is complete.
• External candidates who reach the status HR - Processed remain on your Job Offers list, but no further action is
required. This is the final successful state in the entire recruiting process.

---

## Exceptions in Job Offer Processing
*Chunk ID: OHR-USE-0321 | Chapter: Job Offers | Guide: Using Recruiting*

One exception to the above series of steps to process external candidates is if there's some error in creating the pending
worker or pending work relationship automatically. The error may be due to a recently inactivated work location, for
instance, or the associated position suddenly being frozen or filled. Or the error may be due to finding a possible

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0322 | Chapter: Job Offers | Guide: Using Recruiting*

duplicate of the new candidate. In any of these situations, the job offer lands in status HR - Error During Processing, and
the errors are displayed in the message banner and the Error section.
After you fix the situation that caused the error, or if you decide to disregard the potential duplicate records, you can try
to perform the action again. If the Process Now action appears, you can use it to create the pending worker as originally
intended. If the Add Pending Worker action appears, you can use it to enter the guided process Create Pending Worker
or Create Pending Work Relationship with the offer's values prefilled. Here you must change any field or resolve any
issue that was preventing the pending worker from being created. You must visit every section to ensure that the field
values that were promised in the offer get copied into the new assignment. Then submit this information to create the
pending worker or pending work relationship. When this succeeds, the status changes to HR - Processing in Progress.
There is usually no need to take any action on the external candidate who has reached the status HR - Processing in
Progress. The action Return to Manual Processing is available on the HR specialist's menu, but instead the candidate
is expected to proceed automatically into the status HR - Processed. After the corresponding worker is created by
converting the pending worker, the status change occurs based on the scheduled process Complete the Recruiting
Process.
As an HR specialist, you only need to use the action Return to Manual Processing on external candidates after an
attempt to manually create a pending worker was interrupted, and you need to make another attempt. This rare
situation can arise as follows:
1. The candidate has been moved into the HR phase.
2. Some error occurred and they go into status HR - Error During Processing.
3. The HR specialist performed the action Add Pending Worker, which changed the candidate's status to HR Processing in Progress.
4. The user landed on the HR guided process where the offer values are prefilled in the pending worker's fields.
5. The HR specialist was unable to submit the flow Add Pending Worker, due to lack of time for instance, so they
canceled it.
6. Now the candidate's offer is no longer getting recreated as a pending worker, though the status is still HR Processing in Progress. And there is no way for the HR specialist to continue where they stopped in creating the
pending worker based on the offer's values.
7. Now you must use the action Return to Manual Processing to restart creating a pending worker. This action
changes the candidate's status from HR - Processing in Progress to HR - Pending Manual Processing.
8. In status HR - Pending Manual Processing, you will again see the action Add Pending Worker.
9. You must perform the action Add Pending Worker, which again changes the candidate's status to HR Processing in Progress.
10. You will land on the HR guided process where the offer values are prefilled in the pending worker's fields, and
you can proceed from this point.
Other rare exceptions to the above series of steps are when the candidate's situation changes after their candidate's
offer was drafted.

---

## Resulting Actions
*Chunk ID: OHR-USE-0323 | Chapter: Job Offers | Guide: Using Recruiting*

When the pending worker is created successfully, then after the standard Convert process, the candidate will be ready to
become a worker on the projected start date. On the start date:
• You can view the person's resume in the Talent Profile.
• You can view the job offer letter in the person's Document Records.
• You can view the job application's cover letter and social media attachments in the person's Document Records.
• The person is no longer considered as an external candidate for the purposes of recruiting and job searching.
• The person can view and apply for jobs that are posted for internal candidates.

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0324 | Chapter: Job Offers | Guide: Using Recruiting*

• The person's job application Talent Profile data appears in their Skills and Qualifications (Me > Career and
Performance > Skills and Qualifications).

---

## Internal Job Offers: How They're Processed
*Chunk ID: OHR-USE-0325 | Chapter: Job Offers | Guide: Using Recruiting*

An internal job offer refers to the offer extended to a worker who has a current work relationship with the organization.
When the internal job application is moved to the HR phase, the offer is listed in the Job Offers page, available using the
Manage Job Offers quick action.
When recruiters originally draft each job offer, they need to select the Human Resources (HR) action that will be
appropriate to use for processing this assignment, based on the offer's information and the candidate's existing work
relationship if any. This HR action is preselected based on the information available in the job offer and the candidate's
existing work relationship. Now in the HR phase the appropriate records need to be created to give this candidate their
promised new assignment. Creating these records can be done manually by an HR specialist, or automatically if autoprocess is enabled. The type of the internal job offer, whether it's a global change, a local change, a change worker type,
determines how it must be processed. For details, see Actions Available Based on Employment Scenarios.
Note: When you're selecting the action to process the assignment, make sure you click through each of the sections
before submitting the action to ensure the latest data is processed successfully.

Note: You need the appropriate privileges to perform the HR actions for each type of internal job offer.

---

## Job Offer Processing Methods
*Chunk ID: OHR-USE-0326 | Chapter: Job Offers | Guide: Using Recruiting*

As an HR specialist, you might have different ways to process internal candidates who aren't in complex situations.
Automatically Process Internal Candidates in the HR Phase (if your administrator enabled the feature): Internal
candidates who accepted their job offer and were moved to the HR phase can be automatically processed into their new
roles in the HR system as their proposed start date approaches.
When the automated processing capabilities are enabled, most internal candidates reach the HR phase in the state
Pending Automated Processing. When their proposed start date approaches, the new assignment is automatically
created from their offer. Each candidate’s state becomes Processing in Progress when the assignment is successfully
created, and becomes Processed when the assignment is approved and committed as the candidate’s new job.
Every internal candidate will be automatically processed when their assignment’s proposed start date is 7 days or fewer
from today, by default. Administrators can configure the desired number of days in advance of the start date.
If some problem arises while automatically processing the offer into the new assignment, the candidate’s job application
will automatically move from the state Pending Automated Processing into the state Error During Processing. These
errors can occur for the usual reasons, such as the offer’s intended position suddenly has a hiring status of Frozen,
or the offer’s promised location has been inactivated. If the situation causing the error can be resolved, you can try
processing the candidate again, using either the manual process or the Quick Process Offer action. However this offer
won't get automatically processed again, regardless of its approaching start date.
Note: If your organization is using Payroll-based Salary Basis in their offers, or has salary element eligibility defined
on Payroll, the Payroll section should be populated during the offer creation to avoid any errors when the job
application of the internal candidate is moved to HR phase.

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0327 | Chapter: Job Offers | Guide: Using Recruiting*

For internal candidates in a complex hiring situation, they still go into the state Pending Manual Processing and you'll
still need to manually process them. Any candidates in complex hiring situations usually arrive in the HR phase in
the state Pending Manual Processing, even if the automated processing feature is enabled. These offers won't be
automatically processed; they need to be manually processed as usual. For details, see Complex Job Offers: How They're
Processed.
Quickly Process Internal Candidates in the HR Phase (if your administrator enabled the feature): As an HR
specialist, you can use the Quick Process Offer action in the Manager Job Offers page to process most internal
candidates into their new assignment with a single click after they're moved to the final HR phase of the recruiting life
cycle. You can process candidates as early as you want, as you don’t have to wait for the automatic processing date to
arrive for each candidate.
When you use the Quick Process Offer action, you don't review all the offer information while creating the new
assignment and you can’t change any values. This ensures consistent information from each accepted offer is copied
identically into each new assignment and salary.
You can use the Quick Process Offer action for most internal candidates in the following states of the HR phase:
• HR - Pending Automated Processing
• HR - Pending Manual Processing
• HR - Error During Processing
The Quick Process Offer action isn’t available for candidates in complex hiring situations, even if this feature is enabled.
These offers need to be manually processed as usual. For details, see Complex Job Offers: How They're Processed.
Manually Process Internal Candidates in the HR Phase: As an HR specialist, you can manually process any internal
job offers shown on the Manager Job Offers page into their new assignment. Regardless of whether the automated
process and quick process are enabled, you can go into the selected HR action's flow, go through all its sections, review,
and even change the original values from the offer while creating the worker's new assignment.
You can manually process internal candidates in the following states of the HR phase:
• HR - Pending Automated Processing
• HR - Pending Manual Processing
• HR - Error During Processing
You first select the HR action that was chosen while the offer was drafted. When you confirm your intention to process
the candidate, their job application status reflects this by changing automatically from HR - Pending Manual Processing
to HR - Processing in Progress. This new status is visible on your Job Offers list and also in the job application in the
Hiring work area.
You then arrive at the appropriate HR guided process, which has field values populated from the job offer. For example:
• If you selected and confirmed the Global Transfer action, you can view the Local and Global Transfer guided
process with the offer title, assignment, salary, and all other values populated from the offer.
• If you selected an action of type Promote, Transfer, or Change Assignment, you can view the Change
Assignment flow with all the values populated from the offer.
You need to visit every section to ensure that these values get copied into the new assignment. At this stage, you might
change the populated values and add information in other fields. However, be careful when considering changes to any
information that was already viewed and understood by the candidate or offer approvers.

---

## Job Offer Process Completion
*Chunk ID: OHR-USE-0328 | Chapter: Job Offers | Guide: Using Recruiting*

After the internal candidate’s new assignment is submitted, using any of the available methods, they remain visible on
the list in the status HR – Processing in Progress. Their assignments might be awaiting approvals if configured for their
transaction, and no further action is required.
When the transaction is approved, the offer status will soon automatically change to HR - Processed based on the
scheduled process Complete the Recruiting Process.
Internal candidates who reach the status HR - Processed remain on your Job Offers list, but no further action is
required. This is the final successful status in the entire recruiting process.
The new status HR - Processed is also reflected in the job application in the Hiring work area, indicating to Recruiting
users that the overall candidate lifecycle is complete.

---

## Exceptions During Job Offer Processing
*Chunk ID: OHR-USE-0329 | Chapter: Job Offers | Guide: Using Recruiting*

An exception to the above series of step to process internal candidates is for current workers who already have two or
more job assignments. For more information about processing offers in these complex situations, see Complex Job
Offers: How They're Processed.

---

## Interruptions in Job Offer Processing
*Chunk ID: OHR-USE-0330 | Chapter: Job Offers | Guide: Using Recruiting*

When you process job offers, you might have to handle unforeseen changes. For example, you plan to process a
candidate and you're working on the appropriate HR guided process, when you unexpectedly need to cancel out the
flow without submitting. This might occur due to some mismatch with the data, or simply due to lack of time to finish
reviewing all the fields. In such cases, the job application is now in status HR - Processing in Progress on the Job Offers
list, and your processing has stopped for now.
To start processing it again, after the mismatched data has been fixed or when time allows, you'll still want to enter the
HR guided process with the offer values filled in advance. To restart from this point, you first need to use the Return to
Manual Processing action, which changes the status from HR - Processing in Progress back to HR - Pending Manual
Processing. Or you or another HR specialist can choose the Quick Process Offer action (if enabled) to perform the
processing of this internal candidate immediately without stepping through the flow again.

---

## Changing the Proposed Start Date
*Chunk ID: OHR-USE-0331 | Chapter: Job Offers | Guide: Using Recruiting*

As an HR specialist, you might be able to change the proposed start date for internal candidates after they've accepted
their job offer, in case the intended date in their offer now needs to be adjusted before their new assignment is
processed.
If your administrator enabled this feature, you use the Change Start Date action to fix the agreed-upon start date that
was in the job offer. This new date will be used when transforming the offer into the new assignment either by using
the automatic processing option, or the Quick Process Offer action, or by using the method where you click through
the guided process to review all the values from the offer. This changed date won't affect the candidate's job offer letter
which was already accepted.
Here’s some more information to consider if you change the proposed start date for candidates:
• The candidate's offer letter and Document Records won't contain this new date. If you need the candidate
to see the new date in their offer letter, you need to move the job application to the Rejected by Employer
or Withdrawn by Candidate state, redraft the offer to add the new date, get an approval for the new offer if
needed, then extend the offer again to the candidate. Then, the candidate needs to accept the offer again.

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0332 | Chapter: Job Offers | Guide: Using Recruiting*

• You can select a new proposed start date anytime in the future or anytime in the past. However, you can't
select a date earlier than when the original offer was drafted nor select a date that will change the worker's
employment or salary.
◦ Changes to the employment could be for example if the worker already had an upcoming termination
date, and you tried to change the date to a time after the worker left the company. Or, the worker was
already planning to take on a second job by the time of the proposed change.
◦ Changes to the salary could be for example if the new job would start so far in the future that a futuredated grade change or grade ladder change would calculate a difference in salary for the worker by that
time.

---

## Resulting Actions
*Chunk ID: OHR-USE-0333 | Chapter: Job Offers | Guide: Using Recruiting*

When the new records have been created successfully, the new assignment is ready to begin on the projected start date.
By the start date:
• You can view the person's resume from this job application in the Talent Profile.
• You can view this job offer letter in the person's Document Records.
• You can view this job application's cover letter and social media attachments in the person's Document
Records.

---

## Complex Job Offers: How They're Processed
*Chunk ID: OHR-USE-0334 | Chapter: Job Offers | Guide: Using Recruiting*

Complex job offer refers to the way that the HR specialist will process the job offer. If a candidate with a complicated or
dynamically changing job situation accepts a job offer, the HR specialist will need to take additional steps to complete
the job application lifecycle, compared to other candidates in more straightforward situations.

---

## Situations Requiring Complex Processing
*Chunk ID: OHR-USE-0335 | Chapter: Job Offers | Guide: Using Recruiting*

The following examples describe hiring situations that require more complexity in transforming the offer into the final
assignment for the candidate.
• An internal candidate currently holding more than one job receives a job offer. You need to know whether this
offer is intended as a new assignment (for example, a third job) or whether it will replace one of the worker's
current jobs.
• An external candidate having no history with the company receives a job offer, or an ex-worker is offered a job
as a rehire. However, while the offer was getting created or approved, the candidate also got hired for another
job at the company, with a start date earlier than this offer's proposed start date. As a result, you'll need to
process this offer for the candidate as a second job for a current worker, rather than a new job or a rehire.
• An internal candidate was offered a job that was to be treated as a routine transfer. However, by the time you're
ready to process this offer, the worker has announced their intention to leave the company before this offer's
start date. If the job offer will still proceed, you'll have to handle it manually as a rehire.
You'll know that a given candidate requires complex processing by the message that appears when you start processing
their job application from the HR - Pending Manual Processing status. In addition to confirming that you want to take
the selected action, the message also states that you'll have to manually enter the data, then update the state.

---

## Job Offer Processing
*Chunk ID: OHR-USE-0336 | Chapter: Job Offers | Guide: Using Recruiting*

Offers for workers in these complex situations require HR specialists to process them differently than more
straightforward internal candidates. Processing is different in the following ways:
• Instead of launching the guided flow which was selected when the offer was drafted, you must examine the
current situation of the offer recipient and then decide whether to launch that action or a different action.
• Instead of seeing the values from the agreed-upon job offer being prepopulated into the relevant fields of the
selected guided flow, you must manually enter the proper value into each field in the new record.
• Instead of the job application status getting automatically updated after the new assignment is submitted and
approved, you must move its status to HR - Processed.
The steps to process these complex offers are as follows:
• When a complex job offer is moved to the HR phase after the candidate accepted it, the offer appears in the
status HR - Pending Manual Processing on your Job Offers list, available from the Manage Job Offers quick
action. Its prior status might have been HR - Pending Automated Processing, but it will soon be changed to HR
- Pending Manual Processing based on the Complete the Recruiting Process scheduled process.
• First, select the action that was chosen while the offer was drafted. When you confirm your intention to process
the candidate, their job application status reflects this by changing automatically from HR - Pending Manual
Processing to HR - Processing in Progress. The new status HR - Processing in Progress indicates that you're
about to create the candidate's new assignment based on this offer, even though you're just starting to process
it at that moment.
• Performing the selected HR action brings you to view the candidate's Employment Info page, not directly
into the guided flow to perform this action. On this page you can review this candidate's current, earlier, and
future work relationships and assignments. You can then decide to perform the HR action which was originally
selected, or any appropriate HR action, depending on how the candidate's current information compares with
the job offer.
• Within the guided flow for that action, you must manually enter all relevant information from the job offer into
the fields of the HR action page you selected. Unlike other types of job offer processing, the field values aren't
populated already with the agreed-upon values from the offer's assignment, salary, compensation, or other
sections. So you should be careful about information that was already viewed and understood in the job offer
while you copy each field's value into the HR flow sections. Then you must submit the HR action.
• After you submit that new assignment, these complex candidates remain visible on the list in status HR Processing in Progress. They won't automatically change to status HR - Processed, even after that assignment
gets manually created, approved if necessary, and committed to HR. You must use the action Move to
Processed to change their status to HR - Processed.
• Complex job offers that have been moved into the status HR - Processed remain on the Job Offers list, but no
further action is required. This is the final successful state in the entire recruiting process.
• The new status HR - Processed is also reflected in the job application in the Hiring work area, indicating to
Recruiting users that the overall candidate lifecycle is complete.
Note: The actions Quick Process Offer and Change Start Date aren't supported for these complex scenarios.

---

## Frequently Asked Questions
*Chunk ID: OHR-USE-0337 | Chapter: Job Offers | Guide: Using Recruiting*

What can I do if the assignment was created in Core HR instead of the Manage Job Offers quick action and the job offer
is stuck in the status Processing in Progress?
1.
2.
3.
4.

In My Client Groups > Quick Actions > Employment, click Manage Job Offers.
Find a job offer in status Processing in Progress.
Click the Actions menu and select the Return to Manual Processing action.
Open the job offer and in the Actions menu, click the action for which the job offer was raised. A read-only
Employment Info page opens.
5. Go back to the Manage Job Offers page.
6. Find the job offer, click the Actions menu and select the action you want to do as per your business need:
Move to Processed or Withdraw Candidate. .

Can I update the status of a candidate who was manually hired and processed into HR?
If it wasn't a complex hire and the candidate was hired manually, you can use the Withdrawn by Candidate or the
Rejected by Employer action.

---

## Unsuccessful Job Offers: How They're Handled
*Chunk ID: OHR-USE-0338 | Chapter: Job Offers | Guide: Using Recruiting*

There may be situations where an internal or external candidate's job application doesn't successfully complete the job
application lifecycle even after the candidate accepted the offer and was moved to the HR phase.

---

## Error During Processing
*Chunk ID: OHR-USE-0339 | Chapter: Job Offers | Guide: Using Recruiting*

The HR - Error During Processing status indicates that a problem must be fixed before the job offer can be processed
successfully. If the recruiter moved the candidate manually into the HR phase, they may have been warned about an
error. However, it's your responsibility as an HR specialist to understand and resolve the error. On the offer details page,
the Errors section contains details of the situation. For example, the offer's promised work location may have been
recently inactivated, or the offer's associated position may have recently become frozen or filled. Or a potential duplicate
person record may have been identified for the candidate (see Check and Merge Duplicates After Job Offer).
After you have resolved the situation causing the error, you can try again to progress the candidate forward through the
lifecycle. If the action encounters additional errors, an error message will appear and the status will remain Error During
Processing.
If the action is successful for an external candidate, then a pending worker will be created and the status will become
Processing in Progress until the new pending worker is converted. If the action is successful for an internal worker, the
status will become Processing in Progress until the new flow is submitted and approved.
After either of those events happen, the status will soon change to the final status HR - Processed based on the
Complete the Recruiting Process scheduled process (or manually updated for the situations that require complex
processing.

---

## Approver Rejects a Job Application
*Chunk ID: OHR-USE-0340 | Chapter: Job Offers | Guide: Using Recruiting*

If an approval cycle is configured for the HR action related to a job offer, an approver may decide to reject the new
assignment which was created based upon the offer assignment. In this scenario, the candidate has accepted a job

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0341 | Chapter: Job Offers | Guide: Using Recruiting*

but doesn't yet have a new assignment. The recruiting requisition believes that the hire has been made; and the job
application remains indefinitely in the inaccurate status HR - Processing in Progress.
You can select the Return To Manual Processing action to change the job application status to HR - Pending Manual
Processing. In this status, you must decide whether to start processing the HR action again in consultation with the
approver or manually select the Reject action. You can do this for internal and external candidates, including complex
job offer situations. But note that any internal job offers waiting in Pending Manual won't be affected by the autoprocessing feature even if enabled.

---

## Decision to Withdraw or Reject a Job Application
*Chunk ID: OHR-USE-0342 | Chapter: Job Offers | Guide: Using Recruiting*

A candidate may decide later to reject the previously accepted job offer, or may be a no-show, or the employer may
decide to not hire for a job offer. As an HR specialist, you must handle these decisions appropriately depending on the
current status of the job application.
• If the decision is made before you begin work on the job application in the HR phase, you must change the
status of the job application. In this case, you can change the status directly from HR - Pending Manual
Processing or HR - Pending Automated Processing to Withdrawn by Candidate or Rejected.
• If the decision is made while you're processing the job application, you must change the status of the job
application. In this case, you can change the status directly from HR - Processing in Progress back to HR Pending Manual Processing and then to Withdrawn by Candidate or Rejected. You also need to ensure that no
HR record exists for this unwanted job offer, or cancel any associated HR record that was created.
• If the decision is made after you successfully processed the job application, you must cancel the associated
HR assignment. For most job offers, this automatically updates the job application status to Withdrawn by
Candidate, based on the Complete the Recruiting Process scheduled process. For complex job offers, you must
first cancel the associated HR assignment, and then manually update the status on your Job Offers page to
Withdrawn by Candidate or Rejected.

---

## Reverse the Rejection or Withdrawal of Job Application
*Chunk ID: OHR-USE-0343 | Chapter: Job Offers | Guide: Using Recruiting*

As an HR specialist, you may incorrectly withdraw or reject a job application. To reverse this incorrect decision, you
need to find the job application in the status Withdrawn by Candidate or Rejected on the Job Offers page, under the
Manage Job Offers quick action. Select the action Return to Manual Processing for the job application so that the status
changes to HR - Pending Manual Processing. From this status, you can now start processing the job application again
by performing the preselected HR action. You can do this for internal and external candidates, including complex job
offer situations.

---

## Offer Mistakenly Moved to Processing in Progress
*Chunk ID: OHR-USE-0344 | Chapter: Job Offers | Guide: Using Recruiting*

Occasionally, as an HR specialist, you perform an action to move a candidate into the Processing In Progress status but
you then must cancel the flow. This may occur due to some mismatch with the data, or simply due to lack of time to
finish reviewing all the fields. When that occurs, the job application will remain incorrectly in the status Processing In
Progress, even though nobody is processing it anymore. To fully complete the hiring process, this candidate's offer must
be processed and submitted without interruption.
So in this case, you must select the Return to Manual Processing action, which moves the job application from the
Processing in Progress status to the Pending Manual Processing status. From there, when you're ready you can perform
the action again which brings the candidate back into Processing in Progress once again. You will see all the offer values
prefilled as before (unless this is a complex offer situation), and you can finish the guided process and submit it.

---

## Offer Must Be Redrafted
*Chunk ID: OHR-USE-0345 | Chapter: Job Offers | Guide: Using Recruiting*

All values agreed upon in the offer assignment will be transferred into the worker's new assignment. However
sometimes the business situation changes unexpectedly. If this requires a different start date or work location, for
instance, then the adjustment can be made directly on the HR pages by updating those values as the pending worker
is being converted or as the new assignment is being created. If a new signed offer letter is required to track these
significant changes, then the offer itself must be redrafted.
To allow a candidate's offer to be redrafted, you must inactivate it first. This means moving it into the status HR Withdrawn by Candidate or HR - Rejected, which can usually be achieved automatically by canceling any Pending
Worker or Worker that has already been created for this candidate. From here recruiters on the Offer Team can access
this job application in the Hiring work area, to perform the Redraft Offer action. This brings the candidate back into the
status Offer - Draft where they can make the necessary changes.

---

## What To Do if an External Candidate Got Hired But
*Chunk ID: OHR-USE-0346 | Chapter: Job Offers | Guide: Using Recruiting*

Changed Their Plans
Occasionally, after completing the full hiring process and transforming an external candidate into a worker, the person
is still unable to work for the organization. The person is a no-show or changed their plans, even though their employee
work relationship or contingent record is fully prepared for their arrival.
The appropriate course of action for an external candidate who reached the final HR - Processed status might depend
on whether or not the recruiting effort will continue for this candidate's replacement.
For a no-show candidate in the HR - Processed status, the HR specialist might choose to terminate the worker. This
would leave their history and records intact for future reference, including their terminated assignment, their job offer in
their job application, and the requisition for which they were successfully hired.
If the HR specialist prefers to restart or continue their hiring efforts to fill the requisition, then the appropriate course of
action might be to cancel the work relationship for this candidate. Many actions within Recruiting happen automatically
based on this cancellation:
• The HR specialist cancels a work relationship that was created from an associated offer.
• Within the person's record, that employment or contingent work relationship is deleted. There's no effect on
the already-terminated Pending Worker record, if any.
• The candidate's status automatically changes from HR - Processed to HR - Withdrawn by Candidate (based on
the frequency of the scheduled process Complete the Recruiting Process).
• The count of candidates hired for the job requisition is automatically decremented to reflect the unsuccessful
status of this candidate.
Some of the above steps must be taken manually in the rare situations where a candidate already had two or more
assignments, or whose status changed during the lifecycle of the offer. These are candidates for which the offer
information needed to be manually retyped into the HR action's flow to create the new assignment. For these situations,
if renewed hiring efforts are wanted, it's still appropriate to cancel the work relationship as follows:
• The HR specialist cancels a work relationship that was created from a complex associated offer.
• Within the person's record, that employment or contingent work relationship is deleted. There's no effect on
the already-terminated Pending Worker record, if any.

---

## HR Specialists and Job Offers
*Chunk ID: OHR-USE-0347 | Chapter: Job Offers | Guide: Using Recruiting*

• The candidate's status doesn't change automatically. The HR specialist must find this candidate on the list
using the quick action called Manage Job Offers to manually move the candidate's status from HR - Processed
to HR - Withdrawn by Candidate.
• The count of candidates hired for the associated requisition is automatically decremented to reflect the
unsuccessful status of this candidate.
Note: For the HR specialist to take action on the job offer using the Manage Job Offers quick action, the
administrator needs to run the scheduled process Complete the Recruiting Process.

---

## What Happens if an External Candidate Got Hired but
*Chunk ID: OHR-USE-0348 | Chapter: Job Offers | Guide: Using Recruiting*

Needs to be Rejected
Usually, reasons to reject a candidate are found in the early stages of the hiring process. It's rare that an external
candidate has reached the final HR phase before the organization discovers some necessity to reject them.
When canceling the new work relationship from the associated job offer, the status automatically changes from HR
- Processed to HR - Withdrawn. But if you want the historical records to show that this candidate completed their job
application with a final status of HR - Rejected instead of HR - Withdrawn, it's possible to make this correction.
• The HR specialist finds a candidate in the status HR - Withdrawn using the quick action Manage Job Offers.
• The HR specialist uses the action Return to Manual Processing to change the status back to HR - Pending
Manual Processing.
• The HR specialist uses the action Reject Candidate to change the status to HR - Rejected by Employer.
Note: For the HR specialist to act on the job offer using the Manage Job Offers quick action, the administrator needs
to run the scheduled process Complete the Recruiting Process.

---

## Grid Views
*Chunk ID: OHR-USE-0349 | Chapter: Job Offers | Guide: Using Recruiting*

16 Grid Views
What's a Grid View
With a grid view, data is displayed in a columnar layout. The grid view is available to view job applications for a
requisition, candidates in a candidate pool, and candidates in a candidate search results list.
By default, the Summary view is displayed to all users and contains specific columns. You can zoom in and zoom out to
see a few columns or all columns. You can also scroll horizontally.
If you have the privilege Personalize Candidates Lists (IRC_PERSONALIZE_CANDIDATE_JOB_APPLICATION_LISTS), you
can access the Manage Views page available in the View menu. From there, you can:
• Create your own personal views to display the columns and fields that you're interested in. This is useful when
you want to review and compare job applications for instance.
• Set a personal view as your personal default view. This personal default view has precedence over the global
default view.
• Edit, delete, and copy views.
If you have the privilege Manage Candidate Lists (IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS), more actions
are available from the Manage Views page.
• Manage Compound Fields: You can create compounds fields to display only specific fields that are of interest in
the grid view. You can also edit and delete compound fields.
• Manage Mask Data: If your organization is using blind sifting or name blind recruiting processes, you can mask
data in the job application grid view. You can write an EL Expression to define the roles, phases, and states to
mask data and select which grid view fields to anonymize.
• Manage Global Default Views: When you have several grid views, you can use this action to define which view
will be the global default view for all users, instead of the default Summary view.

---

## Default Summary View in Grid View
*Chunk ID: OHR-USE-0350 | Chapter: Job Offers | Guide: Using Recruiting*

This table lists the columns and fields displayed in the Summary view of the grid view. The Summary view is the default
view for all users. Columns will vary depending on where the grid view is used.

Column

Field

Candidate

---

## Candidate Number
*Chunk ID: OHR-USE-0351 | Chapter: Job Offers | Guide: Using Recruiting*

Candidate Location
Candidate Email Address: When you click the
email address, it opens the email automatically.
You need the privilege View Person Email for

Column

---

## Recruiting Data (IRC_VIEW_ PERSON_EMAIL_
*Chunk ID: OHR-USE-0352 | Chapter: Job Offers | Guide: Using Recruiting*

FOR_RECRUITING_DATA) to view the field.
Candidate Phone Number: You need the
privilege View Person Phone for Recruiting
Data (IRC_VIEW_PERSON_PHONE_FOR_
RECRUITING_DATA) to view the field.
Person Number: For external candidates, the
person number is created during the HR phase.
If the person number isn't yet available, a blank
value appears on the grid view. For internal
candidates, the person number is always
shown.

Details

---

## Recent Certifications (up to 3 most recent
*Chunk ID: OHR-USE-0353 | Chapter: Job Offers | Guide: Using Recruiting*

entries)

Certification Name, Issue Date, Issued By,
State/Province Code, Country Name

---

## Work Preferences (candidate responded Y)
*Chunk ID: OHR-USE-0354 | Chapter: Job Offers | Guide: Using Recruiting*

Travel Domestically, Travel Internationally,
Willing to Relocate, Consider Temporary
Assignment, Consider Part Time Work, Flexible
To Work

---

## Create a Personalized Grid View
*Chunk ID: OHR-USE-0355 | Chapter: Job Offers | Guide: Using Recruiting*

You can create your own personal views to display the columns and fields that you're interested in.
Watch video

Before you start
You need the privilege Personalize Candidates Lists (IRC_PERSONALIZE_CANDIDATE_JOB_APPLICATION_LISTS).
Here's what to do
1. In the View menu, select Manage Views.
2. On the Manage Views page, click Add.

---

## Grid Views
*Chunk ID: OHR-USE-0356 | Chapter: Job Offers | Guide: Using Recruiting*

3. Enter a name for the view.
4. Enter a name for the first column header.
5. Select a field category, then add fields to the category.
You can add a maximum of three individual fields or one compound field to a column. When you add an extensible
flexfield (EFF) in a column, only the EFF value is displayed. Consider using the EFF label as the column header to help
you understand the data displayed.
If your administrator enabled the Labels feature, you can display candidate labels in job application grid views. You
can add the Labels field to a column by itself. The Labels field appear in the Candidate Info category.
6. Add more columns and fields.
There is no limit on the number of columns that you can add to the view.
7. Click Save and Close.
What to do next
You can set this view as you personal default view by using the action Set as Personal Default.

---

## Create Compound Fields for Grid Views
*Chunk ID: OHR-USE-0357 | Chapter: Job Offers | Guide: Using Recruiting*

You can create compound fields and make them available for selection when creating grid views. A compound field
groups together several fields, each separated by a comma when displayed in the grid view.
Compound fields are available to add to grid views by any user who can create views, not only the user who created the
compound field.
Before you start
You need the privilege Manage Candidates Lists (IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS).
Here's what to do
1. In the View menu, select Manage Views.
2. On the Manage Views page, click the Actions menu and select Manage Compound Fields.
3. On the Manage Compound Fields page, click Add.
4. Enter a name for the compound field.
5. Select a field category.
6. Add fields.
7. Click Save.
What to do next
You can translate field names using the Translation Editor on the Manage Compound Fields page.

---

## Mask Job Application Grid View Data
*Chunk ID: OHR-USE-0358 | Chapter: Job Offers | Guide: Using Recruiting*

If your organization is using blind sifting or name blind recruiting processes, you can mask data in the job application
grid view. You write an EL expression to define the roles, phases, and states to mask data and select which grid view
fields to anonymize.
Before you start

---

## Grid Views
*Chunk ID: OHR-USE-0359 | Chapter: Job Offers | Guide: Using Recruiting*

You need the privilege Manage Candidate Lists (IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS).
Here's what to do
1. Go to a requisition's job applications list.
2. In the View menu, select Manage Views.
3. On the Manage Views page, click the Actions menu and select Manage Masked Data.
4. On the Manage Masked Data page, define the EL expression to mask grid view data.
The EL expression field is limited to 2000 characters. The result of the EL expression must be true or false. When
the EL expression is true, the selected fields are masked on all job application grid views. Masked fields appear with
'*****' in the grid view.
Fields that can be used in EL expressions:
Context

---

## EL Expression
*Chunk ID: OHR-USE-0360 | Chapter: Job Offers | Guide: Using Recruiting*

To check for role

securityContext.userInRole[‘ORA_IRC_RECRUITER_JOB’]
Pass the role code for the roles that should see masked
data.

---

## State Name
*Chunk ID: OHR-USE-0361 | Chapter: Job Offers | Guide: Using Recruiting*

item.StateName
Run a query to get the State Name.

Here's an example of an EL expression: #{securityContext.userInRole['ORA_IRC_RECRUITER_JOB'] ? !(item.PhaseId
== 14 and item.StateId == 1020 and item.PhaseName == 'Offer' and item.StateName eq 'Draft') : false}

5. In the Grid View Fields to Mask, click Add to add the fields you want to mask.
6. Click Save and Close.

---

## Job Application Grid View Sample Query for EL
*Chunk ID: OHR-USE-0362 | Chapter: Job Offers | Guide: Using Recruiting*

Expression
If you plan to mask data in the job application grid view, you can find below a sample query for an EL expression, an
example of an EL expression, and a table listing supported operators in EL expressions.

---

## Sample Query to Get CSP Details
*Chunk ID: OHR-USE-0363 | Chapter: Job Offers | Guide: Using Recruiting*

You can run the following query to get the Phase ID, Phase Name, State ID, and State Name for use in the EL expression.
Pass the CSP Name as the input value to the query.
select processesvl.process_id,
processesvl.Name,
processesvl.code,
processesvl.status_code,
rsphases.routing_step_id,
rsphases.phase_id,
rsphases.sequence_number as Phase_sequence_number,
phases.name AS phase_name,
rsstates.state_id,
rsstates.sequence_number as State_sequence_number,
states.name as state_name
from IRC_PROCESSES_VL processesvl,
irc_routing_steps_b rsphases,
irc_phases_tl phases,
irc_routing_steps_b rsstates,
irc_states_tl states
where processesvl.process_id = rsphases.process_id
and rsphases.phase_id = phases.phase_id
AND phases.language = userenv('LANG')
AND rsphases.sub_process_id = rsstates.process_id
AND rsstates.state_id = states.state_id
AND states.language = userenv('LANG')
and processesvl.name = :bindCSPName
order by rsphases.sequence_number, rsstates.sequence_number

---

## Example of an EL Expression
*Chunk ID: OHR-USE-0364 | Chapter: Job Offers | Guide: Using Recruiting*

#{securityContext.userInRole['ORA_IRC_RECRUITER_JOB'] ? !(item.PhaseId == 14 and item.StateId == 1020 and
item.PhaseName == 'Offer' and item.StateName eq 'Draft') : false}

---

## Calculate Computed Fields
*Chunk ID: OHR-USE-0365 | Chapter: Job Offers | Guide: Using Recruiting*

You can manually calculate computed fields by using the Calculate Computed Fields action available on the job
applications list and within job applications.
Computed fields can be configured to appear in job application grid views. Using computed fields, your organization
can help to surface important info, like whether or not the candidate is a veteran or diversity candidate, without
displaying their sensitive data directly in the UI.
Your administrator may have configured the candidate selection process so that the calculation of computed fields in
job application grid views is done automatically when candidates reach the phase and state of the selection process. If
that's not the case, you can use the Calculate Computed Fields action for one or several job applications.
Before you start
• You need the privilege Manage Candidate Lists (IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS) to see
the Calculate Computed Fields action.
• You need the privilege Personalize Candidates Lists
(IRC_PERSONALIZE_CANDIDATE_JOB_APPLICATION_LISTS) or the privilege Manage Candidate Lists
(IRC_MANAGE_CANDIDATE_JOB_APPLICATION_LISTS) to configure computed fields to appear in job
application grid views.
Here's what to do
1. Go to a requisition's job applications list.
2. Select a job application, then select the action Calculate Computed Fields.
You can select up to 10 job applications for the action to be performed in real time. If you select more than 10 job
applications, the action will be processed in the background and you'll be notified when the action is completed.
Results:
If a grid view isn't configured to display computed fields, you can view the values on the Extra Info tab of the job
application.

---

## Notifications and Interactions
*Chunk ID: OHR-USE-0366 | Chapter: Job Offers | Guide: Using Recruiting*

17 Notifications and Interactions
Notifications Sent Automatically During the Candidate
Selection Process
Notifications can automatically be sent to candidates, recruiters, hiring managers, hiring team collaborators, and agents
at specific points in the candidate selection process.
You can view notifications that were sent and the content of those notifications in the Messages tab of a candidate job
application.
Candidates can automatically receive notifications throughout the candidate selection process to be kept informed of
their progress. Candidates can receive notifications when their job applications enter or exit a phase in the candidate
selection process or are moved to a specific state within a phase.
Recruiters and hiring managers can receive a notification informing them that there are job applications to be reviewed.
They can receive a review notification when job applications enter or exit a phase in the candidate selection process
or are moved to a specific state within a phase. The review notification is sent once per day if there are new job
applications in the configured phase and state combination.

---

## Send a Notification to Request More Info
*Chunk ID: OHR-USE-0367 | Chapter: Job Offers | Guide: Using Recruiting*

You can manually send notifications to candidates to request more information. This is useful when the Request
Information Notification is automatically triggered when candidates reach a specific phase or state and you want to
send a notification earlier in the process. It can also be useful when candidates didn’t reply to the request.
Note: You can manually send the Request for More Info notification more than once, as long as the candidate hasn't
completed it.
Before you start
You need the privilege Request More Information from Candidates
(IRC_REQUEST_MORE_INFORMATION_FROM_CANDIDATES).
Here's what to do
1. In the job applications list, select one or more candidates.
2. In the Actions menu, select Request for More Info.
3. On the Request for More Info page, select the notification you want to resend.
Only the Request Information Notification configured within the candidate selection process is displayed.
4. Click Send.
Results:
When the notification is sent, it’s logged in the candidate application Interactions tab.

---

## Send Messages to the Hiring Team
*Chunk ID: OHR-USE-0368 | Chapter: Job Offers | Guide: Using Recruiting*

You can send messages to Hiring Team members to notify them of actions they need to take on job requisitions, job
applications, or job offers and keep them informed through the hiring process.
Before you start
Messages sent to the job offer Hiring Team can only be sent once a draft offer exists.
Here's what to do
1. Open a job requisition, candidate application, or job offer.
2. In the Actions menu, select Send Message to Team.
3. Select how you want to create the message, using a blank form or a template.
Only notification templates assigned to the Hiring Team Notification category are displayed.
4. Select the recipients to whom you want to sent the message.
If you're creating a message using a template, the message might have been configured to be sent to specific hiring
team members such as the hiring manager, recruiter, collaborators. You can adjust the list of recipients as needed.
5. Create the message.
If you create a message from a blank form, enter the subject and content of the message. If you're using a template,
you can adjust the subject and content as needed. Rich text features are available to format the message. You can
also use tokens.
6. Preview the message to ensure the content is correct and tokens are being resolved as expected.
7. Click Send.
Results:
The message is available in the Interactions tab. In the View Interactions field, select With Hiring Team to see the
message. The only information that the hiring team will receive is the information that you provided in the Message
section.

---

## Add and Track Interactions with a Candidate
*Chunk ID: OHR-USE-0369 | Chapter: Job Offers | Guide: Using Recruiting*

You can add interactions you have with a candidate and track them in the Interactions tab. Default interaction types are
by phone, email, text message, and in person.
You can add an interaction from the Candidate Search page and from within a candidate profile, a job application, a
prospect record.
Before you start
You need the Interact with Candidate (IRC_INTERACT_WITH_CANDIDATE_PRIV) privilege.
Here's what to do
1. Open a candidate file.
2. In the Actions menu, select Add Interaction.
3. On the Add Interaction page, select the type of interaction, enter the date when the interaction occurred, and enter a
note about the interaction.

---

## Notifications and Interactions
*Chunk ID: OHR-USE-0370 | Chapter: Job Offers | Guide: Using Recruiting*

4. Click Save and Close.
Results:
The interaction you created appears in the Interactions tab.
When you add a note with the interaction, the note is recorded differently whether it's for a candidate profile, candidate
job application, or prospect record:
• For a candidate profile, the note is recorded in the candidate profile, in the context of the candidate profile. For
a candidate profile as part of a candidate pool, the note is recorded in the candidate profile, in the context of the
candidate pool.
• For a candidate job application, the note is recorded in the job application, in the context of the job requisition.
• For a prospect record, the note is recorded in the prospect record, in the context of the job requisition.
When you have several interactions, you can use the View Interactions filter to filter the list of interactions. Depending
on the context where you added the interaction, filter values will differ:
• With Candidate for This Job Application
• With Pool Member
• Current Prospect Candidate
• All Other Candidate Interactions
• With Hiring Team
• With Agent

---

## Candidate Messaging
*Chunk ID: OHR-USE-0371 | Chapter: Job Offers | Guide: Using Recruiting*

18 Candidate Messaging
Candidate Messaging
You can send emails, SMS messages, or both to external candidates. You can send them using preconfigured email or
SMS templates, or by creating them from scratch. You can send only emails to internal candidates.
Note: When you opt into Recruiting Booster and enable Redwood, you can also send WhatsApp messages to external
candidates.
In the Recruiting Content Library, administrators can preconfigure both email and SMS templates for different types of
notifications such as Candidate Job Application Notification, Hiring Team Notification, and so on.
Choosing Between Email and SMS
By default, candidate communications are delivered via email. However, if you wish to communicate through SMS, your
administrator must configure and enable the SMS Communications feature in Setup and Maintenance.
When this feature is enabled, the application allows candidates to register or sign in using either their email or phone
number. When it’s not enabled, candidates will always register using their email and they will receive emails by default.
The candidate’s preferred communication channel is decided by the method they use during their initial job application:
• If they register with their phone number, SMS becomes their preferred communication channel. They receive
only SMS messages and not emails, until they change their preferences.
• If they register with an email address, email becomes their preferred communication channel. They continue to
receive only emails and not SMS messages, until they change their preferences.
• After they sign in, candidates have the option to opt in for both email and SMS as their preferred
communication channels. In this case, they receive both SMS messages and emails.
When SMS communications is enabled, the following rules apply:
• If you’re using preconfigured templates from the Recruiting Content Library, and they contain both email and
SMS content, candidates will receive messages according to their communication preferences.
• If the organization decides to send only emails to candidates, the SMS message content in the Recruiting
Content Library must empty. In this case, candidates will receive emails even if SMS is their preferred
communication method.
Note that the features described in Candidate Messaging apply to Responsive UI and not Redwood. For features specific
to Redwood, see Overview of the Candidate Messaging Feature in Redwood

---

## Email and SMS for Candidate Identity Verification and
*Chunk ID: OHR-USE-0372 | Chapter: Job Offers | Guide: Using Recruiting*

Communication
Recruiters and hiring managers can use email and SMS to verify candidate identity and as a communication channel
throughout the selection process.
By default, the candidate email address is used for identity verification and communication. When SMS communication
is enabled, candidates can confirm their identity and receive communication using their email address or phone
number.
The communication channel (email or SMS) used by candidates for their first authentication on the career site is
automatically marked as their preferred communication channel, and that's where the recruiting related communication
will be sent by default. Candidates can manage their communication preferences on the candidate self service page and
in the application flow, but they always need to have at least one channel marked as preferred. If the SMS feature isn’t
enabled, the checkbox to change the communication preference isn't displayed to candidates, so email is used as the
communication channel.
Note: The phone number provided by candidates must be able to receive SMS. Otherwise, candidates won't be able
to confirm their identity.
Here are examples of when email and phone number are used:
• Verify the identity of new candidates and confirm that talent community sign up (through email) and job
applications (through email or phone number) were made by the candidate who has that email or phone
number.
• Verify the identity of returning candidates to reuse data they provided in previous job applications.
• Verify the identity of returning candidates when they access their candidate self service dashboard on career
sites.
• Verify the identity of returning candidates when they schedule interviews, provide more information, or view
and accept job offers.
• Verify if the email belongs to current employees. If so, redirect the employee to the company's internal career
site.
• Communicate with candidates during the selection process. When new external candidates apply for a job,
they will receive communication by email or SMS depending on whether they used email or phone number
to confirm their identity at the beginning of the application process. After that, candidates can change their
communication preference to receive communications by email, SMS, or both when needed.
All candidates using an email or phone number are authenticated using a 6-digit verification code. Let's say for example
that a candidate uses an email to apply for a job. The candidate will receive an email with a 6-digit code to confirm
their job application. Similarly, the candidate will receive an SMS with a 6-digit code if applying for a job using a phone
number. Candidates are locked out after they enter an incorrect code 5 times. They have to wait for 30 minutes before
another authentication attempt.
You must use the Candidate Verification Notification email template to authenticate candidates on their preferred
communication channel. This sends an automated email to candidates with a 6-digit verification code. Note that this
automated email is sent using the no-reply email. This email will be visible in the Messages tab if the Capture Message
feature is enabled for this notification in the Content Library.

---

## Candidate Messaging
*Chunk ID: OHR-USE-0373 | Chapter: Job Offers | Guide: Using Recruiting*

Candidates can choose to be signed in instantly when they go to career site to schedule interviews, provide more
information, view offers, or apply to another job. When candidates select the option Keep me signed in, the next time
they visit the site on the same browser and within validity period, a verification won't be required. For details, see Enable
Keep Me Signed In.

---

## Verification of New Candidates
*Chunk ID: OHR-USE-0374 | Chapter: Job Offers | Guide: Using Recruiting*

When candidates apply for a job, they're asked to provide an email or phone number. If that email or phone number isn't
already being used, candidates are treated as new candidates. Communication with the candidates is done by email or
SMS depending on what the candidates provided.
Candidates must confirm that they own the email or phone number they used to apply for the job. They're sent a 6digit verification code by email or SMS. To confirm their identity, candidates enter the 6-digit code into a form presented
after the job application is submitted.
When candidates remain in the same session, their identity has already been verified and they can apply to other jobs
or access their candidate self service dashboard without the need to confirm their identity again. In general, the identity
of candidates is confirmed within the same session for 4 hours. After that time, candidates need to reconfirm their
identity.
Note: You must use the Job Application Confirmation Notification email template in order for candidates to receive
the verification code the first time they submit an application from an external career site. This email notification is
sent using the no-reply email. It’s displayed in the Messages tab if the Capture Message feature is enabled for this
notification in the Content Library.

When candidates want to join a talent community, they're asked to provide an email address. The same verification
process described above applies when joining a talent community.

---

## Verification of Returning Candidates
*Chunk ID: OHR-USE-0375 | Chapter: Job Offers | Guide: Using Recruiting*

When candidates apply for a job, they're asked to provide an email or phone number. When they want to join a talent
community, they're asked to provide an email address. If that email or phone number matches the info provided by an
existing candidate, the candidate is treated as a returning candidate.
Returning candidates can start the job application process or join the talent community only after their identity is
verified. They're sent a 6-digit verification code by email or SMS to confirm their identity. Upon confirmation of the
email or phone number, the candidates land in the application flow and the application form is prefilled with data from
previous job applications. The most recent data that was submitted is used. Candidates can overwrite that data and
submit their job application with updated details. Their candidate profile data is updated respectively.
When candidates remain in the same session, their identity has already been verified and they can apply to other jobs
or access their candidate self service dashboard without the need to confirm their identity again. In general, the identity
of candidates is confirmed within the same session for 4 hours. After that time, candidates need to reconfirm their
identity.
Returning candidates won't be asked to confirm their identity if they previously selected the option Keep me signed in
and they're using the same browser and are within the validity period.

---

## Verification of Email or Phone Number for Returning Candidates
*Chunk ID: OHR-USE-0376 | Chapter: Job Offers | Guide: Using Recruiting*

If returning candidates try to sign in using either an unverified phone number or email address they're asked to verify
their identity using verified information. This extra security applies to any place a candidate logs in, such as application

---

## Candidate Messaging
*Chunk ID: OHR-USE-0377 | Chapter: Job Offers | Guide: Using Recruiting*

flows, talent communities, events, and candidate self service. This prevents bad actors from being able to access a
candidate's real personal information in the profile.
For example, let's say that a candidate begins an application flow using an unverified email address. They must first
complete a PIN challenge. Next, they're asked to verify that they're the legitimate owner of the candidate profile
associated with that email address by correctly identifying the verified phone number associated with the profile.
If they enter the correct phone number, their unverified email address is marked as verified and they're allowed to
proceed with the application using that profile. If they don't enter the correct phone number, they're allowed to proceed
as a new candidate, and basic info is prepopulated with the phone number and email address they provided on the
verification screen. If this candidate submits an application, they're treated as a new candidate with email verified,
phone unverified.
Similarly, if a candidate begins an application flow with an unverified phone number, they're asked to verify the email
address. If they enter the correct email address, their unverified phone number would be marked as verified and they're
allowed to proceed with the application using that profile. If they don't enter the correct email address, they're allowed
to proceed as a new candidate, and basic info is prepopulated with the phone number and email address they provided
on the verification screen. If this candidate submits an application, they're treated as a new candidate with phone
verified, email address unverified.
Note: If a candidate is identified as having recently logged in via a stored cookie, then this challenge might not be
presented to them.

Note: We recommend that you also enable the feature that verifies date of birth and allows email claim (SeeEnable
Email Authentication and Email Reuse for instructions). This helps ensure that genuine candidates can proceed
through the phone validation screen by creating a new profile, even when using an email address previously used by
another (potentially malicious) candidate.

---

## Verification of Employees
*Chunk ID: OHR-USE-0378 | Chapter: Job Offers | Guide: Using Recruiting*

When former employees or alumni provide their personal email to confirm their identity, they're treated as returning
external candidates and they can access their talent profile data when applying for a job.
When current employees provide an email tied to their employee record, they're treated as internal candidates and
they're redirected to the company's internal career site.

---

## Candidate Authentication Path
*Chunk ID: OHR-USE-0379 | Chapter: Job Offers | Guide: Using Recruiting*

When a phone number or email address is used for authentication, it gets verified. From this point, the field is disabled
for editing and data isn't imported to that field if candidate imports profile from LinkedIn, Indeed or resume.
Candidates can easily edit the phone or email using an edit icon next to the field. They can also change their
communication preference by selecting Use for communication next to either Email Address or Phone Number.
Brand new candidates can only select one communication method. Returning candidates can select both.
The candidate authentication path depends on these criteria:
• If a candidate profile is associated with the email or phone number used for authentication.
• If there's a draft associated with the email or phone number even if a candidate profile doesn't exist yet.
• If the Candidate Autoconfirmation setting is enabled. For details, see Enable Candidate Autoconfirmation.

---

## Candidate Messaging
*Chunk ID: OHR-USE-0380 | Chapter: Job Offers | Guide: Using Recruiting*

Here's what happens when the Candidate Autoconfirmation setting is disabled:
• If there's no candidate profile:

◦ And there's no draft associated with the email or phone number: the verification code is sent at the end
◦

of the apply flow.
And there's a draft associated with the email or phone number: the verification code is sent before
entering the apply flow.

• If there's a candidate profile:

◦ When the candidate enters the apply flow, the verification code is sent as soon as the candidate provides
◦
◦

the email or phone number. After a successful verification, the candidate can enter the flow and see
profile data associated with the email or phone number that was used.
When the candidate enters the talent community flow, the verification code is sent as soon as the
candidate provides the email (there's no phone verification when entering the talent community flow).
After successful verification, the candidate can access the self-service dashboard on the career site to
manage their profile (there's no entry to the talent community flow because the candidate already has a
profile).

Here's what happens when the Candidate Autoconfirmation setting is enabled:
• If there's no candidate profile, and or draft associated with the email or phone number, the verification code
isn't sent after completing the apply flow or the talent community flow, and the email or phone number is auto
confirmed.
• If there's a candidate profile, the behavior is the same as when the Candidate Autoconfirmation setting is
disabled.
Note: If a returning candidate edits their communication preference in the apply flow, they'll have to verify
immediately that they own the email or phone number using an inline PIN challenge during the apply flow. New
candidates verify the communication channel after submitting application.

Related Topics
• Recruiting Content Library
• Can I send messages even if the candidate's communication channel isn't verified?
• Enable Email Authentication and Email Reuse

---

## Ways to Send Messages
*Chunk ID: OHR-USE-0381 | Chapter: Job Offers | Guide: Using Recruiting*

There are two features available in Recruiting to send messages:
• The Send Message feature – This is useful when sending bulk emails or SMS messages to multiple candidates.
• The Compose feature – This is useful when sending individual emails or SMS messages.
These features are available from the Messages tab of a candidate’s page, which you can open using Candidate Search,
from a list of job applications and prospects, or from a candidate pool.

---

## Candidate Messaging
*Chunk ID: OHR-USE-0382 | Chapter: Job Offers | Guide: Using Recruiting*

When you select the Messages tab, you can see the list of emails and SMS messages exchanged with the candidate,
displayed in the order of the most recent to the oldest.
By default, the Emails section displays the list of emails sent to the candidate in the current context, for example, the
current job application or candidate pool. The list can also show all the other emails exchanged with the candidate, if
you have access to them.
Note: In the Redwood experience, the Last Contacted field will update when a message is sent to the candidate from
their profile. It doesn't update when a message is sent from a job requisition.

The Text Messages section displays all SMS messages sent to the candidate, irrespective of the context.
For Twilio and Syniverse service providers, one of these status indicators appear next to each SMS message:
• Sent – Indicates that it was sent successfully from Recruiting.
• Delivered – Indicates that it reached the candidate’s phone number.
• Failed – Indicates that it failed to deliver.
• Received – Indicates that the message has been received in Recruiting.
• Blocked – A message could be blocked because of these reasons:
◦ The candidate's phone number belongs to a country that's not in the allowed list of countries.

◦ The candidate's phone number is in the list of blocked phone numbers or matches a phone number
pattern that's blocked.
The candidate’s daily message limit has been reached (for their phone or candidate number).

◦
◦ The application-wide daily message limit is reached.
For other providers, the default status is Sent.

This feature uses the Webhook functionality. To use it, you must configure the Delivery Status Callback Webhook URL
in the Twilio and Syniverse service providers' accounts. For these configuration steps, see the document Candidate
Communication on My Oracle Support (ID 2968395.1).
To use this feature with Twilio, you need to use the messaging service SID instead of the "From" phone number when
you configure Twilio as an SMS provider.
Related Topics
• Enable Candidates to Opt Out of SMS Messages
• Examples of Adding an SMS Provider
• Candidate Communication
• Enable SMS Communications and Set Limits for Outbound SMS

---

## Send Messages to Multiple Candidates
*Chunk ID: OHR-USE-0383 | Chapter: Job Offers | Guide: Using Recruiting*

When you use the Send Message feature, you can send email and SMS messages to multiple candidates at once. You
need to have the privilege Interact with Candidate (IRC_INTERACT_WITH_CANDIDATE_PRIV) to send messages to
candidates.

---

## Candidate Messaging
*Chunk ID: OHR-USE-0384 | Chapter: Job Offers | Guide: Using Recruiting*

You can send messages from the Candidate Search page, from a list of job applications and prospects, and from within
a candidate pool. Let's say you're on a job applications list:
1. Select one or multiple candidates.
2. In the Actions menu, select Send Message.
3. Create a message using a template or a blank message.
◦ If you select a template, the list of templates available for selection depends on the context where you
initiated the Send Message action. For example, if you use the action from the job applications list, only job
application-related notifications are available. In the requisition context, the list of templates available for
selection might be further refined depending on the contextualization defined on the template. If you have
the privilege Update Email Created from Template (IRC_UPDATE_EMAIL_CREATED_FROM_TEMPLATE),
you can edit the content of the email message provided by the template before sending the email. Tokens
aren't translated to other languages because tokens are variable names. In the sent message, token values
are resolved and translated depending on the context.
◦ If you create a message from scratch, enter the subject and content of the message. Rich text features are
available to format the email text, while only plain text can be used to author SMS text. You can also use
tokens.
◦ When the candidates you selected have a mix of email and SMS preferences, the message is sent to the
candidate in the correct format based on the email or SMS preference.
Note: If a candidate doesn’t have SMS as their preferred communication channel, the SMS message isn’t
sent to them even if you create the message and send it.
4. You can preview the message before sending it to see how it will appear to candidates.

◦ Tokens are resolved and also translated depending on the context. If you send the message to multiple
candidates, tokens are resolved for the first candidate as an example.
Styling, images, and branding are applied.

◦
◦ In preview mode, the View in Browser link doesn't work.
5. Select Send.
Results:

When the message is sent, an interaction note of type email or SMS is automatically added in the Messages tab
where the action was launched (candidate profile, candidate job application, prospect, candidate pool). By default, the
interactions list is filtered to the current candidate context, for example, the current job application or candidate profile.
The interactions list can also show all other interactions to which you have access. The message sent displays the name
of the recruiter, regardless of whether the two-way communication is enabled.

---

## Compose a Message
*Chunk ID: OHR-USE-0385 | Chapter: Job Offers | Guide: Using Recruiting*

You can send an email or SMS message to individual candidates using the Compose feature. You can use this feature
only when the candidate has chosen either email or SMS as their preferred communication channel.
1. Open a candidate page from Candidate Search, Job Requisitions, Job Applications, Prospects, Events, or Candidate
Pools.
2. Select the Messaging tab.
3. Select the Compose button in the email or SMS section.
If the candidate hasn’t chosen email or SMS as their preferred communication channel, this button will be disabled in
the corresponding section.

---

## Candidate Messaging
*Chunk ID: OHR-USE-0386 | Chapter: Job Offers | Guide: Using Recruiting*

4. Create your message and select Send. Note that you can’t use predefined templates or insert tokens automatically.
However, you can manually type in the tokens, and they will display the correct values when the message is sent.
Ensure that the token spellings and capitalization are the same as predefined tokens.

---

## View Reports for Outbound SMS Messages
*Chunk ID: OHR-USE-0387 | Chapter: Job Offers | Guide: Using Recruiting*

You can now generate reports for outbound SMS messages to analyze the volume of messages that were successfully
sent or blocked.
Reports can be generated for these periods:
• Daily: Lists the number of SMS messages sent or blocked per hour of the day. It also displays the cumulative
count of messages from the first hour up to every hour in the day.
• 30 Days: Lists the number of SMS messages sent or blocked in the past 30 days.
• Historical: Lists the number of SMS messages sent or blocked over the past two years.
You can also use this report to understand how many text messages were blocked per country.
The report also categorizes messages according to the notification category defined in the Recruiting Content Library,
such as Candidate Verification Notification, Event Canceled Notification, and so on. Any messages that don’t belong to
these categories appear in the Miscellaneous category.
1. In the Setup and Maintenance work area, go to:

◦ Offering: Recruiting and Candidate Experience
◦ Functional Area: Recruiting and Candidate Experience Management
◦ Task: Recruiting Messaging Configuration
2. Expand the Reports for Text Messages section and select Edit.
3. Select the duration for the report and select Create Report.

---

## Redwood Messaging Features in Recruiting
*Chunk ID: OHR-USE-0388 | Chapter: Job Offers | Guide: Using Recruiting*

When you enable the Redwood experience in Recruiting, these features are available to you:
• View emails and messages in the enhanced Messages tab
• Compose emails and SMS messages Using AI Assist
• Send messages to multiple candidates
• Use attachments with outgoing and incoming emails
• Apply design templates to emails

---

## Recruiting Activity Center
*Chunk ID: OHR-USE-0389 | Chapter: Job Offers | Guide: Using Recruiting*

19 Recruiting Activity Center
Recruiting Activity Center
With the Recruiting Activity Center, recruiters and hiring managers have a place to easily access and manage recruiting
activities related to the job requisitions, job applications, and job offers they own.
Users granted the privilege Access Recruiting Activity Center (IRC_ACCESS_RECRUITING_ACTIVITY_CENTER) can view
and access the Recruiting Activity Center quick action. Recruiters can access the quick action in My Client Groups >
Hiring, while hiring managers can access it in My Team > Hiring.
When you're in the Recruiting Activity Center, you can view a list of activities and easily view which ones are of high
priority. Each activity item is tagged with a High, Medium, or Low priority. When you click the name of an activity, a
drawer opens and you can view more info about the activity.
From the activities list, you can take action directly using an Action button or an action from the Actions menu.
Depending on the action, you're taken to the Hiring work area, either in the job requisition, job application, or job offer
details page. Or, for some actions, an action panel opens and you can perform the action directly in the Recruiting
Activity Center without having to go to Hiring.
You can dismiss an activity. When you that, the activity no longer appears in the activity list. However, it might still
be present in another user's activity list. For example, if a recruiter dismisses a requisition approval rejected activity it
would still appear in the hiring manager's activity list. A dismissed activity item could reappear in a user's activity list if
the triggering conditions were met again. Using the above example, if the hiring manager redrafted the requisition and
the approval was again rejected, the recruiter would see a new activity item for the approval rejection.
Things to consider:
• Some activity items are generated as soon as the triggering conditions have been met whereas other activity
items are created after a specified time delay.
• Many actions suggested in the activity list will bring you to the job requisition, job application, or job offer
details page where you'll need to perform the action. You can use the back arrow on the details page to return
to the activity list.
◦ Some actions might be suggested in the activity list that you might not have the necessary privileges to
perform. You won't see the action available upon navigating to the details page where the action would
typically be performed.
• When Office 365 integration is enabled for interview scheduling, the Interviewer proposed new time activity
item won't be triggered in Recruiting Activity Center.
• When items are displayed on the activities list, the job requisition status isn't considered.

---

# Opportunity Marketplace

## Recruiting Activity Center
*Chunk ID: OHR-USE-0390 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

20 Opportunity Marketplace
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

a preferred job location for their job alerts, the job or gig's primary location matches the seeker's location
preference, and if the seeker hasn't yet applied to the job or gig.
• Favorites - Displays jobs and gigs shortlisted by the user when they bookmark them as their favorite. Users can
remove these from favorites at any time.
Note: When you enable gigs, users will see a splash screen the first time they sign in to Opportunity Marketplace.
Once they save their preferences, this splash screen doesn't display again.

---

## Create a Job Using Opportunity Marketplace
*Chunk ID: OHR-USE-0391 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Create a job opportunity for both internal and external candidates using Opportunity Marketplace.
When you create a job with Opportunity Marketplace, you're creating a job requisition. Job requisitions must be created,
formatted, and posted before they're available to candidates in Opportunity Marketplace.
1. Navigate to Me > Quick Actions > Show More > Opportunity Marketplace.
2. Click Create then click Job.
3. Enter the required information for each section, and click Continue.
4. Click Submit.
Related Topics
• Job Requisition Creation Process
• Create a Job Requisition Template of Type Standalone

---

## Create a Gig Using Opportunity Marketplace
*Chunk ID: OHR-USE-0392 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

You can create a gig in Opportunity Marketplace. Gigs are short-term, temporary assignments that let employees make
use of or gain skills that they may not use in their current role.
Gigs help employees improve the skills they already have, or gain skills they want to have.
1. Navigate to Me > Quick Actions > Show More > Opportunity Marketplace.
2. Click Create, and then click Gig.
3. Enter the required information for each section.
4. If your organization enabled Dynamic Skills, you can associate skills related to this gig. You will be provided with AI
recommendations for related skills based on the gig title and description you entered. You can also type and search
to find the skills you want to add to this gig.
5. Click Save and Close if you need to finish later, or Publish if you're ready to make this gig available for candidates to
find in Opportunity Marketplace.
Results:
Once published, the gig is immediately available for candidates to find and apply to.

---

## Viewing Created Gigs
*Chunk ID: OHR-USE-0393 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

As a gig creator, you can view gigs created in Opportunity Marketplace, whether they're active, draft, completed, or
canceled.
All created gigs are listed in the Created Gigs tab and displayed in several sections.
• Active - Published gigs that aren't completed or canceled. For active gigs, you can:
◦ Unpublish a gig. Unpublishing withdraws a gig from Opportunity Marketplace so that it's not available for
employees to apply to unless it's republished.
◦ Duplicate a gig as a draft which creates a new gig based on an existing gig. Duplicates are added to the
Drafts section.
◦ Cancel a gig. When a gig is canceled, it's not available in Opportunity Marketplace.

◦ Edit a gig to update the gig details.

• History - Completed or canceled gigs.
• Drafts - Saved gigs that aren't yet published or active. Use this section to find draft gigs that need to be edited
or published. You can also create a new gig by duplicating the content of a draft gig. For these gigs, you can:
◦ Duplicate a gig as a draft which creates a new gig based on an existing gig. Duplicates are added to the
Drafts section.
◦ View an assignee’s profile in Connections.

◦ Contact an assignee of a gig.

---

## Unpublish a Gig
*Chunk ID: OHR-USE-0394 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

As a gig creator, you can temporarily unpublish a gig to make updates to it. Unpublished gigs are usually republished
by the gig creator. Once unpublished, candidates who have already been assigned to the gig remain assigned, and they
aren't impacted or notified by this temporary situation.
Candidates are only notified if the gig is canceled.
1. Navigate to Me > Quick Actions > Show More > Opportunity Marketplace.
2. Click Created Gigs.
3. Find an active gig and select Unpublish from the Actions menu.
Results:
The gig is listed in the Drafts section of the page. To make changes, click the gig name and open it in edit mode. When
you're ready, click Publish to republish the gig.

---

## Assign a Candidate to a Gig
*Chunk ID: OHR-USE-0395 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

As a gig creator, you can assign candidates to gigs when you feel they're a good fit.

1. In Opportunity Marketplace, click Created Gigs.
2. Find an active gig and click the candidate count to open the list of candidates.
Basic information about each candidate is displayed, including whether they've completed or participated in any gigs
in the past, and any reviews provided by their peers.
3. Select a candidate and click View Profile to see the full candidate profile on Connections, including education,
experience, interests, skills, and demographic profile.
If Dynamic Skills is enabled, you can also see the list of gig skills that match with the skills of the candidates. Oracle
Dynamic Skills is a separately sold product.
4. Click Assign.
Results:
After the candidate is assigned to the gig, you can perform these actions:
• Mark as Complete: Mark the gig as complete. This moves the gig to the History section in the Created Gigs tab.
• Contact Assignee: Send email messages to candidates who were selected for the gig.
• Release Assignee: Release an assignee from the gig.

---

## Discover, Search, and Apply for Opportunities
*Chunk ID: OHR-USE-0396 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Employees who are seeking jobs, gigs, or career roles can use Opportunity Marketplace to explore new opportunities,
shortlist them, apply to them, or recommend others.
The Opportunity Marketplace landing page (Explore tab) is where employees or seekers browse jobs, gigs and career
roles, or look for opportunities that are recommended to them based on their preferences.
Note:
For jobs posted both internally and externally, if a job has both an internal and external description, the internal
description is displayed to candidates. If there's only an external description, that's what's displayed to candidates.

---

## Set or Update Opportunity Preferences
*Chunk ID: OHR-USE-0397 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers use the Update Interests action to enter or update their interests and preferences about jobs, gigs, and career
roles. Opportunities that match these preferences display on the Opportunity Marketplace Recommendations page
as recommendations. Seekers can also receive email notifications about recommended new opportunities. The
notifications content and their frequency is configured by the administrator.

---

## Discover Recommended Opportunities
*Chunk ID: OHR-USE-0398 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

As seekers look for opportunities on the recommended tab, Opportunity Marketplace automatically recommends them
and displays them at the top of the page. Recommended opportunities are based on the seeker's preferences (like
location), their skills, jobs or gigs they recently applied to, and those they recently shortlisted. Seekers can define or
update their interests or preferences at any time.

---

## Search for Opportunities
*Chunk ID: OHR-USE-0399 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers can search for opportunities using various parameters like job or gig name, job type, hours per week, or
location. Matching opportunities display in the search results.
Seekers can also quickly find opportunities of interest by entering a job title keyword (such as "engineer" or "designer"),
and then use location or time commitment (like hours per week) as filters for the search results.
As a best practice, you should search for job titles by keyword, and filter by location. Let’s say that a gig seeker is looking
for content writer gigs in California. They first search for keywords "content writer", and then filter the search results
using the location called "CA, United States". They can further filter the results by start and end date, posted date, or
weekly commitment (hours per week).
For each filter, seekers see the top values based on the number of available opportunities. They can also use the filter
search box to enter specific values that aren't currently listed as top values for the filter (for example, a specific location).
If Dynamics Skills is enabled, then a Skills facet can be used to further refine results for jobs and gigs.

---

## Saved Searches
*Chunk ID: OHR-USE-0400 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers can use the Saved Searches functionality to:
• Select an existing saved search.
• Create a search.
• Share a search with others.
• Mark a search as their default search, which loads each time they open Opportunity Marketplace.
• Use a system search created by their administrator.

---

## View Opportunity Details
*Chunk ID: OHR-USE-0401 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Once seekers find the opportunity they're looking for, they can view their details. Details vary depending on whether
they're looking at a gig, job, or career role, but this view contains things such as the location, time frame, number of
hours a gig seeker need to spend on a gig, the names of other team players, and the contact details for the opportunity
creator.
If Dynamic Skills is enabled, gig seekers can see the list of skills associated with a gig, and which of those match with
their own Skills Center skills.
For jobs that are either hybrid or on-site, they'll see the location in the card. If a job is a remote job, then only "Remote"
is displayed.

---

## Favorite an Opportunity
*Chunk ID: OHR-USE-0402 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers can shortlist an opportunity using the Mark as Favorite action. To view the list of favorites, seekers use the
Favorites search filter. Once an opportunity is added to favorites, the Mark as Favorite action changes to Remove from
Favorites so that seekers can remove it when they're ready.

---

## Recommend an Opportunity
*Chunk ID: OHR-USE-0403 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers can recommend opportunities or share them with others using the actions available on the details pages.
Depending on opportunity type they can share, copy a link, refer a candidate (jobs only), or refer an employee (jobs
only).

---

## Apply to an Opportunity
*Chunk ID: OHR-USE-0404 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers click Apply to open the application page where they can enter their information.
For gigs, the application form provides a field for candidates to enter a brief profile, or to say why they believe they're
a good fit for a gig. Once submitted, the application goes to the gig creator. When a gig creator reviews a profile and
assigns a candidate to a gig, the candidate receives a notification letting them know that they were assigned to a gig.
For jobs, once the application is submitted, it becomes associated with the related job requisition and follows that flow.
Note: Seekers can only apply once to a gig. If a seeker withdraws from a gig, the Apply button becomes disabled, and
seekers can't reapply.

---

## View and Manage Applications
*Chunk ID: OHR-USE-0405 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers view and manage their submitted applications using the Submitted Applications tab.
Note: Users must have both access and view privileges to access the dashboard.

If both gigs and jobs are enabled, submitted gig applications display first by default. Seekers can click Jobs to view job
applications.
• For gigs, the Active section contains all the ongoing gigs that seekers have applied to, were assigned to, and
that are pending approval from the line manager. Seekers can withdraw from gigs that have the Pending
Approval or Applied status. Once a gig is assigned, a seeker can't withdraw from it. The Inactive section
contains all the gigs that are completed, not selected, withdrawn, and not selected. Seekers can contact the gig
manager, or view the manager’s profile.
• For jobs, seekers can see all the job applications they submitted. The Active section shows all the seeker's
active applications, and the History section shows all the inactive applications (withdrawn and not selected).
They can schedule an interview for an active application if that application is eligible for candidate interview
scheduling as configured in internal career sites. They can view an interviewer's schedule through the job
application, and select an available date and time.

---

## Access Job Offers
*Chunk ID: OHR-USE-0406 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Seekers can access job offers from the job application for which an offer is available. They can then accept or reject the
job.

---

## Saving Jobs and Gigs Searches
*Chunk ID: OHR-USE-0407 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

All Opportunity Marketplace users can:
• Select an existing saved search.
• Create a search.
• Share a search with others.
• Mark a search as their default search, which loads each time they open Opportunity Marketplace.

• Use a system search created by their administrator.
Administrators can:
• Create system searches that are made available to all users.
• Mark any of the system searches as default for all users.
Note: User default searches override administrator default searches.

Note: The administrator must run the scheduled process called “ESS job to create index definition and perform
initial ingest to OSCS” to ensure that all jobs and gigs that already exist in the application are fully indexed for search.
Specify “fa-hcm- requisition” in the Index Name to Reingest field. YThe administrator must also run the scheduled
process called “ESS job to create index definition and perform initial ingest to OSCS” to ensure that saved search
index definitions are set up for usage. Specify “fa-hcm-savedsearch” in the Index Name to Reingest field.

---

## Skills Advisor for Gigs
*Chunk ID: OHR-USE-0408 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

As a gig creator, you can associate skills to your gigs if your organization enabled Dynamic Skills.
Skills Advisor:
• Provides AI recommendations for skills that are related to gig titles and descriptions, which you can then add as
you create gigs.
• Helps attract gig seekers who are interested in those relevant skills so that they can apply to a gig, grow their
skill set, or further develop and attain skills they'd like to have.
• Uses location and skills as part of a matching algorithm to recommend gigs for the employees through the
Opportunity Marketplace dashboard.
Related Topics
• Overview of Dynamic Skills

---

## Explore Career Roles
*Chunk ID: OHR-USE-0409 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Using the Career Roles feature in Opportunity Marketplace, you can browse through career roles that you're interested
in. You can see job openings for these roles. You can also see role guides for career roles, which help you understand
the requirements defined by the organizational leadership for the role. You can also recommend roles that might be of
interest to your peers or reports.
See these topics for more information on these tasks:
• Explore Career Roles in Opportunity Marketplace
• View Job Openings for a Career Role
• View Role Guides for a Career Role

• Set Career Preferences
• Recommend Career Roles

---

## Current Jobs
*Chunk ID: OHR-USE-0410 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

21 Current Jobs
Current Jobs Work Area
The Current Jobs work area provides you with tools to search jobs within your company, to apply for jobs, to see the
status of your job search, to refer someone for a job.
Note: This topic only applies to existing US Government customers with PODs that aren’t configured to use Oracle
Search.
From the Current Jobs page, you can search for jobs and easily access these pages:
• Favorite Jobs: See your preferred jobs and perform actions on them; apply for the job, share the job, refer
someone, copy the link.
• Job Applications: Review the job applications you submitted, view their progress. View interview details for
already scheduled interviews. You can also use the Withdraw action if you no longer want your active job
applications to be considered.
• Referrals: Look at the referrals you made and their status as they progress through the recruiting process.
You can see the same progress as the person you referred. Note that a candidate can only be referred once
on a job requisition. The candidate can't be referred again by a different employee. Also, when a candidate is
added to a job requisition by a referral, using the Copy Link action, or any other method, you can still provide an
endorsement for the candidate.
• Job Offers: See any job offers that are currently pending your response that have been extended to you. You
can accept or decline these here. Also you can see any job offers that you previously accepted.
• Job Alerts: Subscribe to receive notifications about new job opportunities. Set your job preferences regarding
organizations, locations, job families, and jobs.

---

## Search for Internal Jobs
*Chunk ID: OHR-USE-0411 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

You use the Current Jobs functionality to search jobs within your company.
You can search for jobs based on the job title, the organization, the location, or other keywords. The list of jobs matching
the search criteria appears on the Jobs page. Search results are limited to 500 jobs. A default 25 mile radius is applied to
the location. This helps you to see more jobs in your area. You can adjust the radius value by clicking the "Search Radius
25 Miles" link that appears inside the Location menu. You can also remove the value by clicking Clear.
On the job results page, click the job title to review the job details and apply for the job. The process to apply for a job
is quick and straightforward. You have the opportunity to review your skills and qualifications, provide any updates
if needed, answer any job application questions, attach a resume or other supporting documents, and provide an esignature.
On the job results page, click the Star icon to mark the job as a favorite job. Favorite jobs are displayed in the Favorite
Jobs page.

---

## Current Jobs
*Chunk ID: OHR-USE-0412 | Chapter: Opportunity Marketplace | Guide: Using Recruiting*

Here are other actions you can do from the search results page:
• Share the job: Opens your email client with a link to the external job posting. You can share the job by email
with a colleague or someone outside the company.
• Refer an employee: You can select an employee and provide an endorsement. The employee is sent an invite to
apply to the job.
• Refer a candidate: You can quickly refer an external candidate, provide an endorsement, and attach a resume
on their behalf. The candidate is sent an invite to apply to the job.
• Copy the link: Copies the link to your clipboard.

---
