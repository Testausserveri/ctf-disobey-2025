from scapy.all import *

packets = rdpcap('../chal/server-traffic.pcapng')
matching_packets = []
    
for pkt in packets:
    if DNS in pkt:
        try:
            query_name = pkt[DNSQR].qname.decode('utf-8')
            if pkt[DNS].qr == 1 and query_name.endswith('.b.s.tti.sh.'):
                for an in pkt[DNS].an:
                    print(an.rdata)
            if pkt[DNS].qr == 0 and query_name.endswith('.d.s.tti.sh.'):
                print(query_name)
        except Exception as e:
            print(f"Error processing packet: {e}")
    
