---
layout: page
title: Meetings
permalink: /meetings/
order: 3
---
### Telecons

Telecons are held approximately every two weeks on Mondays at 09:00 AM Mountain time, but this can fluctuate depending on holidays/conferences/etc. See the Calendar below for the next telecon time. Telecon notes are shared on [Google Drive](https://drive.google.com/drive/u/0/folders/1AhFUli3SGW9DHvIh81tFxPMgLtYSPXDm), and presentations can be found on the [PyHC YouTube Channel](https://www.youtube.com/@pythoninheliophysicscommun3732).

<br>

### Events

#### [Community Meetings]({% link
_pages/meetings/community_meetings/community_meetings.md %})

#### [Conference Sessions]({% link
_pages/meetings/conference_sessions/conference_sessions.md %})

#### [Summer Schools]({% link
_pages/meetings/summer_schools/summer_schools.md %})

<br>

### Calendars

PyHC meetings and telecon times are available as a [Google calendar](https://calendar.google.com/calendar?cid=NG42Z3YyaWZncDZyZ25rOGF1N2pzZjF1azBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ):
<br>
<div id="pyhccalendar-container"></div>
<br>

Additionally, there is a more [general calendar](https://helioanalytics.io/events-calendar) that serves as an exhaustive list of events related to the Heliophysics and space physics communities. If you have an event you'd like added to this calendar, please email: <a href="mailto:pyhc-confidential@lasp.colorado.edu">pyhc-confidential@lasp.colorado.edu</a>
<br><br>

<div id="helioanalyticscalendar-container"></div>

<script type="text/javascript">
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const pyhchtml = `<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23f9e79f&showTitle=0&title=PyHC%20Events&showDate=1&showPrint=0&showTabs=1&showCalendars=0&showNav=1&src=NG42Z3YyaWZncDZyZ25rOGF1N2pzZjF1azBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%237CB342&ctz=${timezone}" width="100%" height="600" frameborder="0" scrolling="no"></iframe>`;
    const helioanalyticshtml = `<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&src=aWJwbWhrMTFlMWEyMTFpa3V0bGY1M2d0ZnNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%23D50000&ctz=${timezone}" width="100%" height="600" frameborder="0" scrolling="no"></iframe>`;
    document.getElementById('pyhccalendar-container').innerHTML = pyhchtml;
    document.getElementById('helioanalyticscalendar-container').innerHTML = helioanalyticshtml;
</script>
