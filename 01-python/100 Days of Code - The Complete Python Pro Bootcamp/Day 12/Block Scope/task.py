my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3            #  isko ma kahi bhe use kr sakta hu not only in for

#    khoi variable agar if , loop , mai define hota hai toh kahi bhe
#  use ho sakta hai ye but agar khoi function ka inside hua toh wo local variable only wahi use hoga

