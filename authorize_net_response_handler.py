def createTransactionResponse_parser(response):

    response_dict={}
    response_dict['refId'] = response.refId
    response_dict['resultCode'] = response.messages.resultCode
    response_dict['resultMessageCode'] = []
    for message in response.messages.message:
        response_dict['resultMessageCode'].append((message.code, message.text))
    response_dict['responseCode'] = response.transactionResponse.responseCode
    response_dict['authCode'] = response.transactionResponse.authCode
    response_dict['avsResultCode'] = response.transactionResponse.avsResultCode
    response_dict['cvvResultCode'] = response.transactionResponse.cvvResultCode
    response_dict['cavvResultCode'] = response.transactionResponse.cavvResultCode
    response_dict['transId'] = response.transactionResponse.transId
    response_dict['retransId'] = response.transactionResponse.refTransID
    response_dict['transHash'] = response.transactionResponse.transHash
    response_dict['testRequest'] = response.transactionResponse.testRequest
    response_dict['accountNumber'] = response.transactionResponse.accountNumber
    response_dict['accountType'] = response.transactionResponse.accountType
    response_dict['responseMessageCode'] = []
    try:
        for message in response.transactionResponse.messages.message:
            response_dict['responseMessageCode'].append((message.code, message.text))
    except AttributeError:
        pass
    response_dict['responseErrorCode'] = []
    try:
        for error in response.transactionResponse.errors.error:
            response_dict['responseErrorCode'].append((error.errorCode, error.errorText))
    except AttributeError:
        pass

    return response_dict
