
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  elif value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

# lower limit assignment removed from the if else conditions
def classify_temperature_breach(coolingType, temperatureInC):

  lowerLimit = 0
  upperLimit = 0
  coolingTypeLimitDict = {'PASSIVE_COOLING':35,'HI_ACTIVE_COOLING':45,'MED_ACTIVE_COOLING':40}
  upperLimit = coolingTypeLimitDict[coolingType]
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  # recepient repeated - refactored
  print(f'To: {recepient}')
  breachTypeStatusDict = {'TOO_LOW' : 'too low','TOO_HIGH': 'too high'}
  status = breachTypeStatusDict[breachType]
  print('Hi, the temperature is '+status)

