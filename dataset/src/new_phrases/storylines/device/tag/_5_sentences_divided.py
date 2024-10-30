# List of sentences representing slices of storylines for each commercially available item in the full_list.py
import time
sentences = {
    'Alien Technology ALN-9640 Squiggle RFID Tag': ["David's warehouse became more organized and efficient with the help of Alien Technology ALN-9640 Squiggle RFID Tags that allowed him to track inventory movement in real-time.",
                                                    "Jenny's company adopted the use of Alien Technology ALN-9640 Squiggle RFID Tags to monitor and track the location of goods in transit, reducing theft and lost items.",
                                                    "The Alien Technology ALN-9640 Squiggle RFID Tag helped improve the supply chain management process at Mike's company by providing real-time location tracking of shipments and goods.",
                                                    "Using Alien Technology ALN-9640 Squiggle RFID Tags, the hospital staff could easily identify and track medical equipment, reducing the risk of loss or misplacement.",
                                                    "Jake's retail store implemented Alien Technology ALN-9640 Squiggle RFID Tags to optimize inventory management, reducing the need for manual stock-taking and improving efficiency."],

    'Avery Dennison AD-383r6 RFID Tag': ["With Avery Dennison AD-383r6 RFID Tags, the logistics team at Sarah's company could track the location and movement of cargo in real-time.",
                                         "John's manufacturing plant implemented Avery Dennison AD-383r6 RFID Tags to track the status and location of materials and equipment, reducing the time and effort required for inventory management.",
                                         "The Avery Dennison AD-383r6 RFID Tag was used to monitor the temperature and humidity of a sensitive shipment during transportation, ensuring the product arrived in pristine condition.",
                                         "By using Avery Dennison AD-383r6 RFID Tags, a food company was able to improve the freshness and quality of their products by monitoring the location and conditions of the goods during transportation.",
                                         "The Avery Dennison AD-383r6 RFID Tag was instrumental in improving the accuracy of the supply chain management process at a pharmaceutical company, reducing the risk of lost or misplaced items."],
    "Impinj Monza X-2K RFID Tag": ["The Impinj Monza X-2K RFID Tag's tamper-evident seal ensured the security and authenticity of the product.", "The Impinj Monza X-2K RFID Tag's large memory capacity enabled the storage of detailed product information.", "With the Impinj Monza X-2K RFID Tag, Jack was able to track the entire supply chain of his products, from production to delivery.", "The Impinj Monza X-2K RFID Tag's excellent read rate made it a reliable choice for high-speed inventory management.", "The Impinj Monza X-2K RFID Tag's unique identifier made it easy to distinguish between different products in a large inventory."],

    "Confidex Ironside UHF RFID Tag": [
        "The manufacturing company was able to track their inventory in real-time with the Confidex Ironside UHF RFID tags.",
        "The Confidex Ironside UHF RFID tags helped the logistics company to improve their shipment tracking and delivery time.",
        "The Confidex Ironside UHF RFID tags helped the retailer to reduce their out-of-stock items and improve their inventory accuracy.",
        "The Confidex Ironside UHF RFID tags were used to track and locate the equipment in the hospital, which increased the operational efficiency and saved time.",
        "The Confidex Ironside UHF RFID tags were used to track and monitor the livestock's health and location, which helped the farmers to improve their productivity and reduce their operational costs."
    ],
    "NXP MIFARE Classic RFID Tag": [
        "Tom was able to easily access his office building by simply waving his NXP MIFARE Classic RFID Tag over the reader at the entrance.",
        "The NXP MIFARE Classic RFID Tag was the perfect solution for Alice's inventory management needs, allowing her to easily track and locate her products.",
        "John's hotel implemented the NXP MIFARE Classic RFID Tag as a keycard system, ensuring only authorized guests had access to their rooms.",
        "Using the NXP MIFARE Classic RFID Tag, Sophia was able to quickly pay for her coffee without having to fumble for cash or cards.",
        "The NXP MIFARE Classic RFID Tag was a game changer for Maria's warehouse management system, enabling her to quickly scan and locate her products."
    ],
    "Omni-ID Flex 600 RFID Tag": [
        "The Omni-ID Flex 600 RFID Tag allowed David to track his high-value assets across multiple locations, giving him peace of mind.",
        "Emma's manufacturing company improved its supply chain efficiency with the help of the Omni-ID Flex 600 RFID Tag, which enabled them to track inventory in real-time.",
        "Using the Omni-ID Flex 600 RFID Tag, Alex was able to monitor the temperature and humidity of his perishable goods, ensuring they were stored in optimal conditions.",
        "Sophie's hospital implemented the Omni-ID Flex 600 RFID Tag to track medical equipment, saving precious time and reducing equipment loss.",
        "The Omni-ID Flex 600 RFID Tag was instrumental in Mark's construction site safety program, allowing him to monitor worker movements and ensure they were in the right areas at the right times."
    ],
    "Smartrac Circus Tamper Loop RFID Tag": [
        "John was confident that his shipment would be safe from tampering thanks to the Smartrac Circus Tamper Loop RFID Tag.",
        "Sophie was impressed by the Smartrac Circus Tamper Loop RFID Tag's ability to detect and alert her if her luggage had been tampered with during her trip.",
        "The Smartrac Circus Tamper Loop RFID Tag was instrumental in ensuring the authenticity of the high-end products sold by the luxury retailer.",
        "Thanks to the Smartrac Circus Tamper Loop RFID Tag's tamper-evident design, the pharmaceutical company was able to maintain the integrity of its products throughout the supply chain.",
        "The Smartrac Circus Tamper Loop RFID Tag helped the logistics company to streamline its operations by providing real-time tracking and tamper-evident security features."
    ],
    "Tageos EOS-400 RFID Tag": [
        "The Tageos EOS-400 RFID Tag was an ideal solution for the warehouse manager looking to automate his inventory management process.",
        "The Tageos EOS-400 RFID Tag's long read range made it a perfect fit for the retailer looking to speed up its checkout process.",
        "The Tageos EOS-400 RFID Tag's high-performance capabilities made it a popular choice for the automotive manufacturer looking to improve its supply chain visibility.",
        "Thanks to the Tageos EOS-400 RFID Tag's small and unobtrusive design, the medical equipment manufacturer was able to easily integrate it into its products.",
        "The Tageos EOS-400 RFID Tag's high memory capacity made it an excellent option for the library looking to streamline its book borrowing process."
    ],
    "UPM Raflatac DogBone RFID Tag": [
        "The inventory management system of the warehouse was greatly improved after the implementation of the UPM Raflatac DogBone RFID Tag.",
        "As a veterinarian, Dr. Smith found the UPM Raflatac DogBone RFID Tag to be very useful for identifying and tracking pets.",
        "The UPM Raflatac DogBone RFID Tag was used in the transportation industry to monitor and track shipments in real-time.",
        "The UPM Raflatac DogBone RFID Tag made it easy for hikers to keep track of their gear and supplies on long backpacking trips.",
        "By using the UPM Raflatac DogBone RFID Tag, the shipping company was able to automate their supply chain and reduce manual labor costs."
    ],
    "Zebra Silverline RFID Tag": [
        "The Zebra Silverline RFID Tag was used to improve the accuracy of patient tracking in hospitals and medical facilities.",
        "A retail store was able to reduce the time it took to check inventory levels by using the Zebra Silverline RFID Tag.",
        "The Zebra Silverline RFID Tag was utilized in a food processing plant to track the movement of goods from the production line to the warehouse.",
        "The Zebra Silverline RFID Tag helped farmers in tracking the growth and distribution of crops.",
        "The Zebra Silverline RFID Tag was used to track and monitor the usage of rental equipment, which helped to reduce losses and increase profits."
    ],
    "NXP MIFARE Classic 1K NFC Tag": [
        "John used his NXP MIFARE Classic 1K NFC Tag to easily access his office building with just a tap of his phone.",
        "The NXP MIFARE Classic 1K NFC Tag's compatibility with a variety of devices made it the perfect choice for Mary's IoT project.",
        "With the NXP MIFARE Classic 1K NFC Tag's large memory capacity, Tim was able to store all the necessary data for his project.",
        "The NXP MIFARE Classic 1K NFC Tag's durable construction allowed it to withstand harsh environments, making it ideal for outdoor use.",
        "Jessica's smart home was even smarter with the addition of the NXP MIFARE Classic 1K NFC Tag, which allowed her to control various devices with ease."
    ],
    "STMicroelectronics M24LR16E-R NFC Tag": [
        "The STMicroelectronics M24LR16E-R NFC Tag's long-range communication made it the perfect choice for Alex's industrial IoT project.",
        "Thanks to the STMicroelectronics M24LR16E-R NFC Tag's low power consumption, the battery life of Bill's device was greatly extended.",
        "The STMicroelectronics M24LR16E-R NFC Tag's compact size allowed it to be easily integrated into Sarah's wearable device.",
        "With the STMicroelectronics M24LR16E-R NFC Tag's secure data storage, Susan's confidential information was kept safe from prying eyes.",
        "The STMicroelectronics M24LR16E-R NFC Tag's ability to communicate with both NFC-enabled devices and RFID readers made it a versatile choice for Tom's project."
    ],
    "NTAG 213 NFC Tag": ["Samantha enjoyed the convenience of using her smartphone to unlock her front door with the NTAG 213 NFC Tag.",
                         "Michael was able to easily transfer data between his smartphone and computer using the NTAG 213 NFC Tag.",
                         "The NTAG 213 NFC Tag allowed Emma to quickly and securely make payments without the need for cash or cards.",
                         "Thanks to the NTAG 213 NFC Tag, Jake was able to instantly connect his smartphone to his wireless speaker.",
                         "Using the NTAG 213 NFC Tag, Olivia was able to quickly launch her favorite app on her smartphone."],
    "Sony FeliCa RC-S380 NFC Tag": ["Emily was able to easily make contactless payments on the go with the Sony FeliCa RC-S380 NFC Tag.",
                                    "John enjoyed the ease of using his Sony FeliCa RC-S380 NFC Tag to quickly transfer data between his devices.",
                                    "Thanks to the Sony FeliCa RC-S380 NFC Tag, Rachel was able to effortlessly unlock her front door with her smartphone.",
                                    "The Sony FeliCa RC-S380 NFC Tag made it simple for Alex to quickly connect to the Wi-Fi network at his friend's house.",
                                    "By using the Sony FeliCa RC-S380 NFC Tag, David was able to quickly access his electronic boarding pass at the airport."],
    "Texas Instruments Tag-it HF-I Plus NFC Tag": [
        "John used his Texas Instruments Tag-it HF-I Plus NFC Tag to unlock his smart door lock without fumbling for his keys.",
        "Lena quickly paid for her coffee with her Texas Instruments Tag-it HF-I Plus NFC Tag using her phone's mobile wallet.",
        "By using his Texas Instruments Tag-it HF-I Plus NFC Tag, Adam was able to access his office building without the need for a physical access card.",
        "Sophia's Texas Instruments Tag-it HF-I Plus NFC Tag helped her quickly retrieve her lost luggage at the airport.",
        "Thanks to his Texas Instruments Tag-it HF-I Plus NFC Tag, David was able to easily and securely access his bank account on his phone."
    ],
    "Invengo Inlays NFC Tag": [
        "Mary uses her Invengo Inlays NFC Tag to easily track her pet's movements and monitor their health.",
        "By using an Invengo Inlays NFC Tag, Sam was able to securely and quickly access his medical records.",
        "Jane's Invengo Inlays NFC Tag helped her keep track of her fitness routine and achieve her health goals.",
        "Using Invengo Inlays NFC Tags, the warehouse manager was able to easily and accurately track the location of inventory items.",
        "Thanks to the Invengo Inlays NFC Tag, Maria was able to quickly pay for her public transportation fare without fumbling for cash or a card."
    ],
    "SMARTRAC DogBone NFC Tag": ["John never had to worry about losing his luggage again thanks to the SMARTRAC DogBone NFC Tag securely attached to his bags.",
                                 "The SMARTRAC DogBone NFC Tag allowed Sarah to quickly and easily track her inventory levels for her small business.",
                                 "With the SMARTRAC DogBone NFC Tag, James was able to efficiently manage the parking lot of his busy restaurant.",
                                 "The SMARTRAC DogBone NFC Tag's durability made it the perfect solution for tracking the maintenance schedules of heavy machinery for Tim's company.",
                                 "Alice never forgot to take her medication thanks to the reminders provided by the SMARTRAC DogBone NFC Tag attached to her pillbox."],
    "GAO RFID NFC Tag": ["With the GAO RFID NFC Tag, Maria was able to securely and accurately monitor the location and status of her company's assets.",
                         "The GAO RFID NFC Tag helped Jake streamline the check-in process at his busy gym, making it faster and more efficient for his customers.",
                         "Samantha was able to improve her farm's yield by using the GAO RFID NFC Tag to track the growth and health of her crops.",
                         "The GAO RFID NFC Tag's long read range allowed Derek to quickly and easily inventory his warehouse's stock, saving him valuable time and money.",
                         "The GAO RFID NFC Tag's rugged design made it the perfect choice for tracking the maintenance schedules of heavy machinery for Mark's construction company."],
    "Identiv NFC Tag": ["John used an Identiv NFC Tag to easily transfer information between his smartphone and other devices.",
                        "Emily was able to make secure payments using her Identiv NFC Tag-enabled credit card.",
                        "The Identiv NFC Tag allowed Alex to quickly and easily access his personal data.",
                        "Susan used the Identiv NFC Tag to keep track of her inventory in real-time.",
                        "Using the Identiv NFC Tag, Peter was able to open doors and access control systems with just a tap."],
    "Alien Technology Squiggle NFC Tag": ["The Alien Technology Squiggle NFC Tag allowed Mary to track and manage inventory in real-time.",
                                          "The NFC-enabled Alien Technology Squiggle NFC Tag helped David to quickly and easily access product information.",
                                          "Jane used the Alien Technology Squiggle NFC Tag to easily make mobile payments with her smartphone.",
                                          "The Alien Technology Squiggle NFC Tag allowed Michael to easily share data with his colleagues.",
                                          "Using the Alien Technology Squiggle NFC Tag, Chris was able to streamline his supply chain management."],
    "Barcode tag": [
        "Jane used a barcode tag to quickly scan and track inventory in her warehouse.",
        "The store implemented a barcode tag system to efficiently manage their inventory.",
        "With the help of a barcode tag, John was able to quickly and accurately identify a product.",
        "The hospital used barcode tags to easily identify and track medical supplies and equipment.",
        "The barcode tag on the package helped the delivery person to quickly and easily scan and deliver the package to the right address."
    ],
    "QR code tag": [
        "The museum used QR code tags to provide visitors with additional information about the artwork on display.",
        "The event organizers placed QR code tags around the venue to provide attendees with easy access to the schedule and map.",
        "The QR code tag on the poster led to a website with more information about the upcoming concert.",
        "The restaurant used QR code tags on their menu to allow customers to quickly and easily access nutritional information.",
        "The real estate agent placed QR code tags on the property listings to allow potential buyers to view virtual tours of the homes."
    ],
    "Ekahau Wi-Fi Tags": ["John was able to track the location of valuable assets in real-time using Ekahau Wi-Fi Tags.",
                          "By implementing Ekahau Wi-Fi Tags, the hospital was able to improve patient safety and reduce equipment loss.",
                          "Samantha was able to quickly find an available conference room using the Ekahau Wi-Fi Tags' location tracking feature.",
                          "The Ekahau Wi-Fi Tags' long battery life allowed the university to track the location of students and staff members for extended periods of time.",
                          "By analyzing the data collected by the Ekahau Wi-Fi Tags, the company was able to optimize its workflow and improve efficiency."],
    "AiRISTA Flow Wi-Fi Tags": ["The AiRISTA Flow Wi-Fi Tags enabled the warehouse manager to track the location of inventory in real-time.",
                                "By using AiRISTA Flow Wi-Fi Tags, the hotel was able to improve its guest experience by offering personalized services based on guests' location.",
                                "The AiRISTA Flow Wi-Fi Tags' real-time location tracking allowed the manufacturing company to optimize its production process and reduce waste.",
                                "By implementing AiRISTA Flow Wi-Fi Tags, the school was able to improve the safety of its students and staff members by monitoring their location in real-time.",
                                "The AiRISTA Flow Wi-Fi Tags' ability to provide location-based analytics allowed the retailer to optimize its store layout and improve customer experience."],
    "AeroScout Wi-Fi Tags": ["John never had to worry about losing his equipment again with the AeroScout Wi-Fi Tags that allowed him to track their location in real-time.",
                             "The AeroScout Wi-Fi Tags helped the warehouse manager optimize the placement of their goods to maximize space utilization.",
                             "Samantha was able to monitor her patients' movements and ensure their safety with the AeroScout Wi-Fi Tags.",
                             "With the AeroScout Wi-Fi Tags, the manufacturing company was able to streamline their inventory management and improve efficiency.",
                             "The AeroScout Wi-Fi Tags enabled the school to track their equipment and prevent theft."],
    "CenTrak Wi-Fi Tags": ["The CenTrak Wi-Fi Tags allowed the hospital staff to quickly locate and attend to patients in need.",
                           "Peter was able to track the movements of his workers and optimize their workflow with the CenTrak Wi-Fi Tags.",
                           "The CenTrak Wi-Fi Tags enabled the airport to improve passenger experience by reducing wait times and tracking the location of their luggage.",
                           "With the CenTrak Wi-Fi Tags, the retail store was able to analyze customer traffic and optimize their store layout.",
                           "The CenTrak Wi-Fi Tags helped the university library keep track of their books and ensure they were always available to students."],
    "RF Code Wi-Fi Tags": ["John was able to track the location and temperature of his products in real-time using RF Code Wi-Fi tags, ensuring their safe transport.", "RF Code Wi-Fi tags helped Anna to quickly locate her misplaced assets, saving her valuable time and effort.", "RF Code Wi-Fi tags helped Richard to monitor the temperature of his warehouse and ensure the safety of his perishable products.", "The use of RF Code Wi-Fi tags helped Sarah to optimize her supply chain and reduce operational costs.", "By using RF Code Wi-Fi tags, James was able to automate his inventory management process, reducing manual errors and saving time."],
    "Zebra Wi-Fi Tags": ["Zebra Wi-Fi tags helped Mary to efficiently manage her large fleet of vehicles by providing real-time location data.", "The use of Zebra Wi-Fi tags helped Jack to improve his warehouse efficiency and reduce the time spent locating products.", "Zebra Wi-Fi tags helped Sophia to streamline her asset management process and improve her inventory accuracy.", "By using Zebra Wi-Fi tags, Michael was able to monitor the temperature and humidity of his products and prevent spoilage.", "Zebra Wi-Fi tags helped Emily to optimize her supply chain and reduce operational costs."],
    "IDENTEC SOLUTIONS Wi-Fi Tags": ["John was able to track the location of his inventory in real-time using IDENTEC SOLUTIONS Wi-Fi Tags, improving his supply chain management.", "Sophie's factory was able to improve worker safety by using IDENTEC SOLUTIONS Wi-Fi Tags to monitor their location and provide real-time alerts in case of emergency.", "IDENTEC SOLUTIONS Wi-Fi Tags allowed Emily to optimize her warehouse layout, improving efficiency and reducing wasted space.", "With IDENTEC SOLUTIONS Wi-Fi Tags, Mark was able to track the temperature of his perishable goods in real-time, ensuring they stayed fresh during transit.", "IDENTEC SOLUTIONS Wi-Fi Tags made it easy for Tom to keep track of his equipment, saving him time and reducing the risk of loss or theft."],

    "Ubisense Wi-Fi Tags": ["By using Ubisense Wi-Fi Tags, Maria was able to monitor the location of her staff in real-time, improving safety and reducing response times in case of emergency.", "John's factory was able to optimize their production flow and reduce bottlenecks by using Ubisense Wi-Fi Tags to track the movement of materials and equipment.", "Ubisense Wi-Fi Tags allowed Sarah to monitor the location and temperature of her sensitive medical supplies in real-time, ensuring they were always stored at the right conditions.", "With Ubisense Wi-Fi Tags, James was able to track the progress of his shipments in real-time, ensuring they arrived at their destination on time.", "Ubisense Wi-Fi Tags helped David optimize his workspace layout, improving efficiency and reducing wasted space."],
    "Sonitor Wi-Fi Tags": ["John received real-time updates on the location and movement of his inventory with Sonitor Wi-Fi tags, allowing him to optimize his warehouse operations.", "Using Sonitor Wi-Fi tags, Maria was able to quickly locate and retrieve the medical equipment needed for an emergency surgery.", "The Sonitor Wi-Fi tags' long battery life ensured that Jack's assets were always being tracked, even in remote areas without power outlets.", "Sonitor Wi-Fi tags helped Sarah reduce her inventory loss and theft by providing real-time alerts when items were removed from the premises without authorization.", "Thanks to Sonitor Wi-Fi tags, David was able to increase his team's productivity by reducing the time spent searching for misplaced tools."],

    "Decawave Wi-Fi tags": ["Andrew was able to accurately track the location and status of his assets with Decawave Wi-Fi tags, helping him optimize his supply chain operations.", "Using Decawave Wi-Fi tags, Julia was able to keep track of the movements of personnel and equipment within a construction site, enhancing safety and security.", "The high-precision location data provided by Decawave Wi-Fi tags allowed Michael to improve the efficiency of his manufacturing process.", "Decawave Wi-Fi tags helped Alex prevent unauthorized access to restricted areas by providing real-time alerts and location data of all personnel within the facility.", "Thanks to Decawave Wi-Fi tags, Rachel was able to monitor the movements of her livestock, ensuring their safety and well-being."],
    "HID Global Magnetic Stripe Card": ["As the employees entered the secure facility, they swiped their HID Global magnetic stripe card at the access control point.", "John forgot his HID Global magnetic stripe card at home, so he had to get a temporary one from the security office.", "The HID Global magnetic stripe card enabled the company to monitor the movement of employees throughout the building.", "Sara was able to easily purchase items from the vending machine by swiping her HID Global magnetic stripe card.", "The security team was able to quickly revoke access to the building for former employees by deactivating their HID Global magnetic stripe card."],
    "Zebra Magnetic Stripe Card": ["The Zebra magnetic stripe card allowed the university to track student attendance at sporting events.", "Tom was able to easily pay for his meal at the cafeteria by swiping his Zebra magnetic stripe card.", "The Zebra magnetic stripe card allowed the library to efficiently manage book checkouts and returns.", "The new Zebra magnetic stripe card were more durable than the previous ones, reducing the need for replacements.", "The Zebra magnetic stripe card made it easy for employees to access the parking garage and secure their vehicles."],
    "Datacard Magnetic Stripe Cards": ["John easily tracked the access to his building by implementing Datacard Magnetic Stripe Cards for his employees.", "The Datacard Magnetic Stripe Cards provided a simple and reliable way to manage access control for the company's facilities.", "Sophie was impressed with how the Datacard Magnetic Stripe Cards streamlined her daily office routine.", "The Datacard Magnetic Stripe Cards were essential for ensuring the safety and security of the company's sensitive areas.", "By using Datacard Magnetic Stripe Cards, Rachel's company was able to reduce the risk of unauthorized access."],
    "Magicard Magnetic Stripe Cards": ["Magicard Magnetic Stripe Cards helped prevent theft and unauthorized access by providing a secure identification system.", "By implementing Magicard Magnetic Stripe Cards, David's company was able to better monitor employee access to restricted areas.", "The Magicard Magnetic Stripe Cards were a simple and effective way to manage access control for the company's buildings and facilities.", "With the Magicard Magnetic Stripe Cards, Sam was able to restrict access to certain areas of his building to authorized personnel only.", "The Magicard Magnetic Stripe Cards provided a reliable and secure solution for managing access control in the company's facilities."],
    "Evolis Magnetic Stripe Cards": [
        "The Evolis Magnetic Stripe Cards allowed the company to easily track employee access to secure areas.",
        "The Evolis Magnetic Stripe Cards were quickly implemented and integrated with the company's existing security system.",
        "The use of Evolis Magnetic Stripe Cards improved the company's overall security measures.",
        "With the Evolis Magnetic Stripe Cards, the company was able to limit access to certain areas for specific employees.",
        "The Evolis Magnetic Stripe Cards were an affordable and efficient solution to the company's security needs."
    ],
    "NBS Technologies Magnetic Stripe Cards": [
        "The NBS Technologies Magnetic Stripe Cards made it easy to track employee attendance and timekeeping.",
        "The NBS Technologies Magnetic Stripe Cards were easily integrated into the company's payroll system.",
        "By using the NBS Technologies Magnetic Stripe Cards, the company was able to streamline its HR processes.",
        "The NBS Technologies Magnetic Stripe Cards allowed the company to monitor employee access to sensitive areas.",
        "The NBS Technologies Magnetic Stripe Cards were a cost-effective solution to the company's employee tracking needs."
    ],
    "Matica Magnetic Stripe Cards": [
        "Samantha used her Matica magnetic stripe cards to grant access to employees at her small business.",
        "John's company used Matica magnetic stripe cards to control access to their secure server room.",
        "Matica magnetic stripe cards allowed Rachel to easily and securely pay for her purchases at the grocery store.",
        "David's gym used Matica magnetic stripe cards to track members' gym usage and ensure only authorized users had access.",
        "By implementing Matica magnetic stripe cards, Alex's university was able to secure access to sensitive areas and reduce the risk of theft."
    ],
    "ZXP Series 7 Magnetic Stripe Cards": [
        "Jasmine's company used ZXP Series 7 magnetic stripe cards to track employee attendance.",
        "Using ZXP Series 7 magnetic stripe cards, Michael was able to easily and securely access his office building.",
        "ZXP Series 7 magnetic stripe cards allowed Michelle to quickly and easily make payments for her online purchases.",
        "The ZXP Series 7 magnetic stripe cards were an important part of Max's company's security system, granting access to only authorized personnel.",
        "Implementing ZXP Series 7 magnetic stripe cards helped Natalie's school improve their attendance tracking and reduce errors."
    ],
    "Smart ID Dynamics Magnetic Stripe Cards": ["John was able to seamlessly integrate the Smart ID Dynamics Magnetic Stripe Cards with his existing access control system, improving security and convenience for his employees.",
                                                "Lisa's company was able to increase productivity by using Smart ID Dynamics Magnetic Stripe Cards to track employee time and attendance.",
                                                "With the Smart ID Dynamics Magnetic Stripe Cards, Mark was able to easily grant and revoke access to sensitive areas of his facility.",
                                                "The Smart ID Dynamics Magnetic Stripe Cards helped Sarah streamline her event management process by allowing for easy check-in and tracking of attendees.",
                                                "The use of Smart ID Dynamics Magnetic Stripe Cards helped Tom reduce the risk of identity theft and fraud by implementing a secure and reliable identification system."],
    "IDP Magnetic Stripe Cards": ["With the IDP Magnetic Stripe Cards, Emily was able to enhance the security of her organization by implementing a two-factor authentication system.",
                                  "Jason's business was able to improve customer loyalty by using IDP Magnetic Stripe Cards to offer rewards and discounts.",
                                  "The IDP Magnetic Stripe Cards helped Michael to manage his inventory more efficiently by using them to track product movement.",
                                  "Using IDP Magnetic Stripe Cards, Michelle was able to streamline the payment process at her restaurant, resulting in faster service and happier customers.",
                                  "The IDP Magnetic Stripe Cards helped Robert to monitor employee attendance and performance, leading to increased productivity and a more engaged workforce."],
    "Pozyx Ultrasonic Anchor Tag": ["The Pozyx Ultrasonic Anchor Tag is revolutionizing the way we track objects indoors.",
                                    "With the Pozyx Ultrasonic Anchor Tag, businesses can easily track the movement of assets and inventory within their facilities.",
                                    "The Pozyx Ultrasonic Anchor Tag is particularly useful for logistics companies looking to optimize their warehouse operations.",
                                    "Thanks to the Pozyx Ultrasonic Anchor Tag, retailers can now better manage their inventory and restocking processes.",
                                    "The Pozyx Ultrasonic Anchor Tag is helping hospitals keep track of critical medical equipment, ensuring it is always in the right place at the right time."],
    "Acconeer XM132 Ultrasonic Sensor Tag": ["The Acconeer XM132 Ultrasonic Sensor Tag is a game-changer for IoT devices.",
                                             "The Acconeer XM132 Ultrasonic Sensor Tag can detect movement and distance with incredible accuracy.",
                                             "With the Acconeer XM132 Ultrasonic Sensor Tag, smart homes can become even smarter, automating everyday tasks with ease.",
                                             "The Acconeer XM132 Ultrasonic Sensor Tag is making waves in the robotics industry, enabling robots to better navigate their environments.",
                                             "Thanks to the Acconeer XM132 Ultrasonic Sensor Tag, vehicles can now detect and avoid obstacles with greater precision."],
    "M5Stack Ultrasonic Distance Tag": ["John attached the M5Stack Ultrasonic Distance Tag to his drone to improve its obstacle avoidance capabilities.",
                                        "Sophie used the M5Stack Ultrasonic Distance Tag to measure the distance between her plants and her grow light, ensuring optimal light levels.",
                                        "By using the M5Stack Ultrasonic Distance Tag, Alex was able to accurately measure the depth of the water in his well.",
                                        "The M5Stack Ultrasonic Distance Tag was a crucial component in Maria's robot, allowing it to navigate through complex environments.",
                                        "Thanks to the M5Stack Ultrasonic Distance Tag, Eric's automated garage door was able to detect when a car was entering and exiting."],
    "LightWare SF23/B Ultrasonic Rangefinder Tag": ["Using the LightWare SF23/B Ultrasonic Rangefinder Tag, Tom was able to accurately measure the distance between two moving objects.",
                                                    "Sarah incorporated the LightWare SF23/B Ultrasonic Rangefinder Tag into her robot, giving it the ability to navigate through dark environments.",
                                                    "The LightWare SF23/B Ultrasonic Rangefinder Tag was an essential tool for Mark's surveying work, providing accurate distance measurements in challenging conditions.",
                                                    "By using the LightWare SF23/B Ultrasonic Rangefinder Tag, Emma's drone was able to create a 3D map of the environment it was flying in.",
                                                    "Thanks to the LightWare SF23/B Ultrasonic Rangefinder Tag, James' autonomous lawnmower was able to accurately detect obstacles and avoid them."],
    "Ultrasonic Smart Tag by iTraq": [
        "John was able to track the location of his luggage during a trip thanks to his Ultrasonic Smart Tag by iTraq.",
        "The Ultrasonic Smart Tag by iTraq helped Susan locate her lost pet dog.",
        "Thanks to its long battery life, Ultrasonic Smart Tag by iTraq can be used to track valuable assets for an extended period.",
        "The Ultrasonic Smart Tag by iTraq has a built-in accelerometer that detects motion and alerts the user if an asset is moved.",
        "With its global coverage, the Ultrasonic Smart Tag by iTraq can be used to track assets anywhere in the world."
    ],
    "SRF-U-02 Ultrasonic Sensor Tag by Sonarax": [
        "The SRF-U-02 Ultrasonic Sensor Tag by Sonarax helped Jane detect water leaks in her house before they caused any damage.",
        "Using the SRF-U-02 Ultrasonic Sensor Tag by Sonarax, David was able to monitor the level of liquid in a tank remotely.",
        "Thanks to its small size, the SRF-U-02 Ultrasonic Sensor Tag by Sonarax can be used in a variety of applications, including healthcare and industrial automation.",
        "The SRF-U-02 Ultrasonic Sensor Tag by Sonarax is capable of detecting the presence of objects and measuring distance accurately.",
        "The SRF-U-02 Ultrasonic Sensor Tag by Sonarax is equipped with Bluetooth Low Energy (BLE) and can be connected to a smartphone or a gateway."
    ],
    "Blueberry iMOTION Ultrasonic Positioning Tag": [
        "Jane, the warehouse manager, used the Blueberry iMOTION Ultrasonic Positioning Tag to track the location of inventory in real-time.",
        "Thanks to the Blueberry iMOTION Ultrasonic Positioning Tag, warehouse workers no longer waste time searching for misplaced inventory.",
        "Mike, a retail store owner, implemented the Blueberry iMOTION Ultrasonic Positioning Tag to monitor foot traffic patterns in his store.",
        "The Blueberry iMOTION Ultrasonic Positioning Tag allowed the warehouse supervisor to optimize the layout of the warehouse to increase efficiency.",
        "By using the Blueberry iMOTION Ultrasonic Positioning Tag, John was able to track the location of his lost luggage at the airport and retrieve it in no time.",
    ],
    "Polarbeacon Ultrasonic Beacon Tag": [
        "The Polarbeacon Ultrasonic Beacon Tag was used by hikers to navigate through a dense forest with ease.",
        "The Polarbeacon Ultrasonic Beacon Tag helped the search and rescue team locate the missing hiker in the wilderness.",
        "By using the Polarbeacon Ultrasonic Beacon Tag, swimmers at the waterpark were able to easily find the entrance to the lazy river.",
        "The Polarbeacon Ultrasonic Beacon Tag was used to guide visitors through a large museum and provide them with relevant information about the exhibits.",
        "With the help of the Polarbeacon Ultrasonic Beacon Tag, the theme park was able to improve the visitor experience by providing them with real-time information about ride wait times.",
    ],
    "Ultrack Ultrasonic Vehicle Tracker Tag": ["John felt more secure with Ultrack Ultrasonic Vehicle Tracker Tag installed in his car.",
                                               "Samantha was able to easily monitor her vehicle's location with Ultrack Ultrasonic Vehicle Tracker Tag.",
                                               "The Ultrack Ultrasonic Vehicle Tracker Tag was able to provide detailed information about the vehicle's movement and speed.",
                                               "Ultrack Ultrasonic Vehicle Tracker Tag's battery lasted longer than expected, making it a reliable choice for vehicle tracking.",
                                               "Ultrack Ultrasonic Vehicle Tracker Tag was able to withstand harsh weather conditions and continue functioning."],
    "RACOON Ultrasonic Beacon Tag": ["Robert was able to locate his lost luggage in the airport with RACOON Ultrasonic Beacon Tag.",
                                     "The RACOON Ultrasonic Beacon Tag's small size made it easy to attach to luggage and other items.",
                                     "The RACOON Ultrasonic Beacon Tag's long battery life allowed it to be used for extended periods of time.",
                                     "Jane was able to track her package throughout the delivery process with RACOON Ultrasonic Beacon Tag.",
                                     "The RACOON Ultrasonic Beacon Tag's accuracy in locating items made it a popular choice among logistics companies."],
    "Dialog Bluetooth 5.1 Beacon": ["John was able to track the location of his lost luggage at the airport using the Dialog Bluetooth 5.1 Beacon attached to it.",
                                    "Sophie's retail store was able to send targeted promotions to customers in the store through the Dialog Bluetooth 5.1 Beacons strategically placed around the store.",
                                    "The Dialog Bluetooth 5.1 Beacon in the parking lot of the shopping mall helped Steven locate his car easily.",
                                    "The Dialog Bluetooth 5.1 Beacon placed in the museum helped guide visitors through the exhibits and provide additional information on their smartphones.",
                                    "The Dialog Bluetooth 5.1 Beacon attached to the dog's collar helped its owner track its movements and ensure it didn't get lost."],
    "Portable Tag BLE5.1 iBeacon": ["The Portable Tag BLE5.1 iBeacon on Jane's keychain helped her locate her lost keys within seconds.",
                                    "The Portable Tag BLE5.1 iBeacon attached to the suitcase helped Tom easily identify his luggage at the airport.",
                                    "The Portable Tag BLE5.1 iBeacon placed in the parking lot of the stadium helped Alex locate his car easily after the game.",
                                    "The Portable Tag BLE5.1 iBeacon in the shopping mall helped guide customers to specific stores and provide promotional offers.",
                                    "The Portable Tag BLE5.1 iBeacon attached to the necklace of a senior citizen helped their family keep track of their movements and ensure their safety."],
    "Bluetooth Tag": ["Lisa never lost her keys again, thanks to the Bluetooth Tag that she attached to her keyring.",
                      "The Bluetooth Tag was a game-changer for Mark, who often forgot where he parked his car.",
                      "Sophie's suitcase was safely returned to her thanks to the Bluetooth Tag that she had placed inside it.",
                      "Thanks to the Bluetooth Tag, David was able to track the location of his dog and make sure he didn't wander too far from home.",
                      "The Bluetooth Tag made it easy for Emily to keep track of her belongings, especially when she was traveling."],
    "RAK5010 NB-IoT Bluetooth & LTE-M Bluetooth Tracker": ["John was able to monitor his fleet of trucks in real-time using the RAK5010 NB-IoT Bluetooth & LTE-M Bluetooth Tracker.",
                                                           "Thanks to the RAK5010 NB-IoT Bluetooth & LTE-M Bluetooth Tracker, Sarah never lost her luggage during her travels.",
                                                           "The RAK5010 NB-IoT Bluetooth & LTE-M Bluetooth Tracker helped Mike keep track of his expensive camera equipment while on assignment.",
                                                           "Using the RAK5010 NB-IoT Bluetooth & LTE-M Bluetooth Tracker, Jessica was able to monitor the temperature and humidity of her greenhouse.",
                                                           "The RAK5010 NB-IoT Bluetooth & LTE-M Bluetooth Tracker was a lifesaver for Tim, who was able to locate his stolen bike with its help."],
    "Bluetooth Low Energy Beacon": ["The Bluetooth Low Energy Beacon and Eddystone technology allowed the store to send personalized offers to customers' smartphones as they walked by.", "Tom was able to easily find his way around the unfamiliar museum thanks to the Bluetooth Low Energy Beacon's indoor navigation system.", "The Eddystone Bluetooth Low Energy Beacon technology was used to track attendance at the conference and send notifications to attendees' smartphones.", "The Bluetooth Low Energy Beacon and Eddystone helped the park track the number of visitors and gather data on popular areas of the park.", "The Eddystone Bluetooth Low Energy Beacon technology enabled the bus stop to send real-time bus arrival information to commuters' smartphones."],
    "bluetooth tag": ["The bluetooth tag allowed the logistics company to track inventory throughout the supply chain.", "Sara was able to easily find her lost luggage thanks to the bluetooth tag attached to it.", "The bluetooth tag was used to track the location of assets and equipment in the warehouse.", "The bluetooth tag helped the hospital track the location of medical equipment and ensure it was always available when needed.", "The bluetooth tag enabled the restaurant to track food delivery and ensure orders were delivered in a timely manner."],
    "bluetooth beacon": ["John was able to navigate the museum with ease, thanks to the bluetooth beacon's ability to provide indoor navigation.", "The bluetooth beacon in the grocery store helped Lisa quickly locate the item she was looking for.", "David's office implemented bluetooth beacons to automatically adjust the lighting and temperature when he entered.", "Thanks to the bluetooth beacon installed in the parking lot, Sarah was able to easily find her car.", "The bluetooth beacon installed in the mall sent promotions and offers directly to Michael's phone."],
    "bluetooth tracker": ["Tom was able to keep track of his pet's location with the bluetooth tracker attached to its collar.", "The bluetooth tracker on his luggage gave Jack peace of mind during his travels.", "The bluetooth tracker on the truck helped the delivery company keep track of the shipment.", "The bluetooth tracker on the bike provided real-time location tracking and anti-theft features.", "Jenny never lost her keys again, thanks to the bluetooth tracker she attached to them."],
    "Spytec GPS GL300 GPS Tracker": ["John was able to track the location of his lost luggage using the Spytec GPS GL300 GPS Tracker.", "The Spytec GPS GL300 GPS Tracker helped Sarah to locate her stolen car and alert the authorities.", "Mike used the Spytec GPS GL300 GPS Tracker to track the location of his delivery trucks in real-time.", "The Spytec GPS GL300 GPS Tracker's long battery life ensured that it could provide uninterrupted tracking for weeks.", "The Spytec GPS GL300 GPS Tracker's compact design allowed it to be easily concealed."],
    "Tracki GPS Tracker": ["Tom used the Tracki GPS Tracker to keep track of his elderly father's location in case he wandered off.", "The Tracki GPS Tracker's geofencing feature alerted Mary when her dog left the designated area.", "With the Tracki GPS Tracker, Alex was able to monitor the location and speed of his teenage son's car.", "The Tracki GPS Tracker's SOS button allowed Mark to quickly call for help during an emergency.", "The Tracki GPS Tracker's real-time location tracking feature helped Anna to locate her lost phone."],
    "Amcrest GPS Tracker": ["Alex was able to keep track of his delivery truck's location using the Amcrest GPS Tracker, which helped him optimize his delivery routes.",
                            "The Amcrest GPS Tracker allowed Lisa to keep track of her teenage son's location, giving her peace of mind when he was out with friends.",
                            "Using the Amcrest GPS Tracker, Jason was able to track his pet's location during a walk in the park, which gave him an added layer of security.",
                            "The Amcrest GPS Tracker helped John monitor the location and speed of his company vehicles, making it easier to ensure employee safety and productivity.",
                            "Mary used the Amcrest GPS Tracker to monitor her elderly mother's location and ensure she didn't wander off and get lost."],
    "LandAirSea 54 GPS Tracker": ["After his bike was stolen, Eric was able to track it down using the LandAirSea 54 GPS Tracker he had attached to it.",
                                  "The LandAirSea 54 GPS Tracker helped Sarah keep track of her luggage during a trip overseas, ensuring it didn't get lost or stolen.",
                                  "Mike was able to monitor his fleet of trucks using the LandAirSea 54 GPS Tracker, which helped him optimize his routes and improve his delivery times.",
                                  "Using the LandAirSea 54 GPS Tracker, Jennifer was able to keep track of her teenage daughter's location, ensuring she was safe and not getting into any trouble.",
                                  "The LandAirSea 54 GPS Tracker helped Bob keep track of his boat's location, which gave him peace of mind when it was out on the water."],
    "Gf07 Magnetic Mini Car Gps Tracker": [
        "John was able to track his car's location in real-time using the Gf07 Magnetic Mini Car GPS Tracker.",
        "Maria installed the Gf07 Magnetic Mini Car GPS Tracker on her delivery truck to keep track of her drivers and packages.",
        "Thanks to the Gf07 Magnetic Mini Car GPS Tracker's compact size, it can be easily hidden in a car or backpack for covert tracking.",
        "The Gf07 Magnetic Mini Car GPS Tracker's long battery life ensures that it can be used for extended periods of time without needing a recharge.",
        "With the Gf07 Magnetic Mini Car GPS Tracker's geofencing feature, you can set up alerts to be notified if your vehicle enters or exits a specific area."
    ],
    "Piccolo ATX Gps Tracker": [
        "The Piccolo ATX GPS Tracker is a powerful tool for fleet managers to optimize their operations and improve efficiency.",
        "Sarah uses the Piccolo ATX GPS Tracker on her boat to keep track of its location and ensure that it doesn't drift too far out to sea.",
        "The Piccolo ATX GPS Tracker's rugged design allows it to withstand harsh environments and extreme temperatures.",
        "The Piccolo ATX GPS Tracker's real-time tracking capabilities allow users to monitor the location and status of their assets 24/7.",
        "With the Piccolo ATX GPS Tracker's advanced reporting and analytics features, businesses can gain valuable insights into their operations and make data-driven decisions."
    ],
    "Solar Powered LoRa GPS Tracker": [
        "John was able to track his shipment even in remote areas using the Solar Powered LoRa GPS Tracker.",
        "The Solar Powered LoRa GPS Tracker helped Anna to monitor the location and temperature of her food delivery truck.",
        "Thanks to the long battery life of the Solar Powered LoRa GPS Tracker, Peter was able to monitor his solar panels for weeks without recharging the device.",
        "The Solar Powered LoRa GPS Tracker's compact and waterproof design made it the perfect solution for tracking boats and other watercraft.",
        "The Solar Powered LoRa GPS Tracker helped Sarah keep an eye on her outdoor equipment, ensuring that nothing went missing or was damaged."
    ],
    "Piccolo ATMS GPS Tracker": [
        "Mike was able to track his fleet of delivery trucks in real-time with the Piccolo ATMS GPS Tracker.",
        "The Piccolo ATMS GPS Tracker's geofencing feature alerted Amy when her car entered or exited a predefined area.",
        "Using the Piccolo ATMS GPS Tracker, Kevin was able to monitor the speed and location of his teenage daughter's car, ensuring her safety on the road.",
        "The Piccolo ATMS GPS Tracker helped Jake recover his stolen bike by providing the location of the thief's hideout.",
        "Sophie was able to monitor the location and movement of her luggage using the Piccolo ATMS GPS Tracker during her travels."
    ],
    "ReachFar Rf-v26 Solar Power Waterproof Gps Tracker": [
        "When Jennifer went on her hiking trip, she was able to keep her family updated on her location using her ReachFar Rf-v26 Solar Power Waterproof Gps Tracker.",
        "The ReachFar Rf-v26 Solar Power Waterproof Gps Tracker allowed James to track his dog's movements and keep him safe while on walks.",
        "With the ReachFar Rf-v26 Solar Power Waterproof Gps Tracker, Susan was able to easily locate her lost luggage during her travels.",
        "The ReachFar Rf-v26 Solar Power Waterproof Gps Tracker's long battery life was a lifesaver for John during his week-long camping trip.",
        "Thanks to the ReachFar Rf-v26 Solar Power Waterproof Gps Tracker, David was able to accurately track the miles he ran during his morning jog."
    ],
    "Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator": [
        "The Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator was the perfect size for Sarah's small dog.",
        "With the Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator, Mark was able to track his bike's movements and prevent theft.",
        "The Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator helped Olivia keep track of her elderly mother's movements and ensure her safety.",
        "Thanks to the Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator, Daniel was able to locate his lost phone within minutes.",
        "When Thomas went on his solo backpacking trip, he felt more at ease knowing he had the Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator in case of an emergency."
    ],
    "ReachFar Rf-v26 Solar Power Waterproof Gps Tracker": [
        "When Jennifer went on her hiking trip, she was able to keep her family updated on her location using her ReachFar Rf-v26 Solar Power Waterproof Gps Tracker.",
        "The ReachFar Rf-v26 Solar Power Waterproof Gps Tracker allowed James to track his dog's movements and keep him safe while on walks.",
        "With the ReachFar Rf-v26 Solar Power Waterproof Gps Tracker, Susan was able to easily locate her lost luggage during her travels.",
        "The ReachFar Rf-v26 Solar Power Waterproof Gps Tracker's long battery life was a lifesaver for John during his week-long camping trip.",
        "Thanks to the ReachFar Rf-v26 Solar Power Waterproof Gps Tracker, David was able to accurately track the miles he ran during his morning jog."
    ],
    "Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator": [
        "The Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator was the perfect size for Sarah's small dog.",
        "With the Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator, Mark was able to track his bike's movements and prevent theft.",
        "The Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator helped Olivia keep track of her elderly mother's movements and ensure her safety.",
        "Thanks to the Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator, Daniel was able to locate his lost phone within minutes.",
        "When Thomas went on his solo backpacking trip, he felt more at ease knowing he had the Super Mini Size Gps Tracker Gsm Agps Wifi Lbs Locator in case of an emergency."
    ]
}


if __name__ == "__main__":
    start = time.time()
    phrases = []
    with open("./_6_sentences.py", 'w') as f:
        phrase_count = 0
        for phrase_dic in sentences:
            for key in phrase_dic:
                for phrase in phrase_dic[key]:
                    phrases.append(
                        {'type': 'DEVICE', 'word': key, 'phrase': phrase})
        print(f'phrase count: {len(phrases)}')
        print(f'This operation took {time.time()-start} seconds to complete.')
        f.write(f'{phrases}')
    # for l in all_sentences:
    #     for k in l.keys():
    #         if len(l[k]) != 5:
    #             print(f'Key: {k}')
