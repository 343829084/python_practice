import struct
import string


class Pktheader():
    def __init__(self, content):
        self.pkt_type_no_f = ['PktTypeNo_def', 'pkt_type_no', '报文类型代码', '100101']
        self.pkt_body_length_f = ['PktLength_def', 'pkt_body_length', '数据长度', '100']
        self.fields = []
        self.msg = []
        self.content = content

    def process(self):
        self.fields += self.pkt_type_no_f,
        self.fields += self.pkt_body_length_f,
        return self.fields

    def unpack(self):
        tmp, = struct.unpack('!I', self.content[:4])
        self.msg.append(('报文类型代码', tmp))
        self.content = self.content[4:]
        tmp, = struct.unpack('!I', self.content[:4])
        self.msg.append(('数据长度', tmp))
        self.content = self.content[4:]
        return self.msg


def getInstance(class_name, content):
    name = class_name + "(" +repr(content) +")"
    t = eval(name)
    return t


def getclass(pkt_type):
    if pkt_type == 202202:
        return "PktUserLogin"


def getField(pkt_type, pkt_content):
    if isinstance(pkt_type, int):
        class_name = getclass(pkt_type)

    ins = getInstance(class_name, pkt_content)
    ins_field = ins.process()
    return ins_field


def typedef(type):
    data = []
    for i in type:
        if i == 'ch':
            data.append('c')
        elif i == 'uint32':
            data.append('I')
        elif i[-1] == 's':
            data.append(i)

    return data



def getPktHeader():
    ins = Pktheader('')
    ins_field = ins.process()
    def_list = list(zip(*ins_field))[0]
    types = Def_Type()
    type_list = types.process(def_list)
    head_code = typedef(type_list)
    head_code_str = ''
    for i in head_code:
        head_code_str += i
    return head_code_str

def encode(pkt_type, pkt_content):
    ins_field = getField(pkt_type, pkt_content)
    print("encode: ins_field ", ins_field)
    def_name = []
    for i in range(len(pkt_content)):
        for j in range(len(ins_field)):
            if pkt_content[i][0] == ins_field[j][2]:
                def_name.append(ins_field[j][0])
                break

    print("encode def_name ", def_name)
    types = Def_Type()
    type_list = types.process(def_name)
    print("encode types.process: ",type_list)
    code = typedef(type_list)

    msg = b''
    for i in range(len(pkt_content)):
        if "s" in code[i]:
            code_len = int(code[i][:-1])
            print("code_len", code_len)
            print("pkt_content:", (str(pkt_content[i][1]).ljust(code_len)).encode('utf-8'))
            msg += struct.pack("!%s"%code[i], (str(pkt_content[i][1]).ljust(code_len)).encode('utf-8'))


    pkt_len = len(msg)
    head_code = getPktHeader()
    head = struct.pack("!%s"%head_code, pkt_type, pkt_len)
    msg = head + msg
    return msg



class PktUserOrder():
    def __init__(self, content):
        self.submit_pbu_id_f = ['PBUID_def', 'submit_put_id', '申报交易单元', '000100']
        self.appl_id_f = ['ApplID_def', 'appl_id', '应用标识', '010']
        self.security_id = ['SecurityID_def', 'security_id', '证券代码', '0001']

    def process(self):
        self.fields += self.submit_pbu_id_f,
        self.fields += self.appl_id_f,
        self.fields += self.security_id,
        print("PktUserOrder, fields:", self.fields)
        return self.fields

    def unpack(self):
        tmp, = struct.unpack('!4s', self.content[:4])
        self.msg.append(('证券代码', tmp))
        self.content = self.content[4:]
        tmp, = struct.unpack('!3s', self.content[:3])
        self.msg.append(('应用标识', tmp))
        self.content = self.content[3:]
        tmp, = struct.unpack('!6s', self.content[:6])
        self.msg.append(('申报交易单元', tmp))
        self.content = self.content[6:]
        return self.msg


class PktUserLogin(PktUserOrder):
    def __init__(self, content):
        self.firm_f = ['Firm_def', 'firm_type', '机构代码', '99']

        self.submit_pbu_id_f = ['PBUID_def', 'submit_put_id', '申报交易单元', '000100']
        self.appl_id_f = ['ApplID_def', 'appl_id', '应用标识', '010']
        self.security_id = ['SecurityID_def', 'security_id', '证券代码', '0001']

        self.fields = []
        self.msg = []
        self.content = content

    def process(self):
        self.fields += self.firm_f,
        self.fields += self.submit_pbu_id_f, self.appl_id_f, self.security_id,
        return self.fields

    def unpack(self):
        tmp, = struct.unpack('!2s', self.content[:2])
        self.msg.append(('机构代码', tmp))
        self.content = self.content[8:]
        tmp, = " "
        ins = PktUserOrder(self.content)
        tmp = ins.unpack()
        self.msg.extend(tmp)
        self.content = ins.content
        return self.msg

class Def_Type():
    def __init__(self):
        self.ApplID_def = '3s'
        self.PBUID_def = '6s'
        self.SecurityID_def = '4s'
        self.Firm_def = '2s'
        self.PktTypeNo_def = 'uint32'
        self.PktLength_def = 'uint32'
        self.list = []
        self.type_list = []

    def process(self, filed):
        for i in filed:
            if 'string' in i:
                self.list.append('uint32')
            elif 'seq_' in i:
                self.list.append('uint32')
            elif 'uint' in i:
                self.list.append(i)
            else:
                self.list.append(eval('self.' + i))
        return self.list

    def type_process(self, field):
        for i in filed:
            if 'string' in i:
                self.list.append('uint32')
            elif 'seq_' in i:
                self.list.append('uint32')
            elif 'uint' in i:
                self.list.append(i)
            else:
                self.list.append(eval('self.' + i))
        return self.list




if __name__ == '__main__':
    report_data = [
        ('申报交易单元', '000100'),
        ('应用标识', '010'),
        ('证券代码', '0001'),
        ('机构代码', '99'),
    ]
    msg = encode(202202, report_data)
    print("send msg=", msg)
