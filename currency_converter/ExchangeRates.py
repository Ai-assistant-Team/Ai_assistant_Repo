"""
Created on Sat May 8 
@author: Δημήτρης Σούμπασης
"""

from forex_python.converter import CurrencyRates

c = CurrencyRates()
#c1 = the key the user gives for the currency you are converting from 
#c2= the key theuser givesfor the currency you are converting to
#c3= Full name of the currency that the user wants to conver to 
#amount= the amount you are converting
currencyMatches = {
    'Albania Lek'				:		'ALL',
    'Afghanistan Afghani'		:			'AFN',
    'Argentina Peso'			:			'ARS',
    'Aruba Guilder'				:		'AWG',
    'Australia Dollar'			:		'AUD',
    'Azerbaijan Manat'			:		'AZN',
    'Bahamas Dollar'			:			'BSD',
    'Barbados Dollar'		:				'BBD',
    'Belarus Ruble'			:			'BYN',
    'Belize Dollar'			:			'BZD',
    'Bermuda Dollar'		:				'BMD',
    'Bolivia Bolíviano'		:			'BOB',
    'Bosnia and Herzegovina Convertible Mark'	:	'BAM',
    'Botswana Pula'				:		'BWP',
    'Bulgaria Lev'				:		'BGN',
    'Brazil Real'					:	'BRL',
    'Brunei Darussalam Dollar'		:		'BND',
    'Cambodia Riel'				:		'KHR',
    'Canada Dollar'				:		'CAD',
    'Cayman Islands Dollar'		:			'KYD',
    'Chile Peso'				:		'CLP',
    'China Yuan Renminbi'		:			'CNY',
    'Colombia Peso'				:	'COP',
    'Costa Rica Colon'			:		'CRC',
    'Croatia Kuna'				:		'HRK',
    'Cuba Peso'					:	'CUP',
    'Czech Republic Koruna'		:			'CZK',
    'Denmark Krone'				:		'DKK',
    'Dominican Republic Peso'		:			'DOP',
    'East Caribbean Dollar'			:		'XCD',
    'Egypt Pound'					:	'EGP',
    'El Salvador Colon'				:	'SVC',
    'Euro Member Countries'			:		'EUR',
    'Falkland Islands (Malvinas) Pound'		:	'FKP',
    'Fiji Dollar'				:		'FJD',
    'Ghana Cedi'				:		'GHS',
    'Gibraltar Pound'			:			'GIP',
    'Guatemala Quetzal'			:		'GTQ',
    'Guernsey Pound'			:			'GGP',
    'Guyana Dollar'				:		'GYD',
    'Honduras Lempira'			:		'HNL',
    'Hong Kong Dollar'			:		'HKD',
    'Hungary Forint'			:			'HUF',
    'Iceland Krona'				:		'ISK',
    'India Rupee'			:			'INR',
    'Indonesia Rupiah'		:			'IDR',
    'Iran Rial'				:		'IRR',
    'Isle of Man Pound'			:		'IMP',
    'Israel Shekel'			:			'ILS',
    'Jamaica Dollar'		:				'JMD',
    'Japan Yen'				:		'JPY',
    'Jersey Pound'				:		'JEP',
    'Kazakhstan Tenge'		:			'KZT',
    'Korea (North) Won'			:		'KPW',
    'Korea (South) Won'			:		'KRW',
    'Kyrgyzstan Som'			:			'KGS',
    'Laos Kip'					:	'LAK',
    'Lebanon Pound'				:		'LBP',
    'Liberia Dollar'			:			'LRD',
    'Macedonia Denar'			:			'MKD',
    'Malaysia Ringgit'			:		'MYR',
    'Mauritius Rupee'			:			'MUR',
    'Mexico Peso'				:		'MXN',
    'Mongolia Tughrik'			:		'MNT',
    'Mozambique Metical'		:			'MZN',
    'Namibia Dollar'			:			'NAD',
    'Nepal Rupee	'			:		'NPR',
    'Netherlands Antilles Guilder'		:		'ANG',
    'New Zealand Dollar'			:		'NZD',
    'Nicaragua Cordoba'			:		'NIO',
    'Nigeria Naira'				:		'NGN',
    'Norway Krone'				:		'NOK',
    'Oman Rial'				:		'OMR',
    'Pakistan Rupee'		:				'PKR',
    'Panama Balboa'			:			'PAB',
    'Paraguay Guarani'		:			'PYG',
    'Peru Sol'				:		'PEN',
    'Philippines Peso'		:			'PHP',
    'Poland Zloty'			:			'PLN',
    'Qatar Riyal'			:			'QAR',
    'Romania Leu'			:			'RON',
    'Russia Ruble'			:			'RUB',
    'Saint Helena Pound'		:			'SHP',
    'Saudi Arabia Riyal'		:			'SAR',
    'Serbia Dinar'				:		'RSD',
    'Seychelles Rupee'			:		'SCR',
    'Singapore Dollar'		:			'SGD',
    'Solomon Islands Dollar'	:				'SBD',
    'Somalia Shilling'			:		'SOS',
    'South Africa Rand'		:			'ZAR',
    'Sri Lanka Rupee'		:			'LKR',
    'Sweden Krona'			:			'SEK',
    'Switzerland Franc'		:			'CHF',
    'Suriname Dollar'		:				'SRD',
    'Syria Pound	'		:			'SYP',
    'Taiwan New Dollar'		:			'TWD',
    'Thailand Baht'			:			'THB',
    'Trinidad and Tobago Dollar'	:			'TTD',
    'Turkey Lira'			:			'TRY',
    'Tuvalu Dollar'			:			'TVD',
    'Ukraine Hryvnia'		:				'UAH',
    'United Kingdom Pound'	:				'GBP',
    'United States Dollar'	:				'USD',
    'Uruguay Peso'		:				'UYU',
    'Uzbekistan Som'	:					'UZS',
    'Venezuela Bolívar'	:				'VEF',
    'Viet Nam Dong'		:				'VND',
    'Yemen Rial'	:					'YER',
    'Zimbabwe Dollar'	:					'ZWD'
}


def cconvert(c1, c2, amount):       #Converts the amount from currency 1 to currency 2
    try:
        
        c3=f2                       # c3 
        c1=currencyMatches['c1']
        c2=currencyMatches['c2']
        fin=(c.convert(c1, c2, amount))
        
        fin= str(fin) + ' ' + c3
        
        
        return fin
    except:
        return 1
