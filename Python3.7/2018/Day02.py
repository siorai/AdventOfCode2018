def findChecksum(data: list) -> int:
    countTwo = 0
    countThree = 0
    for eachID in data:
        checksumDict = {}
        for eachLetter in eachID:
            if eachLetter not in checksumDict.keys():
                checksumDict[eachLetter] = 1
            elif eachLetter in checksumDict.keys():
                checksumDict[eachLetter] += 1
        addTwoCount = False
        addThreeCount = False
        for eachKey in checksumDict.keys():
            if checksumDict[eachKey] == 2:
                addTwoCount = True
            elif checksumDict[eachKey] == 3:
                addThreeCount = True
        if addTwoCount is True:
            countTwo += 1
        if addThreeCount is True:
            countThree +=1
    return countTwo * countThree


def findNearestIDs(data: list) -> str:
    for eachIDIter, eachID in enumerate(data):
        for eachOtherID in data:
            if eachID == eachOtherID:
                continue
            offCount = 0
            offLetter = []
            for eachLetterPlace, eachLetter in enumerate(eachID):
                if eachID[eachLetterPlace] != eachOtherID[eachLetterPlace]:
                    offCount += 1
                    offLetter.append(eachLetter)
            if offCount >= 2:
                continue
            commonLetters = ''
            for eachLetter in eachID:
                if eachLetter != offLetter[0]:
                    commonLetters += eachLetter
            return commonLetters

sampleArray = [
"xrysntkqrduheficajodiglvzw",
"xzymntkqrbuhefmcajodiflvzw",
"xpysetkyrbuhefmcajodiglvgw",
"xtysnykqrbuhefmczjodiglvzw",
"xpysntkqyvuhefmjajodiglvzw",
"xpysntkqrbuqjfmcajodiglvzu",
"xpysntkqrbuhefmvaoodimlvzw",
"xplsntkqrbuhefmcajohimlvzw",
"cpysntkqrbuhefmcajodiglpmw",
"xpysndkqrbuhefmcajzdiglmzw",
"xpysntkqrbuhsfmctjoqiglvzw",
"xpysztkkrbuhewmcajodiglvzw",
"xpysntkguzuhefmcajodiglvzw",
"xpysnbkvrbuhyfmcajodiglvzw",
"xpgsntkqrbphefmcajodzglvzw",
"xpysntkqrbdhefmcajodvgqvzw",
"xpmsntkqrbuhedmcajodiglvnw",
"wpysntkqmbuheemcajodiglvzw",
"xpysntdvrbuhdfmcajodiglvzw",
"xpbsetkqrbuhefmcayodiglvzw",
"xpasntkqrbuhefmcajydigovzw",
"xpylntkqrbuhefmcajudiglnzw",
"xpysqtkqrbuoefmcrjodiglvzw",
"xlysntkqrbuhefmuejodiglvzw",
"xpysntkqrzuhewmcajodaglvzw",
"xpysotkqrbuhefmxajowiglvzw",
"xpysntkqrbuhefmcajodinlyza",
"xpysntkqrbuhemmmajofiglvzw",
"xpysntkqcbuhezmcyjodiglvzw",
"xpysntyqrbuhefmcajodiglvfn",
"xpysntkqrbudefmcarodcglvzw",
"xpysntkqrjuhefkcajodiglvzg",
"xpysntkqrbuhefmcahooiglvow",
"xpysntkqrqfhevmcajodiglvzw",
"xpysntlqrbuhefmcajodivlvzu",
"xpyjotkqrbuhefmcavodiglvzw",
"xpysntqqrbuhebmcgjodiglvzw",
"xpjsnikqbbuhefmcajodiglvzw",
"xpysntkqrbuhefmcalodeflvzw",
"xpysntktrbuhefmcaqoviglvzw",
"xpysntkqrbuhefmcrjogiglvzk",
"xpysntkqrjuhekmcajodixlvzw",
"xpypntyqrbuhefmcajodigzvzw",
"cpysnwkqrbuhefmcajodiglvww",
"xpysntkqqbuqefmcajodiglvlw",
"xpysntkqrbuhvfmcajldiglvzh",
"xpysntkqrbuhefmzmjodislvzw",
"xpysnnkqrbuhefmcajodjplyzw",
"xpysntdqobuhefmcajbdiglvzw",
"xpyzntknrbuhefmcajodigtvzw",
"xpysntkqbbohefmcajodialvzw",
"xpysntkqryuhefmcayoxiglvzw",
"xxysntkqrbuhefmcajodiglgzl",
"jzysntkqrbuhmfmcajodiglvzw",
"xpysntocrbuhefmcakodiglvzw",
"xpysntkqrbuheomrgjodiglvzw",
"xpysntkerbuhefmxajoduglvzw",
"xpysntkqobuhefpcajodiglvzd",
"xpysntkqrbvhefmcajopislvzw",
"xpysntkqrbuhefucqjodiglvqw",
"xpysvtkqrbuhdfmcajokiglvzw",
"xqysnjkqrbuhemmcajodiglvzw",
"xpysnteqxbuhefmcajodiglvdw",
"xpysntkqrbuhefzcajodignvzc",
"xpysntkqrbuledmcajoyiglvzw",
"xpysntkqrbuhofmcajkdigpvzw",
"xpysmtkqrbuhefmcajodaglvze",
"xlysntiqrbuhefmqajodiglvzw",
"xpysntvqrbugefmcajodiglizw",
"xpysntkqrbuhefmuwjndiglvzw",
"ypysntkqrbuhefmbajodislvzw",
"xpycntkqrbuhemmcaqodiglvzw",
"xpysntkqrbuhefmcajobivdvzw",
"xpysnfkprbuhefmcajodiglvkw",
"xtysntkwrjuhefmcajodiglvzw",
"xpysntkqrbqhefmcaxodiulvzw",
"xpysntkqrbuhefmcajsdigkvkw",
"xpysnekqrbugefmcajwdiglvzw",
"xpysntkqjbuhefmcajoduglbzw",
"xpysntkqrbohlfmcajodiggvzw",
"xpysntkqrbfhefmcajodiglhnw",
"xpmsntkirbusefmcajodiglvzw",
"xpnsntkqrbehefmcajodigrvzw",
"xpytntgqrbuhefmcajodigllzw",
"xpysntkqrbuhefmcejodiglvvm",
"xpyvntkqrbuhefmmajodiglmzw",
"rpysntkirbuhefmcajodiglyzw",
"xpysntkqrbuhefmcajoznglvzz",
"xpysntkqrbmhefmcafodigwvzw",
"xpysntkqrbuhetmcarodiglvzx",
"xpysntnqrbuhefmcajogiglfzw",
"xpysutkqjbuheomcajodiglvzw",
"xpysnqkprbuhefkcajodiglvzw",
"xpysntuqrbuhemmcajodyglvzw",
"spysntkqrbupefmcajodigpvzw",
"qpygntkqrbuhefmcajodqglvzw",
"xpysnteqrbuhefmcatodiylvzw",
"xpysntkqrbusefsckjodiglvzw",
"xpysntkqrbubeflcajodiglvcw",
"xpysntwqrbuhefmcajodigekzw",
"xpysntkqrbuhefmcnjodiguvtw",
"xpysntkqrbqhefmkasodiglvzw",
"xmysntkqrbuhefmkcjodiglvzw",
"xpysntkqrquhefmcajodiouvzw",
"xpysnnkqrbuhefmcajodiplyzw",
"xpysntkorbuhefaqajodiglvzw",
"npysntkqobuhefmcajodiglvfw",
"xlysntkqrbuhefmcazbdiglvzw",
"xpysftkqrbihefmcajodiglezw",
"xpysolqqrbuhefmcajodiglvzw",
"xpysntkqrwuheixcajodiglvzw",
"xoysntkqibuhefmcqjodiglvzw",
"xpysntkqrbupefmcajodtulvzw",
"xpyentkqrbuhvfmcajudiglvzw",
"xpysntksrbuhefmgajodqglvzw",
"xpysntkqrbuhcfmcvjodigldzw",
"gpyrntdqrbuhefmcajodiglvzw",
"vpysntvqrbuhefmcajndiglvzw",
"xpvsntkqrbuhefvcajhdiglvzw",
"xpysntkqrbubefmcajowiglvzl",
"xpysndkqibuhefmcajodiblvzw",
"xpysntkqrbuhefmldjodjglvzw",
"xpysntzqrbuhefmcyjomiglvzw",
"xpysntkqrbuhefmedjodiwlvzw",
"xpysntklrbuhefmcyjodiglvjw",
"xpypnlkqrbehefmcajodiglvzw",
"xpysntkqrbuhefycacodiglvzz",
"ypysntkqrbuhefmcajadiglvew",
"xpysntkqobuhefmcajadiglhzw",
"xpysbtxlrbuhefmcajodiglvzw",
"xpysntkqrbuhefdcajoviglvww",
"xpysntkqrbuhefmcaaodiblvzc",
"wpysntkqrbuhefmcajddiglvbw",
"wpysntmqrbuhefmcajodiglvza",
"epysntkqrbuhemmcajoniglvzw",
"vpysntkqrbuhejmcajodiglvzo",
"xpysntkqrbuhebmmajodiglazw",
"lpysntkqrguhtfmcajodiglvzw",
"xpksndkqpbuhefmcajodiglvzw",
"xpydnukqrbuhefmcajmdiglvzw",
"xpysnmkqrbuhefioajodiglvzw",
"xpysntkqruuhefmcajodyglvzx",
"xpysntkqrmuhefmcmjidiglvzw",
"xpysntksrbupefmcajodiplvzw",
"xpykntkqrbuhefmmajodiglxzw",
"xpssntkqrbuhefmzajodiglvgw",
"xpysntkqrbuhefmcrjodigovzd",
"xpysntkqrbuhefmpajodirlvqw",
"xpysnskqrruhefmtajodiglvzw",
"xpysnzkqrbuhezmcajodiglvzj",
"xpysntkcrburefmckjodiglvzw",
"xpysntkqrbuhefecpoodiglvzw",
"xpysnjkqrbuhexmcajodigrvzw",
"xpysztkqhbuhefmcanodiglvzw",
"xpysntkqrbuhefmcajozyelvzw",
"xpyuntkmrbuhefmcajodigcvzw",
"xpysnykmrbuhefmaajodiglvzw",
"jpysntkqrbuhefmcajodigumzw",
"xtysntkqhbuhefmcajodiglvzz",
"xpysntkqrbqhefmcxjouiglvzw",
"xpysntkqreujefmmajodiglvzw",
"xnysntzqrbuhefacajodiglvzw",
"xpysntkqriuhefmcajkdiqlvzw",
"xposntkqrbuheffcajodihlvzw",
"xpysntkqpquhefmcajodrglvzw",
"xpysjtkqrbudefmcajouiglvzw",
"xpysnxkqrbulefmcacodiglvzw",
"xpygntkqrbuhefmfajzdiglvzw",
"xpysntkqrbuhefmuayodiglyzw",
"xpysnbksrbuhefmcajediglvzw",
"xkyzntkqrbuhefmcajodiglvzz",
"xpysntkqrbehlxmcajodiglvzw",
"xpysntkqryuhefmcaxodiklvzw",
"xpysntdqrbuhefmcjjodiglvzt",
"xpysntkqrbuhefmcauodigqvzy",
"xpysftkqrbuhefmcajodrgvvzw",
"xpysntkqrbuhefmczjodiglivw",
"xpysatkorbuhefmcyjodiglvzw",
"xhysntkqrbthefmcajodxglvzw",
"xpysnpkqrbuhefmcajoqyglvzw",
"xpyyntkqrbuhefmcjjodxglvzw",
"xpysntkqrozhefhcajodiglvzw",
"xpymftkqrbuhefmcajodiglvzo",
"xpysntkqrbuhvfmcajodiyllzw",
"xpysatsqrbuhefmcajodiglvzo",
"cpysntkqqbuhefmcajodlglvzw",
"xpysntkyrblhefmcajodiglvzz",
"xpysntkfrbuhefbcajodiglbzw",
"upysotkqrbuhpfmcajodiglvzw",
"xpysdokqrbuheflcajodiglvzw",
"xrysntkqrbuhefpcanodiglvzw",
"xdysntkqrbuhefpcajodiglmzw",
"xpyynteqrbjhefmcajodiglvzw",
"xpysntkqrbuhefkcajodielvhw",
"xplsktkqrbuhefmcajodtglvzw",
"xpysrtkqrbuhefmcdjodiglvzx",
"upysntkmrbuhefmcajodiglvzt",
"xnysnpkqrbusefmcajodiglvzw",
"xtysntnqrbuhexmcajodiglvzw",
"xpysngkmrbfhefmcajodiglvzw",
"xpysnhkhrbuhefmcajodiplvzw",
"xpysntvqrbuhefmcaoodsglvzw",
"xpyzntkqrbuhefmcajlviglvzw",
"xpysndkqrbuievmcajodiglvzw",
"xpysntkqrsuhcfzcajodiglvzw",
"xpysntkqlbuhefmcajjdlglvzw",
"xpysntkqrbuhifmcajoliylvzw",
"xpysntkqxbphefmcajodialvzw",
"bnyswtkqrbuhefmcajodiglvzw",
"upysatkqrbuhefmcajodvglvzw",
"xpysntkqqbuhefmcajodxglzzw",
"xpysntkqryuhefmcafodinlvzw",
"xpzsntkqrcuhefmcajokiglvzw",
"xpynntkqrbuheimccjodiglvzw",
"xpysnfkqduuhefmcajodiglvzw",
"xpywntkqrbuhefmcajodigllzz",
"xpysftkqrbahefmcajsdiglvzw",
"xpysntkkrbutefmcljodiglvzw",
"xfysntkqrbbhkfmcajodiglvzw",
"xpysgtksrbuhefkcajodiglvzw",
"xpysntyqrbuhefmcajodijlvzg",
"xpysnpkqobuhefmcljodiglvzw",
"xvysntkqrbuhefmcsjodiclvzw",
"xpysntkqrtuhwfmcajodillvzw",
"xpysntkprbuhejmcajouiglvzw",
"apysntkqrbuhefmcaboviglvzw",
"xpysqykqrbuhefmcajodirlvzw",
"xpysntkqrluhefmcajowiglvzf",
"dpysnokqrbuhefmcajoaiglvzw",
"xppsntkqmbuheumcajodiglvzw",
"xpysntkqrbuhlymcaoodiglvzw",
"dpysntkqrbuhmfmcajodiglvzt",
"xpysltbqrbuhefmcajoliglvzw",
"xpysntpqrbuhefmcnjoniglvzw",
"xpysntpqrbuhektcajodiglvzw",
"xpysntkhrbshefmqajodiglvzw",
"zpysntuqrbuhefmcajmdiglvzw",
"xpysxtdqrbuhefmcajoyiglvzw",
"xpysntkubbumefmcajodiglvzw",
"xpysntkqzouhefmcajsdiglvzw",
"xpysntkqrbuhefmcojoziglvyw",
"jpysntkqrmuhefmcajodidlvzw",
"xpmsttkqrhuhefmcajodiglvzw",
"xpysntkqlbuhefmcajgdiflvzw",
"xpysntxkrbuhefmcauodiglvzw",
"xpysotkqubuhefscajodiglvzw",
"xjysntkqrbvheemcajodiglvzw",
"xpykntkqrbuhefmcpjodiglvow",
"xplsntkqrbuvefmcajediglvzw",
"upysntwqrbuhefmfajodiglvzw"]
