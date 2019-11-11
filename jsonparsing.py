# -*- coding: utf-8 -*-
# python version 3
import json
import sys
import io

def parse(aaa):
    # {"api":"POST /n2mt/translate","n2mt":true,"params":{"caller":"PID.line_transbot","source":"ja","target":"ko","text":"","dict":false,"dictDisplay":3,"honorific":false,"instant":false,"service":"DEFAULT","agree":false},"result":{"json":{"message":{"@type":"response","@service":"naverservice.nmt.proxy","@version":"1.0.0","result":{"srcLangType":"ja","tarLangType":"ko","translatedText":""}}},"elapsed":70,"textLen":7},"langDetect":"ja","modelVer":"n2mt_decoder_centos7_jako_20191014_1457_tensorflow"}'
    temp_a = aaa.split(" (OK) ")
    if len(temp_a) == 1:
        return "aaaaa"

    a = aaa.split(" (OK) ")[1]
    b = json.loads(a)  # b["api"] # POST /n2mt/translate
    if not b:
        return "aaaaa"
    if "langDetect" not in b:
        return "aaaaa"
    lang_detect = b["langDetect"]
    if "message" not in b["result"]["json"]:
        return "aaaaa"
    if "result" not in b["result"]["json"]["message"]:
        return "aaaaa"
    result_values = b["result"]["json"]["message"]["result"]
    params = b["params"]
    src_lang = params["source"]
    tar_lang = params["target"]
    src_text = params["text"]
    translated_text = result_values["translatedText"]
    src_text = " ".join(src_text.strip().split())
    return src_lang, tar_lang, lang_detect, src_text.strip(), translated_text


file_name = sys.argv[1]

f = io.open(file_name, "r", encoding="utf-8")
detail_file = open("detail.txt", "a")

enko_file = open("enko_result.txt", "a")
koen_file = open("koen_result.txt", "a")

jako_file = open("jako_result.txt", "a")
koja_file = open("koja_result.txt", "a")

enja_file = open("enja_result.txt", "a")
jaen_file = open("jaen_result.txt", "a")

deko_file = open("deko_result.txt", "a")
kode_file = open("kode_result.txt", "a")

kozh_file = open("kozh_result.txt", "a")
zhko_file = open("zhko_result.txt", "a")

enzh_file = open("enzh_result.txt", "a")
zhen_file = open("zhen_result.txt", "a")

esko_file = open("esko_result.txt", "a")
koes_file = open("koes_result.txt", "a")

koth_file = open("koth_result.txt", "a")
thko_file = open("thko_result.txt", "a")

koru_file = open("koru_result.txt", "a")
ruko_file = open("ruko_result.txt", "a")

idko_file = open("idko_result.txt", "a")
koid_file = open("koid_result.txt", "a")

itko_file = open("itko_result.txt", "a")
koit_file = open("koti_result.txt", "a")

enfr_file = open("enfr_result.txt", "a")
fren_file = open("fren_result.txt", "a")

kovi_file = open("kovi_result.txt", "a")
viko_file = open("viko_result.txt", "a")

frko_file = open("frko_result.txt", "a")
kofr_file = open("kofr_result.txt", "a")

jazh_file = open("jazh_result.txt", "a")
zhja_file = open("zhja_result.txt", "a")


# 파일 두개 열어서 하나는 원본 그대로 다 쓰고 다른 하나는 타겟 맞는 문장만 골라서 넣고
# 파일 위에다가 써놓기
# src, tar, detected, text, translatedText

while True:
    line = f.readline()
    if not line:
        break
    src_lang, tar_lang, lang_detect, src_text, translated_text = parse(line)
    if src_lang == "aaaaa":
        continue
    long_result = "{}, {}, {}, {}, {}\n".format(src_lang, tar_lang, lang_detect, src_text, translated_text)
    detail_file.write(long_result)
    if src_text and src_lang == lang_detect:
        if src_lang == "en":
            if tar_lang == "ko":
                enko_file.write(src_text + "\n")
            elif tar_lang == "ja":
                enja_file.write(src_text + "\n")
            elif tar_lang == "zh-TW" or tar_lang == "zh-CN":
                enzh_file.write(src_text + "\n")
            elif tar_lang == "fr":
                enfr_file.write(src_text + "\n")
        elif src_lang == "ko":
            if tar_lang == "en":
                koen_file.write(src_text + "\n")
            elif tar_lang == "ja":
                koja_file.write(src_text + "\n")
            elif tar_lang == "de":
                kode_file.write(src_text + "\n")
            elif tar_lang == "zh-CN":
                kozh_file.write(src_text + "\n")
            elif tar_lang == "zh-TW":
                kozh_file.write(src_text + "\n")
            elif tar_lang == "es":
                koes_file.write(src_text + "\n")
            elif tar_lang == "id":
                koid_file.write(src_text + "\n")
            elif tar_lang == "it":
                koit_file.write(src_text + "\n")
            elif tar_lang == "th":
                koth_file.write(src_text + "\n")
            elif tar_lang == "ru":
                koru_file.write(src_text + "\n")
            elif tar_lang == "fr":
                kofr_file.write(src_text + "\n")
            elif tar_lang == "vi":
                kovi_file.write(src_text + "\n")
        elif src_lang == "ja":
            if tar_lang == "zh-CN":
                jazh_file.write(src_text + "\n")
            if tar_lang == "zh-TW":
                jazh_file.write(src_text + "\n")
            elif tar_lang == "ko":
                jako_file.write(src_text + "\n")
            elif tar_lang == "en":
                jaen_file.write(src_text + "\n")
        elif src_lang == "zh-CN" or src_lang == "zh-TW" :
            if tar_lang == "ko":
                zhko_file.write(src_text + "\n")
            elif tar_lang == "en":
                zhen_file.write(src_text + "\n")
            elif tar_lang == "ja":
                zhja_file.write(src_text + "\n")

        elif src_lang == "de" and tar_lang == "ko":
            deko_file.write(src_text + "\n")

        elif src_lang == "es" and tar_lang == "ko":
            esko_file.write(src_text + "\n")

        elif src_lang == "th" and tar_lang == "ko":
            thko_file.write(src_text + "\n")

        elif src_lang == "ru" and tar_lang == "ko":
            ruko_file.write(src_text + "\n")

        elif src_lang == "id" and tar_lang == "ko":
            idko_file.write(src_text + "\n")

        elif src_lang == "it" and tar_lang == "ko":
            itko_file.write(src_text + "\n")

        elif src_lang == "fr" and tar_lang == "en":
            fren_file.write(src_text + "\n")

        elif src_lang == "vi" and tar_lang == "ko":
            viko_file.write(src_text + "\n")

        elif src_lang == "fr" and tar_lang == "ko":
            frko_file.write(src_text + "\n")

f.close()
detail_file.close()
enko_file.close()
koen_file.close()
jako_file.close()
koja_file.close()
enja_file.close()
jaen_file.close()
deko_file.close()
kode_file.close()
kozh_file.close()
zhko_file.close()
enzh_file.close()
zhen_file.close()
esko_file.close()
koes_file.close()
koth_file.close()
thko_file.close()
koru_file.close()
ruko_file.close()
idko_file.close()
koid_file.close()
itko_file.close()
koit_file.close()
enfr_file.close()
fren_file.close()
kovi_file.close()
viko_file.close()
frko_file.close()
kofr_file.close()
jazh_file.close()
zhja_file.close()
print("############DONE##############")

# split -l 100000 api_n2mt.log
# for x in {a..t};do echo ab"$x";python a.py ../ab"$x";done