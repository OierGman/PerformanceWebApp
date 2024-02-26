import pywhatkit as kit

# Performance messages

# DCR
dcrTarget = 98.5
dcr = "% - DCR (Delivery Completion Rate)\n" \
      "This is a summary of all parcels assigned to deliver against parcels actually delivered. The target " \
      "is 99%. \n"
dcr_good = "You have received a score of GREAT or above - Your delivering capabilities have been noticed."
dcr_bad = "You have received a score of Fair or below - This is because too many of your parcels are coming back " \
          "to the depo. Whether it be Customer Unavailable, Unable to Access or Damaged parcel. " \
          "You can improve this by re-attempting deliveries at the end of your shift under Itinerary > Summary > " \
          "re-attemptable."

# DNR DPMO
dnrTarget = 1900
dnr = " - DNR DPMO (Did Not Receive per million opportunities)\n" \
      "What you might know as concessions (per million opportunities), this means that the number of parcels you have "\
      "delivered is taken into account. The target is less than 1100.\n"
dnr_good = "You have received a score of GREAT or above - You are delivering with quality."
dnr_bad = "You have received a score of Fair or below - Reasons for this vary, parcel being left in unsecure" \
          " locations, resulting in theft or simply that the customer was not able to locate the parcel. How can " \
          "it be improved? always find a secure location, use the miss you card and explain how to find the parcel."

# POD
podTarget = 96
pod = "% - POD (Photo on Delivery)\n" \
      "This is The quality of the pictures taken. This checks whether your images contain hands, people, " \
      "personal information like licence plates, blurriness and light level. The target is above 97%.\n"
pod_good = "You have received a score of GREAT or above - The images you are taking are in line with what is expected."
pod_bad = "You have received a score of Fair or below - You need to start taking better images, you can do this by" \
          "making sure you clearly capture the parcel in your image. No hands holding parcels, no people in your " \
          "images and use the flash to capture images."

# CC
ccTarget = 95
cc = "% - CC (Contact Compliance)\n" \
     "This metric is checking if the customer was contacted before delivery is attempted and then marked as " \
     "undeliverable. If the Flex app prompts you to contact the customer, you must contact the customer. The " \
     "target is 98%. \n"
cc_good = "You have received a score of GREAT or above - Keep calling and texting it significantly helps your score"
cc_bad = "You have received a score of Fair or below - You must make sure that customers are being called before " \
         "marking parcels as undeliverable. Alternatively you can skip the delivery and re-attempt later. " \
         "Improving this score will significantly help with DCR, contacting for safe place or access results" \
         " in delivered parcels."

# PHR
phrTarget = 96.5
phr = "% - PHR (Preference Honor Rate)\n" \
      "PHR is checking if we are being loyal to the customers preferred delivery location. The top option before " \
      "swiping to finish. The target is 97%. \n"
phr_good = "You have received a score of GREAT or above - Keep selecting the customers preferred delivery location."
phr_bad = "You have received a score of Fair or below - This is because you are not delivering where the customer " \
          "has requested. If you think it is not safe to deliver. Contact the customer and ask for a new safe location" \
          " then continue on the app with preferred location and take a clear image. You can also use the miss you card" \
          " instead of calling the customer."

# DEX
dexTarget = 83
dex = "% - DEX (Delivery Experience)\n" \
      "This is the customer feedback per delivery. Note - concessions are counted within this metric. The target " \
      "is 84.5%.\n"
dex_good = "You have received a score of GREAT or above - Customers are happy with your service"
dex_bad = "You have received a score of Fair or below - You need to improve your interaction with customers. " \
          "simply asking about their day/wishing them a good day will massively increase this metric. " \
          "poor DEX is often a sign of doorstepping - doorstepping will negatively affect your score across" \
          " all metrics."


closingMessage = "This message aims to constructively support you, our delivery partners in achieving the best" \
                 " possible score by studying your week on week trends.\n\n" \
                 "Many thanks, FUKP Management\n\n" \
                 "This message has been automatically generated - no need to reply"


def sendperformancemessage(dict):
    message = ''

    message += str(round(float(dict['DCR']) * 100, 2))
    message += dcr

    if float(dict['DCR']) * 100 > dcrTarget:
        message += dcr_good
        message += "\n\n"
    else:
        message += dcr_bad
        message += "\n\n"

    if dict['DNR'] == '-':
        message += '0'
        message += dnr
        message += dnr_good
        message += "\n\n"
    elif int(dict['DNR']) < 1900:
        message += str(dict['DNR'])
        message += dnr
        message += dnr_good
        message += "\n\n"
    else:
        message += str(dict['DNR'])
        message += dnr
        message += dnr_bad
        message += "\n\n"

    # if float(dict['POD']) * 100 > podTarget or dict['POD'] == '-':
    if dict['POD'] == '-':
        message += "100"
        message += pod
        message += pod_good
        message += "\n\n"
    elif float(dict['POD']) * 100 > podTarget:
        message += str(round(float(dict['POD']) * 100, 2))
        message += pod
        message += pod_good
        message += "\n\n"
    else:
        message += str(round(float(dict['POD']) * 100, 2))
        message += pod
        message += pod_bad
        message += "\n\n"

    if dict['CC'] == '-':
        message += '100'
        message += cc
        message += cc_good
        message += "\n\n"
    elif float(dict['CC']) * 100 > ccTarget:
        message += str(round(float(dict['CC']) * 100, 2))
        message += cc
        message += cc_good
        message += "\n\n"
    else:
        message += str(round(float(dict['CC']) * 100, 2))
        message += cc
        message += cc_bad
        message += "\n\n"

    if dict['PHR'] == '-':
        message += '100'
        message += phr
        message += phr_good
        message += "\n\n"
    elif float(dict['PHR']) * 100 > phrTarget:
        message += str(round(float(dict['PHR']) * 100, 2))
        message += phr
        message += phr_good
        message += "\n\n"
    else:
        message += str(round(float(dict['PHR']) * 100, 2))
        message += phr
        message += phr_bad
        message += "\n\n"

    if dict['DEX'] == '-':
        message += '100'
        message += dex
        message += dex_good
        message += "\n\n"
    elif float(dict['DEX']) * 100 > dexTarget:
        message += str(round(float(dict['DEX']) * 100, 2))
        message += dex
        message += dex_good
        message += "\n\n"
    else:
        message += str(round(float(dict['DEX']) * 100, 2))
        message += dex
        message += dex_bad
        message += "\n\n"

    message += closingMessage

    # str(dict['Num'])
    kit.sendwhatmsg_instantly("+" + str(dict['Num']), "Hello " + dict['Name'] + ", \n\nThis is an update on your "
                              "performance based on last weeks deliveries. This will help you get an understanding of "
                              "how you are performing against the benchmark. This will also help you identify the areas"
                              " of operation that require some due diligence.\n\n"+"Your overall score last week was: "
                              + dict['Status'] + " - " + str(dict['Score'])
                              + "\n\n" + message, 15, True)


