#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:51:44 2021
@author: masum
@mail: billahcse@gmail.com
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c","--classes", metavar='', required=True, help="classes name")
parser.add_argument("-p","--annotation", metavar='', required=True, help="path to annotation file")
parser.add_argument("-t","--type", metavar='', required=True, help="file type e.g train/test/validation")
args = vars(parser.parse_args())

classIDs = {'Tortoise':'/m/011k07','Container':'/m/011q46kg','Magpie':'/m/012074','Sea turtle':'/m/0120dh','Football':'/m/01226z','Ambulance':'/m/012n7d',
       'Ladder':'/m/012w5l','Toothbrush':'/m/012xff','Syringe':'/m/012ysf','Sink':'/m/0130jx','Toy':'/m/0138tl','Organ (Musical Instrument)':'/m/013y1f',
       'Cassette deck':'/m/01432t','Apple':'/m/014j1m','Human eye':'/m/014sv8','Cosmetics':'/m/014trl','Paddle':'/m/014y4n','Snowman':'/m/0152hh',
       'Beer':'/m/01599','Chopsticks':'/m/01_5g','Human beard':'/m/015h_t','Bird':'/m/015p6','Parking meter':'/m/015qbp','Traffic light':'/m/015qff',
       'Croissant':'/m/015wgc','Cucumber':'/m/015x4r','Radish':'/m/015x5n','Towel':'/m/0162_1','Doll':'/m/0167gd','Skull':'/m/016m2d','Washing machine':'/m/0174k2',
       'Glove':'/m/0174n1','Tick':'/m/0175cv','Belt':'/m/0176mf','Sunglasses':'/m/017ftj','Banjo':'/m/018j2','Cart':'/m/018p4k','Ball':'/m/018xm',
       'Backpack':'/m/01940j','Bicycle':'/m/0199g','Home appliance':'/m/019dx1','Centipede':'/m/019h78','Boat':'/m/019jd','Surfboard':'/m/019w40','Boot':'/m/01b638',
       'Headphones':'/m/01b7fy','Hot dog':'/m/01b9xk','Shorts':'/m/01bfm9','Fast food':'/m/01_bhs','Bus':'/m/01bjv','Boy':'/m/01bl7v','Screwdriver':'/m/01bms0',
       'Bicycle wheel':'/m/01bqk0','Barge':'/m/01btn','Laptop':'/m/01c648','Miniskirt':'/m/01cmb2','Drill (Tool)':'/m/01d380','Dress':'/m/01d40f',
       'Bear':'/m/01dws','Waffle':'/m/01dwsz','Pancake':'/m/01dwwc','Brown bear':'/m/01dxs','Woodpecker':'/m/01dy8n','Blue jay':'/m/01f8m5',
       'Pretzel':'/m/01f91_','Bagel':'/m/01fb_0','Tower':'/m/01fdzj','Teapot':'/m/01fh4r','Person':'/m/01g317','Bow and arrow':'/m/01g3x7',
       'Swimwear':'/m/01gkx_','Beehive':'/m/01gllr','Brassiere':'/m/01gmv2','Bee':'/m/01h3n','Bat (Animal)':'/m/01h44','Starfish':'/m/01h8tj',
       'Popcorn':'/m/01hrv5','Burrito':'/m/01j3zr','Chainsaw':'/m/01j4z9','Balloon':'/m/01j51','Wrench':'/m/01j5ks','Tent':'/m/01j61q',
       'Vehicle registration plate':'/m/01jfm_','Lantern':'/m/01jfsr','Toaster':'/m/01k6s3','Flashlight':'/m/01kb5b','Billboard':'/m/01knjb',
       'Tiara':'/m/01krhy','Limousine':'/m/01lcw4','Necklace':'/m/01llwg','Carnivore':'/m/01lrl','Scissors':'/m/01lsmm','Stairs':'/m/01lynh',
       'Computer keyboard':'/m/01m2v','Printer':'/m/01m4t','Traffic sign':'/m/01mqdt','Chair':'/m/01mzpv','Shirt':'/m/01n4qj','Poster':'/m/01n5jq',
       'Cheese':'/m/01nkt','Sock':'/m/01nq26','Fire hydrant':'/m/01pns0','Land vehicle':'/m/01prls','Earrings':'/m/01r546','Tie':'/m/01rkbr',
       'Watercraft':'/m/01rzcn','Cabinetry':'/m/01s105','Suitcase':'/m/01s55n','Muffin':'/m/01tcjp','Bidet':'/m/01vbnl','Snack':'/m/01ww8y',
       'Snowmobile':'/m/01x3jk','Clock':'/m/01x3z','Medical equipment':'/m/01xgg_','Cattle':'/m/01xq0k1','Cello':'/m/01xqw','Jet ski':'/m/01xs3r',
       'Camel':'/m/01x_v','Coat':'/m/01xygc','Suit':'/m/01xyhv','Desk':'/m/01y9k5','Cat':'/m/01yrx','Bronze sculpture':'/m/01yx86','Juice':'/m/01z1kdw',
       'Gondola':'/m/02068x','Beetle':'/m/020jm','Cannon':'/m/020kz','Computer mouse':'/m/020lf','Cookie':'/m/021mn','Office building':'/m/021sj1',
       'Fountain':'/m/0220r2','Coin':'/m/0242l','Calculator':'/m/024d2','Cocktail':'/m/024g6','Computer monitor':'/m/02522','Box':'/m/025dyy',
       'Stapler':'/m/025fsf','Christmas tree':'/m/025nd','Cowboy hat':'/m/025rp__','Hiking equipment':'/m/0268lbt','Studio couch':'/m/026qbn5',
       'Drum':'/m/026t6','Dessert':'/m/0270h','Wine rack':'/m/0271qf7','Drink':'/m/0271t','Zucchini':'/m/027pcv','Ladle':'/m/027rl48',
       'Human mouth':'/m/0283dt1','Dairy Product':'/m/0284d','Dice':'/m/029b3','Oven':'/m/029bxz','Dinosaur':'/m/029tx','Ratchet (Device)':'/m/02bm9n',
       'Couch':'/m/02crq1','Cricket ball':'/m/02ctlc','Winter melon':'/m/02cvgx','Spatula':'/m/02d1br','Whiteboard':'/m/02d9qx',
       'Pencil sharpener':'/m/02ddwp','Door':'/m/02dgv','Hat':'/m/02dl1y','Shower':'/m/02f9f_','Eraser':'/m/02fh7f','Fedora':'/m/02fq_6',
       'Guacamole':'/m/02g30s','Dagger':'/m/02gzp','Scarf':'/m/02h19r','Dolphin':'/m/02hj4','Sombrero':'/m/02jfl0','Tin can':'/m/02jnhm',
       'Mug':'/m/02jvh9','Tap':'/m/02jz0l','Harbor seal':'/m/02l8p9','Stretcher':'/m/02lbcq','Can opener':'/m/02mqfb','Goggles':'/m/02_n6y',
       'Human body':'/m/02p0tk3','Roller skates':'/m/02p3w7d','Coffee cup':'/m/02p5f1q','Cutting board':'/m/02pdsw','Blender':'/m/02pjr4',
       'Plumbing fixture':'/m/02pkr5','Stop sign':'/m/02pv19','Office supplies':'/m/02rdsp','Volleyball (Ball)':'/m/02rgn06','Vase':'/m/02s195',
       'Slow cooker':'/m/02tsc9','Wardrobe':'/m/02vkqh8','Coffee':'/m/02vqfm','Whisk':'/m/02vwcm','Paper towel':'/m/02w3r3',
       'Personal care':'/m/02w3_ws','Food':'/m/02wbm','Sun hat':'/m/02wbtzl','Tree house':'/m/02wg_p','Flying disc':'/m/02wmf','Skirt':'/m/02wv6h6',
       'Gas stove':'/m/02wv84t','Salt and pepper shakers':'/m/02x8cch','Mechanical fan':'/m/02x984l','Face powder':'/m/02xb7qb','Fax':'/m/02xqq',
       'Fruit':'/m/02xwb','French fries':'/m/02y6n','Nightstand':'/m/02z51p','Barrel':'/m/02zn6n','Kite':'/m/02zt3','Tart':'/m/02zvsm',
       'Treadmill':'/m/030610','Fox':'/m/0306r','Flag':'/m/03120','French horn':'/m/0319l','Window blind':'/m/031b6r','Human foot':'/m/031n1',
       'Golf cart':'/m/0323sq','Jacket':'/m/032b3c','Egg (Food)':'/m/033cnk','Street light':'/m/033rq4','Guitar':'/m/0342h','Pillow':'/m/034c16',
       'Human leg':'/m/035r7c','Isopod':'/m/035vxb','Grape':'/m/0388q','Human ear':'/m/039xj_','Power plugs and sockets':'/m/03bbps',
       'Panda':'/m/03bj1','Giraffe':'/m/03bk1','Woman':'/m/03bt1vf','Door handle':'/m/03c7gz','Rhinoceros':'/m/03d443','Bathtub':'/m/03dnzn',
       'Goldfish':'/m/03fj2','Houseplant':'/m/03fp41','Goat':'/m/03fwl','Baseball bat':'/m/03g8mr','Baseball glove':'/m/03grzl',
       'Mixing bowl':'/m/03hj559','Marine invertebrates':'/m/03hl4l9','Kitchen utensil':'/m/03hlz0c','Light switch':'/m/03jbxj',
       'House':'/m/03jm5','Horse':'/m/03k3r','Stationary bicycle':'/m/03kt2w','Hammer':'/m/03l9g','Ceiling fan':'/m/03ldnb','Sofa bed':'/m/03m3pdh',
       'Adhesive tape':'/m/03m3vtv','Harp':'/m/03m5k','Sandal':'/m/03nfch','Bicycle helmet':'/m/03p3bw','Saucer':'/m/03q5c7','Harpsichord':'/m/03q5t',
       'Human hair':'/m/03q69','Heater':'/m/03qhv5','Harmonica':'/m/03qjg','Hamster':'/m/03qrc','Curtain':'/m/03rszm','Bed':'/m/03ssj5',
       'Kettle':'/m/03s_tn','Fireplace':'/m/03tw93','Scale':'/m/03txqz','Drinking straw':'/m/03v5tg','Insect':'/m/03vt0','Hair dryer':'/m/03wvsk',
       'Kitchenware':'/m/03_wxk','Indoor rower':'/m/03wym','Invertebrate':'/m/03xxp','Food processor':'/m/03y6mg','Bookcase':'/m/03__z0',
       'Refrigerator':'/m/040b_t','Wood-burning stove':'/m/04169hn','Punching bag':'/m/0420v5','Common fig':'/m/043nyj','Cocktail shaker':'/m/0440zs',
       'Jaguar (Animal)':'/m/0449p','Golf ball':'/m/044r5d','Fashion accessory':'/m/0463sg','Alarm clock':'/m/046dlr','Filing cabinet':'/m/047j0r',
       'Artichoke':'/m/047v4b','Table':'/m/04bcr3','Tableware':'/m/04brg2','Kangaroo':'/m/04c0y','Koala':'/m/04cp_','Knife':'/m/04ctx',
       'Bottle':'/m/04dr76w','Bottle opener':'/m/04f5ws','Lynx':'/m/04g2r','Lavender (Plant)':'/m/04gth','Lighthouse':'/m/04h7h','Dumbbell':'/m/04h8sr',
       'Human head':'/m/04hgtk','Bowl':'/m/04kkgm','Humidifier':'/m/04lvq_','Porch':'/m/04m6gz','Lizard':'/m/04m9y','Billiard table':'/m/04p0qw',
       'Mammal':'/m/04rky','Mouse':'/m/04rmv','Motorcycle':'/m/04_sv','Musical instrument':'/m/04szw','Swim cap':'/m/04tn4x','Frying pan':'/m/04v6l4',
       'Snowplow':'/m/04vv5k','Bathroom cabinet':'/m/04y4h8h','Missile':'/m/04ylt','Bust':'/m/04yqq2','Man':'/m/04yx4','Waffle iron':'/m/04z4wx',
       'Milk':'/m/04zpv','Ring binder':'/m/04zwwv','Plate':'/m/050gv4','Mobile phone':'/m/050k8','Baked goods':'/m/052lwg6','Mushroom':'/m/052sf',
       'Crutch':'/m/05441v','Pitcher (Container)':'/m/054fyh','Mirror':'/m/054_l','Personal flotation device':'/m/054xkw','Table tennis racket':'/m/05_5p_0',
       'Pencil case':'/m/05676x','Musical keyboard':'/m/057cc','Scoreboard':'/m/057p5t','Briefcase':'/m/0584n8','Kitchen knife':'/m/058qzx',
       'Nail (Construction)':'/m/05bm6','Tennis ball':'/m/05ctyq','Plastic bag':'/m/05gqfk','Oboe':'/m/05kms','Chest of drawers':'/m/05kyg_',
       'Ostrich':'/m/05n4y','Piano':'/m/05r5c','Girl':'/m/05r655','Plant':'/m/05s2s','Potato':'/m/05vtc','Hair spray':'/m/05w9t9',
       'Sports equipment':'/m/05y5lj','Pasta':'/m/05z55','Penguin':'/m/05z6w','Pumpkin':'/m/05zsy','Pear':'/m/061_f','Infant bed':'/m/061hd_',
       'Polar bear':'/m/0633h','Mixer':'/m/063rgb','Cupboard':'/m/0642b4','Jacuzzi':'/m/065h6l','Pizza':'/m/0663v','Digital clock':'/m/06_72j',
       'Pig':'/m/068zj','Reptile':'/m/06bt6','Rifle':'/m/06c54','Lipstick':'/m/06c7f7','Skateboard':'/m/06_fw','Raven':'/m/06j2d',
       'High heels':'/m/06k2mb','Red panda':'/m/06l9r','Rose':'/m/06m11','Rabbit':'/m/06mf6','Sculpture':'/m/06msq','Saxophone':'/m/06ncr',
       'Shotgun':'/m/06nrc','Seafood':'/m/06nwz','Submarine sandwich':'/m/06pcq','Snowboard':'/m/06__v','Sword':'/m/06y5r','Picture frame':'/m/06z37_',
       'Sushi':'/m/07030','Loveseat':'/m/0703r8','Ski':'/m/071p9','Squirrel':'/m/071qp','Tripod':'/m/073bxn','Stethoscope':'/m/073g6',
       'Submarine':'/m/074d1','Scorpion':'/m/0755b','Segway':'/m/076bq','Training bench':'/m/076lb9','Snake':'/m/078jl','Coffee table':'/m/078n6m',
       'Skyscraper':'/m/079cl','Sheep':'/m/07bgp','Television':'/m/07c52','Trombone':'/m/07c6l','Tea':'/m/07clx','Tank':'/m/07cmd',
       'Taco':'/m/07crc','Telephone':'/m/07cx4','Torch':'/m/07dd4','Tiger':'/m/07dm6','Strawberry':'/m/07fbm7','Trumpet':'/m/07gql','Tree':'/m/07j7r',
       'Tomato':'/m/07j87','Train':'/m/07jdr','Tool':'/m/07k1x','Picnic basket':'/m/07kng9','Cooking spray':'/m/07mcwg','Trousers':'/m/07mhn',
       'Bowling equipment':'/m/07pj7bq','Football helmet':'/m/07qxg_','Truck':'/m/07r04','Measuring cup':'/m/07v9_z','Coffeemaker':'/m/07xyvk',
       'Violin':'/m/07y_7','Vehicle':'/m/07yv9','Handbag':'/m/080hkjn','Paper cutter':'/m/080n7g','Wine':'/m/081qc','Weapon':'/m/083kb',
       'Wheel':'/m/083wq','Worm':'/m/084hf','Wok':'/m/084rd','Whale':'/m/084zz','Zebra':'/m/0898b','Auto part':'/m/08dz3q','Jug':'/m/08hvt4',
       'Pizza cutter':'/m/08ks85','Cream':'/m/08p92x','Monkey':'/m/08pbxl','Lion':'/m/096mb','Bread':'/m/09728','Platter':'/m/099ssp',
       'Chicken':'/m/09b5t','Eagle':'/m/09csl','Helicopter':'/m/09ct_','Owl':'/m/09d5_','Duck':'/m/09ddx','Turtle':'/m/09dzg',
       'Hippopotamus':'/m/09f20','Crocodile':'/m/09f_2','Toilet':'/m/09g1w','Toilet paper':'/m/09gtd','Squid':'/m/09gys','Clothing':'/m/09j2d',
       'Footwear':'/m/09j5n','Lemon':'/m/09k_b','Spider':'/m/09kmb','Deer':'/m/09kx5','Frog':'/m/09ld4','Banana':'/m/09qck','Rocket':'/m/09rvcxw',
       'Wine glass':'/m/09tvcd','Countertop':'/m/0b3fp9','Tablet computer':'/m/0bh9flk','Waste container':'/m/0bjyj5','Swimming pool':'/m/0b_rs',
       'Dog':'/m/0bt9lr','Book':'/m/0bt_c3','Elephant':'/m/0bwd_0j','Shark':'/m/0by6g','Candle':'/m/0c06p','Leopard':'/m/0c29q','Axe':'/m/0c2jj',
       'Hand dryer':'/m/0c3m8g','Soap dispenser':'/m/0c3mkw','Porcupine':'/m/0c568','Flower':'/m/0c9ph5','Canary':'/m/0ccs93','Cheetah':'/m/0cd4d',
       'Palm tree':'/m/0cdl1','Hamburger':'/m/0cdn1','Maple':'/m/0cffdh','Building':'/m/0cgh4','Fish':'/m/0ch_cf','Lobster':'/m/0cjq5',
       'Garden Asparagus':'/m/0cjs7','Furniture':'/m/0c_jw','Hedgehog':'/m/0cl4p','Airplane':'/m/0cmf2','Spoon':'/m/0cmx8','Otter':'/m/0cn6p',
       'Bull':'/m/0cnyhnx','Oyster':'/m/0_cp5','Horizontal bar':'/m/0cqn2','Convenience store':'/m/0crjs','Bomb':'/m/0ct4f','Bench':'/m/0cvnqh',
       'Ice cream':'/m/0cxn2','Caterpillar':'/m/0cydv','Butterfly':'/m/0cyf8','Parachute':'/m/0cyfs','Orange':'/m/0cyhj_','Antelope':'/m/0czz2',
       'Beaker':'/m/0d20w4','Moths and butterflies':'/m/0d_2m','Window':'/m/0d4v4','Closet':'/m/0d4w1','Castle':'/m/0d5gx','Jellyfish':'/m/0d8zb',
       'Goose':'/m/0dbvp','Mule':'/m/0dbzx','Swan':'/m/0dftk','Peach':'/m/0dj6p','Coconut':'/m/0djtd','Seat belt':'/m/0dkzw','Raccoon':'/m/0dq75',
       'Chisel':'/m/0_dqb','Fork':'/m/0dt3t','Lamp':'/m/0dtln','Camera':'/m/0dv5r','Squash (Plant)':'/m/0dv77','Racket':'/m/0dv9c',
       'Human face':'/m/0dzct','Human arm':'/m/0dzf4','Vegetable':'/m/0f4s2w','Diaper':'/m/0f571','Unicycle':'/m/0f6nr','Falcon':'/m/0f6wt',
       'Chime':'/m/0f8s22','Snail':'/m/0f9_l','Shellfish':'/m/0fbdv','Cabbage':'/m/0fbw6','Carrot':'/m/0fj52s','Mango':'/m/0fldg','Jeans':'/m/0fly7',
       'Flowerpot':'/m/0fm3zh','Pineapple':'/m/0fp6w','Drawer':'/m/0fqfqc','Stool':'/m/0fqt361','Envelope':'/m/0frqm','Cake':'/m/0fszt',
       'Dragonfly':'/m/0ft9s','Common sunflower':'/m/0ftb8','Microwave oven':'/m/0fx9l','Honeycomb':'/m/0fz0h','Marine mammal':'/m/0gd2v',
       'Sea lion':'/m/0gd36','Ladybug':'/m/0gj37','Shelf':'/m/0gjbg72','Watch':'/m/0gjkl','Candy':'/m/0gm28','Salad':'/m/0grw1','Parrot':'/m/0gv1x',
       'Handgun':'/m/0gxl3','Sparrow':'/m/0h23m','Van':'/m/0h2r6','Grinder':'/m/0h8jyh6','Spice rack':'/m/0h8kx63','Light bulb':'/m/0h8l4fh',
       'Corded phone':'/m/0h8lkj8','Sports uniform':'/m/0h8mhzd','Tennis racket':'/m/0h8my_4','Wall clock':'/m/0h8mzrc','Serving tray':'/m/0h8n27j',
       'Kitchen & dining room table':'/m/0h8n5zk','Dog bed':'/m/0h8n6f9','Cake stand':'/m/0h8n6ft','Cat furniture':'/m/0h8nm9j',
       'Bathroom accessory':'/m/0h8nr_l','Facial tissue holder':'/m/0h8nsvg','Pressure cooker':'/m/0h8ntjv','Kitchen appliance':'/m/0h99cwc',
       'Tire':'/m/0h9mv','Ruler':'/m/0hdln','Luggage and bags':'/m/0hf58v5','Microphone':'/m/0hg7b','Broccoli':'/m/0hkxq','Umbrella':'/m/0hnnb',
       'Pastry':'/m/0hnyx','Grapefruit':'/m/0hqkz','Band-aid':'/m/0j496','Animal':'/m/0jbk','Bell pepper':'/m/0jg57','Turkey':'/m/0jly1',
       'Lily':'/m/0jqgx','Pomegranate':'/m/0jwn_','Doughnut':'/m/0jy4k','Glasses':'/m/0jyfg','Human nose':'/m/0k0pj','Pen':'/m/0k1tl','Ant':'/m/0_k2',
       'Car':'/m/0k4j','Aircraft':'/m/0k5j','Human hand':'/m/0k65p','Skunk':'/m/0km7z','Teddy bear':'/m/0kmg4','Watermelon':'/m/0kpqd',
       'Cantaloupe':'/m/0kpt_','Dishwasher':'/m/0ky7b','Flute':'/m/0l14j_','Balance beam':'/m/0l3ms','Sandwich':'/m/0l515','Shrimp':'/m/0ll1f78',
       'Sewing machine':'/m/0llzx','Binoculars':'/m/0lt4_','Rays and skates':'/m/0m53l','Ipod':'/m/0mcx2','Accordion':'/m/0mkg','Willow':'/m/0mw_6',
       'Crab':'/m/0n28_','Crown':'/m/0nl46','Seahorse':'/m/0nybt','Perfume':'/m/0p833','Alpaca':'/m/0pcr','Taxi':'/m/0pg52','Canoe':'/m/0ph39',
       'Remote control':'/m/0qjjc','Wheelchair':'/m/0qmmr','Rugby ball':'/m/0wdt60w','Armadillo':'/m/0xfy','Maracas':'/m/0xzly','Helmet':'/m/0zvk5'}

classes = args['classes'].strip().split(',')

f = open(args['type']+".txt", "w")

selected = []
for key in classIDs:
    if key in classes:
        selected.append(classIDs[key])
           
if len(selected) != len(classes):
    print("Error: check class name")
    exit()       

with open(args['annotation']) as lines:
    for line in lines:
        line = line.strip().split(',')
        if line[2] in selected:
            f.write("{}/{}\n".format(args['type'],line[0]))
f.close()


