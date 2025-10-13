// Main JavaScript for Super20 Academy Management System

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Form validation enhancements
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Phone number formatting
    var phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            var value = e.target.value.replace(/\D/g, '');
            if (value.length > 0) {
                if (value.length <= 5) {
                    value = value;
                } else if (value.length <= 10) {
                    value = value.slice(0, 5) + '-' + value.slice(5);
                } else {
                    value = value.slice(0, 5) + '-' + value.slice(5, 10) + '-' + value.slice(10, 15);
                }
            }
            e.target.value = value;
        });
    });

    // Percentage input validation (do not cap fields used for payments/rates)
    var percentageInputs = document.querySelectorAll('input[type="number"][step="0.01"]');
    percentageInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            // Skip capping for payment-related fields
            var skipCap = input.name === 'per_lecture_rate' || input.name === 'amount' || input.classList.contains('no-percentage-cap');
            if (skipCap) {
                if (parseFloat(e.target.value) < 0) {
                    e.target.value = 0;
                }
                return;
            }
            var value = parseFloat(e.target.value);
            if (value < 0) {
                e.target.value = 0;
            } else if (value > 100) {
                e.target.value = 100;
            }
        });
    });

    // Date input restrictions
    var dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        // Set max date to today for date of birth
        if (input.id === 'id_date_of_birth') {
            var today = new Date().toISOString().split('T')[0];
            input.setAttribute('max', today);
        }
        
        // Set min date to today for follow-up dates
        if (input.id === 'id_followup_date') {
            var today = new Date().toISOString().split('T')[0];
            input.setAttribute('min', today);
        }
    });

    // Search functionality enhancement
    var searchInputs = document.querySelectorAll('input[name="search"]');
    searchInputs.forEach(function(input) {
        var timeout = null;
        input.addEventListener('input', function(e) {
            clearTimeout(timeout);
            timeout = setTimeout(function() {
                // Auto-submit search after 1 second of no typing
                var form = input.closest('form');
                if (form) {
                    form.submit();
                }
            }, 1000);
        });
    });

    // Add click feedback to buttons
    document.querySelectorAll('.btn').forEach(function(button) {
        button.addEventListener('click', function(e) {
            // Add a small delay to show the click effect
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
            
            // Log button clicks for debugging
            if (this.href) {
                console.log('Button clicked, navigating to:', this.href);
            }
            
            // Add visual feedback
            this.style.backgroundColor = this.style.backgroundColor === 'rgb(255, 255, 255)' ? '#f8f9fa' : '#ffffff';
            setTimeout(() => {
                this.style.backgroundColor = '';
            }, 200);
        });
    });

    // Special handling for home page buttons
    document.querySelectorAll('.hero-section .btn, .bg-primary .btn').forEach(function(button) {
        button.addEventListener('click', function(e) {
            console.log('Home page button clicked:', this.textContent.trim());
            
            // Add ripple effect
            var ripple = document.createElement('span');
            ripple.style.position = 'absolute';
            ripple.style.borderRadius = '50%';
            ripple.style.background = 'rgba(255,255,255,0.3)';
            ripple.style.transform = 'scale(0)';
            ripple.style.animation = 'ripple 0.6s linear';
            ripple.style.left = (e.clientX - this.offsetLeft) + 'px';
            ripple.style.top = (e.clientY - this.offsetTop) + 'px';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Form submission feedback
    document.querySelectorAll('form').forEach(function(form) {
        form.addEventListener('submit', function(e) {
            var submitBtn = this.querySelector('#submitBtn');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Submitting...';
                submitBtn.disabled = true;
            }
        });
    });

    // Table row selection
    var tableRows = document.querySelectorAll('.table tbody tr');
    tableRows.forEach(function(row) {
        row.addEventListener('click', function(e) {
            // Don't trigger if clicking on buttons or links
            if (e.target.tagName === 'BUTTON' || e.target.tagName === 'A' || e.target.closest('button') || e.target.closest('a')) {
                return;
            }
            
            // Toggle selection
            this.classList.toggle('table-active');
        });
    });

    // Bulk actions for selected rows
    var bulkActionBtn = document.getElementById('bulk-action-btn');
    if (bulkActionBtn) {
        bulkActionBtn.addEventListener('click', function() {
            var selectedRows = document.querySelectorAll('.table tbody tr.table-active');
            if (selectedRows.length === 0) {
                alert('Please select at least one item.');
                return;
            }
            
            var action = document.getElementById('bulk-action-select').value;
            if (action === '') {
                alert('Please select an action.');
                return;
            }
            
            // Confirm action
            if (confirm('Are you sure you want to perform this action on ' + selectedRows.length + ' selected items?')) {
                // Perform bulk action
                console.log('Performing ' + action + ' on ' + selectedRows.length + ' items');
            }
        });
    }

    // Export functionality
    var exportBtn = document.getElementById('export-btn');
    if (exportBtn) {
        exportBtn.addEventListener('click', function() {
            var format = this.dataset.format || 'csv';
            var table = document.querySelector('.table');
            
            if (table) {
                exportTableToCSV(table, 'super20_data_' + new Date().toISOString().split('T')[0] + '.csv');
            }
        });
    }

    // Print functionality
    var printBtn = document.querySelector('.btn[onclick="window.print()"]');
    if (printBtn) {
        printBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.print();
        });
    }

    // Image preview enhancement
    var imageInputs = document.querySelectorAll('input[type="file"]');
    imageInputs.forEach(function(input) {
        input.addEventListener('change', function(e) {
            var file = e.target.files[0];
            if (file) {
                if (file.size > 5 * 1024 * 1024) { // 5MB limit
                    alert('File size should be less than 5MB.');
                    this.value = '';
                    return;
                }
                
                if (!file.type.startsWith('image/')) {
                    alert('Please select an image file.');
                    this.value = '';
                    return;
                }
                
                var reader = new FileReader();
                reader.onload = function(e) {
                    var preview = document.getElementById('photo-preview');
                    if (!preview) {
                        preview = document.createElement('img');
                        preview.id = 'photo-preview';
                        preview.className = 'mt-2 rounded';
                        preview.style.maxWidth = '200px';
                        preview.style.maxHeight = '200px';
                        input.parentNode.appendChild(preview);
                    }
                    preview.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    });

    // Dashboard chart animations
    var statCards = document.querySelectorAll('.card.bg-info, .card.bg-success, .card.bg-warning, .card.bg-danger');
    statCards.forEach(function(card, index) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(function() {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Smooth scrolling for anchor links
    var anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Loading states for forms
    var forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            var submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
            }
        });
    });

    // Auto-save form data to localStorage
    var formInputs = document.querySelectorAll('input, textarea, select');
    formInputs.forEach(function(input) {
        var key = input.name || input.id;
        if (key) {
            // Load saved data
            var savedValue = localStorage.getItem('form_' + key);
            if (savedValue && input.value === '') {
                input.value = savedValue;
            }
            
            // Save data on input
            input.addEventListener('input', function() {
                localStorage.setItem('form_' + key, this.value);
            });
        }
    });

    // Clear form data from localStorage on successful submission
    var forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            setTimeout(function() {
                var inputs = form.querySelectorAll('input, textarea, select');
                inputs.forEach(function(input) {
                    var key = input.name || input.id;
                    if (key) {
                        localStorage.removeItem('form_' + key);
                    }
                });
            }, 1000);
        });
    });

    // Responsive table enhancements
    var tables = document.querySelectorAll('.table-responsive');
    tables.forEach(function(table) {
        var wrapper = table.parentElement;
        if (wrapper) {
            wrapper.style.overflowX = 'auto';
        }
    });

    // Modal enhancements
    var modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        modal.addEventListener('show.bs.modal', function() {
            this.querySelector('.modal-content').style.transform = 'scale(0.7)';
            this.querySelector('.modal-content').style.opacity = '0';
        });
        
        modal.addEventListener('shown.bs.modal', function() {
            this.querySelector('.modal-content').style.transition = 'all 0.3s ease';
            this.querySelector('.modal-content').style.transform = 'scale(1)';
            this.querySelector('.modal-content').style.opacity = '1';
        });
    });

    // Notification system
    function showNotification(message, type = 'info') {
        var notification = document.createElement('div');
        notification.className = 'alert alert-' + type + ' alert-dismissible fade show position-fixed';
        notification.style.top = '20px';
        notification.style.right = '20px';
        notification.style.zIndex = '9999';
        notification.style.minWidth = '300px';
        
        notification.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'} me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(function() {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    // Global notification function
    window.showNotification = showNotification;

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + S to save
        if ((e.ctrlKey || e.metaKey) && e.key === 's') {
            e.preventDefault();
            var activeForm = document.querySelector('form:focus-within');
            if (activeForm) {
                activeForm.submit();
            }
        }
        
        // Escape to close modals
        if (e.key === 'Escape') {
            var openModals = document.querySelectorAll('.modal.show');
            openModals.forEach(function(modal) {
                var modalInstance = bootstrap.Modal.getInstance(modal);
                if (modalInstance) {
                    modalInstance.hide();
                }
            });
        }
    });

    // Utility function to export table to CSV
    function exportTableToCSV(table, filename) {
        var csv = [];
        var rows = table.querySelectorAll('tr');
        
        for (var i = 0; i < rows.length; i++) {
            var row = [], cols = rows[i].querySelectorAll('td, th');
            
            for (var j = 0; j < cols.length; j++) {
                var text = cols[j].innerText.replace(/"/g, '""');
                row.push('"' + text + '"');
            }
            
            csv.push(row.join(','));
        }
        
        var csvContent = 'data:text/csv;charset=utf-8,' + csv.join('\n');
        var encodedUri = encodeURI(csvContent);
        var link = document.createElement('a');
        link.setAttribute('href', encodedUri);
        link.setAttribute('download', filename);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    // Initialize any additional plugins or features
    console.log('Super20 Academy Management System initialized successfully!');
}); 