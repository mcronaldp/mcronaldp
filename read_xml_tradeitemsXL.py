# https://www.youtube.com/watch?v=5SlemSWGD1g
# https://www.youtube.com/watch?v=73isvEt3wCU
# https://www.youtube.com/watch?v=R2bhO0kZZnQ
# https://www.youtube.com/watch?v=GFpBYaTJ1uQ
# https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-parsing-xml

# Deze site lezen:
# https://stackoverflow.com/questions/69380594/xml-etree-elementtree-root-findall-not-returning-all
# Deze van datacamp is uitgebreid:
# https://www.datacamp.com/tutorial/python-xml-elementtree
# en deze:
# https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2
# encoding: https://bobbyhadz.com/blog/python-unicodeencodeerror-charmap-codec-cant-encode-characters-in-position
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
import xml.etree.ElementTree as ET
output = open("TradeItemsXL.csv", "w", encoding='utf-8')
output.write('TradeItemID,pcrt_ProcurementGroup,ref_ProductItemToBrand,ref_SupplierCode,ref_productManufacturerCode'
             ',att_StatusCode,att_TradingInfoMandatorySalesQuantity,att_BasicUnit,att_ERPdescription1'
             ',att_TradingInfoDeliveryTime,att_Serie,att_Type,att_TradingInfoUsageUnitsPerOrderQ,att_TradingInfoMinOrderQuantityNumber,'
             'att_TradeItemCode,att_SupplierTradeItemCode,att_TradingInfoOrderStepsNumber,att_ManufacturerPartNumber,att_TradingInfoPackagingUnitCode'
             ',att_Company,att_TypeCode,att_Description,att_ManufacturerGTIN,att_DescriptionLong,att_supplierGLN,att_ParentClassID'
             ',att_CalculatedManufacturerGLN,att_ParentClassNameID,att_Assortmentcode\n') # , ref_productManufacturerCode, att_StatusCode, att_ERPdescription1
file = 'TradeItem_2023-03-23_19.12.17.708.xml'
# encoded_utf = file.encode('utf-8')
# tree = ET.parse(encoded_utf)
tree = ET.parse(file)
root = tree.getroot()
for child in root: # ALle items onder root: Classifications, Entities, Products
    if child.tag == 'Products':
        for products in child: # Alle items onder Products: Product
            pcrt_ProcurementGroup = 'LEEG'
            ref_ProductItemToBrand = 'LEEG'
            ref_SupplierCode = 'LEEG'
            ref_productManufacturerCode = 'LEEG'
            att_StatusCode = 'LEEG'
            att_TradingInfoMandatorySalesQuantity = 'LEEG'
            att_BasicUnit = 'LEEG'
            att_ERPdescription1 = 'LEEG'
            att_TradingInfoDeliveryTime = 'LEEG'
            att_Serie = 'LEEG'
            att_Type = 'LEEG'
            att_TradingInfoUsageUnitsPerOrder = 'LEEG'
            att_TradingInfoMinOrderQuantityNumber = 'LEEG'
            att_TradeItemCode = 'LEEG'
            att_SupplierTradeItemCode = 'LEEG'
            att_TradingInfoOrderStepsNumber = 'LEEG'
            att_ManufacturerPartNumber = 'LEEG'
            att_TradingInfoPackagingUnitCode = 'LEEG'
            att_Company = 'LEEG'
            att_TypeCode = 'LEEG'
            att_Description = 'LEEG'
            att_ManufacturerGTIN = 'LEEG'
            att_DescriptionLong = 'LEEG'
            att_supplierGLN = 'LEEG'
            att_ParentClassID = 'LEEG'
            att_CalculatedManufacturerGLN = 'LEEG'
            att_ParentClassNameID = 'LEEG'
            att_Assortmentcode = 'LEEG'

            TradeItem_ID = products.attrib['ID']
            print(TradeItem_ID)
            for product in products: # Alle items onder Product
                if product.tag == 'ClassificationReference':
                    pcrt_ProcurementGroup = product.attrib['ClassificationID']
                    print(pcrt_ProcurementGroup)
                if product.tag == 'EntityCrossReference' and product.attrib['Type'] == 'ref_ProductItemToBrand':
                    ref_ProductItemToBrand = product.attrib['EntityID']
                    print(ref_ProductItemToBrand)
                if product.tag == 'EntityCrossReference' and product.attrib['Type'] == 'ref_SupplierCode':
                    ref_SupplierCode = product.attrib['EntityID']
                    print(ref_SupplierCode)
                if product.tag == 'EntityCrossReference' and product.attrib['Type'] == 'ref_productManufacturerCode':
                    ref_productManufacturerCode = product.attrib['EntityID']
                    print(ref_productManufacturerCode)# zie item: 188703
                if product.tag == 'Values':
                    for values in product:
                        if values.attrib['AttributeID'] == 'att_StatusCode':
                            att_StatusCode = values.text
                            print(att_StatusCode)
                        if values.attrib['AttributeID'] == 'att_TradingInfoMandatorySalesQuantity':
                            att_TradingInfoMandatorySalesQuantity = values.text
                            print(att_TradingInfoMandatorySalesQuantity)
                        if values.attrib['AttributeID'] == 'att_BasicUnit':
                            att_BasicUnit = values.text
                            print(att_BasicUnit)
                        if values.attrib['AttributeID'] == 'att_ERPdescription1':
                            att_ERPdescription1 = values.text
                            print(att_ERPdescription1)
                        if values.attrib['AttributeID'] == 'att_SupplyChainIndicator':
                            att_SupplyChainIndicator = values.text
                            print(att_SupplyChainIndicator)
                        if values.attrib['AttributeID'] == 'att_TradingInfoDeliveryTime':
                            att_TradingInfoDeliveryTime = values.text
                            print(att_TradingInfoDeliveryTime)
                        if values.attrib['AttributeID'] == 'att_Serie':
                            att_Serie = values.text
                            print(att_Serie)
                        if values.attrib['AttributeID'] == 'att_Type':
                            att_Type = values.text
                            print(att_Type)
                        if values.attrib['AttributeID'] == 'att_TradingInfoUsageUnitsPerOrderQ':
                            att_TradingInfoUsageUnitsPerOrderQ = values.text
                            print(att_TradingInfoUsageUnitsPerOrderQ)
                        if values.attrib['AttributeID'] == 'att_TradingInfoMinOrderQuantityNumber':
                            att_TradingInfoMinOrderQuantityNumber = values.text
                            print(att_TradingInfoMinOrderQuantityNumber)
                        if values.attrib['AttributeID'] == 'att_TradeItemCode':
                            att_TradeItemCode = values.text
                            print(att_TradeItemCode)
                        if values.attrib['AttributeID'] == 'att_SupplierTradeItemCode':
                            att_SupplierTradeItemCode = values.text
                            print(att_SupplierTradeItemCode)
                        if values.attrib['AttributeID'] == 'att_TradingInfoOrderStepsNumber':
                            att_TradingInfoOrderStepsNumber = values.text
                            print(att_TradingInfoOrderStepsNumber)
                        if values.attrib['AttributeID'] == 'att_ManufacturerPartNumber':
                            att_ManufacturerPartNumber = values.text
                            print(att_ManufacturerPartNumber)
                        if values.attrib['AttributeID'] == 'att_TradingInfoPackagingUnitCode':
                            att_TradingInfoPackagingUnitCode = values.text
                            print(att_TradingInfoPackagingUnitCode)
                        if values.attrib['AttributeID'] == 'att_Company':
                            att_Company = values.text
                            print(att_Company)
                        if values.attrib['AttributeID'] == 'att_TypeCode':
                            att_TypeCode = values.text
                            print(att_TypeCode)
                        if values.attrib['AttributeID'] == 'att_Description':
                            att_Description = values.text
                            print(att_Description)
                        if values.attrib['AttributeID'] == 'att_ManufacturerGTIN':
                            att_ManufacturerGTIN = values.text
                            print(att_ManufacturerGTIN)
                        if values.attrib['AttributeID'] == 'att_DescriptionLong':
                            att_DescriptionLong = values.text
                            print(att_DescriptionLong)
                        if values.attrib['AttributeID'] == 'att_supplierGLN':
                            att_supplierGLN = values.text
                            print(att_supplierGLN)
                        if values.attrib['AttributeID'] == 'att_ParentClassID':
                            att_ParentClassID = values.text
                            print(att_ParentClassID)
                        if values.attrib['AttributeID'] == 'att_CalculatedManufacturerGLN':
                            att_CalculatedManufacturerGLN = values.text
                            print(att_CalculatedManufacturerGLN)
                        if values.attrib['AttributeID'] == 'att_ParentClassNameID':
                            att_ParentClassNameID = values.text
                            print(att_ParentClassNameID)
                    for multivalue in product:
                        if multivalue.tag == 'MultiValue':
                            for values in multivalue:
                                att_Assortmentcode = values.text
                                print(att_Assortmentcode)
            output.write(f'{TradeItem_ID},{pcrt_ProcurementGroup},{ref_ProductItemToBrand},{ref_SupplierCode}'
                         f',{ref_productManufacturerCode},{att_StatusCode},{att_TradingInfoMandatorySalesQuantity},{att_BasicUnit},{att_ERPdescription1}'
                         f'{att_SupplyChainIndicator},{att_TradingInfoDeliveryTime},{att_Serie},{att_Type},{att_TradingInfoUsageUnitsPerOrderQ},{att_TradingInfoMinOrderQuantityNumber}'
                         f',{att_TradeItemCode},{att_SupplierTradeItemCode},{att_TradingInfoOrderStepsNumber},{att_ManufacturerPartNumber},{att_TradingInfoPackagingUnitCode}'
                         f',{att_Company},{att_TypeCode},{att_Description},{att_ManufacturerGTIN},{att_DescriptionLong},{att_supplierGLN},{att_ParentClassID}'
                         f',{att_CalculatedManufacturerGLN},{att_ParentClassNameID},{att_Assortmentcode}\n')