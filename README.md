### parse.py

The entry to this module is (currently) the `parse_oscon` function. This takes the URL for the speakers page of an OSCON conference, and returns a list of `Speaker` objects. Currently this can read any of the OSCO 2007-2011 pages.

This will eventually be further abstracted to a `parse_conference` function which can take the URL for more conferences than just OSCON.

### gender.py

The API for this module currently consists of the `classify` function. Given a list of `Speaker` objects, this attempts to apply heuristics to the `bio` attribute of the `Speaker` to determine if the speaker is male or female. Each `Speaker` has its `gender` attribute modified appropriately.

When a Speaker object is first instantiated, its `gender` attribute is set to `"unknown"`. If `classify` can't determine the gender, then it will leave this attribute unchanged.

`classify` does modify the `Speaker` instances in place, but for convenience it also returns four lists, `[male speakers], [female speakers], [ambiguous], [unknown]`.

An "ambiguous" speaker is one where the heuristics identify both male and female aspects.

### output.py

This module provides general functionality for storing and processing results.

The `Output` object is used to create CSV files of the results.

The `process_unknown_speakers` function takes a list of speakers, and an instance of `Output`, and iterates through each `Speaker`, asking the user to identify if the `Speaker` is male or female.

`run` is a convenience method that wraps up most of this process. Given a list of `Speakers` and a desired output filename, it classifies the speakers, executes `process_unknown_speakers` and stores all the results.
