# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TrackList:

    # def __init__(self, name):
    #     # Parameters:
    #     #   name: string
    #     # Side effects:
    #     #   Sets the name property of the self object
    #     pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track name: string representing a song
        pass 

    def list_tracks(self):
        # Returns:
        #   A list of tracks
        pass 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially there are no tracks
"""
track_list = TrackList()
track_list.list_tracks() # => []

"""
When a song is added
it is reflected in the list of tracks
"""
track_list = TrackList()
track_list.add("Sunny Day - Brandy")
track_list.list_tracks() # => ["Sunny Day - Brandy"]

"""
When multiple songs are added
they are all reflected in the list of tracks
"""
track_list = TrackList()
track_list.add("Sunny Day - Brandy")
track_list.add("Cloudy Day - Brandy")
track_list.add("Windy Day - Brandy")
track_list.list_tracks() # => ["Sunny Day - Brandy", "Cloudy Day - Brandy", "Windy Day - Brandy"]

"""
When an empty string is added
it will give us an error
"""
track_list = TrackList()
track_list.add("")
track_list.list_tracks() # => [] this will give us an error "Entry must contain song"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
