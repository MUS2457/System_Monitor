class MetricsAnalysis:

    def __init__(self, metrics):
        self.metrics = metrics
        self.threshold = 70

    
    def cpu_above_threshold(self):
        return [metric for metric in self.metrics if metric.cpu > self.threshold]
    
    def ram_above_threshold(self):
        return [metric for metric in self.metrics if metric.ram > self.threshold]
    
    def disk_above_threshold(self):
        return [metric for metric in self.metrics if metric.disk[3]> self.threshold]
    
    def average_cpu_usage(self):
        return sum(metric.cpu for metric in self.metrics) / len(self.metrics) if self.metrics else 0
    
    def average_ram_usage(self):
        return sum(metric.ram for metric in self.metrics) / len(self.metrics) if self.metrics else 0
    

    def max_ram_usage(self):
        return max(metric.ram for metric in self.metrics)

    def max_cpu_usage(self):
        return max(metric.cpu for metric in self.metrics)
    
    def min_ram_usage(self):
        return min(metric.ram for metric in self.metrics)

    def min_cpu_usage(self):
        return min(metric.cpu for metric in self.metrics)
    
    def alert_ram (self):
        return [metric for metric in self.metrics if metric.ram > self.threshold]
    
    def alert_cpu (self):
        return [metric for metric in self.metrics if metric.cpu > self.threshold]
    
    def alert_disk (self):
        return [metric for metric in self.metrics if metric.disk[3] > self.threshold]
    
    def trend_detection_cpu(self):
        predict = all(x.cpu <= y.cpu for x, y in zip(self.metrics, self.metrics[1:]))
        return "increasing" if predict else "decreasing"


    def trend_detection_ram(self):
        predict = all(x.ram <= y.ram for x, y in zip(self.metrics, self.metrics[1:]))
        return "increasing" if predict else "decreasing"


    def trend_detection_disk(self):
        predict = all(x.disk[3] <= y.disk[3] for x, y in zip(self.metrics, self.metrics[1:]))
        return "increasing" if predict else "decreasing"

        
    def overall_detection(self, parameter):
        if parameter == "disk":  #  cant use getattr in str with index so i used the disk as verification name
            first = self.metrics[0].disk[3]  
            last = self.metrics[-1].disk[3]

        else:
            first = getattr(self.metrics[0], parameter)
            last = getattr(self.metrics[-1], parameter)

        if first < last:
            return "increasing"
        else:
            return "decreasing"
        
    def overall_detection_cpu(self):
        return self.overall_detection("cpu")
    
    def overall_detection_ram(self):
        return self.overall_detection("ram")
    
    def overall_detection_disk(self):
        return self.overall_detection("disk")
    
    def volatility(self, parameter, gap=20):
        for i in range(1, len(self.metrics)):
        
        # disk special case
            if parameter == "disk":
                key_1 = self.metrics[i].disk[3]
                key_2 = self.metrics[i-1].disk[3]
            else:
                key_1 = getattr(self.metrics[i], parameter)
                key_2 = getattr(self.metrics[i-1], parameter)

            delta = abs(key_1 - key_2)

            if delta > gap:
                return "fatal : high volatility"
            elif delta == gap:
                return "moderately volatile"

        return "stable"


    def volatility_cpu(self):
        return self.volatility("cpu")

    def volatility_ram(self):
        return self.volatility("ram")

    def volatility_disk(self):
        return self.volatility("disk")
