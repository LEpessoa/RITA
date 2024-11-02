from ._anvil_designer import pdf_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class pdf_page(pdf_pageTemplate):
  def __init__(self, input_dic=[],**properties):
    self.pdf_page = anvil.js.get_dom_node(self)
    # Set Form properties and Data Bindings.
    self.input_dic = input_dic
    self.init_components(**properties)
    self.dic = [
    {'id': 19, 'name': 'Resource', 'acronym': 'RSC', 'quantity': 1, 'threats': [
            {'id': 236, 'iot_threat_id': 'PLTT4', 'name': 'Collision', 'description': "Collision is similar to the jamming attack, as the loss of data packets happens by virtue of simultaneous existence of signals in the concemed spectrum. Collision may also occur intrinsically in a large network due to problems in the design of synchronization and transmission times. Transmitted data packets can be disrupted by the malicious users transmitting asynchronously that can result in a checksum mismatch or back-off in some MAC protocols. An attacker listens on the communication medium and guesses the expected time of message transmission. The attacker then sends a message at the same time when a proper message is started which results in collision of the message in the wireless medium. Repeated cycles of collision can result in a DoS attack and affect the availability. In IoT, there is a high probability of collision due to co-existence of many protocols in the WIFI 2.4 GHz band [p25]. Monitoring RSSI values such as in jamming mitigation is not of much use, as attacker's signals are more dynamic and stealthier. An autonomic system can recover by dynamically adapting with a variable flow control mechanism for collision mitigation due to a jammer. Autonomic self-healing for collision recovery by random number based mechanisms [p261]", 'quantity': 1, 'rcms': [
                    {'id': 82, 'resilient_solution_id': 'DTK4', 'name': 'Intrusion Detection System', 'description': 'An intrusion detection system is a sottware tool used to detect unauthonzed access to a computer system or network. An intrusion detection system is capable of detecting all types of malicious network traffic and computer usage. This incudes network attacks against vulnerable services, data driven attacks on applications, host-based attacks-such as privilege escalation, unauthorized logins and access to sensitive files-and malware. An intrusion detection system is a dynamic monitoring entity that complements the static monitoring abilities ofa firewall. An intrusion detection system monitors traffic in a network in promiscuous mode, very much like a network sniffer. The network packets that are collected are analyzed for rule violations by a pattem recognition algorithm. When rule violations are detected, the intrusion detection system alerts the administrator. The [p89]', 'quantity': 1
                    }
                ]
            },
            {'id': 238, 'iot_threat_id': 'PLTT6', 'name': 'De-synchronization and replay', 'description': 'Request tor retransmission of missed frames can be made by repeatedly forcing messages into the network which cary sequence numbers to one or both end points. Time Division Multiple Access (TDMA) based schemes are particularly vulnerable and few countemeasures are explained by [p28]. In this scenario, separate methods exist for single hop networks and multi-hop networks. Replay is mostly an attack on synchronization whereby an attacker stores previously transmitted data and repeats it at a later time to mislead the receiver node. Many authentication mechanisms are immune against the replay attack, and lessons can be leamt in order to design an autonomic secure system. Smple encryption of data can also be an etfective means against the replay attack. Replay attack could thus be considered as the easiest attack to be mitigated. It has been placed in a high risk category as failure of mitigation can lead to the downfall of the efficiency in the network. The [p30] mitigates the replay attack by dynamically changing the session key upon fulfillment of certain conditions.', 'quantity': 1, 'rcms': [
                    {'id': 82, 'resilient_solution_id': 'DTK4', 'name': 'Intrusion Detection System', 'description': 'An intrusion detection system is a sottware tool used to detect unauthonzed access to a computer system or network. An intrusion detection system is capable of detecting all types of malicious network traffic and computer usage. This incudes network attacks against vulnerable services, data driven attacks on applications, host-based attacks-such as privilege escalation, unauthorized logins and access to sensitive files-and malware. An intrusion detection system is a dynamic monitoring entity that complements the static monitoring abilities ofa firewall. An intrusion detection system monitors traffic in a network in promiscuous mode, very much like a network sniffer. The network packets that are collected are analyzed for rule violations by a pattem recognition algorithm. When rule violations are detected, the intrusion detection system alerts the administrator. The [p89] show same types of IDS that can be used in IoT application. Bellow we can see the organization of a generalized intusion detection svstem More details in [p89]', 'quantity': 1
                    }
                ]
            }
        ], 'textReference': 'techville'
    },
    {'id': 12, 'name': 'Device', 'acronym': 'DVC', 'quantity': 1, 'threats': [], 'textReference': 'qr code'
    },
    {'id': 12, 'name': 'Device', 'acronym': 'DVC', 'quantity': 1, 'threats': [], 'textReference': 'qr codes'
    },
    {'id': 12, 'name': 'Device', 'acronym': 'DVC', 'quantity': 1, 'threats': [], 'textReference': 'gps'
    },
    {'id': 12, 'name': 'Device', 'acronym': 'DVC', 'quantity': 1, 'threats': [], 'textReference': 'rfid'
    }
]
    # Any code you write here will run before the form opens.
    if len(self.input_dic) != 0:
      self.dic = self.input_dic
    self.report_repeating_panel.items = self.dic

  def print_button_click(self, **event_args):
    pass


