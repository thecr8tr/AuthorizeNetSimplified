from authorizenet import apicontractsv1


class impersonationAuthentication(apicontractsv1.impersonationAuthenticationType):
    """
    Not described in API
    :partnerLoginIdpartnerLoginId: (Up to 25 Characters) REQUIRED
    :partnerTransactionKey: (Up to 16 Characters) REQUIRED
    :return: None
    """
    def __init__(self, partnerLoginIdpartnerLoginId, partnerTransactionKey):
        super(impersonationAuthentication, self).__init__()
        self.partnerLoginIdpartnerLoginId = partnerLoginIdpartnerLoginId
        self.partnerTransactionKey = partnerTransactionKey


class fingerPrint(apicontractsv1.fingerPrintType):
    """
    Not described in API
    :hashValue: REQUIRED
    :timestamp: REQUIRED
    :sequence: OPTIONAL
    :currencyCode: OPTIONAL
    :amount: OPTIONAL
    :return: None
    """
    def __init__(self, hashValue, timestamp, sequence=None, currencyCode=None, amount=None):
        super(fingerPrint, self).__init__()
        self.hashValue = hashValue
        self.timestamp = timestamp
        if sequence:
            self.sequence = sequence
        if currencyCode:
            self.currencyCode = currencyCode
        if amount:
            self.amount = amount


class merchantAuthentication(apicontractsv1.merchantAuthenticationType):
    """
    This class builds a merchant object that identifies the merchant to Authorize.net
    :name: login id/name provided from Authorize.net (Up to 25 Characters) OPTIONAL
    ONE OF THE FOLLOWING REQUIRED:::
        :transactionKey: transaction key provided from Authorize.net (16 Characters) CONDITIONAL
        :sessionToken: CONDITIONAL
        :password: (40 Characters Max) CONDITIONAL
        :impersonationAuthentication: See impersonationAuthentication Object CONDITIONAL
            :partnerLoginIdpartnerLoginId: (Up to 25 Characters) REQUIRED
            :partnerTransactionKey: (Up to 16 Characters) REQUIRED
        :fingerPrint: See fingerPrint Object CONDITIONAL
            :hashValue: REQUIRED
            :timestamp: REQUIRED
            :sequence: OPTIONAL
            :currencyCode: OPTIONAL
            :amount: OPTIONAL
    :mobileDeviceId: (60 Characters Max) OPTIONAL
    :return: None
    """
    def __init__(self, name=None, transactionKey=None, sessionToken=None, password=None,
                 partnerLoginIdpartnerLoginId=None, partnerTransactionKey=None, hashValue=None, timestamp=None,
                 sequence=None, currencyCode=None, amount=None, mobileDeviceId=None):
        super(merchantAuthentication, self).__init__()
        if name:
            self.name = name
        if not(transactionKey or sessionToken or password or (partnerLoginIdpartnerLoginId and partnerTransactionKey)
               or (hashValue and timestamp)):
            pass # TODO raise error
        else:
            if transactionKey:
                self.transactionKey = transactionKey
            elif sessionToken:
                self.sessionToken = sessionToken
            elif password:
                self.password = password
            elif partnerLoginIdpartnerLoginId and partnerTransactionKey:
                self.impersonationAuthentication = impersonationAuthentication(partnerLoginIdpartnerLoginId,
                                                                               partnerTransactionKey)
            elif hashValue and timestamp:
                self.fingerPrint = fingerPrint(hashValue, timestamp, sequence, currencyCode, amount)
        if mobileDeviceId:
            self.mobileDeviceId = mobileDeviceId


class creditCard(apicontractsv1.creditCardType):
    """

    :Extends creditCardSimpleType:
        :cardNumber: Format of cardNumber should be numeric string or four X's followed by the last four digits (4-16 characters) REQUIRED
        :expirationDate: Format of expirationDate should be YearMonth (such as 2001-10) or four X's (4-7 characters) REQUIRED
    :cardCode: (Integer, 3 to 4 digits) OPTIONAL
    :isPaymentToken: True if CardNumber passed in is a PaymentToken, False if a real creditCardNumber. (True, False) OPTIONAL
    :cryptogram: If the CardNumber passed in is a paymentToken, a cryptogram is needed for one-off payments. (String) CONDITIONAL
    :return: None
    """
    def __init__(self, cardNumber, expirationDate, cardCode=None, isPaymentToken=None, cryptogram=None):
        super(creditCard, self).__init__()
        self.cardNumber = cardNumber
        self.expirationDate = expirationDate
        if cardCode:
            self.cardCode = cardCode
        if isPaymentToken is not None:
            self.isPaymentToken = isPaymentToken
        if cryptogram:
            self.cryptogram = cryptogram


class bankAccount(apicontractsv1.bankAccountType):
    """

    :accountType: string containing: checking OR savings OR businessChecking  OPTIONAL
    :routingNumber: Format of routingNumber should be nine digits or four X's followed by the last four digits. (max 9 char)
    :accountNumber: Format of accountNumber should be numeric string or four X's followed by the last four digits. (max 17 char)
    :nameOnAccount: (max 22 char)
    :echeckType: string containing: PPD or WEB or CCD or TEL or ARC or BOC  OPTIONAL
    :bankName: (max 50 char) OPTIONAL
    :checkNumber: (max 15 char) OPTIONAL
    :return: None
    """
    def __init__(self, routingNumber, accountNumber, nameOnAccount, accountType=None,
                 echeckType=None, bankName=None, checkNumber=None):
        super(bankAccount, self).__init__()
        if accountType:
            self.accountType = accountType
        self.routingNumber = routingNumber
        self.accountNumber = accountNumber
        self.nameOnAccount = nameOnAccount
        if echeckType:
            self.echeckType = echeckType
        if bankName:
            self.bankName = bankName
        if checkNumber:
            self.checkNumber = checkNumber


# TODO define 'Valid Track 1/2 data'
class creditCardTrackData(apicontractsv1.creditCardTrackType):
    """
    This class builds a track object with one of the two children required if Credit Card is Present and card number and
            expiration date are absent (one of the following is required: track1, track2, or expiration date and card
            number (stored elsewhere))
    :track1: ???Valid Track1 data with starting and ending sentinel characters discarded??? (string) CONDITIONAL
    :track2: ???Valid Track1 data with starting and ending sentinel characters discarded??? (string) CONDITIONAL
    :return: None
    """
    def __init__(self, track1=None, track2=None):
        super(creditCardTrackData, self).__init__()
        self.track1 = track1
        self.track2 = track2


#TODO Need more information about this element and it's children
class KeyManagementScheme(apicontractsv1.KeyManagementScheme):
    """
    No documentation in API reference...Not sure how this works
    :DUKPT:
        :Operation:
            :DECRYPT:
        :Mode:
            :PIN: (string) OPTIONAL/CONDITIONAL???
            :Data: (string) OPTIONAL/CONDITIONAL???
        :DeviceInfo:
            :Description: (string)
        :EncryptedData:
            :Value: (string)
        :return: None
    """
    def __init__(self, DECRYPT=None, PIN=None, Data=None, Description=None, Value=None):
        super(KeyManagementScheme, self).__init__()
        self.DUKPT = None
        self.DUKPT.Operation = None
        self.DUKPT.Operation.DECRYPT = DECRYPT
        self.DUKPT.Mode = None
        self.DUKPT.Mode.PIN = PIN
        self.DUKPT.Mode.Data = Data
        self.DUKPT.DeviceInfo = None
        self.DUKPT.DeviceInfo.Description = Description
        self.DUKPT.EncryptedData = None
        self.DUKPT.EncryptedData.Value = Value
        
        
#TODO Need more information about this element and it's children
class encryptedTrackData(apicontractsv1.encryptedTrackDataType):
    """

    :FormOfPayment:KeyBlock:KeyValue:
        :Encoding: string containing: Base64 or Hex
        :EncryptionAlgorithm: string containing: TDES or AES or RSA
        :Scheme: See KeyManagementScheme object
        :return: None
    """
    def __init__(self, Encoding, EncryptionAlgorithm, DECRYPT=None, PIN=None, Data=None, Description=None, Value=None):
        super(encryptedTrackData, self).__init__()
        Scheme = KeyManagementScheme(DECRYPT, PIN, Data, Description, Value)
        KeyValue = apicontractsv1.KeyValue()
        KeyValue.Encoding = Encoding
        KeyValue.EncryptionAlgorithm = EncryptionAlgorithm
        KeyValue.Scheme = Scheme
        KeyBlock= apicontractsv1.KeyBlock()
        KeyBlock.KeyValue = KeyValue
        self.FormOfPayment = KeyBlock


#TODO Need more information about this element and it's children
class payPal(apicontractsv1.payPalType):
    """

    :successUrl: (max 2048 char)
    :cancelUrl: (max 2048 char)
    :paypalLc: (max 2 char)
    :paypalHdrImg: (max 127 char)
    :paypalPayflowcolor: (max 6 char)
    :payerID: (max 255 char)
    :return: None
    """
    def __init__(self, successUrl=None, cancelUrl=None, paypalLc=None, paypalHdrImg=None,
                 paypalPayflowcolor=None, payerID=None):
        super(payPal, self).__init__()
        if successUrl:
            self.successUrl= successUrl
        if cancelUrl:
            self.cancelUrl= cancelUrl
        if paypalLc:
            self.paypalLc= paypalLc
        if paypalHdrImg:
            self.paypalHdrImg= paypalHdrImg
        if paypalPayflowcolor:
            self.paypalPayflowcolor= paypalPayflowcolor
        if payerID:
            self.payerID= payerID
        

#TODO Need more information about this element and it's children
class opaqueData(apicontractsv1.opaqueDataType):
    """

    :dataDescriptor: (string) REQUIRED
    :dataValue: (string) REQUIRED
    :dataKey: (string) OPTIONAL
    :return: None
    """
    def __init__(self, dataDescriptor, dataValue, dataKey=None):
        super(opaqueData, self).__init__()
        self.dataDescriptor = dataDescriptor
        self.dataValue = dataValue
        if dataKey:
            self.dataKey = dataKey


class payment(apicontractsv1.paymentType):
    """
    This class builds a payment object that contains the data for the payment, ONE OF THE FOLLOWING
    :creditCard: See creditCard object CONDITIONAL
    :bankAccount: See bankAccount object CONDITIONAL
    :trackData: See creditCardTrackData object CONDITIONAL
    :encryptedTrackData: See encryptedTrackData object CONDITIONAL
    :payPal: See payPal object CONDITIONAL
    :opaqueData: See opaqueData object CONDITIONAL
    :return: None
    """
    def __init__(self, cardNumber=None, expirationDate=None, cardCode=None, isPaymentToken=False, cryptogram=None,
                 track1=None, track2=None, routingNumber=None, accountNumber=None, nameOnAccount=None, accountType=None,
                 echeckType=None, bankName=None, checkNumber=None, Encoding=None, EncryptionAlgorithm=None,
                 DECRYPT=None, PIN=None, Data=None, Description=None, Value=None, successUrl=None, cancelUrl=None,
                 paypalLc=None, paypalHdrImg=None, paypalPayflowcolor=None, payerID=None, dataDescriptor=None,
                 dataValue=None, dataKey=None):
        super(payment, self).__init__()
        if cardNumber and expirationDate:
            self.creditCard = creditCard(cardNumber, expirationDate, cardCode, isPaymentToken, cryptogram)
        elif routingNumber and accountNumber and nameOnAccount:
            self.bankAccount = bankAccount(routingNumber, accountNumber, nameOnAccount,
                                           accountType, echeckType, bankName, checkNumber)
        elif track1 or track2:
            self.trackData = creditCardTrackData(track1, track2)
        elif Encoding and EncryptionAlgorithm:
            self.encryptedTrackData = encryptedTrackData(Encoding, EncryptionAlgorithm, DECRYPT, PIN, Data,
                                                         Description, Value)
        elif successUrl or cancelUrl or paypalLc or paypalHdrImg or paypalPayflowcolor or payerID:
            self.payPal = payPal(successUrl, cancelUrl, paypalLc, paypalHdrImg, paypalPayflowcolor, payerID)
        elif dataDescriptor and dataValue:
            self.opaqueData = opaqueData(dataDescriptor, dataValue, dataKey)


class customerProfilePayment(apicontractsv1.customerProfilePaymentType):
    """
    
    :createProfile: (boolean) OPTIONAL
    :customerProfileId: (integer) OPTIONAL
    :paymentProfile: OPTIONAL
        :paymentProfileId: (integer) REQUIRED
        :cardCode: (Integer, 3 to 4 digits) OPTIONAL
    :shippingProfileId: (integer) OPTIONAL
    :return: None
    """
    def __init__(self, createProfile=None, customerProfileId=None, paymentProfileId=None,
                 cardCode=None, shippingProfileId=None):
        super(customerProfilePayment,self).__init__()
        if createProfile:
            self.createProfile = createProfile
        if customerProfileId:
            self.customerProfileId = customerProfileId
        if paymentProfileId:
            self.paymentProfile = apicontractsv1.paymentProfile()
            self.paymentProfile.paymentProfileId = paymentProfileId
            self.paymentProfile.cardCode = cardCode
        if shippingProfileId:
            self.shippingProfileId = shippingProfileId


class solution(apicontractsv1.solutionType):
    """
    This class builds information regarding the software that generated the transaction
    :id: solution id generated by Authorize.net and provided to the solution provider (Up to 50 Characters) OPTIONAL
    :name: (string) OPTIONAL
    :vendorName: (string) OPTIONAL
    :return: None
    """
    def __init__(self, id=None, name=None, vendorName=None):
        super(solution,self).__init__()
        if id:
            self.id = id
        if name:
            self.name = name
        if vendorName:
            self.vendorName = vendorName


class order(apicontractsv1.orderType):
    """
    This class contains order details
    :invoiceNumber: merchant defined invoice number (max 20 characters) OPTIONAL
    :description: merchant defined item description (max 255 characters) OPTIONAL
    :return: None
    """
    def __init__(self, invoiceNumber=None, description=None):
        super(order, self).__init__()
        if invoiceNumber:
            self.invoiceNumber = invoiceNumber
        if description:
            self.description = description


class lineItem(apicontractsv1.lineItemType):
    """
    This object contains one item and the values associated with it
    :itemId: (from 1 to 31 characters)
    :name: (from 1 to 31 characters)
    :description: (up to 255 characters) OPTIONAL
    :quantity: (float with 4 decimal places and gte 0.00)
    :unitPrice: (float with 4 decimal places and gte 0.00)
    :taxable: (boolean) OPTIONAL
    :return: None
    """
    def __init__(self, itemId, quantity, unitPrice, name=None, description=None, taxable=None):
        super(lineItem, self).__init__()
        self.itemId = itemId
        if name:
            self.name = name
        if description:
            self.description = description
        if quantity >=0:
            self.quantity = quantity
        else:
            pass # TODO Error Catching
        if unitPrice >=0:
            self.unitPrice = unitPrice
        else:
            pass # TODO Error Catching
        if taxable != None:
            self.taxable = taxable


class ArrayOfLineItem:
    """
    This class takes all lineItem objects for a transaction as a list and iterates through them to build object
    NOTE::: All line item lists must be the same length
    :lineItem: see object lineItem (cannot be null)
    """
    def __init__(self, itemId_list, quantity_list, unitPrice_list, name_list, description_list, taxable_list):
        if len(itemId_list) == len(quantity_list) == len(unitPrice_list) == len(name_list)\
                == len(description_list) == len(taxable_list):
            self.lineItem = []
            x = 0
            while x < len(itemId_list):
                self.lineItem.append(lineItem(itemId_list[x], quantity_list[x], unitPrice_list[x], name_list[x],
                                              description_list[x], taxable_list[x]))
                x += 1
        else:
            pass # TODO Error Catching


class extendedAmount(apicontractsv1.extendedAmountType):
    """

    :amount: (float with 4 decimal places and gte 0.00)
    :name: (up to 31 characters) OPTIONAL
    :description: (up to 255 characters) OPTIONAL
    """
    def __init__(self, amount, name=None, description=None):
        super(extendedAmount, self).__init__()
        self.amount = amount
        if name:
            self.name = name
        if description:
            self.description = description


class driversLicense(apicontractsv1.driversLicenseType):
    """

    :number: Format of number should be string or four X's followed by the last four digits. (from 5 to 20 characters)
    :state: (2 characters)
    :dateOfBirth: Format of dateOfBirth should be xs:date (1965-01-28) or XX/XX/1965. (8 to 10 characters) OPTIONAL
    """
    def __init__(self, number, state, dateOfBirth):
        super(driversLicense, self).__init__()
        self.number = number
        self.state = state
        self.dateOfBirth = dateOfBirth


class customerData(apicontractsv1.customerDataType):
    """

    :type: value is either individual OR business  OPTIONAL
    :id: (up to 20 characters) OPTIONAL
    :email: (up to 255 characters) OPTIONAL
    :driversLicense: see driversLicense object OPTIONAL
    :taxId: (from 8 to 9 characters) OPTIONAL
    """
    def __init__(self, type=None, id=None, email=None, number=None, state=None, dateOfBirth=None, taxId=None):
        super(customerData, self).__init__()
        if type:
            self.type = type
        if id:
            self.id = id
        if email:
            self.email = email
        if number and state and dateOfBirth:
            self.driversLicense = driversLicense(number, state, dateOfBirth)
        if taxId:
            self.taxId = taxId


class customerAddress(apicontractsv1.customerAddressType):
    """

    :Extends:nameAndAddressType:
        :firstName: (up to 50 characters) OPTIONAL
        :lastName: (up to 50 characters) OPTIONAL
        :company: (up to 50 characters) OPTIONAL
        :address: (up to 60 characters) OPTIONAL
        :city: (up to 40 characters) OPTIONAL
        :state: (up to 40 characters) OPTIONAL
        :zip: (up to 20 characters) OPTIONAL
        :country: (up to 60 characters) OPTIONAL
    :phoneNumber: (up to 25 characters) OPTIONAL
    :faxNumber: (up to 25 characters) OPTIONAL
    :email: (string) OPTIONAL
    """
    def __init__(self, firstName=None, lastName=None, company=None, address=None, city=None, state=None, zip=None,
                 country=None, phoneNumber=None, faxNumber=None, email=None):
        super(customerAddress, self).__init__()
        if firstName:
            self.firstName = firstName
        if lastName:
            self.lastName = lastName
        if company:
            self.company = company
        if address:
            self.address = address
        if city:
            self.city = city
        if state:
            self.state = state
        if zip:
            self.zip = zip
        if country:
            self.country = country
        if phoneNumber:
            self.phoneNumber = phoneNumber
        if faxNumber:
            self.faxNumber = faxNumber
        if email:
            self.email = email


class shipTo(apicontractsv1.nameAndAddressType):
    """

    :firstName: (up to 50 characters) OPTIONAL
    :lastName: (up to 50 characters) OPTIONAL
    :company: (up to 50 characters) OPTIONAL
    :address: (up to 60 characters) OPTIONAL
    :city: (up to 40 characters) OPTIONAL
    :state: (up to 40 characters) OPTIONAL
    :zip: (up to 20 characters) OPTIONAL
    :country: (up to 60 characters) OPTIONAL
    """
    def __init__(self, firstName=None, lastName=None, company=None, address=None, city=None, state=None, zip=None,
                 country=None):
        super(shipTo, self).__init__()
        if firstName:
            self.firstName = firstName
        if lastName:
            self.lastName = lastName
        if company:
            self.company = company
        if address:
            self.address = address
        if city:
            self.city = city
        if state:
            self.state = state
        if zip:
            self.zip = zip
        if country:
            self.country = country


class ccAuthentication(apicontractsv1.ccAuthenticationType):
    """

    :authenticationIndicator: (string)
    :cardholderAuthenticationValue: (string)
    """
    def __init__(self, authenticationIndicator, cardholderAuthenticationValue):
        super(ccAuthentication, self).__init__()
        self.authenticationIndicator = authenticationIndicator
        self.cardholderAuthenticationValue = cardholderAuthenticationValue


class transRetailInfo(apicontractsv1.transRetailInfoType):
    """

    :marketType: (string, default=2) OPTIONAL
    :deviceType: (string) OPTIONAL
    """
    def __init__(self, marketType=None, deviceType=None):
        super(transRetailInfo, self).__init__()
        if marketType:
            self.marketType = marketType
        if deviceType:
            self.deviceType = deviceType


class ArrayOfSetting(apicontractsv1.ArrayOfSetting):
    """

    :setting:settingType:
        :settingName: (string) OPTIONAL
        :settingValue: (string) OPTIONAL
    """
    def __init__(self, settingName=None, settingValue=None):
        super(ArrayOfSetting, self).__init__()
        self.setting = apicontractsv1.settingType()
        if settingName:
            self.setting.settingName = settingName
        if settingValue:
            self.setting.settingValue = settingValue


class userField(apicontractsv1.userField):
    """

    :name: (string) OPTIONAL
    :value: (string) OPTIONAL
    """
    def __init__(self, name=None, value=None):
        super(userField, self).__init__()
        if name:
            self.name = name
        if value:
            self.value = value


# TODO define Types of credit card transactions in transactionType
# TODO define payment information in payment
# TODO define profile
# TODO define CIM Profile in createProfile
# TODO define solution ID in solution
class transactionRequest(apicontractsv1.transactionRequestType):
    """
    This class builds an object containing transaction information.
    :transactionType: Type of credit card transaction (string, default = authCaptureTransaction)
    :amount: Total amount of transaction including tax, shipping, and all other charges (15 digit float, no $) OPTIONAL
    :currencyCode: (string) OPTIONAL
    :payment: See payment object OPTIONAL
    :profile: See customerProfilePayment object OPTIONAL
    :solution: see solution object OPTIONAL
    :callId: (string) OPTIONAL
    :authCode: (string) OPTIONAL
    :refTransId: (string) OPTIONAL
    :splitTenderId: (string) OPTIONAL
    :order: see order object OPTIONAL
    :lineItems: see ArrayOfLineItem Object OPTIONAL
    :tax: see extendedAmount Object OPTIONAL
    :duty: see extendedAmount Object OPTIONAL
    :shipping: see extendedAmount Object OPTIONAL
    :taxExempt: (boolean) OPTIONAL
    :poNumber: (string) OPTIONAL
    :customer: see cutomerData object OPTIONAL
    :billTo: see customerAddress object OPTIONAL
    :shipTo: see nameAndAddress object OPTIONAL
    :customerIP: (string) OPTIONAL
    :cardholderAuthentication: see ccAuthentication object OPTIONAL
    :retail: see transRetailInfo object OPTIONAL
    :employeeId: (string) OPTIONAL
    :transactionSettings: see ArrayOfSetting object OPTIONAL
    :userFields: see userField object (max 20) OPTIONAL
    :return: None
    """
    def __init__(self, transactionType='authCaptureTransaction', amount=None, currencyCode=None, cardNumber=None,
                 expirationDate=None, cardCode=None, isPaymentToken=False, cryptogram=None, track1=None, track2=None,
                 routingNumber=None, accountNumber=None, nameOnAccount=None, accountType=None, echeckType=None,
                 bankName=None, checkNumber=None, Encoding=None, EncryptionAlgorithm=None,DECRYPT=None, PIN=None,
                 Data=None, Description=None, Value=None, successUrl=None, cancelUrl=None,paypalLc=None,
                 paypalHdrImg=None, paypalPayflowcolor=None, payerID=None, dataDescriptor=None, dataValue=None,
                 dataKey=None, createProfile=None, customerProfileId=None, paymentProfileId=None,
                 shippingProfileId=None, solution_id=None, solution_name=None, vendorName=None, callId=None, authCode=None,
                 refTransId=None, splitTenderId=None, invoiceNumber=None, description=None, itemId_list=None,
                 quantity_list=None, unitPrice_list=None, name_list=None, description_list=None, taxable_list=None,
                 tax_amount=None, tax_name=None, tax_description=None, duty_amount=None, duty_name=None,
                 duty_description=None, shipping_amount=None, shipping_name=None, shipping_description=None,
                 taxExempt=None, poNumber=None, type=None, customer_id=None, email=None, number=None, state=None,
                 dateOfBirth=None, taxId=None, customerAddress_firstName=None, customerAddress_lastName=None,
                 customerAddress_company=None, customerAddress_address=None, customerAddress_city=None,
                 customerAddress_state=None, customerAddress_zip=None, customerAddress_country=None,
                 customerAddress_phoneNumber=None, customerAddress_faxNumber=None, customerAddress_email=None,
                 shipTo_firstName=None, shipTo_lastName=None, shipTo_company=None, shipTo_address=None,
                 shipTo_city=None,  shipTo_state=None, shipTo_zip=None, shipTo_country=None, customerIP=None,
                 authenticationIndicator=None, cardholderAuthenticationValue=None, marketType=None, deviceType=None,
                 employeeId=None, settingName=None, settingValue=None, userField_name=None, userField_value=None):
        super(transactionRequest, self).__init__()
        self.transactionType = transactionType

        if amount:
            self.amount = amount

        if currencyCode:
            self.currencyCode = currencyCode

        if (cardNumber and expirationDate) or (routingNumber and accountNumber and nameOnAccount) or (track1 or track2)\
                or (Encoding and EncryptionAlgorithm) or\
                (successUrl or cancelUrl or paypalLc or paypalHdrImg or paypalPayflowcolor or payerID) or\
                (dataDescriptor and dataValue):
            self.payment = payment(cardNumber, expirationDate, cardCode, isPaymentToken, cryptogram, track1, track2,
                                   routingNumber, accountNumber, nameOnAccount, accountType, echeckType, bankName,
                                   checkNumber, Encoding, EncryptionAlgorithm, DECRYPT, PIN, Data, Description, Value,
                                   successUrl, cancelUrl, paypalLc, paypalHdrImg, paypalPayflowcolor, payerID,
                                   dataDescriptor, dataValue, dataKey)

        if createProfile or customerProfileId or paymentProfileId or shippingProfileId:
            self.profile = customerProfilePayment(createProfile, customerProfileId, paymentProfileId,
                                                  cardCode, shippingProfileId)
        if solution_id or solution_name or vendorName:
            self.solution = solution(solution_id, solution_name, vendorName)
        if callId:
            self.callId = callId
        if authCode:
            self.authCode = authCode
        if refTransId:
            self.refTransId = refTransId
        if splitTenderId:
            self.splitTenderId = splitTenderId
        if invoiceNumber or description:
            self.order = order(invoiceNumber, description)
        if itemId_list or quantity_list or unitPrice_list or name_list or description_list or taxable_list:
            self.lineItems = ArrayOfLineItem(itemId_list, quantity_list, unitPrice_list, name_list,
                                             description_list, taxable_list)
        if tax_amount:
            self.tax = extendedAmount(tax_amount, tax_name, tax_description)
        if duty_amount:
            self.duty = extendedAmount(duty_amount, duty_name, duty_description)
        if shipping_amount:
            self.shipping = extendedAmount(shipping_amount, shipping_name, shipping_description)
        if taxExempt != None:
            self.taxExempt = taxExempt
        if poNumber:
            self.poNumber = poNumber
        if customer_id or email or (number and state and dateOfBirth) or taxId:
            self.customer = customerData(customer_id, email, number, state, dateOfBirth, taxId)
        if customerAddress_firstName or customerAddress_lastName or customerAddress_company or customerAddress_address\
                or customerAddress_city or customerAddress_state or customerAddress_zip or customerAddress_country\
                or customerAddress_phoneNumber or customerAddress_faxNumber or customerAddress_email:
            self.billTo = customerAddress(customerAddress_firstName, customerAddress_lastName,
                                          customerAddress_company, customerAddress_address, customerAddress_city,
                                          customerAddress_state, customerAddress_zip, customerAddress_country,
                                          customerAddress_phoneNumber, customerAddress_faxNumber, customerAddress_email)
        if shipTo_firstName or shipTo_lastName or shipTo_company or shipTo_address or shipTo_city or shipTo_state\
                or shipTo_zip or shipTo_country:
            self.shipTo = shipTo(shipTo_firstName, shipTo_lastName, shipTo_company, shipTo_address, shipTo_city,
                                 shipTo_state, shipTo_zip, shipTo_country)
        if customerIP:
            self.customerIP = customerIP
        if authenticationIndicator and cardholderAuthenticationValue:
            self.cardholderAuthentication = ccAuthentication(authenticationIndicator, cardholderAuthenticationValue)
        if marketType or deviceType:
            self.retail = transRetailInfo(marketType, deviceType)
        if employeeId:
            self.employeeId = employeeId
        if settingName or settingValue:
            self.transactionSettings = ArrayOfSetting(settingName, settingValue)
        if userField_name or userField_value:
            self.userFields = userField(userField_name, userField_value)




class CreateTransactionRequest():
    """
    This method is used to process transactions.
    Extends: ANetApiRequest:
        :merchantAuthentication: See merchantAuthentication object
        :refId: OPTIONAL (Max length = 20)
    :transactionRequest:
    :return: None
    """
    def __new__(cls, merchant_name=None, transactionKey=None, sessionToken=None, password=None,
                 partnerLoginIdpartnerLoginId=None, partnerTransactionKey=None, hashValue=None, timestamp=None,
                 sequence=None, fingerprint_currencyCode=None, fingerprint_amount=None, mobileDeviceId=None, refId=None,
                 transactionType='authCaptureTransaction', amount=None, currencyCode=None, cardNumber=None,
                 expirationDate=None, cardCode=None, isPaymentToken=False, cryptogram=None, track1=None, track2=None,
                 routingNumber=None, accountNumber=None, nameOnAccount=None, accountType=None, echeckType=None,
                 bankName=None, checkNumber=None, Encoding=None, EncryptionAlgorithm=None,DECRYPT=None, PIN=None,
                 Data=None, Description=None, Value=None, successUrl=None, cancelUrl=None,paypalLc=None,
                 paypalHdrImg=None, paypalPayflowcolor=None, payerID=None, dataDescriptor=None, dataValue=None,
                 dataKey=None, createProfile=None, customerProfileId=None, paymentProfileId=None,
                 shippingProfileId=None, solution_id=None, solution_name=None, vendorName=None, callId=None, authCode=None,
                 refTransId=None, splitTenderId=None, invoiceNumber=None, description=None, itemId_list=None,
                 quantity_list=None, unitPrice_list=None, name_list=None, description_list=None, taxable_list=None,
                 tax_amount=None, tax_name=None, tax_description=None, duty_amount=None, duty_name=None,
                 duty_description=None, shipping_amount=None, shipping_name=None, shipping_description=None,
                 taxExempt=None, poNumber=None, type=None, customer_id=None, email=None, number=None, state=None,
                 dateOfBirth=None, taxId=None, customerAddress_firstName=None, customerAddress_lastName=None,
                 customerAddress_company=None, customerAddress_address=None, customerAddress_city=None,
                 customerAddress_state=None, customerAddress_zip=None, customerAddress_country=None,
                 customerAddress_phoneNumber=None, customerAddress_faxNumber=None, customerAddress_email=None,
                 shipTo_firstName=None, shipTo_lastName=None, shipTo_company=None, shipTo_address=None,
                 shipTo_city=None,  shipTo_state=None, shipTo_zip=None, shipTo_country=None, customerIP=None,
                 authenticationIndicator=None, cardholderAuthenticationValue=None, marketType=None, deviceType=None,
                 employeeId=None, settingName=None, settingValue=None, userField_name=None, userField_value=None):

        TransactionRequest = apicontractsv1.createTransactionRequest()
        TransactionRequest.merchantAuthentication = merchantAuthentication(merchant_name, transactionKey, sessionToken, password,
                                                             partnerLoginIdpartnerLoginId, partnerTransactionKey,
                                                             hashValue, timestamp, sequence, fingerprint_currencyCode,
                                                             fingerprint_amount, mobileDeviceId)
        if refId:
            TransactionRequest.refId = refId

        TransactionRequest.transactionRequest = transactionRequest(transactionType, amount, currencyCode, cardNumber, expirationDate,
                                                     cardCode, isPaymentToken, cryptogram, track1, track2,
                                                     routingNumber, accountNumber, nameOnAccount, accountType,
                                                     echeckType, bankName, checkNumber, Encoding, EncryptionAlgorithm,
                                                     DECRYPT, PIN, Data, Description, Value, successUrl, cancelUrl,
                                                     paypalLc, paypalHdrImg, paypalPayflowcolor, payerID,
                                                     dataDescriptor, dataValue, dataKey, createProfile,
                                                     customerProfileId, paymentProfileId, shippingProfileId,
                                                     solution_id, solution_name, vendorName, callId, authCode,
                                                     refTransId, splitTenderId, invoiceNumber, description, itemId_list,
                                                     quantity_list, unitPrice_list, name_list, description_list,
                                                     taxable_list, tax_amount, tax_name, tax_description, duty_amount,
                                                     duty_name, duty_description, shipping_amount, shipping_name,
                                                     shipping_description, taxExempt, poNumber, type, customer_id,
                                                     email, number, state, dateOfBirth, taxId,
                                                     customerAddress_firstName, customerAddress_lastName,
                                                     customerAddress_company, customerAddress_address,
                                                     customerAddress_city, customerAddress_state, customerAddress_zip,
                                                     customerAddress_country, customerAddress_phoneNumber,
                                                     customerAddress_faxNumber, customerAddress_email, shipTo_firstName,
                                                     shipTo_lastName, shipTo_company, shipTo_address, shipTo_city,
                                                     shipTo_state, shipTo_zip, shipTo_country, customerIP,
                                                     authenticationIndicator, cardholderAuthenticationValue,
                                                     marketType, deviceType, employeeId, settingName, settingValue,
                                                     userField_name, userField_value)
        return TransactionRequest
