from authorizenet.apicontrollers import createTransactionController
from errors import Error_E00027
from authorize_net_xml_elements import CreateTransactionRequest

# TODO Build transaction with mult elements of the same type, ie. lineItems


def authorize_credit_card(merchant_name, merchant_transactionKey, transaction_amount, mobileDeviceId=None, refId=None,
                          employeeId=None, track1=None, track2=None, credit_card_number=None,
                          credit_card_expiration_date=None, cardCode=None, createProfile=None, solution_id=None,
                          invoiceNumber=None, order_description=None, #lineItems,
                          tax_amount=None, tax_name=None, tax_description=None, duty_amount=None, duty_name=None,
                          duty_description=None, shipping_amount=None, shipping_name=None, shipping_description=None,
                          taxExempt=None, poNumber=None, customer_type=None, customer_id=None, customer_email=None,
                          billTo_firstName=None, billTo_lastName=None, billTo_company=None, billTo_address=None,
                          billTo_city=None, billTo_state=None, billTo_zip=None, billTo_country=None,
                          billTo_phoneNumber=None, billTo_faxNumber=None, shipTo_firstName=None, shipTo_lastName=None,
                          shipTo_company=None, shipTo_address=None, shipTo_city=None, shipTo_state=None,
                          shipTo_zip=None, shipTo_country=None, customerIp=None, authenticationIndicator=None,
                          cardholderAuthenticationValue=None, marketType=None, deviceType=None, settingName=None,
                          settingValue=None, userField_name=None, userField_value=None,
                           ):

    # must provide track1, track2 or cardNumber and expirationDate
    if not (track1 or track2 or (credit_card_number and credit_card_expiration_date)):
        pass # TODO raise error

    TransactionRequest = CreateTransactionRequest(merchant_name=merchant_name,
                                                  transactionKey=merchant_transactionKey,
                                                  amount=transaction_amount,
                                                  employeeId=employeeId,
                                                  track1=track1,
                                                  track2=track2,
                                                  cardNumber=credit_card_number,
                                                  expirationDate=credit_card_expiration_date,
                                                  cardCode=cardCode,
                                                  createProfile=createProfile,
                                                  solution_id=solution_id,
                                                  invoiceNumber=invoiceNumber,
                                                  description=order_description,
                                                  #TODO lineItems,
                                                  tax_amount=tax_amount,
                                                  tax_name=tax_name,
                                                  tax_description=tax_description,
                                                  duty_amount=duty_amount,
                                                  duty_name=duty_name,
                                                  duty_description=duty_description,
                                                  shipping_amount=shipping_amount,
                                                  shipping_name=shipping_name,
                                                  shipping_description=shipping_description,
                                                  taxExempt=taxExempt,
                                                  poNumber=poNumber,
                                                  type=customer_type,
                                                  customer_id=customer_id,
                                                  email=customer_email,
                                                  customerAddress_firstName=billTo_firstName,
                                                  customerAddress_lastName=billTo_lastName,
                                                  customerAddress_company=billTo_company,
                                                  customerAddress_address=billTo_address,
                                                  customerAddress_city=billTo_city,
                                                  customerAddress_state=billTo_state,
                                                  customerAddress_zip=billTo_zip,
                                                  customerAddress_country=billTo_country,
                                                  customerAddress_phoneNumber=billTo_phoneNumber,
                                                  customerAddress_faxNumber=billTo_faxNumber,
                                                  shipTo_firstName=shipTo_firstName,
                                                  shipTo_lastName=shipTo_lastName,
                                                  shipTo_company=shipTo_company,
                                                  shipTo_address=shipTo_address,
                                                  shipTo_city=shipTo_city,
                                                  shipTo_state=shipTo_state,
                                                  shipTo_zip=shipTo_zip,
                                                  shipTo_country=shipTo_country,
                                                  customerIP=customerIp,
                                                  authenticationIndicator=authenticationIndicator,
                                                  cardholderAuthenticationValue=cardholderAuthenticationValue,
                                                  marketType=marketType,
                                                  deviceType=deviceType,
                                                  settingName=settingName,
                                                  settingValue=settingValue,
                                                  userField_name=userField_name,
                                                  userField_value=userField_value,
                                                  mobileDeviceId=mobileDeviceId,
                                                  transactionType='authOnlyTransaction',
                                                  refId=refId,
                                                  )

    TransactionController = createTransactionController(TransactionRequest)
    TransactionController.execute()
    response = TransactionController.getresponse()

    if response.messages.resultCode == 'Error':
        for message in response.messages.message:
            if message.code == 'E00027':
                raise Error_E00027(response)

    return response


def charge_new_credit_card(merchant_name, merchant_transactionKey, transaction_amount, employeeId=None, track1=None,
                           track2=None, credit_card_number=None, credit_card_expiration_date=None, cardCode=None,
                           createProfile=None, solution_id=None, invoiceNumber=None, order_description=None, #lineItems,
                           tax_amount=None, tax_name=None, tax_description=None, duty_amount=None, duty_name=None,
                           duty_description=None, shipping_amount=None, shipping_name=None, shipping_description=None,
                           taxExempt=None, poNumber=None, customer_type=None, customer_id=None, customer_email=None,
                           billTo_firstName=None, billTo_lastName=None, billTo_company=None, billTo_address=None,
                           billTo_city=None, billTo_state=None, billTo_zip=None, billTo_country=None,
                           billTo_phoneNumber=None, billTo_faxNumber=None, shipTo_firstName=None, shipTo_lastName=None,
                           shipTo_company=None, shipTo_address=None, shipTo_city=None, shipTo_state=None,
                           shipTo_zip=None, shipTo_country=None, customerIp=None, authenticationIndicator=None,
                           cardholderAuthenticationValue=None, marketType=None, deviceType=None, settingName=None,
                           settingValue=None, userField_name=None, userField_value=None, mobileDeviceId=None,
                           refId=None,):

    # must provide track1, track2 or cardNumber and expirationDate
    if not (track1 or track2 or (credit_card_number and credit_card_expiration_date)):
        pass # TODO raise error

    TransactionRequest = CreateTransactionRequest(merchant_name=merchant_name,
                                                  transactionKey=merchant_transactionKey,
                                                  amount=transaction_amount,
                                                  employeeId=employeeId,
                                                  track1=track1,
                                                  track2=track2,
                                                  cardNumber=credit_card_number,
                                                  expirationDate=credit_card_expiration_date,
                                                  cardCode=cardCode,
                                                  createProfile=createProfile,
                                                  solution_id=solution_id,
                                                  invoiceNumber=invoiceNumber,
                                                  description=order_description,
                                                  #TODO lineItems,
                                                  tax_amount=tax_amount,
                                                  tax_name=tax_name,
                                                  tax_description=tax_description,
                                                  duty_amount=duty_amount,
                                                  duty_name=duty_name,
                                                  duty_description=duty_description,
                                                  shipping_amount=shipping_amount,
                                                  shipping_name=shipping_name,
                                                  shipping_description=shipping_description,
                                                  taxExempt=taxExempt,
                                                  poNumber=poNumber,
                                                  type=customer_type,
                                                  customer_id=customer_id,
                                                  email=customer_email,
                                                  customerAddress_firstName=billTo_firstName,
                                                  customerAddress_lastName=billTo_lastName,
                                                  customerAddress_company=billTo_company,
                                                  customerAddress_address=billTo_address,
                                                  customerAddress_city=billTo_city,
                                                  customerAddress_state=billTo_state,
                                                  customerAddress_zip=billTo_zip,
                                                  customerAddress_country=billTo_country,
                                                  customerAddress_phoneNumber=billTo_phoneNumber,
                                                  customerAddress_faxNumber=billTo_faxNumber,
                                                  shipTo_firstName=shipTo_firstName,
                                                  shipTo_lastName=shipTo_lastName,
                                                  shipTo_company=shipTo_company,
                                                  shipTo_address=shipTo_address,
                                                  shipTo_city=shipTo_city,
                                                  shipTo_state=shipTo_state,
                                                  shipTo_zip=shipTo_zip,
                                                  shipTo_country=shipTo_country,
                                                  customerIP=customerIp,
                                                  authenticationIndicator=authenticationIndicator,
                                                  cardholderAuthenticationValue=cardholderAuthenticationValue,
                                                  marketType=marketType,
                                                  deviceType=deviceType,
                                                  settingName=settingName,
                                                  settingValue=settingValue,
                                                  userField_name=userField_name,
                                                  userField_value=userField_value,
                                                  mobileDeviceId=mobileDeviceId,
                                                  transactionType='authCaptureTransaction',
                                                  refId=refId,
                                                  )

    TransactionController = createTransactionController(TransactionRequest)
    TransactionController.execute()
    response = TransactionController.getresponse()

    if response.messages.resultCode == 'Error':
        for message in response.messages.message:
            if message.code == 'E00027':
                raise Error_E00027(response)

    return response


def charge_authorized_credit_card(merchant_name, merchant_transactionKey, transaction_amount, refTransId,
                                  credit_card_number, credit_card_expiration_date, mobileDeviceId=None, refId=None,):

    TransactionRequest = CreateTransactionRequest(merchant_name=merchant_name,
                                                  transactionKey=merchant_transactionKey,
                                                  transactionType='authCaptureTransaction',
                                                  amount=transaction_amount,
                                                  refTransId=refTransId,
                                                  cardNumber=credit_card_number,
                                                  expirationDate=credit_card_expiration_date,
                                                  mobileDeviceId=mobileDeviceId,
                                                  refId=refId,
                                                  )
    TransactionController = createTransactionController(TransactionRequest)
    TransactionController.execute()
    response = TransactionController.getresponse()

    if response.messages.resultCode == 'Error':
        for message in response.messages.message:
            if message.code == 'E00027':
                raise Error_E00027(response)

    return response


def refund_credit_card(merchant_name, merchant_transactionKey, transaction_amount, refTransId, credit_card_number,
                       credit_card_expiration_date, mobileDeviceId=None, refId=None, paymentProfileId=None,
                       cardCode=None, shippingProfileId=None, bankAccount_accountNumber=None,):


    TransactionRequest = CreateTransactionRequest(merchant_name=merchant_name,
                                                  transactionKey=merchant_transactionKey,
                                                  transactionType='refundTransaction',
                                                  amount=transaction_amount,
                                                  refTransId=refTransId,
                                                  cardNumber=credit_card_number,
                                                  expirationDate=credit_card_expiration_date,
                                                  mobileDeviceId=mobileDeviceId,
                                                  refId=refId,
                                                  paymentProfileId=paymentProfileId,
                                                  cardCode=cardCode,
                                                  shippingProfileId=shippingProfileId,
                                                  accountNumber=bankAccount_accountNumber,
                                                  )

    TransactionController = createTransactionController(TransactionRequest)
    TransactionController.execute()
    response = TransactionController.getresponse()

    if response.messages.resultCode == 'Error':
        for message in response.messages.message:
            if message.code == 'E00027':
                raise Error_E00027(response)

    return response


def void_credit_card(merchant_name, merchant_transactionKey, refTransId, mobileDeviceId=None, refId=None,):
    TransactionRequest = CreateTransactionRequest(merchant_name=merchant_name,
                                                  transactionKey=merchant_transactionKey,
                                                  refTransId=refTransId,
                                                  transactionType='voidTransaction',
                                                  refId=refId,
                                                  )
    TransactionController = createTransactionController(TransactionRequest)
    TransactionController.execute()
    response = TransactionController.getresponse()

    if response.messages.resultCode == 'Error':
        for message in response.messages.message:
            if message.code == 'E00027':
                raise Error_E00027(response)

    return response

