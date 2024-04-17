from smartphone import Smartphone

# catalog = [Smartphone("nokia", "3110", "+79186544551"), 
#         Smartphone("samsung", "S10", "+79186544552"),
#         Smartphone("huawei", "H6", "+79186544553"),
#         Smartphone("HONOR", "H7", "+79186544554"),
#         Smartphone("OPPO", "OPPO8", "+79186544555") ]

catalog = []

catalog.append(Smartphone("nokia", "3110", "+79186544551"))
catalog.append(Smartphone("samsung", "S10", "+79186544552"))
catalog.append(Smartphone("huawei", "H6", "+79186544553"))
catalog.append(Smartphone("HONOR", "H7", "+79186544554"))
catalog.append(Smartphone("OPPO", "OPPO8", "+79186544555"))

for i in catalog:
    i.print_phone()